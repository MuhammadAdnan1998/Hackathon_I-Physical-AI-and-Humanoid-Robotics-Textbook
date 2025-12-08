#pragma once

#include "json_features.h"
#include "Value.h"
#include <string>
#include <vector>

namespace json {

class Reader {
public:
  typedef char Char;
  typedef const Char *Location;
  Reader(const Features &features = Features::all());
  bool parse(const std::string &document, Value &root,
             bool collectComments = true);
  bool parse(const char *beginDoc, const char *endDoc, Value &root,
             bool collectComments = true);
  std::string getFormattedErrorMessages() const;

private:
  bool parse(const Location &beginDoc, const Location &endDoc,
             Value &root);
  // ...
};

} // namespace json
