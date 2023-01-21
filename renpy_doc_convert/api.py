from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

def convert(docx_file_path: str, renpy_file_path : str):

  document = Document(docx_file_path)
  obj = Consolidate(document)
  obj.consolidate_paragraphs()

  cr = ConvertToRenpy(document, obj.text_chunks, renpy_file_path)
  cr.output_renpy_text()

