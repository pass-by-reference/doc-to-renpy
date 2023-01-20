from user.document import Document
from user.user_settings import UserSettings
from typing import List
import json

from tkinter import StringVar
from constants import SAVED_WORKSPACE

# SAVED_WORKSPACE = "/home/panda/Desktop/Programming/python/tkinter/saved.json"
# SAVED_WORKSPACE = "/Users/panda/Desktop/programming/gui_prototype/saved.json"

CURRENT_DOC_VERSION = "1.0.0"

# choices : List[Document] = []

# def does_file_name_exist(filename: str) -> bool:
#   for document in choices:
#     if filename.lower() == document.filename.lower():
#       return True

#   return False

class State:
  def __init__(self):
    # Maybe add check if state dict is corrupted

    self.doc_list : List[Document] = []
    self.user_settings : UserSettings = UserSettings()
    self.save_file_version : str = CURRENT_DOC_VERSION

  def does_file_name_exist(self, filename: str) -> bool:
    for document in self.doc_list:
      if filename.lower() == document.filename.lower():
        return True

    return False

  def get_document(self, filename: str) -> Document:
    for document in self.doc_list:
      if filename.lower() == document.filename.lower():
        return document

    return None

  def load(self, list_box_var : StringVar):
    try:
      saved_json = open(SAVED_WORKSPACE, "r")
    except FileNotFoundError:
      print("No saved file")
      return

    saved_state_dict : dict = json.load(saved_json)

    if saved_state_dict: # Found save file
      for doc_dict in saved_state_dict.get("documents"): 
        self.doc_list.append(Document(doc_dict=doc_dict))

      self.user_settings = UserSettings(settings_dict=saved_state_dict.get("user_settings"))
      self.save_file_version : str = saved_state_dict.get("save_file_version")

      list_box_var.set(self.doc_list)
      saved_json.close()

  def save(self):

    doc_dict_list : List[dict] = []
    for document in self.doc_list:
      doc_dict : dict = document.dict()
      doc_dict_list.append(doc_dict)

    save_state_dict = {
      "save_file_version": self.save_file_version,
      "user_settings": self.user_settings.dict(),
      "documents": doc_dict_list
    }

    try:
      file = open(SAVED_WORKSPACE, "w")
    except FileNotFoundError:
      return

    json.dump(save_state_dict, file, indent=4)

    file.close()

    
