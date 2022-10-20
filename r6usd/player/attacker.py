from player.character import Character
from player.weapon import PrimWeap, SecdWeap
from player.gadget import Gadget, SpecialGadget
from random import choice


class Attacker(Character):
  """ attacking operator class"""
  def __init__(self, prim=None, secd=None, gadg=None, arm=None, spd=None, roles=None, name=""):
    assert name in atkrs
    super().__init__(prim, secd, gadg, arm, spd, roles, name)
    # self.drone = 2
    # self.rein = 0
    # if self.name == "Twitch":
    #   self.drone = 0
    self.rappel = True
    self.barricade = False
    self.viewcam = False
  
  def __str__(self):
    return super().__str__()

class AtkOp(Attacker):
  """ class for atk op init"""
  def __init__(self, name, gnum=-1, wnum=-1):
    assert gnum in [-1, 1, 2]
    assert wnum in [-1, 1, 2]
    if name == "Random" or name == "random" or name == "RANDOM":
      name = choice(atkrs)
    prims = []
    secds = [SecdWeap(45, 17, 450, 2.1, 1.0, "P9")] # making secd weap default for now
    gadgs = []
    arm = 0
    spd = 0
    roles = []
    ability = None

    if name == "Sledge":
      spd = 2
      arm = 2
      prims.append(PrimWeap(47, 31, 670, 3.3, 2.5, "L85A2"))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Tactical Breaching Hammer", 25, 2.0)
      roles.extend(["Flanker", "Soft Breacher", "Disabler", "Gadget User"])
    if name == "Thatcher":
      spd = 2
      arm = 2
      prims.append(PrimWeap(41, 26, 749, 3.3, 2.5, "AR33"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("EMP Grenade", 3, 1.0)
      roles.extend(["Intel Denier", "Disabler", "Backliner", "Gadget User"])
    if name == "Ash":
      spd = 3
      arm = 1
      prims.append(PrimWeap(39, 31, 860, 3.4, 2.5, "R4C"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Breaching Round", 3, 1.0)
      roles.extend(["Frontliner", "Soft Breacher", "Flanker", "Gadget User"])
    if name == "Thermite":
      spd = 2
      arm = 2
      prims.append(PrimWeap(47, 31, 690, 3.7, 2.5, "556xi"))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Exothermic Charge", 2, 2.0)
      roles.extend(["Hard Breacher", "Backliner", "Area Denier", "Gadget User"])
    if name == "Montagne":
      spd = 1
      arm = 3
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      ability = SpecialGadget("Extendable Shield", 10000, 2.0)
      roles.extend(["Shielder", "Frontliner", "Intel Gatherer", "Crowd Controller", "Area Denier", "Ability User"])
    if name == "Twitch":
      spd = 2
      arm = 2
      prims.append(PrimWeap(37, 31, 980, 3.1, 2.5, "F2"))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Shock Drone", 2, 2.0)
      roles.extend(["Backliner", "Frontliner", "Disabler", "Intel Gatherer", "Intel Denier", "Flanker", "Gadget User"])
    if name == "Iq":
      spd = 3
      arm = 1
      prims.append(PrimWeap(48, 31, 690, 3.1, 2.5, "552 Commando"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Electronics Detector", 10000, 1.5)
      roles.extend(["Intel Gatherer", "Frontliner", "Flanker", "Backliner", "Counter Roamer", "Ability User"])
    if name == "Blitz":
      spd = 2
      arm = 2
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      ability = SpecialGadget("Flash Shield", 4, 1.0, 7.0)
      roles.extend(["Shielder", "Frontliner", "Intel Denier", "Crowd Controller", "Counter Roamer", "Gadget User"])
    if name == "Glaz":
      spd = 2
      arm = 2
      prims.append(PrimWeap(71, 11, 380, 3.4, 3.0, "OTS-03"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Flip Sight", 10000, 1.5)
      roles.extend(["Backliner", "Soft Breacher", "Intel Gatherer", "Flanker", "Ability User"])
    if name == "Fuze":
      spd = 1
      arm = 3
      prims.append(PrimWeap(46, 101, 680, 8.5, 2.5, "6P41"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      ability = SpecialGadget("Cluster Charge", 4, 3.0)
      roles.extend(["Gadget User", "Area Denier", "Flanker", "Crowd Controller", "Disabler"])
    if name == "Buck":
      spd = 2
      arm = 2
      prims.append(PrimWeap(40, 31, 837, 2.9, 2.5, "C8-SFW"))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      ability = SpecialGadget("Skeleton Key", 26, 1.0)
      roles.extend(["Flanker", "Frontliner", "Soft Breacher", "Gadget User"])
    if name == "Blackbeard":
      spd = 2
      arm = 2
      prims.append(PrimWeap(49, 21, 585, 3.1, 2.5, "MK17 CQB"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      ability = SpecialGadget("Rifle Shield", 2, 2.0)
      roles.extend(["Backliner", "Frontliner", "Gadget User"])
    if name == "Capitao":
      spd = 3
      arm = 1
      prims.append(PrimWeap(48, 31, 650, 3.3, 2.5, "PARA-308"))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Tactical Crossbow", 4, 1.0)
      roles.extend(["Gadget User", "Flanker", "Frontliner", "Intel Denier", "Area Denier", "Crowd Controller", "Counter Roamer"])
    if name == "Hibana":
      spd = 3
      arm = 1
      prims.append(PrimWeap(40, 21, 850, 3.3, 2.5, "TYPE-89"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      ability = SpecialGadget("X-KAIROS", 3, 1.5)
      roles.extend(["Hard Breacher", "Frontliner", "Backliner", "Flanker", "Gadget User"])
    if name == "Jackal":
      spd = 2
      arm = 2
      prims.append(PrimWeap(46, 31, 800, 2.7, 2.5, "C7E"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Eyenox Model III", 3, 2.5)
      roles.extend(["Counter Roamer", "Intel Gatherer", "Flanker", "Gadget User"])
    if name == "Ying":
      spd = 2
      arm = 2
      prims.append(PrimWeap(46, 81, 650, 3.0, 2.5, "T-95 LSW"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      ability = SpecialGadget("Candela", 3, 1.5)
      roles.extend(["Crowd Controller", "Intel Denier", "Flanker", "Frontliner", "Area Denier", "Gadget User"])
    if name == "Zofia":
      spd = 2
      arm = 2
      prims.append(PrimWeap(45, 31, 730, 3.3, 2.5, "M762"))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      ability = SpecialGadget("KS79 Lifeline", 4, 1.0)
      roles.extend(["Crowd Controller", "Intel Denier", "Frontliner", "Area Denier", "Gadget User", "Counter Roamer", "Soft Breacher"])
    if name == "Dokkaebi":
      spd = 2
      arm = 2
      prims.append(PrimWeap(60, 21, 450, 3.4, 3.0, "MK 14 EBR"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Logic Strike", 2, 4.0)
      roles.extend(["Crowd Controller", "Intel Denier", "Intel Gatherer", "Flanker", "Counter Roamer", "Gadget User"])
    if name == "Finka":
      spd = 2
      arm = 2
      prims.append(PrimWeap(42, 31, 700, 3.3, 2.5, "Spear .308"))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Adrenal Surge", 3, 2.5)
      roles.extend(["Backliner", "Frontliner", "Buffer", "Flanker", "Gadget User"])
    if name == "Lion":
      spd = 2
      arm = 2
      prims.append(PrimWeap(44, 31, 700, 3.3, 2.5, "V308"))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      ability = SpecialGadget("EE-ONE-D", 3, 2.0, 15.0)
      roles.extend(["Intel Gatherer", "Gadget User", "Crowd Controller", "Counter Roamer", "Flanker", "Backliner"])
    if name == "Maverick":
      spd = 3
      arm = 1
      prims.append(PrimWeap(44, 31, 750, 3.4, 2.5, "M4 GS"))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Breaching Torch", 6, 5.0)
      roles.extend(["Hard Breacher", "Soft Breacher", "Flanker", "Disabler", "Backliner", "Gadget User"])
    if name == "Nomad":
      spd = 2
      arm = 2
      prims.append(PrimWeap(44, 41, 650, 3.4, 2.5, "AK-74M"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      ability = SpecialGadget("Airjab Launcher", 3, 1.0)
      roles.extend(["Counter Roamer", "Flanker", "Frontliner", "Crowd Controller", "Area Denier", "Trapper", "Gadget User"])
    if name == "Gridlock":
      spd = 1
      arm = 3
      prims.append(PrimWeap(38, 31, 780, 3.1, 2.5, "F90"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      ability = SpecialGadget("Trax Stingers", 3, 9.0)
      roles.extend(["Area Denier", "Crowd Controller", "Flanker", "Frontliner", "Counter Roamer", "Trapper", "Gadget User"])
    if name == "Nokk":
      spd = 2
      arm = 2
      prims.append(PrimWeap(34, 31, 800, 3.0, 1.5, "FMG-9"))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      ability = SpecialGadget("HEL Presence Reduction", 1, 12.0, 6.0)
      roles.extend(["Flanker", "Intel Denier", "Ability User"])
    if name == "Amaru":
      spd = 2
      arm = 2
      prims.append(PrimWeap(37, 51, 850, 3.9, 2.5, "G8A1"))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      gadgs.append(Gadget("Stun Grenade", 3, 1.0))
      ability = SpecialGadget("Garra Hook", 4, 1.0)
      roles.extend(["Flanker", "Gadget User"])
    if name == "Kali":
      spd = 2
      arm = 2
      prims.append(PrimWeap(97, 6, 50, 3.1, 3.0, "CSRX 300"))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      ability = SpecialGadget("LV Explosive Lance", 3, 1.0)
      roles.extend(["Backliner", "Soft Breacher", "Disabler", "Gadget User"])
    if name == "Iana":
      spd = 2
      arm = 2
      prims.append(PrimWeap(47, 21, 700, 3.4, 2.5, "ARX200"))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      gadgs.append(Gadget("Frag Grenade", 2, 1.0))
      ability = SpecialGadget("Gemini Replicator", 1, 15.0, 30.0)
      roles.extend(["Intel Denier", "Intel Gatherer", "Flanker", "Backliner", "Gadget User"])
    if name == "Ace":
      spd = 2
      arm = 2
      prims.append(PrimWeap(45, 31, 850, 3.4, 2.5, "AK-12"))
      gadgs.append(Gadget("Breach Charge", 3, 2.0))
      gadgs.append(Gadget("Smoke Grenade", 2, 1.0))
      ability = SpecialGadget("S.E.L.M.A Aqua Breacher", 3, 1.0)
      roles.extend(["Frontliner", "Hard Breacher", "Gadget User"])
    if name == "Zero":
      spd = 2
      arm = 2
      prims.append(PrimWeap(45, 26, 800, 3.4, 2.5, "SC3000K"))
      gadgs.append(Gadget("Hard Breach Charge", 1, 3.0))
      gadgs.append(Gadget("Claymore", 1, 1.5))
      ability = SpecialGadget("Argus Launcher", 4, 1.0)
      roles.extend(["Intel Gatherer", "Disabler", "Flanker", "Frontliner", "Gadget User"])
    if len(prims) == 0:
      prims.append(PrimWeap(0, 0, 0, 0.0, 0.0, "Shield"))

    super().__init__(choice(prims), choice(secds), choice(gadgs), spd, arm, roles, name)
    self.ability = ability

atkrs = ["Sledge", "Thatcher", "Ash", "Thermite", "Montagne", "Twitch", "Iq",
  "Blitz", "Fuze", "Glaz", "Buck", "Blackbeard", "Capitao", "Hibana", 
  "Jackal", "Ying", "Zofia", "Dokkaebi", "Finka", "Lion", "Maverick",
  "Nomad", "Gridlock", "Nokk", "Amaru", "Kali", "Iana", "Ace", "Zero"]