from gamemap.transition import Transition
from gamemap.statuses import wallstatuses, WallStatus

class BrkFloor(Transition):
  """ stores breakable floor locations in the game map"""
  def __init__(self, pos, con=(), status=WallStatus.DEFAULT):
    assert status in wallstatuses
    assert status != WallStatus.DESTROYED
    assert status != WallStatus.REINFORCED
    assert status != WallStatus.UNBREAKABLE
    self.id = "f"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Breakable Floor" + super().__str__()