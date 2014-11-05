#!/bin/python

import util
import string

freqTable = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3,
				 'e':12.7, 'f':2.2, 'g':2.0, 'h':6.1,
				 'i':7.0, 'j':0.2, 'k':0.8, 'l':4.0,
				 'm':2.4, 'n':6.7, 'o':7.5, 'p':1.9,
				 'q':0.1, 'r':6.0, 's':6.3, 't':9.1,
				 'u':2.8, 'v':1.0, 'w':2.4, 'x':0.2,
				 'y':2.0, 'z':0.1} 

freq = "etaoinsrhdlucmfywgpbvkxqjz"
char = string.ascii_lowercase+string.ascii_uppercase+string.digits
hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
filename = "/usr/share/dict/words"

# find the xor encoding for hexString
def findBestFit(hexString):
	cipher = util.hexToAscii(hexString)
	length = len(cipher)
	maxScore = 0

	for key in char:
		decipher = util.xorStrings(cipher, key*length)
		score = profiles(decipher)
		if maxScore < score:
			maxScore = score
			maxKey = key
			plaintext = decipher		
		#print score, '\n', decipher, '\n', '-'*length, '\n'
	return plaintext, maxKey


# using frequency as scoring criteria
def profiles2(searchString):
	score = 0.0
	for c in string.lower(searchString):
		if c in freq:
			score += freqTable[c]
	return score

# using dictionary words as scoring criteria
def profiles(searchString):
	dictionary = open(filename).read()
	
	score = 0
	wordList = searchString.split()
	dictList = dictionary.split()
	for word in wordList:
		for dictWord in dictList:
			if word == dictWord:
				score += 1 
	return score

# main interface
def main():
	print findBestFit(hexString)


# call main
main()


