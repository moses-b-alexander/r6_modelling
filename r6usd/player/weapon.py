from player.errors import Error

class Weapon:
  """ repr of weapons"""
  def __init__(self, dmg=None, siz=None, rat=None, rel=None, mag=None, name=""):
    assert isinstance(dmg, int)
    assert isinstance(siz, int)
    assert isinstance(rat, int)
    assert isinstance(rel, float)
    assert isinstance(mag, float)
    assert isinstance(name, str)
    self.dmg = dmg
    self.siz = siz
    self.rel = rel
    self.mag = mag
    self.rat = rat
    self.name = name
    self.cur = siz

  def __str__(self):
    return f"Weapon: {self.name} | {self.dmg} | {self.cur}/{self.siz} | {self.rat} | {self.rel} | {self.mag}"

  def fire(self, n):
    if self.cur == 0:
      return Error("Out of ammo")
    if n > self.siz or n > self.cur:
      self.cur = 0
    else:
      self.cur -= n

  def reload(self):
    self.cur = int(self.siz)

class PrimWeap(Weapon):
  """ repr of primary weapons"""
  def __init__(self, dmg=None, siz=None, rat=None, rel=None, mag=None, name=""):
    super().__init__(dmg, siz, rat, rel, mag, name)

  def __str__(self):
    return "Primary " + super().__str__()

class SecdWeap(Weapon):
  """ repr of secondary weapons"""
  def __init__(self, dmg=None, siz=None, rat=None, rel=None, mag=None, name=""):
    super().__init__(dmg, siz, rat, rel, mag, name)

  def __str__(self):
    return "Secondary " + super().__str__()
