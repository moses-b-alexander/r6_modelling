from gamemap.transition import Transition
from gamemap.statuses import wallstatuses, WallStatus

class Trapdoor(Transition):
  """ repr of trapdoors within game map"""
  def __init__(self, pos, con=(), status=WallStatus.DEFAULT):
    assert status in wallstatuses
    assert status != WallStatus.UNBREAKABLE
    if status == WallStatus.DEFAULT:
      self.id = "T"
    elif status == WallStatus.DAMAGED:
      self.id = "t"
    elif status == WallStatus.DESTROYED:
      self.id = "o"
    elif status == WallStatus.REINFORCED:
      self.id = "e"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Trapdoor" + super().__str__()