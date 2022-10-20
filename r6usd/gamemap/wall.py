from gamemap.transition import Transition
from gamemap.statuses import wallstatuses, WallStatus

class Wall(Transition):
  """ repr of walls within game map"""
  def __init__(self, pos, con=(), status=WallStatus.DEFAULT, halflen=False, halfhgt=False):
    assert status in wallstatuses
    if status == WallStatus.DEFAULT:
      self.id = "W"
    elif status == WallStatus.DAMAGED:
      self.id = "w"
    elif status == WallStatus.DESTROYED:
      self.id = "O"
    elif status == WallStatus.REINFORCED:
      self.id = "E"
    elif status == WallStatus.UNBREAKABLE:
      self.id = "U"
    self.halflen = halflen
    self.halfhgt = halfhgt
    super().__init__(pos, con, status)

  def __str__(self):
    return "Wall" + super().__str__()