from gamemap.pos import Pos

class Transition:
  """ superclass for all transitional objects in a game map"""
  def __init__(self, pos, con=(), status=None):
    assert isinstance(pos, Pos)
    assert isinstance(con, tuple)
    # TODO verify `con` items in room/hallway/stairs lists
    self.pos = pos
    self.con = con
    self.status = status
    self.id = None

  def __str__(self):
    return f" @ {self.pos} | connects {self.con} | status: {self.status}"

  def add_con(self, a, b):
    self.con = (str(a), str(b))

  def getstatus(self):
    return self.status

  def __hash__(self):
    return hash((self.pos, self.con))