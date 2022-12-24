import os
import logging

from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

def parse_through_documents():

  for filename in os.listdir("docx"):
    path = os.path.join("docx", filename)

    convert(path, filename)

def convert(path: str, filename: str):

  print("Converting {0}".format(filename))

  if filename != "zed.docx":
    return

  document = Document(path)

  for para in document.paragraphs:
    # print(para._p.xml)
    # print(para.style.font.size)
    for run in para.runs:

      if(run.font.size):
        print(run.text + " : " + str(run.font.size.pt))
      else:
        print(run.text)

    # print(para.text + " : " + str(para.style.font.size.pt))

  # for para in document.paragraphs:
  #   print("===================")
  #   print(para.text)
  #   if(para.style.font.size):
  #     print(para.style.font.size.pt)


  # output_file = filename.replace(" ", "_").replace(".docx", "")
  # document = Document(path)
  # obj = Consolidate(document)
  # obj.consolidate_paragraphs()

  # cr = ConvertToRenpy(obj.text_chunks, output_file)
  # cr.output_renpy_text()

def setup_logging():
  format = '%(levelname)s: %(message)s'
  level = logging.DEBUG
  logging.basicConfig(format=format, level=level)

if __name__ == "__main__":
  
  setup_logging()
  parse_through_documents()
  
