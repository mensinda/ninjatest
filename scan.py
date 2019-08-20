#!/usr/bin/env python3

import argparse
import re
import os

parser = argparse.ArgumentParser(description='File Scanner')
parser.add_argument('--output', '-o', metavar='O', type=str, required=True)
parser.add_argument('--to-scan', '-s', metavar='S', type=str, required=True)

args = parser.parse_args()

inc_reg = re.compile(r'^#include\s+[<"]([^>"]+)[>"].*$')

def baseFileName(path: str) -> str:
  path = os.path.basename(path)
  path = os.path.splitext(path)
  return path[0]

scan_file_base = baseFileName(args.to_scan)

to_scan = [args.to_scan]

dynC = False
dynH = False

for i in to_scan:
  with open(i, 'r') as fp:
    for j in fp:
      m = inc_reg.match(j)
      if not m:
        continue

      inc_file = m.group(1)
      if scan_file_base == baseFileName(inc_file):
        to_scan += [inc_file]
      elif inc_file == 'dynC.hpp':
        dynC = True
      elif inc_file == 'dynH.hpp':
        dynH = True

with open(args.output, 'w') as fp:
  fp.write('ninja_dyndep_version = 1\n')
  deps = []
  if dynC:
    deps += ['dynC.hpp']
  if dynH:
    deps += ['dynH.hpp']
  fp.write('build {}.o: dyndep | {}\n'.format(args.to_scan, ' '.join(deps)))
  fp.write('build main.cpp.o: dyndep | {}\n'.format(' '.join(deps)))
