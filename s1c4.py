#!/bin/python

import util

filename = "s1c4.txt"

cipherList = open(filename).read().split()
maxSet = (0.0, None, None, None)

for cipherhex in cipherList:
	score, key, plaintext = util.find_single_byte_xor_of(util.hex2byte(cipherhex[:-2]))
	if score > maxSet[0]:
		print (score, key, plaintext)
		maxSet = (score, key, plaintext, cipherhex)

print (maxSet)


