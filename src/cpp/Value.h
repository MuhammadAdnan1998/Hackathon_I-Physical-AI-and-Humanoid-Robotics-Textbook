#pragma once

#include "json_features.h"
#include <string>
#include <vector>

namespace json {

class Value {
public:
  Value(ValueType type = nullValue);
  Value(const char *value);
  Value(const std::string &value);
  Value(double value);
  Value(int value);
  Value(bool value);
  Value(const Value &other);
  ~Value();

  Value &operator=(const Value &other);

  ValueType type() const;

  bool operator<(const Value &other) const;
  bool operator<=(const Value &other) const;
  bool operator>=(const Value &other) const;
  bool operator>(const Value &other) const;

  bool operator==(const Value &other) const;
  bool operator!=(const Value &other) const;

  int compare(const Value &other) const;

  const char *asCString() const;
  std::string asString() const;
  double asDouble() const;
  int asInt() const;
  bool asBool() const;

  bool isNull() const;
  bool isBool() const;
  bool isInt() const;
  bool isDouble() const;
  bool isString() const;
  bool isArray() const;
  bool isObject() const;

  bool isNumeric() const;

  Value &operator[](ArrayIndex index);
  const Value &operator[](ArrayIndex index) const;
  Value get(ArrayIndex index, const Value &defaultValue) const;

  Value &operator[](const char *key);
  const Value &operator[](const char *key) const;
  Value get(const char *key, const Value &defaultValue) const;

  void append(const Value &value);

  void clear();

  void resize(ArrayIndex newSize);

  typedef std::vector<std::string> Members;
  Members getMemberNames() const;

  void setComment(const char *comment, CommentPlacement placement);
  void setComment(const std::string &comment, CommentPlacement placement);
  std::string getComment(CommentPlacement placement) const;
  bool hasComment(CommentPlacement placement) const;

  std::string toStyledString() const;

  const Value &resolve(const Value &path, const Value &defaultValue) const;
};

class Path {
public:
  Path(const std::string &path, const Path &parent = Path());
  const std::string &get() const;

private:
  std::string path_;
};

class PathArgument {
public:
  PathArgument();
  PathArgument(const Path &path);
  PathArgument(const char *key);
  PathArgument(const std::string &key);
  PathArgument(ArrayIndex index);
};

} // namespace json
