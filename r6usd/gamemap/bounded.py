

class Bounded:
  """ repr of bounded spaces"""
  def __init__(self, poss=[], name="", outsd=False):
    assert isinstance(poss, list)
    assert isinstance(name, str)
    self.poss = poss
    self.name = name
    self.id = None
    self.con = []
    self.outsd = outsd

  def __str__(self):
    ts = "[ "
    for p in self.poss[:-1]:
      ts += str(p)
      ts += ", "
    ts += f"{self.poss[-1]} ]"
    return f"{self.name} @ " + ts

  def mark_outsd(self):
    self.outsd = True

  def __hash__(self):
    return hash((frozenset(self.poss), self.name))

  def __eq__(self, x):
    return hash(self) == hash(x)