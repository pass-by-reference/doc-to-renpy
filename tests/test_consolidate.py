import unittest

from renpy_doc_convert.consolidate import Consolidate, TextType, TextChunk
from docx import Document

TEST_FILE_NAME = "dummy.docx"

class MockParagraph:

  def __init__(self, text: str):
    self.text : str = text

class ConslidateTests(unittest.TestCase):

  document : Document
  consolidate : Consolidate

  @classmethod
  def setUpClass(cls):
    cls.document = Document('tests/data/{0}'.format(TEST_FILE_NAME))
    cls.consolidate : Consolidate = Consolidate(cls.document)

  def test_consolidate_paragraphs(self):
    self.consolidate.consolidate_paragraphs()

    text_chunks : list[TextChunk] = self.consolidate.text_chunks

    # Check data/dummy.docx that there is one continious line so there is one chunk
    self.assertEqual(len(text_chunks), 1)

  def test_get_character(self):
    expected_chara = "Hector"
    mock_para = MockParagraph("{0}: *Ding Ding Ding*".format(expected_chara))
    text_type = TextType.DIALOGUE

    actual_chara = self.consolidate.get_character(mock_para, text_type)

    self.assertEqual(expected_chara, actual_chara)

  def test_get_text_type(self):
    param_list = [
      (MockParagraph("Lena: I will catchup one day"), TextType.DIALOGUE),
      (MockParagraph("Life is tough"), TextType.NARRATION),
      (MockParagraph("*BANG*"), TextType.SOUND)
    ]

    for paragraph, expected_text_type in param_list:
      with self.subTest():
        actual_text_type = self.consolidate.get_text_type(paragraph)
        self.assertEqual(expected_text_type, actual_text_type)

  def test_is_dialogue(self):
    text : str = "Narrator: Hello there"

    is_dialogue = self.consolidate.is_dialogue(text)

    self.assertTrue(is_dialogue)

  def test_is_sound(self):
    text : str = "*BOOM*"

    is_sound = self.consolidate.is_sound(text)

    self.assertTrue(is_sound)

  def test_is_narration(self):
    text : str = "And at that moment he knew he messed up"

    is_sound = self.consolidate.is_narration(text)

    self.assertTrue(is_sound)

if __name__ == '__main__':
  unittest.main()