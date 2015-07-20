/*-
 * This file is part of Libight <https://libight.github.io/>.
 *
 * Libight is free software. See AUTHORS and LICENSE for more
 * information on the copying conditions.
 *
 * =========================================================================
 *
 * Portions Copyright (c) 2015, Adriano Faggiani, Enrico Gregori,
 * Luciano Lenzini, Valerio Luconi
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

/// Implementation of traceroute interface

// Disable for non Linux until we figure out how to build on iOS
#ifdef __linux__

#include <ight/common/log.hpp>
#include <ight/traceroute/interface.hpp>

#include <netinet/ip.h> // Defines n_short etc on MacOSX
#include <netinet/icmp6.h>
#include <netinet/ip_icmp.h>

namespace ight {
namespace traceroute {

struct ProbeResultMapping {
  unsigned char type;
  unsigned char code;
  ProbeResultMeaning meaning;
};

#define PRM_ ProbeResultMeaning // For readability

static ProbeResultMapping MAPPINGv4[] = {
    {ICMP_TIMXCEED, ICMP_TIMXCEED_INTRANS, PRM_::TTL_EXCEEDED},
    {ICMP_UNREACH, ICMP_UNREACH_PORT, PRM_::DEST_REACHED},
    {ICMP_UNREACH, ICMP_UNREACH_PROTOCOL, PRM_::PROTO_NOT_IMPL},
    {ICMP_UNREACH, ICMP_UNREACH_NET, PRM_::NO_ROUTE_TO_HOST},
    {ICMP_UNREACH, ICMP_UNREACH_HOST, PRM_::ADDRESS_UNREACH},
    {255, 255, PRM_::OTHER},
};

static ProbeResultMapping MAPPINGv6[] = {
    {ICMP6_TIME_EXCEEDED, ICMP6_TIME_EXCEED_TRANSIT, PRM_::TTL_EXCEEDED},
    {ICMP6_DST_UNREACH, ICMP6_DST_UNREACH_NOPORT, PRM_::DEST_REACHED},
    {ICMP6_DST_UNREACH, ICMP6_DST_UNREACH_NOROUTE, PRM_::NO_ROUTE_TO_HOST},
    {ICMP6_DST_UNREACH, ICMP6_DST_UNREACH_ADDR, PRM_::ADDRESS_UNREACH},
    {ICMP6_DST_UNREACH, ICMP6_DST_UNREACH_ADMIN, PRM_::ADMIN_FILTER},
    {255, 255, PRM_::OTHER},
};

#undef PRM_

ProbeResultMeaning ProbeResult::get_meaning() {
  for (auto m = is_ipv4 ? &MAPPINGv4[0] : &MAPPINGv6[0];
       m->meaning != ProbeResultMeaning::OTHER; ++m) {
    if (m->type == icmp_type && m->code == icmp_code) {
      ight_debug("type %d code %d meaning %d", icmp_type, icmp_code,
                 m->meaning);
      return m->meaning;
    }
  }
  ight_debug("type %d code %d meaning %d", icmp_type, icmp_code,
             ProbeResultMeaning::OTHER);
  return ProbeResultMeaning::OTHER;
}

ProberInterface::~ProberInterface() {}

} // namespace traceroute
} // namespace ight

#endif