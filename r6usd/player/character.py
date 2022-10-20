from player.weapon import PrimWeap, SecdWeap
from player.gadget import Gadget, SpecialGadget

class Character:
  """ generic r6 character"""
  def __init__(self, prim=None, secd=None, gadg=None, arm=None, spd=None, roles=[], name=""):
    assert isinstance(prim, PrimWeap)
    assert isinstance(secd, SecdWeap)
    self.prim = prim
    self.secd = secd
    assert arm > 0 and arm < 4 and isinstance(arm, int)
    assert spd > 0 and spd < 4 and isinstance(spd, int)
    self.arm = arm
    self.spd = spd
    self.roles = roles
    assert isinstance(gadg, Gadget)
    self.gadg = gadg
    assert isinstance(name, str)
    self.name = name
    self.ability = None

  def __str__(self):
    return f"{self.name}: \n{str(self.prim)}\n{str(self.secd)}\n{str(self.gadg)}\narmor: {self.arm}, speed: {self.spd}\n{str(self.ability)}\n{str(self.roles)}\n"

  def __eq__(self, x):
    if self.name == x.name:
      return True
    return False