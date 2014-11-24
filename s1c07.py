#!/bin/python3

from Crypto.Cipher import AES
import util

key = b"YELLOW SUBMARINE"

def decryptAESECB(cipherbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.decrypt(cipherbyte)

def encryptAESECB(plainbyte, keybyte):
	aesObj = AES.new(keybyte)
	return aesObj.encrypt(plainbyte)

def main():
	filename = "s1c7.txt"
	cipherbyte = util.b642byte(open(filename).read().strip('\n'))
	print (decryptAESECB(cipherbyte, key).decode())

main()
	

