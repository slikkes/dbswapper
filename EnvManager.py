import re

class EnvManager:
	def __init__(self, _data_service):
		self.data_service = _data_service

	def swap_db(self, env, toDb):
		config = self.data_service.find_config_by_name(toDb)
		env = self.data_service.find_env_by_name(env)

		lines = self.get_lines(env["env_path"])
		lines = self.swap(lines, config)
		self.write_file(lines, env["env_path"])


	def get_current(self, env_name):
		env = self.data_service.find_env_by_name(env_name)

		lines = self.get_lines(env["env_path"])

		regex = re.compile('^DB_HOST')
		db = None

		for line in lines:
			if regex.match(line):
				db =  line.split("=")[1].replace("\n", "")

		return self.data_service.find_config_by_host(db)

	def get_lines(self, env_path):
		file = open(env_path, "r")
		lines = file.readlines()
		file.close()

		return lines


	def swap(self, lines, config):
		conf_keys = config["conf_data"].keys()

		swapped = []
		for line in lines:
			parts = line.split("=")
			if len(parts) > 1 and parts[0] in conf_keys:
				changedLine = parts[0] + "=" + config["conf_data"][parts[0]] + "\n"
				swapped.append(changedLine)
			else:
				swapped.append(line)

		return swapped


	def write_file(self, lines, path):
		file = open(path,"w")

		file.write("".join(lines))
		file.flush()
		file.close()

