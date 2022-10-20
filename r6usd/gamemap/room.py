from gamemap.bounded import Bounded
from gamemap.pos import Pos

class Room(Bounded):
  """ stores rooms within buildings on the game map"""
  def __init__(self, poss=[], name=""):
    self.id = "R"
    super().__init__(poss, name)

  def __str__(self):
    return "Room: " + super().__str__()