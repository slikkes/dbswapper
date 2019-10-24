import sys
import utils

def main(toDb):
	lines = utils.get_lines()
	lines = utils.swap(lines, toDb)
	utils.write_file(lines)

	print("swapped to: " + toDb)

# call from cli like: 
# python3 dbswapper.py option
# options: ["prod", "dev"]
main(sys.argv[1])