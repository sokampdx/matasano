#!/bin/python3

import util


def checkECBmode(cipherhexList):
	for cipherhex in cipherhexList:
		blocks = [cipherhex[i:i+32] for i in range(0, len(cipherhex), 32)]
		if len(blocks) != len(set(blocks)):
			print ("AES ECB mode cipher")
			for b in blocks:
				print (b)	


def main():
	filename = "s1c08.txt"
	cipherhexList = open(filename).read().split('\n')
	checkECBmode(cipherhexList)


main()
