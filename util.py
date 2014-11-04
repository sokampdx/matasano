#!/bin/python
import base64
import binascii

def hexToAscii(s):
	return binascii.unhexlify(s)

def asciiToHex(s):
	return binascii.hexlify(s)

def asciiToBase64(s):
	return binascii.b2a_base64(s)

def base64ToAscii(s):
	return binascii.a2b_base64(s)

def xorHexStrings(s1, s2):
	result = ''
	for c1, c2 in zip(hexToAscii(s1), hexToAscii(s2)):
		result += chr(ord(c1) ^ ord(c2))
	return asciiToHex(result)

