#!/usr/bin/python
import sys
from tkinter import *
import data_service
import gui_utils 
import utils

master = Tk()

configs = data_service.get_db_opts()
values = [x["name"] for x in configs]


envs = data_service.get_envs()


for i,item in enumerate(envs):
	item["current"] = utils.get_current(item["name"])["name"]
	gui_utils.init_env_menu(master, item, values, i)



Button(master, text='Save', command=lambda: gui_utils.save_changes(envs)).grid(row=len(envs), column=1, sticky=W, pady=4)
Button(master, text='Reload', command=lambda:gui_utils.reload_state(envs) ).grid(row=len(envs), column=2, sticky=W, pady=4)







#w = StringVar()
#w.set("dev")
#
#Label(master, text="First Name").grid(row=0)
#w = Spinbox(master, values=values, textvariable='dev')
#w.grid(row=0, column=1)
#print(w.get())
#
#
#Button(master, text='Save', command=gui_utils.save_changes).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
