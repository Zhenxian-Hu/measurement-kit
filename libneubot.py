#
# LibNeubot interface - Public domain.
# WARNING: Autogenerated file - do not edit!
#

# pylint: disable = C0111, C0103

import _ctypes
import ctypes
import logging
import os
import sys

if sys.platform == "darwin":
    LIBNEUBOT_NAME = "/usr/local/lib/libneubot.dylib.3"
else:
    LIBNEUBOT_NAME = "/usr/local/lib/libneubot.so.3"

LIBNEUBOT = ctypes.CDLL(LIBNEUBOT_NAME)

DIE = getattr(os, '_exit')

NEUBOT_SLOT_VO = ctypes.CFUNCTYPE(None, ctypes.py_object)

NEUBOT_HOOK_VO = ctypes.CFUNCTYPE(None, ctypes.py_object)
NEUBOT_HOOK_VOS = ctypes.CFUNCTYPE(None, ctypes.py_object,
  ctypes.c_char_p)

class ConnectionBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class EchoServerBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class PollableBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class PollerBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class ProtocolBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class StringVectorBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_



LIBNEUBOT.NeubotConnection_attach.restype = ctypes.c_void_p
LIBNEUBOT.NeubotConnection_attach.argtypes = (
    ProtocolBase,
    ctypes.c_longlong,
)



LIBNEUBOT.NeubotConnection_connect.restype = ctypes.c_void_p
LIBNEUBOT.NeubotConnection_connect.argtypes = (
    ProtocolBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotConnection_connect_hostname.restype = ctypes.c_void_p
LIBNEUBOT.NeubotConnection_connect_hostname.argtypes = (
    ProtocolBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotConnection_get_protocol.restype = ctypes.c_void_p
LIBNEUBOT.NeubotConnection_get_protocol.argtypes = (
    ConnectionBase,
)



LIBNEUBOT.NeubotConnection_set_timeout.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_set_timeout.argtypes = (
    ConnectionBase,
    ctypes.c_double,
)



LIBNEUBOT.NeubotConnection_clear_timeout.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_clear_timeout.argtypes = (
    ConnectionBase,
)



LIBNEUBOT.NeubotConnection_start_tls.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_start_tls.argtypes = (
    ConnectionBase,
    ctypes.c_uint,
)



LIBNEUBOT.NeubotConnection_read.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_read.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_readline.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_readline.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_readn.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_readn.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_discardn.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_discardn.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_write.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_write.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_puts.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_puts.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotConnection_write_rand.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_write_rand.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_write_readbuf.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_write_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_puts_readbuf.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_puts_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotConnection_write_rand_readbuf.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_write_rand_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotConnection_read_into_.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_read_into_.argtypes = (
    ConnectionBase,
    ctypes.c_void_p,
)



LIBNEUBOT.NeubotConnection_write_from_.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_write_from_.argtypes = (
    ConnectionBase,
    ctypes.c_void_p,
)



LIBNEUBOT.NeubotConnection_enable_read.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_enable_read.argtypes = (
    ConnectionBase,
)



LIBNEUBOT.NeubotConnection_disable_read.restype = ctypes.c_int
LIBNEUBOT.NeubotConnection_disable_read.argtypes = (
    ConnectionBase,
)



LIBNEUBOT.NeubotConnection_close.argtypes = (
    ConnectionBase,
)



LIBNEUBOT.NeubotEchoServer_construct.restype = ctypes.c_void_p
LIBNEUBOT.NeubotEchoServer_construct.argtypes = (
    PollerBase,
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotPollable_construct.restype = ctypes.c_void_p
LIBNEUBOT.NeubotPollable_construct.argtypes = (
    PollerBase,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    ctypes.py_object,
)

def NeubotPollable_handle_read_slot_vo(selfptr):
    try:
        selfptr.handle_read()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLABLE_HANDLE_READ_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotPollable_handle_read_slot_vo
)

def NeubotPollable_handle_write_slot_vo(selfptr):
    try:
        selfptr.handle_write()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLABLE_HANDLE_WRITE_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotPollable_handle_write_slot_vo
)

def NeubotPollable_handle_error_slot_vo(selfptr):
    try:
        selfptr.handle_error()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLABLE_HANDLE_ERROR_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotPollable_handle_error_slot_vo
)



LIBNEUBOT.NeubotPollable_attach.restype = ctypes.c_int
LIBNEUBOT.NeubotPollable_attach.argtypes = (
    PollableBase,
    ctypes.c_longlong,
)



LIBNEUBOT.NeubotPollable_detach.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_get_fileno.restype = ctypes.c_longlong
LIBNEUBOT.NeubotPollable_get_fileno.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_set_readable.restype = ctypes.c_int
LIBNEUBOT.NeubotPollable_set_readable.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_unset_readable.restype = ctypes.c_int
LIBNEUBOT.NeubotPollable_unset_readable.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_set_writable.restype = ctypes.c_int
LIBNEUBOT.NeubotPollable_set_writable.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_unset_writable.restype = ctypes.c_int
LIBNEUBOT.NeubotPollable_unset_writable.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_set_timeout.argtypes = (
    PollableBase,
    ctypes.c_double,
)



LIBNEUBOT.NeubotPollable_clear_timeout.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPollable_close.argtypes = (
    PollableBase,
)



LIBNEUBOT.NeubotPoller_construct.restype = ctypes.c_void_p
LIBNEUBOT.NeubotPoller_construct.argtypes = (
)



LIBNEUBOT.NeubotPoller_sched.restype = ctypes.c_int
LIBNEUBOT.NeubotPoller_sched.argtypes = (
    PollerBase,
    ctypes.c_double,
    NEUBOT_HOOK_VO,
    ctypes.py_object,
)

def NeubotPoller_sched_callback_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["callback"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_SCHED_CALLBACK_HOOK_VO = NEUBOT_HOOK_VO(
    NeubotPoller_sched_callback_hook_vo
)



LIBNEUBOT.NeubotPoller_defer_read.restype = ctypes.c_int
LIBNEUBOT.NeubotPoller_defer_read.argtypes = (
    PollerBase,
    ctypes.c_longlong,
    NEUBOT_HOOK_VO,
    NEUBOT_HOOK_VO,
    ctypes.py_object,
    ctypes.c_double,
)

def NeubotPoller_defer_read_handle_ok_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_ok"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_DEFER_READ_HANDLE_OK_HOOK_VO = NEUBOT_HOOK_VO(
    NeubotPoller_defer_read_handle_ok_hook_vo
)

def NeubotPoller_defer_read_handle_timeout_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_timeout"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_DEFER_READ_HANDLE_TIMEOUT_HOOK_VO = NEUBOT_HOOK_VO(
    NeubotPoller_defer_read_handle_timeout_hook_vo
)



LIBNEUBOT.NeubotPoller_defer_write.restype = ctypes.c_int
LIBNEUBOT.NeubotPoller_defer_write.argtypes = (
    PollerBase,
    ctypes.c_longlong,
    NEUBOT_HOOK_VO,
    NEUBOT_HOOK_VO,
    ctypes.py_object,
    ctypes.c_double,
)

def NeubotPoller_defer_write_handle_ok_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_ok"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_DEFER_WRITE_HANDLE_OK_HOOK_VO = NEUBOT_HOOK_VO(
    NeubotPoller_defer_write_handle_ok_hook_vo
)

def NeubotPoller_defer_write_handle_timeout_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_timeout"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_DEFER_WRITE_HANDLE_TIMEOUT_HOOK_VO = NEUBOT_HOOK_VO(
    NeubotPoller_defer_write_handle_timeout_hook_vo
)



LIBNEUBOT.NeubotPoller_resolve.restype = ctypes.c_int
LIBNEUBOT.NeubotPoller_resolve.argtypes = (
    PollerBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    NEUBOT_HOOK_VOS,
    ctypes.py_object,
)

def NeubotPoller_resolve_callback_hook_vos(closure, string):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["callback"](closure.opaque, string)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPOLLER_RESOLVE_CALLBACK_HOOK_VOS = NEUBOT_HOOK_VOS(
    NeubotPoller_resolve_callback_hook_vos
)



LIBNEUBOT.NeubotPoller_loop.argtypes = (
    PollerBase,
)



LIBNEUBOT.NeubotPoller_break_loop.argtypes = (
    PollerBase,
)



LIBNEUBOT.NeubotProtocol_construct.restype = ctypes.c_void_p
LIBNEUBOT.NeubotProtocol_construct.argtypes = (
    PollerBase,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    NEUBOT_SLOT_VO,
    ctypes.py_object,
)

def NeubotProtocol_handle_connect_slot_vo(selfptr):
    try:
        selfptr.handle_connect()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_CONNECT_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_connect_slot_vo
)

def NeubotProtocol_handle_ssl_slot_vo(selfptr):
    try:
        selfptr.handle_ssl()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_SSL_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_ssl_slot_vo
)

def NeubotProtocol_handle_data_slot_vo(selfptr):
    try:
        selfptr.handle_data()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_DATA_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_data_slot_vo
)

def NeubotProtocol_handle_flush_slot_vo(selfptr):
    try:
        selfptr.handle_flush()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_FLUSH_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_flush_slot_vo
)

def NeubotProtocol_handle_eof_slot_vo(selfptr):
    try:
        selfptr.handle_eof()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_EOF_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_eof_slot_vo
)

def NeubotProtocol_handle_error_slot_vo(selfptr):
    try:
        selfptr.handle_error()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

NEUBOTPROTOCOL_HANDLE_ERROR_SLOT_VO = NEUBOT_SLOT_VO(
    NeubotProtocol_handle_error_slot_vo
)



LIBNEUBOT.NeubotProtocol_get_poller.restype = ctypes.c_void_p
LIBNEUBOT.NeubotProtocol_get_poller.argtypes = (
    ProtocolBase,
)



LIBNEUBOT.NeubotProtocol_destruct.argtypes = (
    ProtocolBase,
)



LIBNEUBOT.NeubotStringVector_construct.restype = ctypes.c_void_p
LIBNEUBOT.NeubotStringVector_construct.argtypes = (
    PollerBase,
    ctypes.c_size_t,
)



LIBNEUBOT.NeubotStringVector_append.restype = ctypes.c_int
LIBNEUBOT.NeubotStringVector_append.argtypes = (
    StringVectorBase,
    ctypes.c_char_p,
)



LIBNEUBOT.NeubotStringVector_get_poller.restype = ctypes.c_void_p
LIBNEUBOT.NeubotStringVector_get_poller.argtypes = (
    StringVectorBase,
)



LIBNEUBOT.NeubotStringVector_get_next.restype = ctypes.c_char_p
LIBNEUBOT.NeubotStringVector_get_next.argtypes = (
    StringVectorBase,
)



LIBNEUBOT.NeubotStringVector_destruct.argtypes = (
    StringVectorBase,
)



class NeubotHookClosure(object):
    def __init__(self):
        self.opaque = None
        self.functions = {}



class Connection(ConnectionBase):

    def __init__(self):
        ConnectionBase.__init__(self)
        self.context_ = None

    @staticmethod
    def attach(proto, filenum):
        self = Connection()
        self.context_ = LIBNEUBOT.NeubotConnection_attach(proto, filenum)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        return self

    @staticmethod
    def connect(proto, family, address, port):
        self = Connection()
        self.context_ = LIBNEUBOT.NeubotConnection_connect(proto, family,
          address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        return self

    @staticmethod
    def connect_hostname(proto, family, address, port):
        self = Connection()
        self.context_ = LIBNEUBOT.NeubotConnection_connect_hostname(proto,
          family, address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        return self

    def get_protocol(self):
        return LIBNEUBOT.NeubotConnection_get_protocol(self)

    def set_timeout(self, timeo):
        return LIBNEUBOT.NeubotConnection_set_timeout(self, timeo)

    def clear_timeout(self):
        return LIBNEUBOT.NeubotConnection_clear_timeout(self)

    def start_tls(self, server_side):
        return LIBNEUBOT.NeubotConnection_start_tls(self, server_side)

    def read(self, base, count):
        return LIBNEUBOT.NeubotConnection_read(self, base, count)

    def readline(self, base, count):
        return LIBNEUBOT.NeubotConnection_readline(self, base, count)

    def readn(self, base, count):
        return LIBNEUBOT.NeubotConnection_readn(self, base, count)

    def discardn(self, count):
        return LIBNEUBOT.NeubotConnection_discardn(self, count)

    def write(self, base, count):
        return LIBNEUBOT.NeubotConnection_write(self, base, count)

    def puts(self, base):
        return LIBNEUBOT.NeubotConnection_puts(self, base)

    def write_rand(self, count):
        return LIBNEUBOT.NeubotConnection_write_rand(self, count)

    def write_readbuf(self, base, count):
        return LIBNEUBOT.NeubotConnection_write_readbuf(self, base, count)

    def puts_readbuf(self, base):
        return LIBNEUBOT.NeubotConnection_puts_readbuf(self, base)

    def write_rand_readbuf(self, count):
        return LIBNEUBOT.NeubotConnection_write_rand_readbuf(self, count)

    def read_into_(self, evdest):
        return LIBNEUBOT.NeubotConnection_read_into_(self, evdest)

    def write_from_(self, evsource):
        return LIBNEUBOT.NeubotConnection_write_from_(self, evsource)

    def enable_read(self):
        return LIBNEUBOT.NeubotConnection_enable_read(self)

    def disable_read(self):
        return LIBNEUBOT.NeubotConnection_disable_read(self)

    def close(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBNEUBOT.NeubotConnection_close(self)
        self.context_ = None



class EchoServer(EchoServerBase):

    def __init__(self, poller, use_ipv6, address, port):
        EchoServerBase.__init__(self)
        self.context_ = LIBNEUBOT.NeubotEchoServer_construct(poller, use_ipv6,
          address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)



class Pollable(PollableBase):

    def handle_read(self):
        pass

    def handle_write(self):
        pass

    def handle_error(self):
        pass

    def __init__(self, poller):
        PollableBase.__init__(self)
        self.context_ = LIBNEUBOT.NeubotPollable_construct(poller,
          NEUBOTPOLLABLE_HANDLE_READ_SLOT_VO,
          NEUBOTPOLLABLE_HANDLE_WRITE_SLOT_VO,
          NEUBOTPOLLABLE_HANDLE_ERROR_SLOT_VO, self)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def attach(self, filenum):
        return LIBNEUBOT.NeubotPollable_attach(self, filenum)

    def detach(self):
        LIBNEUBOT.NeubotPollable_detach(self)

    def get_fileno(self):
        return LIBNEUBOT.NeubotPollable_get_fileno(self)

    def set_readable(self):
        return LIBNEUBOT.NeubotPollable_set_readable(self)

    def unset_readable(self):
        return LIBNEUBOT.NeubotPollable_unset_readable(self)

    def set_writable(self):
        return LIBNEUBOT.NeubotPollable_set_writable(self)

    def unset_writable(self):
        return LIBNEUBOT.NeubotPollable_unset_writable(self)

    def set_timeout(self, delta):
        LIBNEUBOT.NeubotPollable_set_timeout(self, delta)

    def clear_timeout(self):
        LIBNEUBOT.NeubotPollable_clear_timeout(self)

    def close(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBNEUBOT.NeubotPollable_close(self)
        self.context_ = None



class Poller(PollerBase):

    def __init__(self):
        PollerBase.__init__(self)
        self.context_ = LIBNEUBOT.NeubotPoller_construct()
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def sched(self, delta, callback, opaque):

        closure = NeubotHookClosure()
        closure.functions['callback'] = callback
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBNEUBOT.NeubotPoller_sched(self, delta,
          NEUBOTPOLLER_SCHED_CALLBACK_HOOK_VO, closure)

    def defer_read(self, fileno, handle_ok, handle_timeout, opaque, timeout):

        closure = NeubotHookClosure()
        closure.functions['handle_ok'] = handle_ok
        closure.functions['handle_timeout'] = handle_timeout
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBNEUBOT.NeubotPoller_defer_read(self, fileno,
          NEUBOTPOLLER_DEFER_READ_HANDLE_OK_HOOK_VO,
          NEUBOTPOLLER_DEFER_READ_HANDLE_TIMEOUT_HOOK_VO, closure, timeout)

    def defer_write(self, fileno, handle_ok, handle_timeout, opaque,
          timeout):

        closure = NeubotHookClosure()
        closure.functions['handle_ok'] = handle_ok
        closure.functions['handle_timeout'] = handle_timeout
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBNEUBOT.NeubotPoller_defer_write(self, fileno,
          NEUBOTPOLLER_DEFER_WRITE_HANDLE_OK_HOOK_VO,
          NEUBOTPOLLER_DEFER_WRITE_HANDLE_TIMEOUT_HOOK_VO, closure, timeout)

    def resolve(self, family, name, callback, opaque):

        closure = NeubotHookClosure()
        closure.functions['callback'] = callback
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBNEUBOT.NeubotPoller_resolve(self, family, name,
          NEUBOTPOLLER_RESOLVE_CALLBACK_HOOK_VOS, closure)

    def loop(self):
        LIBNEUBOT.NeubotPoller_loop(self)

    def break_loop(self):
        LIBNEUBOT.NeubotPoller_break_loop(self)



class Protocol(ProtocolBase):

    def handle_connect(self):
        pass

    def handle_ssl(self):
        pass

    def handle_data(self):
        pass

    def handle_flush(self):
        pass

    def handle_eof(self):
        pass

    def handle_error(self):
        pass

    def __init__(self, poller):
        ProtocolBase.__init__(self)
        self.context_ = LIBNEUBOT.NeubotProtocol_construct(poller,
          NEUBOTPROTOCOL_HANDLE_CONNECT_SLOT_VO,
          NEUBOTPROTOCOL_HANDLE_SSL_SLOT_VO,
          NEUBOTPROTOCOL_HANDLE_DATA_SLOT_VO,
          NEUBOTPROTOCOL_HANDLE_FLUSH_SLOT_VO,
          NEUBOTPROTOCOL_HANDLE_EOF_SLOT_VO,
          NEUBOTPROTOCOL_HANDLE_ERROR_SLOT_VO, self)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def get_poller(self):
        return LIBNEUBOT.NeubotProtocol_get_poller(self)

    def destruct(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBNEUBOT.NeubotProtocol_destruct(self)
        self.context_ = None



class StringVector(StringVectorBase):

    def __init__(self, poller, count):
        StringVectorBase.__init__(self)
        self.context_ = LIBNEUBOT.NeubotStringVector_construct(poller, count)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def append(self, str):
        return LIBNEUBOT.NeubotStringVector_append(self, str)

    def get_poller(self):
        return LIBNEUBOT.NeubotStringVector_get_poller(self)

    def get_next(self):
        return LIBNEUBOT.NeubotStringVector_get_next(self)

    def destruct(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBNEUBOT.NeubotStringVector_destruct(self)
        self.context_ = None

