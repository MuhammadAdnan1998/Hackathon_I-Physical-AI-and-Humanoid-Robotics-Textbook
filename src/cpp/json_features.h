#pragma once

#if !defined(JSON_IS_AMALGAMATION)
#include "forwards.h"
#endif // if !defined(JSON_IS_AMALGAMATION)

#if defined(JSON_USE_EXCEPTION)
#if !JSON_USE_EXCEPTION
#undef JSON_USE_EXCEPTION
#endif
#endif

namespace json {

class Features {
public:
  static Features all();
  static Features strictMode();
  Features();
  bool allowComments_ : 1;
  bool strictRoot_ : 1;
  bool allowDroppedNullPlaceholders_ : 1;
  bool allowNumericKeys_ : 1;
};

} // namespace json
