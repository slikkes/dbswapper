import sys
import utils

def main(params):

	if params[1] == "swap":
		utils.swap_db(params[2], params[3])

		print(params[2] + "swapped to: " + params[3])

	if params[1] == "which":
		db = utils.get_current(params[2])
		msg = db["name"] + " - " + db["conf_data"]["DB_HOST"]

		print("current db: " + msg)

# call from cli like: 
# python3 dbswapper.py option
# options: ["prod", "dev"]
main(sys.argv)