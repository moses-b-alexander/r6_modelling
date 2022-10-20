from gamemap.bounded import Bounded
from gamemap.pos import Pos

class StairsU(Bounded):
  """ repr of stairs going up in buildings on game map"""
  def __init__(self, poss=[], name=""):
    self.id = "^"
    super().__init__(poss, name)

  def __str__(self):
    return f"Stairs UP: " + super().__str__()

class StairsD(Bounded):
  """ repr of stairs going down in buildings on game map"""
  def __init__(self, poss=[], name=""):
    self.id = "v"
    super().__init__(poss, name)

  def __str__(self):
    return f"Stairs DOWN: " + super().__str__()