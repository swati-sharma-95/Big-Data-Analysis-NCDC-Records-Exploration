#!/usr/bin/env python

import sys

def average(numbers):
    if not numbers:
        return 0 
    return sum(numbers) / len(numbers)

(last_key, values) = (None, [])
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    if last_key and last_key != key:
        print "%s\t%s" % (last_key, average(values))
        (last_key, values) = (key, [int(val)])
    else:
        values.append(int(val))
        last_key = key

if last_key:
    print "%s\t%s" % (last_key, average(values))
