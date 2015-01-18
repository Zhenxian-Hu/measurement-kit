/*-
 * This file is part of Libight <https://libight.github.io/>.
 *
 * Libight is free software. See AUTHORS and LICENSE for more
 * information on the copying conditions.
 */

//
// Tests for src/net/connection.h's IghtConnection{State,}
//

#define CATCH_CONFIG_MAIN
#include "src/ext/Catch/single_include/catch.hpp"

#include "common/check_connectivity.hpp"
#include "common/log.h"

#include "net/connection.h"

TEST_CASE("Ensure that the constructor socket-validity checks work") {

	SECTION("Invalid values are properly normalized") {
		{
			/* Common for both Unix and Windows */
			IghtConnection conn(-1);
			REQUIRE(conn.get_fileno() == -1);
		}
#ifndef WIN32
		{
			IghtConnection conn(-2);
			REQUIRE(conn.get_fileno() == -1);
		}
		/* ... */
		{
			IghtConnection conn(INT_MIN);
			REQUIRE(conn.get_fileno() == -1);
		}
#endif
	}

	SECTION("Valid values are accepted") {
		{
			IghtConnection conn(0);
			REQUIRE(conn.get_fileno() == 0);
		}
		{
			IghtConnection conn(1);
			REQUIRE(conn.get_fileno() == 1);
		}
		{
			IghtConnection conn(2);
			REQUIRE(conn.get_fileno() == 2);
		}
#ifdef WIN32
		{
			IghtConnection conn(INTPTR_MAX);
			REQUIRE(conn.get_fileno() == INTPTR_MAX);
		}
		/* Skip -1 that is INVALID_SOCKET */
		{
			IghtConnection conn(-2);
			REQUIRE(conn.get_fileno() == -2);
		}
		{
			IghtConnection conn(-3);
			REQUIRE(conn.get_fileno() == -3);
		}
		/* ... */
		{
			IghtConnection conn(INTPTR_MIN);
			REQUIRE(conn.get_fileno() == INTPTR_MIN);
		}
#else
		{
			IghtConnection conn(INT_MAX);
			REQUIRE(conn.get_fileno() == INT_MAX);
		}

#endif
	}
}

TEST_CASE("IghtConnection::close() is idempotent") {
    if (ight::Network::is_down()) {
        return;
    }
    IghtConnection s("PF_INET", "nexa.polito.it", "80");
    s.on_connect([&s]() {
        REQUIRE(s.enable_read() == 0);
        REQUIRE(s.puts("GET / HTTP/1.0\r\n\r\n") == 0);
    });
    s.on_data([&s](evbuffer *) {
        s.close();
        // It shall be safe to call close() more than once
        s.close();
        s.close();
        ight_break_loop();
    });
    ight_loop();
}

TEST_CASE("It is safe to manipulate IghtConnection after close") {
    if (ight::Network::is_down()) {
        return;
    }
    IghtConnection s("PF_INET", "nexa.polito.it", "80");
    s.on_connect([&s]() {
        REQUIRE(s.enable_read() == 0);
        REQUIRE(s.puts("GET / HTTP/1.0\r\n\r\n") == 0);
    });
    s.on_data([&s](evbuffer *) {
        s.close();
        // It shall be safe to call any API after close()
	// where safe means that we don't segfault
        REQUIRE_THROWS(s.enable_read());
        REQUIRE_THROWS(s.disable_read());
        ight_break_loop();
    });
    ight_loop();
}

TEST_CASE("It is safe to close IghtConnection while resolve is in progress") {
    if (ight::Network::is_down()) {
        return;
    }
    ight_set_verbose(1);
    IghtConnection s("PF_INET", "nexa.polito.it", "80");
    IghtDelayedCall unsched(0.001, [&s]() {
        s.close();
    });
    IghtDelayedCall bail_out(2.0, []() {
        ight_break_loop();
    });
    ight_loop();
}