# -*- coding: utf-8 -*-
"""
Spyder Editor

lets try putting this up on github

echo "# pydata" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/KDFerreira/pydata.git
git push -u origin master



"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def top_counts(count_dict,n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
# open(path).readline()
records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

counts = get_counts(time_zones)

top = top_counts(counts, 15)

"""
another way of doing this
"""
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)
