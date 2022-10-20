from gamemap.transition import Transition
from gamemap.statuses import wallstatuses, WallStatus

class Hatch(Transition):
  """ repr of ceiling hatches within game map"""
  def __init__(self, pos, con=(), status=WallStatus.DEFAULT):
    assert status in wallstatuses
    assert status != WallStatus.UNBREAKABLE
    if status == WallStatus.DEFAULT:
      self.id = "&"
    elif status == WallStatus.DAMAGED:
      self.id = "7"
    elif status == WallStatus.DESTROYED:
      self.id = "9"
    elif status == WallStatus.REINFORCED:
      self.id = "3"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Hatch" + super().__str__()