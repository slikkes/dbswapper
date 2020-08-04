import sys
from DataService import DataService
from EnvManager import EnvManager

def main(params):
	
	data_service = DataService()
	env_manager = EnvManager(data_service)

	if params[1] == "swap":
		env_manager.swap_db(params[2], params[3])

		print(params[2] + " swapped to: " + params[3])

	if params[1] == "which":
		db = env_manager.get_current(params[2])
		msg = db["name"] + " - " + db["conf_data"]["DB_HOST"]

		print("current db: " + msg)

# call from cli like: 
# python3 dbswapper.py option
# options: ["prod", "dev"]
main(sys.argv)