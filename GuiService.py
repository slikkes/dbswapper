from tkinter import *

class GuiService:
	def __init__(self, _env_manager):
		self.env_manager = _env_manager


	def save_changes(self, envs):
		for env in envs:
			if self.is_chaged(env):
				to_db = env["var"].get()
				self.env_manager.swap_db(env["name"],to_db)
				env["current"] = to_db



	def is_chaged(self, item):
		return item["var"].get() != item["current"]

	def init_env_menu(self, parent, env, values, row):
		Label(parent, text=env["name"]).grid(row=row)

		env["var"] = StringVar(parent)
		env["var"].set(env["current"])
		env["menu"] = OptionMenu(parent, env["var"], *values)
		env["menu"].grid(row=row, column=1)

	def reload_state(self, envs):
		#if env changed???
		for env in envs:
			curr = self.env_manager.get_current(env["name"])["name"]
			env["var"].set(curr)
			env["current"] = curr
