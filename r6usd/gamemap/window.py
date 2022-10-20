from gamemap.transition import Transition
from gamemap.statuses import doorstatuses, DoorStatus

class Window(Transition):
  """ repr of windows within game map; default windows are equivalent to
  horizontal/vertical vaults"""
  def __init__(self, pos, con=(), status=DoorStatus.DEFAULT, dbl=False):
    assert status in doorstatuses
    if status == DoorStatus.DEFAULT:
      self.id = "N"
    elif status == DoorStatus.BARRICADED:
      self.id = "M"
    elif status == DoorStatus.BROKEN:
      self.id = "m"
    elif status == DoorStatus.CASTLED:
      self.id = "y"
    elif status == DoorStatus.SHIELDED:
      self.id = "n"
    self.dbl = dbl
    super().__init__(pos, con, status)

  def __str__(self):
    return "Window" + super().__str__()