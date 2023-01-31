from tkinter import Menu
from gui.user.state import State

import sv_ttk

class MenuBar():
  def __init__(self, root, state : State):
    self.state = state
    self.menubar = Menu(root, tearoff=1)

    self.theme_menu = Menu(self.menubar, tearoff=0)
    self.theme_menu.add_command(label="Light", command=self.set_light_mode)
    self.theme_menu.add_command(label="Dark", command=self.set_dark_mode)

    self.menubar.add_cascade(label="Themes", menu=self.theme_menu) 
  def set_light_mode(self):
    self.state.user_settings.theme = "light"
    sv_ttk.set_theme("light")
  def set_dark_mode(self):
    self.state.user_settings.theme = "dark"
    sv_ttk.set_theme("dark")
