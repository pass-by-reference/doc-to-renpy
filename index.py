import os

from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

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

  cr = ConvertToRenpy(obj.text_chunks, output_file)
  cr.output_renpy_text()

if __name__ == "__main__":
  
  parse_through_documents()
  
