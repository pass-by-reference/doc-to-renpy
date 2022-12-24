import unittest

from renpy_doc_convert.to_renpy import FontStandards
from renpy_doc_convert.consolidate import Consolidate

from docx import Document
from docx.shared import RGBColor

TEST_FILE_NAME = "document_default.docx"

class FontStandardsTest(unittest.TestCase):

  document : Document
  consolidate : Consolidate

  @classmethod
  def setUpClass(cls):
    cls.document : Document = Document('tests/data/{0}'.format(TEST_FILE_NAME))
    cls.consolidate : Consolidate = Consolidate(cls.document)
  
  def test_font_default_from_doc(self):

    fs = FontStandards(self.document, self.consolidate.text_chunks)

    self.assertEqual(fs.color, RGBColor.from_string("000000"))
    self.assertEqual(fs.size, 11)

  def test_font_default_from_code(self):
    
    fs = FontStandards(None, [])

    self.assertEqual(fs.color, RGBColor.from_string("000000"))
    self.assertEqual(fs.size, 11)

