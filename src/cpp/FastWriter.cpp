#include "FastWriter.h"
#include "Value.h"
#include <sstream>

namespace json {

FastWriter::FastWriter() {}

std::string FastWriter::write(const Value &root) {
  std::ostringstream sout;
  root.write(sout);
  return sout.str();
}

} // namespace json
