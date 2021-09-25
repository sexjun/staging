#pragma once
#include <tinyxml2.h>
using namespace tinyxml2;

#define SUCCESS 1
#define FAILD 0

int loadFile(const char* file_name);

int create_xml_file(const char* file_name);

int NewFunction(bool& retflag);
