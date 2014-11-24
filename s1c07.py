#!/bin/python3

import crypto
import util

key = b"YELLOW SUBMARINE"


def main():
	filename = "s1c07.txt"
	cipherbyte = util.b642byte(open(filename).read().strip('\n'))
	print (crypto.decryptAESECB(cipherbyte, key).decode())

main()
	

