from gamemap.bounded import Bounded
from gamemap.pos import Pos

class Outside(Bounded):
  """ stores outside zone information on the game map"""
  def __init__(self, poss=[], name="", outsd=True):
    self.id = "0"
    super().__init__(poss, name, outsd)

  def __str__(self):
    return "EXT: " + super().__str__()