import config
import re

def get_lines():
	file = open(config.file, "r")
	lines = file.readlines()

	return lines


def swap(lines, toDb):
	swapped = []
	for line in lines:
		parts = line.split("=")
		if len(parts) > 1 and parts[0] in config.databases[toDb]:
			changedLine = parts[0] + "=" + config.databases[toDb][parts[0]] + "\n"
			swapped.append(changedLine)
		else:
			swapped.append(line)

	return swapped


def write_file(lines):
	file = open(config.file,"w")

	file.write("".join(lines))
	file.close()



def get_current():
	lines = get_lines()

	regex = re.compile('^DB_HOST')
	db = None

	for line in lines:
		if regex.match(line):
			db =  line.split("=")[1].replace("\n", "")

	name = "None"
	for key, item in config.databases.items():
		if item["DB_HOST"] == db:
			name = key + " - " + item["DB_HOST"]
			

	return name