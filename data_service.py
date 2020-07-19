import json

def _get_db():
	db = open("db.json", "r")
	return json.load(db)


def get_db_opts():
	db = _get_db()

	configs = db["db_configs"]
	
	return [{"_id": x["_id"], "name": x["name"]} for x in configs]


def get_envs():
	db = _get_db()
	return db["envs"]

def find_env_by_name(name):
	db = _get_db()

	envs = [item for item in db["envs"] if item["name"] == name]

	return None if len(envs) == 0 else envs[0]


def find_config_by_host(host):
	db = _get_db()

	configs = list(filter(lambda x: x["conf_data"]["DB_HOST"] == host, db["db_configs"]))

	return None if len(configs) == 0 else configs[0]

def find_config_by_name(name):
	db = _get_db()

	configs = list(filter(lambda x: x["name"] == name, db["db_configs"]))
	return None if len(configs) == 0 else configs[0]

