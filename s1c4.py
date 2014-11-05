#!/bin/python

import util

filename = "s1c4.txt"

cipherList = open(filename).read().split()

for cipher in cipherList:
	maxScore = 0.9
	score, key, plaintext = util.testSingleXor(cipher)
	wordlist = plaintext.split(' ')
	if (plaintext != '') and (score > maxScore):
		maxScore = score
		maxSet = cipher, score, key, plaintext

print maxSet[0]
print maxSet[1:]


