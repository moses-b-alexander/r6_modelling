from gamemap.bounded import Bounded
from gamemap.pos import Pos

class Spawn(Bounded):
  """ stores atk spawn locations on the game map"""
  def __init__(self, poss=[], name=""):
    self.id = "S"
    super().__init__(poss, name)

  def __str__(self):
    return "Spawn Area: " + super().__str__()