import crypto

def main():
	s = b"YELLOW SUBMARINE"
	size = 20
	output=crypto.pkcs7pad(s, size)
	print(len(output),output)
main()
