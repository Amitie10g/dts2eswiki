#!/usr/bin/env python3
import re
import sys
import getopt

def callback(match):
	
	print(match.group(0))
	
	import timestring
	date_ob = timestring.Date(match.group(0))
	
	dts = "{{dts|" + str(date_ob.day) + "|" + str(date_ob.month) + "|" + str(date_ob.year) + "}}"
	return dts

try:
	filename = sys.argv[1]
except IndexError:
	print('Please provide a valid filename to be parsed')
	exit(1)

try:
	data = open(filename, 'r', encoding="utf8").read()
except FileNotFoundError as e:
	print(e)
	exit(1)

data = re.sub('{{(dts|Dts)\|[\w, \|]+}}', callback, data)

with open(filename, 'w', encoding="utf8") as f:
    f.write(data)
