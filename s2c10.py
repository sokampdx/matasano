#!/bin/python3

import util
import crypto

filename = 's2c10.txt'
ciphertext = open(filename).read().split('\n')
#print(ciphertext)
size = crypto.AES.block_size
iv = chr(0)*size

cipherbyte = util.b642byte(''.join(ciphertext))
#print (cipherbyte)
ivbyte = util.str2byte(iv)
keybyte = b'YELLOW SUBMARINE'

result = crypto.decryptAESCBC(cipherbyte, keybyte, ivbyte)
print(util.byte2str(result[(size):]))

#verify=crypto.AES.new(keybyte, crypto.AES.MODE_CBC, ivbyte)
#print (verify.decrypt(cipherbyte))
