from enum import Enum
import shutil
import os
import logging

from tkinter import messagebox
from renpy_doc_convert.api import convert

from gui.constants import DOCX_FILE_PATH, RPY_FILE_PATH

def get_name_from_path(path : str) -> str:
  path_parts = path.rsplit("/")

  last_index = len(path_parts) - 1

  return path_parts[last_index]

class DocumentStatus(Enum):
  NOT_CONVERTED = 0
  CONVERTED = 1
  ERROR = 2

class Document:
  def __init__(self, 
    docx_file_path : str = None,
    doc_dict : dict = None
  ):
    if(docx_file_path):
      self._init_from_new(docx_file_path)
    elif(doc_dict):
      self._init_from_dict(doc_dict)

  def _init_from_new(self, docx_file_path):
    if docx_file_path is None:
      raise FileNotFoundError("File not found")

    self.filename = get_name_from_path(docx_file_path)
    self.renpy_file_path = ""
    self.docx_file_path = ""
    self.status : DocumentStatus = DocumentStatus.NOT_CONVERTED

    self._copy_file(docx_file_path)

  def _init_from_dict(self, doc_dict : dict):
    self.filename = doc_dict.get("filename")
    self.renpy_file_path = doc_dict.get("renpy_file_path")
    self.docx_file_path = doc_dict.get("docx_file_path")
    self.status = Document.string_to_status(doc_dict.get("status"))

  def _copy_file(self, incoming_file_path : str):
    self.docx_file_path = "{0}/{1}".format(DOCX_FILE_PATH, self.filename)
    shutil.copyfile(incoming_file_path, self.docx_file_path)

  def convert(self):
    filename_no_extension = self.filename.split('.')[0]
    self.renpy_file_path = "{0}/{1}".format(RPY_FILE_PATH, filename_no_extension)

    try:
      # Calls into renpy_doc_convert module
      convert(self.docx_file_path, self.renpy_file_path)
      self.status : DocumentStatus = DocumentStatus.CONVERTED
    except Exception as err:
      self.status : DocumentStatus = DocumentStatus.ERROR
      messagebox.showerror("Convert Error", err)
      logging.error(err)

  def on_select(self) -> str:
    if self.status == DocumentStatus.NOT_CONVERTED:
      return "File Has Not Been Converted"
    elif self.status == DocumentStatus.CONVERTED:
      return self._open_rpy_file()
    elif self.status == DocumentStatus.ERROR:
      return "Error with opening rpy file"
    else:
      return ""

  def _open_rpy_file(self) -> str:
    try:
      rpy = open(self.renpy_file_path, "r")
    except FileNotFoundError:
      print("Cannot find renpy file. Did you modify your appdata")
      return "Error"

    text = ""
    try:
      text = rpy.read()
    except Exception as e:
      print(e)
      self.status : DocumentStatus = DocumentStatus.ERROR
      return "Error with opening renpy file"
      
    rpy.close()
    return text

  def remove_files(self):
    if (self.docx_file_path != "" and
        os.path.isfile(self.docx_file_path)):
      try:
        os.remove(self.docx_file_path)
      except FileNotFoundError:
        print("Cannot remove ${0}".format(self.docx_file_path))
    
    if (self.renpy_file_path != "" and
        os.path.isfile(self.renpy_file_path)):
      try:
        os.remove(self.renpy_file_path)
      except FileNotFoundError:
        print("Cannot remove ${0}".format(self.renpy_file_path))

  def overwrite(self, incoming_file_path):
    self.remove_files()
    self._copy_file(incoming_file_path)
    self.status = DocumentStatus.NOT_CONVERTED

  @staticmethod
  def status_to_string(status: DocumentStatus) -> str:
    if status == DocumentStatus.NOT_CONVERTED:
      return "NOT_CONVERTED"
    elif status == DocumentStatus.CONVERTED:
      return "CONVERTED"
    elif status == DocumentStatus.ERROR:
      return "ERROR"
    else:
      return ""

  @staticmethod
  def string_to_status(status: str) -> DocumentStatus:
    if status == "NOT_CONVERTED":
      return DocumentStatus.NOT_CONVERTED
    elif status == "CONVERTED":
      return DocumentStatus.CONVERTED
    elif status == "ERROR":
      return DocumentStatus.ERROR
    else:
      return DocumentStatus.NOT_CONVERTED

  def dict(self) -> dict:
    return {
      "filename": self.filename,
      "status": Document.status_to_string(self.status),
      "renpy_file_path": self.renpy_file_path,
      "docx_file_path": self.docx_file_path
    }

  def __str__(self):
    return self.filename


