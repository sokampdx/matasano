#!/bin/python

import util
import operator

s1 = "this is a test"
s2 = "wokka wokka!!!"
b1 = util.asciiTobits(s1)
b2 = util.asciiTobits(s2)
print "-------------------beg test1-------------"
print util.hamming(b1, b2)
print util.bitsToAscii(b1)
print util.bitsToAscii(b2)
print "-------------------end test1-------------"

def guessKeySize(s):
	maxn = 12
	keySizeScore = []
	for n in xrange(2, maxn):
		score = 0.0
		x = 2*n
		repeat = len(s)/n/4
		for i in range(repeat):
			str1 = s[(i*x):((i+1)*x)]
			str2 = s[((i+2)*x):((i+3)*x)]
			#print n, i, str1, str2
			bit1 = util.hexTobits(str1)
			bit2 = util.hexTobits(str2)
			score += util.hamming(bit1, bit2)
		keySizeScore.append((n, float(score)/n/repeat))

	return keySizeScore

def sortScore(scorelist):
	return sorted(scorelist, key=operator.itemgetter(1))

def printScore(scorelist):
	for k in scorelist:
		print k

def findMinScore(scorelist):
	minScore = (1, 999.0)
	for k in scorelist:
		if minScore[1] > k[1]:
			minScore = k

	return minScore

plaintext = "I am trying to break this crypto pal challenge. Let see if I can finish the first set this week. I need to work on over the wire krypton wargame as well to be really good at this stuffs. This is a really hard problem that I need to be able to solve but I am not getting the right result at all. Why is it the lowerest hamming distance is not the correct keysize?"
testkey = " 3J#>"
cipher = util.asciiToHex(util.repeatKeyXor(testkey, plaintext))


print "-------------------beg test2-------------"
result = guessKeySize(cipher)
printScore(sortScore(result)[:3])
print "-------------------end test2-------------"





