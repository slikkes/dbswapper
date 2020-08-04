#!/usr/bin/python
import sys
from tkinter import *
from DataService import DataService
from EnvManager import EnvManager
from GuiService import GuiService 

master = Tk()
data_service = DataService()
env_manager = EnvManager(data_service)
gui_service = GuiService(env_manager)

configs = data_service.get_db_opts()
values = [x["name"] for x in configs]


envs = data_service.get_envs()


for i,item in enumerate(envs):
	item["current"] = env_manager.get_current(item["name"])["name"]
	gui_service.init_env_menu(master, item, values, i)



Button(master, text='Save', command=lambda: gui_service.save_changes(envs)).grid(row=len(envs), column=1, sticky=W, pady=4)
Button(master, text='Reload', command=lambda:gui_service.reload_state(envs) ).grid(row=len(envs), column=2, sticky=W, pady=4)

mainloop()
