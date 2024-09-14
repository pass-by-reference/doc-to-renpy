import unittest
from unittest import mock

from renpy_doc_convert.to_renpy import ConvertToRenpy
from renpy_doc_convert.to_renpy import CharNameReturn
from renpy_doc_convert.consolidate import TextChunk, TextType

class MockParagraph:
  def __init__(self):
    self.runs = []

class MockRun:
  def __init__(self):
    self.text = ""

class MockRenpyStyler:
  def __init__(self):
    pass

  def process_run_for_styling(self, run : MockRun) -> str:
    return run.text

class ConvertToRenpyProcessTest(unittest.TestCase):
  def setUp(self):
    # Setup dummy convert to renpy

    self.convert_renpy = ConvertToRenpy(None, [], None)

    # Mock RenpyStyling with custom mock class
    patcher = mock.patch.object(self.convert_renpy, 'renpy_styler', new_callable=MockRenpyStyler)
    self.mock_renpy_styler = patcher.start()

    self.addCleanup(patcher.stop)

  def test_handle_styling(self):
    """
    Test logic in handle styling which is removing the character name and making sure
    if there are more than two colons in a chunk, then only the first colon gets used
    as the seperator and the second colon is kept.
    """
    chunk = TextChunk()
    chunk.text_type = TextType.DIALOGUE

    mock_run_one = MockRun()
    mock_run_one.text = "Prophet: The day starts " # First colon in first run

    mock_run_two = MockRun()
    mock_run_two.text = "on 10:00" # Second colon in second run

    paragraph = MockParagraph()
    paragraph.runs = [mock_run_one, mock_run_two]

    chunk.paragraphs = [paragraph]

    text = self.convert_renpy.handle_styling(chunk)
  
    self.assertEqual(text, "The day starts on 10:00")


class ConvertToRenpyPrivateTest(unittest.TestCase):

  def setUp(self):
    # Setup dummy convert to renpy
    self.convert_renpy = ConvertToRenpy(None, [], None)

  def test_handle_escape_characters_double_quote(self):
    text = "wow that \"thing\" is dumb"

    new_text = self.convert_renpy.handle_escape_characters(text)

    self.assertEqual(new_text, 'wow that \\"thing\\" is dumb')

  def test_handle_escape_characters_single_quote(self):
    text = "I don't think he knows about 'second breakfast'"

    new_text = self.convert_renpy.handle_escape_characters(text)

    self.assertEqual(new_text, "I don\\'t think he knows about \\'second breakfast\\'")

  def test_handle_escape_characters_percent(self):
    text = "0.00001% of success"

    new_text = self.convert_renpy.handle_escape_characters(text)

    self.assertEqual(new_text, "0.00001\\% of success")

  def test_handle_escape_characters_backslash(self):
    text = "what this \\ or that"

    new_text = self.convert_renpy.handle_escape_characters(text)

    # Result is two backslash. But to represent that in a python string
    # we need four backslashes
    self.assertEqual(new_text, "what this \\\\ or that")

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

    ret : CharNameReturn =  self.convert_renpy.remove_character_name_in_text(text)

    self.assertEqual(ret.name_found, True)
    self.assertEqual(ret.text, "You will always be our reaper")

  def test_remove_character_name__multiple_colons(self):
    text = "ratboi: 10:00 is the time"

    ret : CharNameReturn = self.convert_renpy.remove_character_name_in_text(text)

    self.assertEqual(ret.name_found, True)
    self.assertEqual(ret.text, "10:00 is the time")

  def test_get_label(self):
    label_one = self.convert_renpy.get_label("lycoris")
    label_two = self.convert_renpy.get_label("bocchi/the/rock")
    label_three = self.convert_renpy.get_label("sandevistan.os")
    label_four = self.convert_renpy.get_label("jobless/reincarnation.mp4")

    self.assertEqual(label_one, "lycoris")
    self.assertEqual(label_two, "rock")
    self.assertEqual(label_three, "sandevistan")
    self.assertEqual(label_four, "reincarnation")