import unittest

from docx.shared import RGBColor

from renpy_doc_convert.to_renpy import RenpyStyling

class RenpyStylingTests(unittest.TestCase):

  class MockFontStandards():
    def __init__(self):
      self.color : RGBColor = RGBColor(0,0,0)
      self.size = 0

  def setUp(self):
    font_stds : self.MockFontStandards = self.MockFontStandards()
    self.renpy_styling = RenpyStyling(font_stds)

  def test_convert_bold(self):
    text = "the boldness"

    new_text = self.renpy_styling.convert_bold(text)

    self.assertEqual(new_text, "{b}the boldness{/b}")

  def test_convert_italics(self):
    text = "the italics"

    new_text = self.renpy_styling.convert_italics(text)

    self.assertEqual(new_text, "{i}the italics{/i}")

  def test_convert_underline(self):
    text = "the underline"

    new_text = self.renpy_styling.convert_underline(text)

    self.assertEqual(new_text, "{u}the underline{/u}")

  def test_change_font_size(self):
    text = "wowzers"
    
    # Standard is 14, run is 10, difference is -4
    self.renpy_styling.font_stds.size = 14
    font_size = 10

    new_text = self.renpy_styling.convert_font_size(text, font_size)

    self.assertEqual(new_text, "{size=+-4}wowzers{/size}")

  def test_no_change_font_size(self):
    text = "wowzers"

    # Standard and run size is the same. No change
    self.renpy_styling.font_stds.size = 10
    font_size = 10

    new_text = self.renpy_styling.convert_font_size(text, font_size)

    self.assertEqual(new_text, "wowzers")

  def test_change_font_color(self):
    text = "Hits different"

    # Black: #FFFFFF
    self.renpy_styling.font_stds.color = RGBColor(0, 0, 0)
    # Green: #45FF00
    font_color = RGBColor(69, 255, 0)

    new_text = self.renpy_styling.convert_font_color(text, font_color)

    self.assertEqual(new_text, "{color=#45FF00}Hits different{/color}")

  def test_no_change_font_color(self):
    text = "Hits different"

    # Black: #FFFFFF
    self.renpy_styling.font_stds.color = RGBColor(0, 0, 0)
    # Green: #45FF00
    font_color = RGBColor(0, 0, 0)

    new_text = self.renpy_styling.convert_font_color(text, font_color)

    self.assertEqual(new_text, "Hits different")

  def test_convert_strike(self):
    text = "Evangelion"

    new_text = self.renpy_styling.convert_strike(text)

    self.assertEqual(new_text, "{s}Evangelion{/s}")
