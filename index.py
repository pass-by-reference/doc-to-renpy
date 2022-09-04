import os

from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

def parse_through_documents():

  for filename in os.listdir("docx"):
    f = os.path.join("docx", filename)

    convert(f)

def convert(filename):

  output_file = filename.split(".docx")[0].replace(" ", "_").split("docx/")[1]
  document = Document(filename)
  obj = Consolidate(document)
  obj.consolidate_paragraphs()

  cr = ConvertToRenpy(obj.text_chunks, output_file)
  cr.output_renpy_text()

if __name__ == "__main__":
  
  parse_through_documents()
  
