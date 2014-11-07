#!/bin/python3
import base64
import binascii
import string
import bitstring

def asciiTobits(s): #
	return bitstring.Bits(bytes=s)

def bitsToAscii(b): #
	return b.tobytes()

def hexTobits(h): #
	return asciiTobits(hexToAscii(h))

def bitsTohex(h): #
	return b.hex
 
def hexToAscii(h): 
	return binascii.a2b_hex(h)

def asciiToHex(s): 
	return binascii.b2a_hex(s)

def asciiToBase64(s):
	return binascii.b2a_base64(s)

def base64ToAscii(s):
	return binascii.a2b_base64(s)

def xorHexStrings(h1, h2): #
	return asciiToHex(xorStrings(hexToAscii(h1), hexToAscii(h2)))

def xorStrings(s1,s2): #
	result = ''
	for c1, c2 in zip(s1, s2):
		result += chr(c1 ^ c2)
	return bytes(result, 'utf-8')

def testSingleXor(searchStr): #
	char = string.ascii_letters + string.digits + ' '

	# local dictionary file
	filename = "/usr/share/dict/words"

	def wordProfiler(searchStr):
		dictionary = open(filename).read()
		score = 0
		wordList = searchStr.split()
		dictList = dictionary.split()
		
		for word in wordList:
			for dictWord in dictList:
				if word == dictWord:
					score += 1
		return score

	def findXor(searchStr):
		cipher = hexToAscii(searchStr)
		length = len(cipher)
		maxSet = 0, 'a', ''

		for key in char:
			decipher = xorStrings(cipher, key*length)
			score = charProfiler(decipher)
			if maxSet[0] < score:
				maxSet = score, key, decipher
			# print maxSet
		return maxSet

	def charProfiler(searchStr):
		score = 0
		for c in searchStr:
			if c in char:
				score += 1
		return float(score)/len(searchStr)
		#return float("{0:.3f}".format(float(score)/len(searchStr)))

	# main
	return findXor(searchStr)

def repeatKeyXor(key, plaintext): #
	keyLen = len(key)
	length = len(plaintext)
	xorKey = key*(length//keyLen) + key[:(length % keyLen)]
	
	return xorStrings(plaintext, xorKey)

def hamming(b1, b2): #
	return (b1 ^ b2).count(1)


'''
	# frequency alphabet dictionary
	freqDict = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':12.7, 
		 		'f':2.2, 'g':2.0, 'h':6.1, 'i':7.0, 'j':0.2, 
			    'k':0.8, 'l':4.0, 'm':2.4, 'n':6.7, 'o':7.5, 
		    	'p':1.9, 'q':0.1, 'r':6.0, 's':6.3, 't':9.1,
				'u':2.8, 'v':1.0, 'w':2.4, 'x':0.2, 'y':2.0, 'z':0.1}
	freqSeq = "etaoinsrhdlucmfywgpbvkxqjz"
'''
