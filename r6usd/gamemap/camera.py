from gamemap.pos import Pos

class Camera:
  """ stores security camera locations on the game map"""
  def __init__(self, pos, name=""):
    self.id = "C"
    super().__init__(pos, name)

  def __str__(self):
    return f"Camera ({self.name}) @ {self.pos}"