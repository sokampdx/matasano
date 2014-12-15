#!/bin/python3

import crypto
import util

key = b"YELLOW SUBMARINE"


def main():
	filename = "s1c07.txt"
	cipherbyte = util.b642byte(open(filename).read().strip('\n'))
	plainbyte = crypto.decryptAESECB(cipherbyte, key).decode()
	print (plainbyte)
	print (open(filename).read())
	print ((crypto.encryptAESECB(plainbyte, key)).byte())
		
main()
	

