from gamemap.statuses import gamestatuses, GameStatus
from gamemap.pos import Pos
from gamemap.bounded import Bounded
from gamemap.brkfloor import BrkFloor
from gamemap.door import Door
from gamemap.hatch import Hatch
from gamemap.ladder import LadderD, LadderU
from gamemap.rappel import RappelD, RappelU
from gamemap.statuses import WallStatus
from gamemap.transition import Transition
from gamemap.trapdoor import Trapdoor
from gamemap.vault import HVault, VVault
from gamemap.wall import Wall
from gamemap.window import Window
from random import choice

class Gamemap:
  """ contains all game and map information"""
  def __init__(self, roms=[], otsd=[], spwn=[], hals=[],
      strs=[], trns=[], objs=None, name="", status=GameStatus.DEFAULT):
    self.roms = roms
    self.otsd = otsd
    self.spwn = spwn
    self.hals = hals
    self.strs = strs
    self.trns = trns
    self.objs = objs
    assert isinstance(name, str)
    self.name = name
    assert status in gamestatuses
    self.status = status

  def loct(self, p):
    for i in self.trns:
      if p == i.pos:
        return i
    return None

  def loc(self, p):
    if type(p) == Pos:
      for i in [self.roms, self.otsd, self.spwn, self.hals, self.strs]:
        for j in i:
          for p1 in j.poss:
            if p == p1:
              return j
    return self.loct(p)

  def getloc(self, t):
    for i in [self.roms, self.otsd, self.spwn, self.hals, self.strs]:
      for j in i:
        if t == j:
          return j.poss
    for i in self.trns:
      if t == i:
        return i.pos
    return Pos(-1, -1, 0)

  def getbndposs(self, n):
    for i in [self.roms, self.otsd, self.spwn, self.hals, self.strs]:
      for j in i:
        if n == j.name:
          return j.poss
  
  def getbnd(self, n):
    for i in [self.roms, self.otsd, self.spwn, self.hals, self.strs]:
      for j in i:
        if n == j.name:
          return j

  def getrandomspawnpos(self):
    s = choice(self.spwn)
    return choice(s.poss)

  def getrandomobjpos(self):
    o = choice([self.objs.a, self.objs.b])
    return choice(self.getbndposs(o))

