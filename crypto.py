#!/bin/python3

from Crypto.Cipher import AES

def decryptAESECB(cipherbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.decrypt(cipherbyte)

def encryptAESECB(plainbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.encrypt(plainbyte)



