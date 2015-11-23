from __future__ import with_statement, absolute_import
import argparse
from vm import Vm


def main():
	parser = argparse.ArgumentParser(description="A Tiny VM written in Python")
	parser.add_argument('--file', dest="filepath", help='the source file')
	args = parser.parse_args()
	with open(args.filepath) as srcfile:
		instance = Vm(srcfile)
		instance.run() 

if __name__ == "__main__":
	main()
