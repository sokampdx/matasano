#!/bin/python

import util
import operator

# input a cipher byte stringg
def guessKeySize(b):
	maxSize = 41 
	keySizeScore = []
	for n in range(2, maxSize):
		score = 0.0
		x = 2*n
		repeat = (len(b)//n)//4

		for i in range(int(repeat)):
			bstr1 = b[(i*x):((i+1)*x)]
			bstr2 = b[((i+2)*x):((i+3)*x)]
			#print n, i, str1, str2
			bit1 = util.byte2bit(bstr1)
			bit2 = util.byte2bit(bstr2)
			score += util.hamming(bit1, bit2)
		keySizeScore.append((n, float(score)/n/repeat))
	return keySizeScore

# sort a list of score
def sortScore(scorelist):
	return sorted(scorelist, key=operator.itemgetter(1))


def printScore(scorelist):
	for k in scorelist:
		print (k)

def findMinScore(scorelist):
	minScore = (1, 999.0)
	for k in scorelist:
		if minScore[1] > k[1]:
			minScore = k

	return minScore

def decryptXorBlock(cipher, size):
	blocks = [None]*size
	for i in range(size):
		blocks[i] = cipher[i::size]		

	key = ''
	for b in blocks:
		key += util.find_single_byte_xor_of(b)[1]

	return key

# cipher is in byte, return plaintext byte and key byte and keysize
def breakRepeatKey(cipher):
	resultList = guessKeySize(cipher)
	result = findMinScore(resultList)
	key = decryptXorBlock(cipher, result[0])
	plaintext = util.xor_byte(cipher, util.str2byte(key)).decode()
	return plaintext, key

######### tests ############

def main():
	filename = "s1c6.txt"
	cipherbyte = util.b642byte(open(filename).read().strip('\n'))
	plaintext, key = breakRepeatKey(cipherbyte)

	print ("-------------------beg test3-------------")
	#print (util.str2byte(cipher))
	print ("min score \n", findMinScore(guessKeySize(cipherbyte)))
	#print ("cipher text \n", cipher)
	print ("key \n", key)
	print ("plaintext \n", plaintext)
	print ("-------------------end test3-------------")

def test2():
	plaintext = b"I am trying to break this crypto pal challenge. Let see if I can finish the first set this week. I need to work on over the wire krypton wargame as well to be really good at this stuffs. This is a really hard problem that I need to be able to solve but I am not getting the right result at all. Why is it the lowerest hamming distance is not the correct keysize?"
	testkey = b"if7(2 %d3J#>"
	cipher = util.xor_byte(plaintext, testkey)

	result = guessKeySize(cipher)
	print ("-------------------beg test2-------------")
	printScore(sortScore(result)[:5])
	print ("-------------------end test2-------------")

def test1():
	s1 = b"this is a test"
	s2 = b"wokka wokka!!!"
	b1 = util.byte2bit(s1)
	b2 = util.byte2bit(s2)
	print ("-------------------beg test1-------------")
	print (util.hamming(b1, b2))
	print (util.bit2byte(b1).decode())
	print (util.bit2byte(b2).decode())
	print ("-------------------end test1-------------")



# main interface
test1()
test2()
#main()

