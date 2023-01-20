import os

# Get path of directory where constants.py is located
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists("{0}/tempdata".format(BASE_PATH)):
  os.makedirs("{0}/tempdata".format(BASE_PATH))
  os.makedirs("{0}/tempdata/rpy".format(BASE_PATH))
  os.makedirs("{0}/tempdata/docx".format(BASE_PATH))

SAVED_WORKSPACE = "{0}/tempdata/saved.json".format(BASE_PATH)
DOCX_FILE_PATH = "{0}/tempdata/docx".format(BASE_PATH)
RPY_FILE_PATH = "{0}/tempdata/rpy".format(BASE_PATH)