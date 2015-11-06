#!/usr/bin/env python

import json

f =file("../stokeScrapy.json");
s = json.load(f)

#print type(s)
print str(len(s)) # 4
print s.keys()

#print s["hah"]
#print s['hah'][1]

for i in range(0, len(s['hah'])):
	stockCode = int(s['hah'][i]['stockCode'][2:], 10)
	if not ((stockCode > 200000 and stockCode < 300000) or (stockCode >=400000 and stockCode < 600000) or (stockCode >= 700000 )):
		string = str(stockCode).zfill(6)
		print(string)
