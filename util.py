#!/bin/python3
#https://github.com/mmueller/cryptopals/

import base64
import binascii
import itertools
import difflib
import collections
import string

# hex <-> bytes
def hex2byte(h):
	return bytes([int('0x'+h[n:n+2],16) for n in range(0, len(h), 2)])
	#return bytes.fromhex(h)
	#return binascii.unhexlify(h)

def byte2hex(b):
	return ''.join([hex(n)[2:].rjust(2,'0') for n in b])
	#return binascii.b2a_hex(b).decode()
	#return binascii.hexlify(b).decode()

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
	return bytes(map(lambda a, b: a^b, plainbyte, itertools.cycle(keybyte)))
	#return bytes([b1 ^ b2 for b1, b2 in zip(plainbyte, itertools.cycle(keybyte))])	
	#return ''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(plainbyte, itertools.cycle(chr(keybyte))))

def xor_str(plaintext, key):
	return ''.join(chr(c ^ ord(key)) for c in plaintext) 

# single byte xor cipher
freq_str = "etaoinsrhdlucmfywgpbvkxqjz"

def find_single_byte_xor_of(ciphertext):
	match = (0.0, None, None)
	for key in range(256):
		plaintext = xor_str(ciphertext, chr(key))
		score = string_closeness(freq_profile(plaintext), freq_str)
		if score > match[0]:
			match = (score, chr(key), plaintext)
	return match[1:]

# return a string where the most freq alphabet listed first
def freq_profile(text):	
	freq = collections.Counter(text.lower())
	return "".join(map(lambda x: x[0], freq.most_common()))

# higher score mean better closeness
def string_closeness(text1, text2):
	return difflib.SequenceMatcher(None, text1, text2).quick_ratio()
	#seq_matcher = difflib.SequenceMatcher(None, text1, text2)
	#return seq_matcher.quick_ratio()
	


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
	freqStr = "etaoinsrhdlucmfywgpbvkxqjz"
'''
