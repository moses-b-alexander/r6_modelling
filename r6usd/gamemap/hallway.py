from gamemap.bounded import Bounded
from gamemap.pos import Pos

class Hallway(Bounded):
  """ repr of hallways in buildings on game map"""
  def __init__(self, poss=[], name="", outsd=False):
    self.id = "H"
    super().__init__(poss, name, outsd)

  def __str__(self):
    return f"Hallway: " + super().__str__()