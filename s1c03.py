#!/bin/python3

import util

hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print (hexStr)
print (util.find_single_byte_xor_of(util.hex2byte(hexStr)))
