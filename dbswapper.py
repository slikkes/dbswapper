import sys
import utils

def main(command, toDb):
	if command == "swap":
		lines = utils.get_lines()
		lines = utils.swap(lines, toDb)
		utils.write_file(lines)

		print("swapped to: " + toDb)

	if command == "which":
		print("current db: " + utils.get_current())

# call from cli like: 
# python3 dbswapper.py option
# options: ["prod", "dev"]
command = sys.argv[1]
param = sys.argv[2] if len(sys.argv) == 3 else None
main(command, param)