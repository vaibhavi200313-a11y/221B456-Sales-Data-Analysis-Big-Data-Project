#!/usr/bin/env python
import sys

for line in sys.stdin:
    if "order_id" in line:
        continue
    data = line.strip().split(',')
    category = data[2]
    total = float(data[3]) * int(data[4])
    print("%s\t%s" % (category, total))