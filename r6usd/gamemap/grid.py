from collections import defaultdict
import gamemap.gamemap as gm
from gamemap.door import Door
from gamemap.brkfloor import BrkFloor
from gamemap.hallway import Hallway
from gamemap.hatch import Hatch
from gamemap.ladder import LadderD, LadderU
from gamemap.outside import Outside
from gamemap.pos import Pos
from gamemap.rappel import RappelD, RappelU
from gamemap.room import Room
from gamemap.spawn import Spawn
from gamemap.stairs import StairsD, StairsU
from gamemap.statuses import *
from gamemap.trapdoor import Trapdoor
from gamemap.vault import HVault, VVault
from gamemap.wall import Wall
from gamemap.window import Window

class Grid:
  """ string repr of the map, used for initialization;
  items in list go up in elevation (eg lowest floor
  is first list item, second-lowest floor is second 
  list item, etc.)"""
  def __init__(self, s):
    assert isinstance(s, list)
    self.s = s
    self.g = gm.Gamemap()
    self.dd = []

  def parse(self): # map encoding mechanism
    # ' : represents empty areas for aligning floors
    # " : represents restricted/out-of-bounds areas
    # / : obstacles
    # neither tag is tracked or assigned an object,
    # since there's no point tracking placeholders
    def pop_bnds_trns(a, c):
      c *= 10
      h = 0
      k = 0
      d = defaultdict(list)
      for i in a:
        for j in i:
          ix = len(j) if (j.find("*_*") == -1) else j.find("*_*")
          if "*_*" in j:
            d[j[(ix + 3):].replace('_', ' ')].append((j, k, h, c))
          if "W" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c)))
          if "w" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), status=WallStatus.DAMAGED))
          if "O" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), status=WallStatus.DESTROYED))
          if "E" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), status=WallStatus.REINFORCED))
          if "U" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), status=WallStatus.UNBREAKABLE))
          if "<" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), halflen=True))
          if ">" in j[:ix]:
            self.g.trns.append(Wall(Pos(k, h, c), halfhgt=True))
          if "D" in j[:ix]:
            self.g.trns.append(Door(Pos(k, h, c)))
          if "X" in j[:ix]:
            self.g.trns.append(Door(Pos(k, h, c), status=DoorStatus.BARRICADED))
          if "x" in j[:ix]:
            self.g.trns.append(Door(Pos(k, h, c), status=DoorStatus.BROKEN))
          if "Y" in j[:ix]:
            self.g.trns.append(Door(Pos(k, h, c), status=DoorStatus.CASTLED))
          if "d" in j[:ix]:
            self.g.trns.append(Door(Pos(k, h, c), status=DoorStatus.SHIELDED))
          if "N" in j[:ix]:
            self.g.trns.append(Window(Pos(k, h, c)))
          if "M" in j[:ix]:
            self.g.trns.append(Window(Pos(k, h, c), status=DoorStatus.BARRICADED))
          if "m" in j[:ix]:
            self.g.trns.append(Window(Pos(k, h, c), status=DoorStatus.BROKEN))
          if "y" in j[:ix]:
            self.g.trns.append(Window(Pos(k, h, c), status=DoorStatus.CASTLED))
          if "n" in j[:ix]:
            self.g.trns.append(Window(Pos(k, h, c), status=DoorStatus.SHIELDED))
          if "T" in j[:ix]:
            self.g.trns.append(Trapdoor(Pos(k, h, c)))
          if "t" in j[:ix]:
            self.g.trns.append(Trapdoor(Pos(k, h, c), status=WallStatus.DAMAGED))
          if "o" in j[:ix]:
            self.g.trns.append(Trapdoor(Pos(k, h, c), status=WallStatus.DESTROYED))
          if "e" in j[:ix]:
            self.g.trns.append(Trapdoor(Pos(k, h, c), status=WallStatus.REINFORCED))
          if "&" in j[:ix]:
            self.g.trns.append(Hatch(Pos(k, h, c)))
          if "7" in j[:ix]:
            self.g.trns.append(Hatch(Pos(k, h, c), status=WallStatus.DAMAGED))
          if "9" in j[:ix]:
            self.g.trns.append(Hatch(Pos(k, h, c), status=WallStatus.DESTROYED))
          if "3" in j[:ix]:
            self.g.trns.append(Hatch(Pos(k, h, c), status=WallStatus.REINFORCED))
          if "I" in j[:ix]:
            self.g.trns.append(HVault(Pos(k, h, c)))
          if "J" in j[:ix]:
            self.g.trns.append(VVault(Pos(k, h, c)))
          if "{" in j[:ix]:
            self.g.trns.append(RappelU(Pos(k, h, c)))
          if "}" in j[:ix]:
            self.g.trns.append(RappelD(Pos(k, h, c)))
          if "5" in j[:ix]:
            self.g.trns.append(LadderU(Pos(k, h, c)))
          if "%" in j[:ix]:
            self.g.trns.append(LadderD(Pos(k, h, c)))
          if "f" in j[:ix]:
            self.g.trns.append(BrkFloor(Pos(k, h, c)))
          k += 1
        h += 1
        k = 0
      return d
    cx = []
    l = 0
    for flr in self.s:
      lns = flr.split('\n')
      for ln in lns:
        if ln == '':
          continue
        else:
          cx.append(ln.split(' '))
      # print(cx)
      self.dd.append(pop_bnds_trns(cx, l))
      l += 1
      cx = []
    for d in self.dd:
      for k, v in d.items():
        vs = []
        tmp = None
        for i in v:
          vs.append((Pos(i[1], i[2], i[3])))
        if v[0][0][0] == "0":
          self.g.otsd.append(Outside(vs, k, outsd=True))
        if v[0][0][0] == "H":
          self.g.hals.append(Hallway(vs, k))
        if v[0][0][0] == "Q":
          self.g.hals.append(Hallway(vs, k, outsd=True))
        if v[0][0][0] == "R":
          self.g.roms.append(Room(vs, k))
        if v[0][0][0] == "S":
          self.g.spwn.append(Spawn(vs, k))
        if v[0][0][0] == "^":
          self.g.strs.append(StairsU(vs, k))
        if v[0][0][0] == "v":
          self.g.strs.append(StairsD(vs, k))
        if v[0][0][0] == "*" or v[0][0][0] == "" or v[0][0][0] == "_":
          print("ERROR")
