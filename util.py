#!/bin/python3
#https://github.com/mmueller/cryptopals/

import base64
import binascii
import itertools
import difflib
import collections
import string
import bitstring

# find string message (not byte) size
def pkcs7pad(s, blocksize):
	length = len(s)
	padsize = blocksize - (length % blocksize)
	padstr = s + (padsize * chr(padsize))
	return padstr
	
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
	return ''.join(chr(c ^ ord(k)) for c, k in zip(plaintext, itertools.cycle(key))) 

# single byte xor cipher
def find_single_byte_xor_of(cipherbyte):
	match = (0.0, None, None)
	for key in range(256):
		plaintext = xor_str(cipherbyte, chr(key))
		if all(c in string.printable for c in plaintext):
			score = string_scoring(plaintext)
			if score > match[0]:
				match = (score, chr(key), plaintext)
	return match

# return a string where the most freq alphabet listed first
def freq_profile(text):	
	freq = collections.Counter(text.lower())
	return "".join(map(lambda x: x[0], freq.most_common()))

# higher score mean better match to freqency string
freq_str = " etaoinsrhdlucmfywgpbvkxqjz"
freqDict = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':12.7, 
	 		'f':2.2, 'g':2.0, 'h':6.1, 'i':7.0, 'j':0.2, 
		    'k':0.8, 'l':4.0, 'm':2.4, 'n':6.7, 'o':7.5, 
	    	'p':1.9, 'q':0.1, 'r':6.0, 's':6.3, 't':9.1,
			'u':2.8, 'v':1.0, 'w':2.4, 'x':0.2, 'y':2.0, 'z':0.1}

freqDictSpace = {' ':18.29, 'e':10.27, 't':7.52, 'a':6.53,
				 'o':6.16, 'n':5.71, 'i':5.67, 's':5.32,
				 'r':4.99, 'h':4.98, 'l':3.32, 'd':3.28,
				 'u':2.28, 'c':2.23, 'm':2.03, 'f':1.98,
				 'w':1.70, 'g':1.62, 'p':1.50, 'y':1.43,
				 'b':1.26, 'v':0.80, 'k':0.56, 'x':0.14,
				 'j':0.10, 'q':0.08, 'z':0.05}

freql = 10
fst = 5
snd = 10
weight = 3

'''
# using variance of the different in frequency value to return a score
def string_scoring(text1):
	score = 0.0
	freq = collections.Counter(text1.lower())
	length = len(text1)	/ 100
	for key in freq:
		if key in freq_str:
			score += ((freq[key]/length) - freqDictSpace[key])**2
	print (score, freq)
	return (1/score)
'''

# string profile segment match against frequency 
def string_match(text1, start, end):
	return difflib.SequenceMatcher(None, (freq_profile(text1))[start:end], freq_str[start:end]).quick_ratio()
	
# using sequence matcher to return a score
# fast with mix result
def string_scoring(text1):
	top = string_match(text1, 0, freql) * weight
	bottom = string_match(text1, freql, 27)
	return top + bottom
	#seq_matcher = difflib.SequenceMatcher(None, text1, text2)
	#return seq_matcher.quick_ratio()


'''
# using levenshtein to return a score
# fast with mix result
def string_scoring(text1):
	return levenshtein(freq_profile(text1)[:freql], freq_str[:freql])	
'''

# levenshtein scoring between 2 text
def levenshtein(s1, s2):
	if len(s1) < len(s2):
		return levenshtein(s2, s1)

	if len(s2) == 0:
		return len(s1)

	previous = range(len(s2) + 1)
	for i, c1 in enumerate(s1):
		current = [i+1]
		for j, c2 in enumerate(s2):
			insert = previous[j+1] + 1
			delete = current[j] + 1
			substitute = previous[j] + (c1 != c2)
			current.append(min(insert, delete, substitute))
		previous = current
	return previous[-1]

'''
# using word match in dictionary to return a score
# slowest but most acurate
filename = b"/usr/share/dict/words"
def string_scoring(searchStr):
	dictionary = open(filename).read()
	score = 0
	wordList = searchStr.split()
	dictList = dictionary.split()

	for dictWord in dictList:
		for word in wordList:
			if word == dictWord:
				score += 1
	return score
'''

# bit utilities
def byte2bit(b):
	return bitstring.Bits(bytes=b)

def bit2byte(b):
	return b.tobytes()

def hex2bit(h):
	return byte2bit(hex2byte(h))

def bit2hex(b):
	return b.hex

# count xor of 2 bitstring
def hamming(b1, b2):
	assert(len(b1) == len(b2))
	return (b1 ^ b2).count(1)



