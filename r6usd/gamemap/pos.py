from math import sqrt

class Pos:
  """ repr of map coordinates """
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def xx(self, ch):
    self.x = ch

  def yy(self, ch):
    self.y = ch

  def zz(self, ch):
    self.z = ch

  def __str__(self):
    return f"({self.x}, {self.y}, {self.z})"

  def __hash__(self):
    return hash((self.x, self.y, self.z))

  def __eq__(self, p):
    return hash(self) == hash(p)

  def dist(self, p):
    return sqrt((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2)

  def furthz(self, p):
    return max(abs(self.x - p.x), abs(self.y - p.y))