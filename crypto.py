#!/bin/python3

from Crypto.Cipher import AES
import util

def pkcs7pad(textbyte, blocksize):
	length = len(textbyte)
	padsize = blocksize - (length % blocksize)
	if padsize == 0:
		padsize = blocksize
	padbyte = textbyte + (padsize * util.str2byte(chr(padsize)))
	return padbyte

def pkcs7unpad(padbyte):
	padsize = padbyte[-1]
	return padbyte[:-padsize]
		
def decryptAESECB(cipherbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.decrypt(cipherbyte)

def encryptAESECB(plainbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.encrypt(plainbyte)

def decryptAESCBC(cipherbyte, keybyte, ivbyte):
	size = AES.block_size
	cipherblock = [cipherbyte[i:(i+size)] for i in range (0, len(cipherbyte), size)]
	plainbyte = ivbyte
	previousblock = ivbyte
	
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


