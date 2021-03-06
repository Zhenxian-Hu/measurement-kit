// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.
// =============================================================
// Derivative work of r-lyeh/sole@c61c49f10d.
// See NOTICE for original license.

#ifndef PRIVATE_EXT_SOLE_HPP
#define PRIVATE_EXT_SOLE_HPP

#include <string>

namespace mk {
namespace sole {

class uuid {
  public:
    std::string str();
    uint64_t ab;
    uint64_t cd;
};

uuid uuid4();

} // namespace sole
} // namespace mk
#endif
