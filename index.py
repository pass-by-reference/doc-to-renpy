import os
import logging

from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

from gui.app import AppGui

def parse_through_documents():

  for filename in os.listdir("docx"):
    path = os.path.join("docx", filename)

    convert(path, filename)

def convert(path: str, filename: str):

  print("Converting {0}".format(filename))

  output_file = filename.replace(" ", "_").replace(".docx", "")
  document = Document(path)
  obj = Consolidate(document)
  obj.consolidate_paragraphs()

  cr = ConvertToRenpy(document, obj.text_chunks, output_file)
  cr.output_renpy_text()

def setup_logging():
  format = '%(levelname)s: %(message)s'
  level = logging.DEBUG
  logging.basicConfig(format=format, level=level)

if __name__ == "__main__":

  app = AppGui()
  app.run()

  # setup_logging()
  # parse_through_documents()
  
