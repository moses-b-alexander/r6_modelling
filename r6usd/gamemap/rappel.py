from gamemap.transition import Transition
from gamemap.statuses import NopeStatus

class RappelU(Transition):
  """ repr of rappel positions upwards in game map"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "{"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Rappel UP" + super().__str__()

class RappelD(Transition):
  """ repr of rappel positions downwards in game map"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "}"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Rappel DOWN" + super().__str__()