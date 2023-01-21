
class UserSettings:
  def __init__(self, settings_dict : dict = None):

    self.theme : str = "light" # Defaults

    if settings_dict:
      self.theme = settings_dict.get("theme")

  def is_valid_theme(self) -> bool:
    return self.theme == "light" or self.theme == "dark"

  def dict(self):
    return {
      "theme": self.theme
    }
