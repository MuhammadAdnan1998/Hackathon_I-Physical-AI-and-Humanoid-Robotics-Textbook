#pragma once

#include <string>
#include <vector>

namespace json {

class FastWriter {
public:
  FastWriter();
  std::string write(const Value &root);
};

} // namespace json
