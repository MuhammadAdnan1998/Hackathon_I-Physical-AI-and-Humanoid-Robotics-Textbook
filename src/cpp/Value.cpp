#include "Value.h"
#include "json_tool.h"
#include <utility>

namespace json {

const Value Value::null;
const Int Value::maxInt = Int(~(UInt(1) << (sizeof(Int) * 8 - 1)));
const Int Value::minInt = Int(UInt(1) << (sizeof(Int) * 8 - 1));
const UInt Value::maxUInt = UInt(~0);
const LargestInt Value::maxLargestInt =
    LargestInt(~(LargestUInt(1) << (sizeof(LargestInt) * 8 - 1)));
const LargestInt Value::minLargestInt =
    LargestInt(LargestUInt(1) << (sizeof(LargestInt) * 8 - 1));
const LargestUInt Value::maxLargestUInt = LargestUInt(~0);

Value::Value(ValueType type) : type_(type), allocated_(0) {}
// ... more code
}
