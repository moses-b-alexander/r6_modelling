from gamemap.pos import Pos

class Action:
  """ represents a generic action"""
  def __init__(self, desc, pos, time, tcost, posoc=0, negoc=0):
    assert isinstance(pos, Pos)
    assert isinstance(time, int)
    assert isinstance(tcost, int)
    assert isinstance(posoc, int)
    assert isinstance(negoc, int)
    assert isinstance(desc, str)
    self.pos = pos
    self.time = time
    self.gain = gain
    self.desc = desc

  def __str__(self):
    return f"Action: {self.desc}, {self.time} sec, {self.gain} @ {self.pos}"

  def __eq__(self, x):
    if self.desc == x.desc and self.pos == x.pos and self.time == x.time:
      return True
    return False
