#!/bin/python

import util

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def main():
	print ("hex string ----------------------------")
	print (hexString)
	print ("from hex string to ascii (binary) -----")
	print (util.hexToAscii(hexString))
	print ("from ascii (binary) to base64 ---------")
	print (util.asciiToBase64(util.hexToAscii(hexString)))
	print ("from base64 to ascii (binary) ---------")
	print (util.base64ToAscii(b64String))
	print ("from ascii (binary) to hex string -----")
	print (util.asciiToHex(util.base64ToAscii(b64String)))

main()



