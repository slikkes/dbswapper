
conf = dict(
	prod = dict(
		DB_CONNECTION="mysql",
		DB_HOST="10.0.2.1",
		DB_PORT="3306",
		DB_DATABASE="prod",
		DB_USERNAME="produser",
		DB_PASSWORD="yxcvawr"
		),
	dev = dict(
		DB_CONNECTION="localhost",
		DB_HOST="127.0.0.1",
		DB_PORT="3306",
		DB_DATABASE="homestead",
		DB_USERNAME="root",
		DB_PASSWORD="vagrant"
		)
	)


def get_lines():
	file = open(".env", "r")
	lines = file.readlines()

	return lines


def swap(lines, toDb):
	swapped = []
	for line in lines:
		parts = line.split("=")
		if len(parts) > 1 and parts[0] in conf[toDb]:
			changedLine = parts[0] + "=" + conf[toDb][parts[0]] + "\n"
			swapped.append(changedLine)
		else:
			swapped.append(line)

	return swapped


def write_file(lines):
	file = open(".env","w")

	file.write("".join(lines))
	file.close()
