#!/usr/bin/env python3

import json

fileSTR = '''#include "test.hpp"

std::string getStr() {
  return "testSTR";
}

'''

data = {}
with open('settings.json', 'r') as fp:
  data = json.load(fp)

if data['run']:
  with open('test.cpp', 'w') as fp:
    fp.write(fileSTR)
