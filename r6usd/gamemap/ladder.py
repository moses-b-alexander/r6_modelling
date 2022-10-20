from gamemap.transition import Transition
from gamemap.statuses import NopeStatus

class LadderU(Transition):
  """ repr of ladders upwards in game map"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "5"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Ladder UP" + super().__str__()

class LadderD(Transition):
  """ repr of ladders downwards in game map"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "%"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Ladder DOWN" + super().__str__()