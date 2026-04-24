#!/usr/bin/env python
import sys

current_category = None
total_sales = 0

for line in sys.stdin:
    category, sales = line.strip().split('\t')
    sales = float(sales)

    if current_category == category:
        total_sales += sales
    else:
        if current_category:
            print("%s\t%.2f" % (current_category, total_sales))
        current_category = category
        total_sales = sales

if current_category:
    print("%s\t%.2f" % (current_category, total_sales))