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
