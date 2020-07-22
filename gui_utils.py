from tkinter import *
import utils

def save_changes(envs):
	for env in envs:
		if is_chaged(env):
			to_db = env["var"].get()
			utils.swap_db(env["name"],to_db)
			env["current"] = to_db



def is_chaged(item):
	return item["var"].get() != item["current"]

def init_env_menu(parent, env, values, row):
	Label(parent, text=env["name"]).grid(row=row)

	env["var"] = StringVar(parent)
	env["var"].set(env["current"])
	env["menu"] = OptionMenu(parent, env["var"], *values)
	env["menu"].grid(row=row, column=1)

def reload_state(envs):
	#if env changed???
	for env in envs:
		curr = utils.get_current(env["name"])["name"]
		env["var"].set(curr)
		env["current"] = curr
