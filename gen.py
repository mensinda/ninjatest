#!/usr/bin/env python3

import argparse

hppSTR = '''// Automatically generated file (HPP)
#pragma once
#define HPP_FILE_PRESENT

#include <string>

inline std::string getStrForHpp() {
  return "hppStr";
}
'''

cppSTR = '''// Automatically generated file (CPP)
#pragma once
#define CPP_FILE_PRESENT

#include <string>

inline std::string getStrForCpp() {
  return "cppStr";
}
'''

parser = argparse.ArgumentParser(description='File Generator')
parser.add_argument('--output', '-o', metavar='O', type=str, required=True)
parser.add_argument('--type', '-t', metavar='O', type=str, choices=['forHPP', 'forCPP'], required=True)

args = parser.parse_args()

with open(args.output, 'w') as fp:
  if args.type == 'forHPP':
    fp.write(hppSTR)
  elif args.type == 'forCPP':
    fp.write(cppSTR)
