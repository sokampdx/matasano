#!/bin/python

import util

hexS1 = "1c0111001f010100061a024b53535009181c"
hexS2 = "686974207468652062756c6c277320657965"
result = "746865206b696420646f6e277420706c6179"

def main():
	print "hex string 1 -----------------------"
	print hexS1
	print "hex string 2 -----------------------"
	print hexS2
	print "result xor -------------------------"
	print util.xorHexStrings(hexS1, hexS2)

main()
