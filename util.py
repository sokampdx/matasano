#!/bin/python3
#https://github.com/mmueller/cryptopals/

import base64
import binascii
import itertools
import struct


# hex <-> bytes
def hex2byte(h):
	return bytes.fromhex(h)

def byte2hex(b):
	return binascii.b2a_hex(b).decode()

# hex <-> string
def hex2str(h, encoding='utf-8'):
	return binascii.a2b_hex(h).decode(encoding=encoding)

def str2hex(s):
	return byte2hex(str2byte(s))

# bytes <-> base64
def byte2b64(b):
	return base64.b64encode(b).decode()

def b642byte(b):
	return base64.b64decode(b)

# hex <-> base64
def hex2b64(h):
	return byte2b64(hex2byte(h))

def b642hex(b):
	return byte2hex(b642byte(b))

# string <-> byte
def str2byte(s):
	return bytes(s, encoding='utf-8')

def byte2str(b):
	return b.decode()

# string <-> base64
def str2b64(s):
	return base64.b64encode(s)

def b642str(b):
	return base64.b64decode(b).decode()

# byte xor function
def xor_hex(plainhex, keyhex):
	return xor_byte(hex2byte(plainhex), hex2byte(keyhex))

def xor_byte(plainbyte, keybyte):
	return bytes([b1 ^ b2 for b1, b2 in zip(plainbyte, itertools.cycle(keybyte))])	

def xor_str(plaintext, key):
	return xor_byte(str2byte(plaintext), str2byte(key))



'''
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

def xorHexStrings(h1, h2):
	return asciiToHex(xorStrings(hexToAscii(h1), hexToAscii(h2)))

def xorStrings(s1,s2):
	result = ''
	print (s1, s2)
	for c1, c2 in zip(s1, s2):
		result += chr(c1 ^ c2)
	return bytes(result, 'utf-8')

def testSingleXor(searchStr): #
	char = string.ascii_letters + string.digits + ' '
	#char = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'	
	
	# local dictionary file
	filename = b"/usr/share/dict/words"

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
		maxSet = 0, b'', b''

		for c in char:
			print (c)
			key = bytes(c * length, 'utf-8')
			decipher = xorStrings(cipher, key)
			score = charProfiler(decipher)
			if maxSet[0] < score:
				maxSet = score, key, decipher
			# print maxSet
		return maxSet

	def charProfiler(searchStr):
		score = 0
		for c in searchStr:
			match = chr(c)
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


'''
	# frequency alphabet dictionary
	freqDict = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':12.7, 
		 		'f':2.2, 'g':2.0, 'h':6.1, 'i':7.0, 'j':0.2, 
			    'k':0.8, 'l':4.0, 'm':2.4, 'n':6.7, 'o':7.5, 
		    	'p':1.9, 'q':0.1, 'r':6.0, 's':6.3, 't':9.1,
				'u':2.8, 'v':1.0, 'w':2.4, 'x':0.2, 'y':2.0, 'z':0.1}
	freqSeq = "etaoinsrhdlucmfywgpbvkxqjz"
'''
