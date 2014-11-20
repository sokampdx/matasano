import util

def main():
	s = "YELLOW SUBMARINE"
	size = 20
	output=util.pkcs7pad(s, size)
	print(len(output),output)
main()
