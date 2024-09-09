import sys
import random
from collections import deque

def parseInput(filepath):
	names = []
	with open(sys.argv[1], 'r') as file:
		for line in file:
			names.append(line.strip())
	random.shuffle(names)
	return deque(names)

def printNames(names):
	print("")
	while names:
		if len(names)%3 == 2:
			print("    "+names.popleft()+", "+names.popleft()+"\n    ")
		if len(names)%3 == 1:
			print("    "+names.popleft()+", "+names.popleft()+"\n    ")
			print("    "+names.popleft()+", "+names.popleft()+"\n    ")
		else:
			print("    "+names.popleft()+", "+names.popleft()+", "+names.popleft()+"\n    ")


def main():
	if len(sys.argv) != 2:
		print(" Usage: python puzzle.py <names.txt>\n")
		return

	names = parseInput(sys.argv[1])

	printNames(names)

if __name__ == "__main__":
	main()