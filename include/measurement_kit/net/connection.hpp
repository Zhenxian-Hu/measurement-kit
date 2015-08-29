// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.

#ifndef MEASUREMENT_KIT_NET_CONNECTION_HPP
#define MEASUREMENT_KIT_NET_CONNECTION_HPP

#include <measurement_kit/common/bufferevent.hpp>
#include <measurement_kit/common/constraints.hpp>
#include <measurement_kit/common/error.hpp>
#include <measurement_kit/common/log.hpp>
#include <measurement_kit/common/pointer.hpp>
#include <measurement_kit/common/poller.hpp>
#include <measurement_kit/common/string_vector.hpp>
#include <measurement_kit/common/utils.hpp>

#include <measurement_kit/net/buffer.hpp>
#include <measurement_kit/net/transport.hpp>

#include <measurement_kit/dns/dns.hpp>

#include <event2/bufferevent.h>
#include <event2/event.h>

#include <stdexcept>
#include <string.h>

namespace measurement_kit {
namespace net {

using namespace measurement_kit::common;
using namespace measurement_kit::dns;

class ConnectionState {

    Bufferevent bev;
    dns::Request dns_request;
    unsigned int connecting = 0;
    char *address = NULL;
    char *port = NULL;
    StringVector *addrlist = NULL;
    char *family = NULL;
    StringVector *pflist = NULL;
    unsigned int must_resolve_ipv4 = 0;
    unsigned int must_resolve_ipv6 = 0;
    SharedPointer<DelayedCall> start_connect;
    SharedPointer<Logger> logger = DefaultLogger::get();

    // Libevent callbacks
    static void handle_read(bufferevent *, void *);
    static void handle_write(bufferevent *, void *);
    static void handle_event(bufferevent *, short, void *);

    // Functions used when connecting
    void connect_next(void);
    void handle_resolve(int, char, std::vector<std::string>);
    void resolve();
    bool resolve_internal(char);

    std::function<void(void)> on_connect_fn = [](void) {
        /* nothing */
    };

    std::function<void(void)> on_ssl_fn = [](void) {
        /* nothing */
    };

    std::function<void(SharedPointer<Buffer>)> on_data_fn =
        [](SharedPointer<Buffer>) {
        /* nothing */
    };

    std::function<void(void)> on_flush_fn = [](void) {
        /* nothing */
    };

    std::function<void(Error)> on_error_fn = [](Error) {
        /* nothing */
    };

  public:
    ConnectionState(const char *, const char *, const char *, Poller *,
                    SharedPointer<Logger> = DefaultLogger::get(),
                    evutil_socket_t = MEASUREMENT_KIT_SOCKET_INVALID);

    ConnectionState(ConnectionState &) = delete;
    ConnectionState &operator=(ConnectionState &) = delete;
    ConnectionState(ConnectionState &&) = delete;
    ConnectionState &operator=(ConnectionState &&) = delete;

    ~ConnectionState(void);

    void on_connect(std::function<void(void)> fn) { on_connect_fn = fn; };

    void on_ssl(std::function<void(void)> fn) { on_ssl_fn = fn; };

    void on_data(std::function<void(SharedPointer<Buffer>)> fn) {
        on_data_fn = fn;
        enable_read();
    };

    void on_flush(std::function<void(void)> fn) { on_flush_fn = fn; };

    void on_error(std::function<void(Error)> fn) { on_error_fn = fn; };

    evutil_socket_t get_fileno(void) { return (bufferevent_getfd(this->bev)); }

    void set_timeout(double timeout) {
        struct timeval tv, *tvp;
        tvp = measurement_kit::timeval_init(&tv, timeout);
        if (bufferevent_set_timeouts(this->bev, tvp, tvp) != 0) {
            throw std::runtime_error("cannot set timeout");
        }
    }

    void clear_timeout(void) { this->set_timeout(-1); }

    void start_tls(unsigned int) {
        throw std::runtime_error("not implemented");
    }

    void send(const void *base, size_t count) {
        if (base == NULL || count == 0) {
            throw std::runtime_error("invalid argument");
        }
        if (bufferevent_write(bev, base, count) != 0) {
            throw std::runtime_error("cannot write");
        }
    }

    void send(std::string data) { send(data.c_str(), data.length()); }

    void send(SharedPointer<Buffer> data) { send(*data); }

    void send(Buffer &data) { data >> bufferevent_get_output(bev); }

    void enable_read(void) {
        if (bufferevent_enable(this->bev, EV_READ) != 0) {
            throw std::runtime_error("cannot enable read");
        }
    }

    void disable_read(void) {
        if (bufferevent_disable(this->bev, EV_READ) != 0) {
            throw std::runtime_error("cannot disable read");
        }
    }

    void close(void);

    void emit_connect() { on_connect_fn(); }

    void emit_data(SharedPointer<Buffer> data) { on_data_fn(data); }

    void emit_flush() { on_flush_fn(); }

    void emit_error(Error err) { on_error_fn(err); }
};

class Connection : public Transport {

    ConnectionState *state = NULL;

  public:
    virtual void emit_connect() override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->emit_connect();
    }

    virtual void emit_data(SharedPointer<Buffer> data) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->emit_data(data);
    }

    virtual void emit_flush() override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->emit_flush();
    }

    virtual void emit_error(Error err) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->emit_error(err);
    }

    Connection(void) { /* nothing to do */ }
    Connection(evutil_socket_t fd,
               SharedPointer<Logger> lp = DefaultLogger::get(),
               Poller *poller = measurement_kit::get_global_poller()) {
        state = new ConnectionState("PF_UNSPEC", "0.0.0.0", "0",
                                    poller, lp, fd);
    }
    Connection(const char *af, const char *a, const char *p,
               SharedPointer<Logger> lp = DefaultLogger::get(),
               Poller *poller = measurement_kit::get_global_poller()) {
        state = new ConnectionState(af, a, p, poller, lp);
    }

    virtual void close(void) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->close();
    }

    virtual ~Connection();

    virtual void on_connect(std::function<void(void)> fn) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->on_connect(fn);
    };

    virtual void on_ssl(std::function<void(void)> fn) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->on_ssl(fn);
    };

    virtual void
    on_data(std::function<void(SharedPointer<Buffer>)> fn) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->on_data(fn);
    };

    virtual void on_flush(std::function<void(void)> fn) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->on_flush(fn);
    };

    virtual void on_error(std::function<void(Error)> fn) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->on_error(fn);
    };

    evutil_socket_t get_fileno(void) {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        return (state->get_fileno());
    }

    virtual void set_timeout(double timeout) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->set_timeout(timeout);
    }

    virtual void clear_timeout(void) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->clear_timeout();
    }

    void start_tls(unsigned int d) {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->start_tls(d);
    }

    virtual void send(const void *base, size_t count) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->send(base, count);
    }

    virtual void send(std::string str) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->send(str);
    }

    virtual void send(SharedPointer<Buffer> sourcebuf) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->send(sourcebuf);
    }

    virtual void send(Buffer &sourcebuf) override {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->send(sourcebuf);
    }

    void enable_read(void) {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->enable_read();
    }

    void disable_read(void) {
        if (state == NULL)
            throw std::runtime_error("Invalid state");
        state->disable_read();
    }

    virtual std::string socks5_address() override { return ""; /* no proxy */ }

    virtual std::string socks5_port() override { return ""; /* no proxy */ }
};

}}
#endif
