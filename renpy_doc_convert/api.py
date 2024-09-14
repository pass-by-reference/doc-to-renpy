from docx import Document
from renpy_doc_convert.consolidate import Consolidate
from renpy_doc_convert.to_renpy import ConvertToRenpy

import logging

DOC_TO_RENPY_VERSION="1.1.0"

def convert(docx_file_path: str, renpy_file_path : str):

  logging.debug("Docx File->{0}".format(docx_file_path))
  logging.debug("Renpy File->{0}".format(renpy_file_path))

  document = Document(docx_file_path)
  logging.debug("Finish getting document object from dependency docx")
  obj = Consolidate(document)
  obj.consolidate_paragraphs()
  logging.debug("Finish consolidating docx text to chunks")

  cr = ConvertToRenpy(document, obj.text_chunks, renpy_file_path)
  cr.output_renpy_text()
  logging.debug("Finish outputting renpy text from text chunks")

