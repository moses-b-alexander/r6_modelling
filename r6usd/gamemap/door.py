from gamemap.transition import Transition
from gamemap.statuses import doorstatuses, DoorStatus

class Door(Transition):
  """ repr of doors within game map"""
  def __init__(self, pos, con=(), status=DoorStatus.DEFAULT, dbl=False):
    assert status in doorstatuses
    if status == DoorStatus.DEFAULT:
      self.id = "D"
    elif status == DoorStatus.BARRICADED:
      self.id = "X"
    elif status == DoorStatus.BROKEN:
      self.id = "x"
    elif status == DoorStatus.CASTLED:
      self.id = "Y"
    elif status == DoorStatus.SHIELDED:
      self.id = "d"
    self.dbl = dbl
    super().__init__(pos, con, status)

  def __str__(self):
    return "Door" + super().__str__()