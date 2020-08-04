import json

class DataService:
	def __init__(self):
		self.db = self._get_db()

	def get_db_opts(self):
	
		configs = self.db["db_configs"]
		
		return [{"_id": x["_id"], "name": x["name"]} for x in configs]
	
	def get_envs(self):
		return self.db["envs"]
	
	def find_env_by_name(self, name):
	
		envs = [item for item in self.db["envs"] if item["name"] == name]
	
		return None if len(envs) == 0 else envs[0]
	
	
	def find_config_by_host(self, host):
	
		configs = list(filter(lambda x: x["conf_data"]["DB_HOST"] == host, self.db["db_configs"]))
	
		return None if len(configs) == 0 else configs[0]
	
	def find_config_by_name(self, name):
	
		configs = list(filter(lambda x: x["name"] == name, self.db["db_configs"]))
		return None if len(configs) == 0 else configs[0]

	def _get_db(self):
		db = open("db.json", "r")
		return json.load(db)
	
	