from tkinter import *
from tkinter import ttk

from user.state import State
from components.menubar import MenuBar
from components.mainframe import MainFrame

import sv_ttk

class AppGui:
  def __init__(self):
    self.root = Tk()
    self.root.title("Doc To Renpy")
    self.state = State()

    self.mainframe = ttk.Frame(self.root, padding=(12,12,12,12))

    self.menubar : MenuBar = MenuBar(self.root, self.state)
    self.mainframe : MainFrame = MainFrame(self.root, self.state)

    self.__init_configure_weights()

  def __init_configure_weights(self):
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)

  def custom_on_close(self):
    # SAVE FEATURE: Disabled for now
    # self.state.save() # Save the file

    self.delete_rpy_docx_from_workspace()

    self.root.destroy()

  def delete_rpy_docx_from_workspace(self):
    for doc in self.state.doc_list:
      doc.remove_files()

  def run(self):
    self.root.config(menu=self.menubar.menubar)
    self.root.resizable(False, False)
    self.root.protocol("WM_DELETE_WINDOW", self.custom_on_close)

    # SAVE FEATURE: Disabled for now
    # self.state.load(self.mainframe.choice_var)
    # sv_ttk.set_theme(self.state.user_settings.theme)

    sv_ttk.set_theme("light")

    self.root.mainloop()

app = AppGui()
app.run()