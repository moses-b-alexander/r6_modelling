from player.character import Character
from player.weapon import PrimWeap, SecdWeap
from player.gadget import Gadget, SpecialGadget
from random import choice

class Defender(Character):
  """defending operator class"""
  def __init__(self, prim=None, secd=None, gadg=None, arm=None, spd=None, roles=[], name=""):
    assert name in defrs
    super().__init__(prim, secd, gadg, arm, spd, roles, name)
    # self.rein = 2
    # self.drone = 0
    self.rappel = False
    self.barricade = True
    self.viewcam = True

  def __str__(self):
    return super().__str__()

class DefOp(Defender):
  """ class for easier def op init"""
  def __init__(self, name, gnum=-1, wnum=-1):
    assert gnum in [-1, 1, 2]
    assert wnum in [-1, 1, 2]
    if name == "Random" or name == "random" or name == "RANDOM":
      name = choice(defrs)
    prims = []
    secds = [SecdWeap(45, 17, 450, 2.1, 1.0, "P9")] # making secd weap default for now
    gadgs = []
    arm = 0
    spd = 0
    roles = []
    ability = None

    if name == "Mute":
      spd = 2
      arm = 2
      prims.append(PrimWeap(30, 31, 800, 2.8, 1.5, "MP5K"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      ability = SpecialGadget("Mute Jammer", 4, 2.0)
      roles.extend(["Intel Denier", "Gadget Placer", "Counter Hard Breacher", "Disabler", "Area Denier", "Anchor", "Roamer"])
    if name == "Smoke":
      spd = 2
      arm = 2
      prims.append(PrimWeap(34, 31, 800, 3.0, 1.5, "FMG-9"))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Gas Canister", 3, 1.0)
      roles.extend(["Area Denier", "Gadget User", "Crowd Controller", "Sentinel", "Securer", "Coverer", "Intel Denier", "Anchor", "Roamer"])
    if name == "Castle":
      spd = 2
      arm = 2
      prims.append(PrimWeap(38, 26, 600, 2.9, 1.5, "UMP45"))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Castle Barricade", 3, 2.0)
      roles.extend(["Anchor", "Roamer", "Area Denier", "Securer", "Sentinel", "Gadget Placer"])
    if name == "Pulse":
      spd = 3
      arm = 1
      prims.append(PrimWeap(38, 26, 600, 2.9, 1.5, "UMP45"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Pulse Scanner", 10000, 2.0)
      roles.extend(["Gadget User", "Intel Gatherer", "Roamer"])
    if name == "Doc":
      spd = 1
      arm = 3
      prims.append(PrimWeap(27, 31, 800, 2.9, 1.5, "MP5"))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Stim Pistol", 3, 1.0)
      roles.extend(["Anchor", "Securer", "Sentinel", "Buffer", "Coverer", "Gadget User"])
    if name == "Rook":
      spd = 1
      arm = 3
      prims.append(PrimWeap(27, 31, 800, 2.9, 2.0, "MP5"))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Armor Set", 1, 1.0)
      roles.extend(["Anchor", "Securer", "Sentinel", "Coverer", "Gadget Placer", "Buffer"])
    if name == "Jager":
      spd = 2
      arm = 2
      prims.append(PrimWeap(38, 31, 740, 3.4, 1.5, "416-C Carbine"))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Active Defense System", 3, 1.5)
      roles.extend(["Gadget Placer", "Disabler", "Roamer", "Anchor", "Area Denier", "Securer"])
    if name == "Bandit":
      spd = 3
      arm = 1
      prims.append(PrimWeap(32, 31, 900, 2.8, 1.5, "MP7"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Shock Wire", 4, 2.0)
      roles.extend(["Roamer", "Disabler", "Counter Hard Breacher", "Area Denier", "Buffer", "Gadget Placer"])
    if name == "Kapkan":
      spd = 2
      arm = 2
      prims.append(PrimWeap(34, 31, 750, 3.2, 1.5, "9x19VSN"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("Entry Denial Device", 5, 1.5)
      roles.extend(["Gadget Placer", "Trapper", "Anchor", "Area Denier", "Sentinel"])
    if name == "Tachanka":
      spd = 1
      arm = 3
      prims.append(PrimWeap(49, 71, 550, 4.6, 1.0, "DP27"))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Shumikha Launcher", 10, 1.0)
      roles.extend(["Anchor", "Securer", "Sentinel", "Area Denier", "Coverer", "Crowd Controller", "Gadget User"])
    if name == "Frost":
      spd = 2
      arm = 2
      prims.append(PrimWeap(45, 35, 575, 2.6, 1.5, "9mm C1"))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      ability = SpecialGadget("Welcome Mat", 3, 2.0)
      roles.extend(["Trapper", "Roamer", "Intel Gatherer", "Area Denier", "Sentinel", "Gadget Placer"])
    if name == "Valkyrie":
      spd = 2
      arm = 2
      prims.append(PrimWeap(26, 31, 830, 3.1, 1.0, "MPX"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("Black Eye", 3, 1.0)
      roles.extend(["Intel Gatherer", "Anchor", "Roamer", "Securer", "Coverer", "Crowd Controller", "Gadget Placer"])
    if name == "Caveira":
      spd = 3
      arm = 1
      prims.append(PrimWeap(40, 31, 550, 3.0, 1.0, "M12"))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("Silent Step", 1, 10.0, 5.0)
      roles.extend(["Ability User", "Roamer", "Intel Denier", "Intel Gatherer", "Coverer"])
    if name == "Echo":
      spd = 1
      arm = 3
      prims.append(PrimWeap(30, 31, 800, 2.9, 1.5, "MP5SD"))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      ability = SpecialGadget("Yokai Drone", 2, 1.0)
      roles.extend(["Intel Gatherer", "Securer", "Sentinel", "Crowd Controller", "Anchor", "Coverer", "Gadget User"])
    if name == "Mira":
      spd = 1
      arm = 3
      prims.append(PrimWeap(23, 26, 1200, 2.8, 1.5, "Vector .45 ACP"))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      ability = SpecialGadget("Black Mirror", 2, 3.0)
      roles.extend(["Gadget Placer", "Intel Gatherer", "Counter Hard Breacher", "Sentinel", "Anchor", "Area Denier", "Coverer"])
    if name == "Lesion":
      spd = 2
      arm = 2
      prims.append(PrimWeap(28, 31, 900, 3.0, 1.5, "T-5 SMG"))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      ability = SpecialGadget("Gu", 8, 1.0)
      roles.extend(["Roamer", "Intel Gatherer", "Gadget User", "Trapper", "Area Denier", "Securer", "Sentinel"])
    if name == "Ela":
      spd = 3
      arm = 1
      prims.append(PrimWeap(23, 41, 1080, 3.0, 1.0, "Scorpion EVO 3 A1"))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      ability = SpecialGadget("Grzmot Mine", 4, 1.0)
      roles.extend(["Gadget User", "Roamer", "Crowd Controller", "Trapper", "Intel Gatherer", "Area Denier", "Securer"])
    if name == "Vigil":
      spd = 3
      arm = 1
      prims.append(PrimWeap(36, 31, 720, 3.0, 1.0, "K1A"))
      gadgs.append(Gadget("Bulletproof Camera", 1, 2.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("ERC-7", 1, 12.0, 6.0)
      roles.extend(["Ability User", "Roamer", "Intel Denier", "Sentinel", "Coverer"])
    if name == "Alibi":
      spd = 3
      arm = 1
      prims.append(PrimWeap(26, 31, 950, 3.1, 1.0, "Mx4 Storm"))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      ability = SpecialGadget("Prisma", 3, 1.0)
      roles.extend(["Gadget Placer", "Intel Denier", "Intel Gatherer", "Roamer", "Trapper", "Sentinel"])
    if name == "Maestro":
      spd = 1
      arm = 3
      prims.append(PrimWeap(35, 81, 900, 5.7, 1.0, "ALDA 5.56"))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("Evil Eye", 2, 2.5)
      roles.extend(["Gadget Placer", "Anchor", "Intel Gatherer", "Area Denier", "Sentinel", "Coverer", "Crowd Controller", "Disabler"])
    if name == "Clash":
      spd = 1
      arm = 3
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("CCE Shield", 1, 5.0, 5.0)
      roles.extend(["Shielder", "Crowd Controller", "Roamer", "Area Denier", "Sentinel", "Coverer", "Securer", "Ability User"])
    if name == "Kaid":
      spd = 1
      arm = 3
      prims.append(PrimWeap(36, 32, 700, 3.3, 1.5, "AUG A3"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Rtila Electroclaw", 2, 1.0)
      roles.extend(["Counter Hard Breacher", "Anchor", "Securer", "Disabler", "Area Denier", "Buffer", "Gadget Placer"])
    if name == "Mozzie":
      spd = 2
      arm = 2
      prims.append(PrimWeap(36, 26, 780, 2.5, 1.0, "Commando 9"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      ability = SpecialGadget("Pest Launcher", 3, 1.0)
      roles.extend(["Intel Gatherer", "Intel Denier", "Securer", "Disabler", "Anchor", "Roamer", "Coverer", "Gadget Placer"])
    if name == "Warden":
      spd = 2
      arm = 2
      prims.append(PrimWeap(26, 31, 830, 3.1, 1.5, "MPX"))
      gadgs.append(Gadget("Deployable Shield", 1, 3.0))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      ability = SpecialGadget("Glance Smart Glasses", 1, 10.0, 12.0)
      roles.extend(["Anchor", "Intel Denier", "Disabler", "Roamer", "Coverer", "Ability User"])
    if name == "Goyo":
      spd = 2
      arm = 2
      prims.append(PrimWeap(23, 26, 1200, 2.8, 1.0, "Vector .45 ACP"))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Volcan Shield", 2, 3.5)
      roles.extend(["Gadget Placer", "Securer", "Sentinel", "Area Denier", "Anchor", "Roamer", "Crowd Controller"])
    if name == "Wamai":
      spd = 2
      arm = 2
      prims.append(PrimWeap(42, 31, 720, 3.3, 1.0, "AUG A2"))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      ability = SpecialGadget("Mag-NET", 4, 1.0)
      roles.extend(["Anchor", "Roamer", "Disabler", "Area Denier", "Sentinel", "Gadget User"])
    if name == "Oryx":
      spd = 2
      arm = 2
      prims.append(PrimWeap(28, 31, 900, 3.0, 1.5, "T-5 SMG"))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Remah Dash", 3, 1.0, 12.0)
      roles.extend(["Roamer", "Soft Breacher", "Sentinel", "Coverer", "Gadget User"])
    if name == "Melusi":
      spd = 3
      arm = 1
      prims.append(PrimWeap(27, 31, 800, 2.9, 1.0, "MP5"))
      gadgs.append(Gadget("Impact Grenade", 2, 1.0))
      gadgs.append(Gadget("Nitro Cell", 1, 1.0))
      ability = SpecialGadget("Banshee Sonic Defense", 3, 2.5)
      roles.extend(["Gadget Placer", "Crowd Controller", "Securer", "Sentinel", "Coverer", "Roamer", "Anchor", "Intel Gatherer", "Area Denier"])
    if name == "Aruni":
      spd = 2
      arm = 2
      prims.append(PrimWeap(26, 20, 980, 2.7, 1.0, "P10 RONI"))
      gadgs.append(Gadget("Barbed Wire", 2, 1.0))
      gadgs.append(Gadget("Proximity Alarm", 2, 1.0))
      ability = SpecialGadget("Surya Laser Gate", 3, 1.0)
      roles.extend(["Area Denier", "Intel Gatherer", "Disabler", "Securer", "Sentinel", "Counter Hard Breacher", "Anchor", "Roamer", "Intel Denier", "Trapper", "Gadget Placer"])
    if len(prims) == 0:
      prims.append(PrimWeap(0, 0, 0, 0.0, 0.0, "Shield"))

    super().__init__(choice(prims), choice(secds), choice(gadgs), spd, arm, roles, name)
    self.ability = ability

defrs = ["Mute", "Smoke", "Castle", "Pulse", "Doc", "Rook", "Jager", "Bandit",
  "Tachanka", "Kapkan", "Frost", "Valkyrie", "Caveira", "Echo", "Mira",
  "Lesion", "Ela", "Vigil", "Alibi", "Maestro", "Clash", "Kaid", "Mozzie",
  "Warden", "Goyo", "Wamai", "Oryx", "Melusi", "Aruni"]