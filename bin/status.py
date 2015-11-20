#!/usr/bin/env python

__author__ = 'noisufnoc'

import subprocess
import json

data = {}

result = subprocess.check_output("/usr/bin/apcaccess")
for line in result.split('\n'):
    (key, spl, value) = line.partition(': ')
    key = key.rstrip().lower()
    value = value.strip()
    value = value.split(' ', 1)[0]
    data[key] = value

print json.dumps(data, indent=4, sort_keys=True)
