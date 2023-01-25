import os
import logging
import argparse

from renpy_doc_convert.api import convert

from gui.app import AppGui

# Get absolute path of project directory
PROJECT_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
RENPY_DIR = "{0}/quick_convert_data/renpy/".format(PROJECT_BASE_PATH)
DOCX_DIR = "{0}/quick_convert_data/docx/".format(PROJECT_BASE_PATH)

def quick_convert():
  for filename in os.listdir(DOCX_DIR):

    (file_name_no_ext, extension) = os.path.splitext(filename)  

    if extension == ".docx":
      logging.info("Converting {0}".format(filename))

      docx_file_path = os.path.join(DOCX_DIR, filename)
      renpy_file_path = os.path.join(RENPY_DIR, file_name_no_ext + ".rpy")

      convert(docx_file_path, renpy_file_path)
    else:
      logging.info("{0} is not a docx format. Will not convert".format(filename))

def setup_logging(use_debug : bool):
  format = '%(asctime)s (%(filename)s-%(funcName)s) %(levelname)s: %(message)s'
  level = logging.DEBUG if use_debug else logging.INFO
  logging.basicConfig(format=format, level=level)

def setup_arguments():
  parser = argparse.ArgumentParser(description="Convert docx to renpy file format")
  parser.add_argument(
    "--quick_convert", 
    help="Do a quick convert rather going through gui",
    action="store_true")

  parser.add_argument(
    "--verbose",
    help="Log DEBUG level logs",
    action="store_true"
  )

  return parser.parse_args()

if __name__ == "__main__":

  args = setup_arguments()

  setup_logging(args.verbose)
  
  if args.quick_convert:
    logging.info("Using quick convert")
    quick_convert()
  else:
    logging.info("Using GUI")
    app = AppGui()
    app.run()

  
