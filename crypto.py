#!/bin/python3

from Crypto.Cipher import AES
import util

def pkcs7pad(textbyte, blocksize):
	length = len(textbyte)
	padsize = blocksize - (length % blocksize)
	padbyte = textbyte + (padsize * util.str2byte(chr(padsize)))
	return padbyte

def pkcs7unpad(padbyte):
	result = padbyte
	if ispkcs7(padbyte):
		result = padbyte[:-padbyte[-1]]
	return result
		

def ispkcs7(padbyte):
	pad = padbyte[(-padbyte[-1:]):]
	return (len(pad) == ord(pad[0])) and (pad == len(pad) * s[0])	 


def decryptAESECB(cipherbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.decrypt(cipherbyte)

def encryptAESECB(plainbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.encrypt(plainbyte)

def decryptAESCBC(cipherbyte, keybyte, ivbyte):
	sz = AES.block_size
	cipherblock = [cipherbyte[i:(i+sz)] for i in range (0, len(cipherbyte), sz)]
	plainbyte = ivbyte[:]
	previousblock = ivbyte[:]
	
	for currentblock in cipherblock:
		plainbyte += util.xor_byte(decryptAESECB(currentblock, keybyte), previousblock)
		previousblock = currentblock

	return pkcs7unpad(plainbyte)

def encryptAESCBC(plainbyte, keybyte, ivbyte):
	sz = AES.block_size
	plainblock = [plainbyte[i:(i+sz)] for i in range (0, len(plainbyte), sz)] 	
#	if (len(plainblock[:-1]) < sz):
#		plainblock[:-1] = pkcs7pad(plainblock[:-1]

	cipherbyte = ivbyte[:]
	previousblock = ivbyte[:]
	
	for currentblock in plainblock:
		previousblock = encryptAESECB(util.xor_byte(currentblock, previousblock), keybyte) 
		cipherbyte += previousblock
	return cipherbyte


