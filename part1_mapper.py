#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val = line.strip()
    (year, wind_direction, q) = (val[15:21], val[60:63], val[63:64])
    if (wind_direction != "+999" and re.match("[01459]", q)):
        print "%s\t%s" % (year, wind_direction)
