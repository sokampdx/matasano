#!/bin/python3

import util
import crypto

filename = 's2c10.txt'
ciphertext = open(filename).read().split('\n')
sz = crypto.AES.block_size
iv = chr(0)*sz

cipherbyte = util.str2byte(''.join(ciphertext))
print (cipherbyte)
ivbyte = util.str2byte(iv)
keybyte = b'YELLOW SUBMARINE'

result = crypto.decryptAESCBC(cipherbyte, keybyte, ivbyte)

print(result[(crypto.AES.block_size):])


verify=crypto.AES.new(keybyte, crypto.AES.MODE_CBC, ivbyte)

print (verify.decrypt(cipherbyte))
