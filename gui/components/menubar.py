from tkinter import Menu
from user.state import State

import sv_ttk

class MenuBar():
  def __init__(self, root, state : State):
    self.state = state
    self.menubar = Menu(root, tearoff=1)
    self.filemenu = Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Save Workspace")
    self.filemenu.add_command(label="Add")

    self.helpmenu = Menu(self.menubar, tearoff=0)
    self.helpmenu.add_command(label="Video")

    self.theme_menu = Menu(self.menubar, tearoff=0)
    self.theme_menu.add_command(label="Light", command=self.set_light_mode)
    self.theme_menu.add_command(label="Dark", command=self.set_dark_mode)

    self.menubar.add_cascade(label="File", menu=self.filemenu)
    self.menubar.add_cascade(label="Themes", menu=self.theme_menu) 
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)

  def set_light_mode(self):
    self.state.user_settings.theme = "light"
    sv_ttk.set_theme("light")
  def set_dark_mode(self):
    self.state.user_settings.theme = "dark"
    sv_ttk.set_theme("dark")
