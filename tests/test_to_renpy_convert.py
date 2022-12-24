import unittest

from renpy_doc_convert.to_renpy import ConvertToRenpy
from renpy_doc_convert.consolidate import TextChunk, TextType

class ConvertToRenpyPrivateTest(unittest.TestCase):

  def setUp(self):
    # Setup dummy convert to renpy
    self.convert_renpy = ConvertToRenpy(None, [], None)

  def test_handle_escape_characters(self):
    text = "wow that \"thing\" is dumb"

    new_text = self.convert_renpy.handle_escape_characters(text)

    self.assertEqual(new_text, 'wow that \\"thing\\" is dumb')

  def test_format_indentation_dialogue(self):
    chunk = TextChunk()
    chunk.text_type = TextType.DIALOGUE
    chunk.character = "Walter"

    text = "I am danger"

    new_text = self.convert_renpy.format_indentation(chunk, text)

    self.assertEqual(new_text, "  \"Walter\" \"I am danger\"\n\n")

  def test_format_indentation_non_dialogue(self):
    chunk = TextChunk()
    chunk.text_type = TextType.NARRATION
    
    text = "Slipping Jimmy"

    new_text = self.convert_renpy.format_indentation(chunk, text)

    # There are two spaces as prescribed in to_renpy.
    self.assertEqual(new_text, "  \"Slipping Jimmy\"\n\n")

  def test_remove_character_name(self):
    text = "Theo: You will always be our reaper"

    new_text = self.convert_renpy.remove_character_name_in_text(text)

    self.assertEqual(new_text, "You will always be our reaper")