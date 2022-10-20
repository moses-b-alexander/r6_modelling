from gamemap.pos import Pos
from gamemap.statuses import objsstatuses, ObjsStatus

class Objs:
  """ stores the objective site information for the game map"""
  def __init__(self, asite, bsite, status=ObjsStatus.DEFAULT):
    assert isinstance(asite, str)
    assert isinstance(bsite, str)
    self.a = asite
    self.b = bsite
    assert status in objsstatuses
    self.status = status
    self.idA = "A"
    self.idB = "B"

  def __str__(self):
    return f"A: {self.status} @ {self.a}\nB: {self.status} @ {self.b}"