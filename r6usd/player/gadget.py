from player.errors import Error

class Gadget:
  """ tracks gadgets for characters"""
  def __init__(self, typ, num, ust):
    assert typ in atk_gadgs or typ in def_gadgs
    assert isinstance(num, int)
    assert isinstance(ust, float)
    self.typ = typ
    self.num = num
    self.ust = ust

  def __str__(self):
    return f"Gadget: {self.typ}, {self.num}"

  def use(self):
    if self.num == 0:
      return Error("No gadgets remaining")
    self.num -= 1

atk_gadgs = ["Breach Charge", "Frag Grenade", "Smoke Grenade", "Stun Grenade",
  "Claymore", "Hard Breach Charge"]
def_gadgs = ["Barbed Wire", "Barricade", "Bulletproof Camera", "Deployable Shield", 
  "Nitro Cell", "Impact Grenade", "Proximity Alarm"]

class SpecialGadget:
  """ tracks op-specific gadgets for characters"""
  def __init__(self, nam, num, ust, rch=0.0):
    assert isinstance(num, int)
    assert isinstance(ust, float)
    self.nam = nam
    self.num = num
    self.ust = ust
    self.rch = rch

  def __str__(self):
    return f"Special Gadget: {self.nam}, {self.num}"

  def use(self):
    if self.num == 0:
      return Error("No gadgets remaining")
    self.num -= 1