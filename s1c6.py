#!/bin/python

import util

s1 = "this is a test"
s2 = "wokka wokka!!!"


b1 = util.tobits(s1)
b2 = util.tobits(s2)

print util.hamming(b1, b2)
print util.frombits(b1)
print util.frombits(b2)


test1 = util.tobits("ABCDEFGHIJKLMNOPQRSTUVWX")
key2 = util.tobits("ICE"*8)
print util.hamming(test1, key2)
