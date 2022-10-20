# DEAD CODE ??

class Unbounded:
  """ repr of unbounded spaces"""
  def __init__(self, lposs=[], rposs=[], name=""):
    assert isinstance(lposs, list)
    assert isinstance(rposs, list)
    assert isinstance(name, str)
    self.lposs = lposs
    self.rposs = rposs
    self.name = name
    self.id = None

  def __str__(self):
    return f"{self.name} @ {self.lposs[0]}, {self.rposs[0]}"