#!/bin/python3

import util

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def main():
	print ("hex string ----------------------------")
	print (hexString)
	print ("from hex to ascii ---------------------")
	print (util.hex2str(hexString))
	print ("from hex to base64 --------------------")
	print (util.hex2b64(hexString))
	print ("b64 string ----------------------------")
	print (b64String)
	print ("from base64 to ascii ------------------")
	print (util.b642str(b64String))
	print ("from base64 to hex --------------------")
	print (util.b642hex(b64String))

main()



