import argparse
from vm import Vm


def main():
	parser = argparse.ArgumentParser(description="A Tiny VM written in Python")
	parser.add_argument('--file', dest='filename', help='the source file')
	parser.parse_args()
	with open(parser.filename) as srcfile:
		instance = Vm(srcfile)
		instance.run() 

if __name__ == "__main__":
	main()