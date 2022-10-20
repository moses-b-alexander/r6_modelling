from collections import defaultdict, deque
from gamemap.bounded import Bounded
from gamemap.brkfloor import BrkFloor
from gamemap.door import Door
from gamemap.grid import Grid
from gamemap.hatch import Hatch
from gamemap.ladder import LadderD, LadderU
from gamemap.objs import Objs
from gamemap.pos import Pos
from gamemap.rappel import RappelD, RappelU
from gamemap.statuses import *
from gamemap.transition import Transition
from gamemap.trapdoor import Trapdoor
from gamemap.vault import HVault, VVault
from gamemap.wall import Wall
from gamemap.window import Window
from maps.border import BORDER
from player.attacker import atkrs, AtkOp
from player.defender import defrs, DefOp
from player.player import Player
import queue
from random import choice


class Match:
  """ data model for match"""
  def __init__(self, m, ps=[]):
    assert m in map_names
    assert isinstance(ps, list)
    self.prog = 0
    self.term = (150, False)
    self.aps = []
    self.dps = []
    if m == MAPS.BORDER:
      self.gmap = Grid(BORDER)
      self.dim = (125, 92, 2)
      self.all_objs = [Objs("Armory Lockers", "Archives")] #, Objs("Workshop", "Ventilation Room"), 
        #Objs("Supply Room", "Customs Inspection"), Objs("Bathroom", "Tellers")]
    # if m == MAPS.KAFE:
    #   self.gmap = Grid(KAFE)
    #   self.dim = ()
    #   self.all_objs = []
    else:
      self.gmap = Grid(TESTMAP)
      self.dim = (1, 1, 1)
      self.all_objs = []
    self.gmap.parse()
    self.pop_trns()
    self.gmap.g.objs = choice(self.all_objs)
    trk = []
    if len(ps) == 0:
      for _ in range(5):
        t = AtkOp("random")
        if t.name not in trk:
          self.aps.append(t)
          trk.append(t.name)
        else:
          self.aps.append(AtkOp("random"))
      for _ in range(5):
        t = DefOp("random")
        if t.name not in trk:
          self.dps.append(t)
          trk.append(t.name)
        else:
          self.dps.append(DefOp("random"))
    else:
      for p in ps:
        if p in atkrs:
          self.aps.append(AtkOp(p))
        if p in defrs:
          self.dps.append(DefOp(p))
    self.players = []
    for a in self.aps:
      ap = Player(a, self.gmap.g.getrandomspawnpos(), 0)
      ap.match = self
      self.players.append(ap)
    for d in self.dps:
      dp = Player(d, self.gmap.g.getrandomobjpos(), 0)
      dp.match = self
      self.players.append(dp)
    for x in self.players:
      x.match = self


  def vis(self, p, q):
    if p.z != q.z:
      return False
    if p == q:
      return True
    if p.x == q.x and (p.y == q.y + 1 or q.y == p.y + 1):
      return True
    if p.y == q.y and (p.x == q.x + 1 or q.x == p.x + 1):
      return True
    a = min(p.x, q.x)
    b = max(p.x, q.x)
    c = min(p.y, q.y)
    d = max(p.y, q.y)
    if a == b:
      for x in range(c + 1, d):
        p1 = Pos(a, x, p.z)
        tmp = self.gmap.g.loc(p1)
        if type(tmp) == Wall and tmp.getstatus() != WallStatus.DESTROYED:
          return False
        if (type(tmp) == Door or type(tmp) == Window) and \
          (tmp.getstatus() == DoorStatus.BARRICADED or tmp.getstatus() == DoorStatus.CASTLED):
          return False
    if c == d:
      for x in range(a + 1, b):
        p1 = Pos(x, c, p.z)
        tmp = self.gmap.g.loc(p1)
        if type(tmp) == Wall and tmp.getstatus() != WallStatus.DESTROYED:
          return False
        if (type(tmp) == Door or type(tmp) == Window) and \
          (tmp.getstatus() == DoorStatus.BARRICADED or tmp.getstatus() == DoorStatus.CASTLED):
          return False
    else:
      for i in range(a + 1, b):
        for j in range(c + 1, d):
          p1 = Pos(i, j, p.z)
          tmp = self.gmap.g.loc(p1)
          if type(tmp) == Wall and tmp.getstatus() != WallStatus.DESTROYED:
            return False
          if (type(tmp) == Door or type(tmp) == Window) and \
            (tmp.getstatus() == DoorStatus.BARRICADED or tmp.getstatus() == DoorStatus.CASTLED):
            return False
    return True

  def cansee(self, p):
    cs = []
    c = 0
    for i in range(1, sum(self.dim)):
      tmp = self.isdist(p, i)
      for j in tmp:
        if self.vis(p, j):
          cs.append(j)
          c += 1
      if c == 0:
        return cs
      c = 0

  def dist(self, p, n):
    ps = []
    for i in range(self.dim[0]):
      for j in range(self.dim[1]):
        p1 = Pos(i, j, p.z)
        if p.dist(p1) < n and self.gmap.g.loc(p1) is not None:
          ps.append(p1)
    return ps

  def isdist(self, p, n):
    ps = []
    for i in range(self.dim[0]):
      for j in range(self.dim[1]):
        p1 = Pos(i, j, p.z)
        if p.furthz(p1) == n and self.gmap.g.loc(p1) is not None:
          ps.append(p1)
    return ps

  def getnearestbnds(self, p):
    if type(p) == str:
      x = self.gmap.g.getbndposs(p)
    else:
      x = [p]
    abc = defaultdict(list)
    ab = []
    mm = 100
    for i in [self.gmap.g.roms, self.gmap.g.hals, self.gmap.g.strs, self.gmap.g.otsd]:
      for j in i:
        for k in j.poss:
          for l in x:
            abc[j.name].append((l.dist(k)))
    for n in abc.keys():
      ab.append((min(abc[n]), n))
    return ab

  def getnearesttrns(self, s): # rappels not implemented yet
    ret = []
    for t in self.gmap.g.trns:
      if (t.getstatus() != WallStatus.UNBREAKABLE and type(t) != RappelD and type(t) != RappelU and type(t) != BrkFloor):
        if t.con[0] == s or t.con[1] == s:
          ret.append(t)
    return ret

  def filtertrn(self, s, typ, stat=None):
    a = []
    b = []
    for tr in self.getnearesttrns(s):
      if type(tr) == typ:
        a.append(tr)
    if stat:
      for i in a:
        if i.getstatus() == stat:
          b.append(i)
      return b
    else:
      return a

  def find_wall_grp(self, s, atk=False):
    x = []
    y = []
    z = []
    z1 = defaultdict(list)
    z2 = defaultdict(list)
    q = None
    if not atk:
      q = WallStatus.DEFAULT
    for tr in self.filtertrn(s, Wall, q):
      x.append((tr, tr.pos.x))
      y.append((tr, tr.pos.y))
    for i in x:
      z1[i[1]].append(i[0])
    for j in y:
      z2[j[1]].append(j[0])
    for w in z1.keys():
      if len(z1[w]) > 3:
        z.append(z1[w])
    for w in z2.keys():
      if len(z2[w]) > 3:
        z.append(z2[w])
    return z

  def getbndneartrn(self, p):
    pass

  def getnearestrooms(self, s):
    a = []
    ab = {}
    abc = defaultdict(list)
    for i in self.gmap.g.getbndposs(s):
      a.append(self.getnearestbnds(i))
    for x in a:
      for y in x:
        if y[1] != s:
          abc[y[1]].append(y[0])
    for j in abc.keys():
      ab[j] = min(abc[j])
    return ab

  def pop_trns(self):
    for t in self.gmap.g.trns:
      if t.getstatus() == WallStatus.UNBREAKABLE:
        continue
      p = self.gmap.g.getloc(t)
      u = Pos(p.x, p.y - 1, p.z)
      d = Pos(p.x, p.y + 1, p.z)
      l = Pos(p.x - 1, p.y, p.z)
      r = Pos(p.x + 1, p.y, p.z)
      a = Pos(p.x, p.y, p.z + 10)
      b = Pos(p.x, p.y, p.z - 10)
      s1 = type(self.gmap.g.loc(u)).mro()[1]
      s2 = type(self.gmap.g.loc(d)).mro()[1]
      s3 = type(self.gmap.g.loc(l)).mro()[1]
      s4 = type(self.gmap.g.loc(r)).mro()[1]
      if type(t) == Wall or type(t) == Door or type(t) == Window or type(t) == HVault:
        if s1 == Bounded and s2 == Bounded:
          t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(d).name)
        elif s3 == Bounded and s4 == Bounded:
          t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(r).name)
        elif s1 == Bounded and s3 == Bounded:
          t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(l).name)
        elif s1 == Bounded and s4 == Bounded:
          t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(r).name)
        elif s2 == Bounded and s3 == Bounded:
          t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(l).name)
        elif s2 == Bounded and s4 == Bounded:
          t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(r).name)
        else:
          if s3 == Bounded:
            tp = self.gmap.g.loc(Pos(p.x + 1, p.y, p.z - 10))
            if tp and type(tp).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 1, p.y, p.z - 10)).name)
          if s4 == Bounded:
            tp = self.gmap.g.loc(Pos(p.x - 1, p.y, p.z - 10))
            if tp and type(tp).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x - 1, p.y, p.z - 10)).name)
          if s1 == Bounded:
            tp = self.gmap.g.loc(Pos(p.x, p.y + 1, p.z - 10))
            if tp and type(tp).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x, p.y + 1, p.z - 10)).name)
          if s2 == Bounded:
            tp = self.gmap.g.loc(Pos(p.x, p.y - 1, p.z - 10))
            if tp and type(tp).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x, p.y - 1, p.z - 10)).name)
      if type(t) == Hatch:
        if type(self.gmap.g.loc(l)) == Bounded:
          t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x - 1, p.y, p.z + 10)).name)
        else:
          t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x + 1, p.y, p.z + 10)).name)
      if type(t) == Trapdoor:
        if type(self.gmap.g.loc(l)) == Bounded:
          t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x - 1, p.y, p.z - 10)).name)
        else:
          t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x + 1, p.y, p.z - 10)).name)
      if type(t) == LadderU:
        if type(self.gmap.g.loct(Pos(p.x + 1, p.y, p.z + 10))) == LadderD:
          t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 2, p.y, p.z + 10)).name)
        elif type(self.gmap.g.loct(Pos(p.x - 1, p.y, p.z + 10))) == LadderD:
          t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x - 2, p.y, p.z + 10)).name)
        elif type(self.gmap.g.loct(Pos(p.x, p.y + 1, p.z + 10))) == LadderD:
          t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x, p.y + 2, p.z + 10)).name)
        elif type(self.gmap.g.loct(Pos(p.x, p.y - 1, p.z + 10))) == LadderD:
          t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x, p.y - 2, p.z + 10)).name)
        else:
          print(self.gmap.g.loc(Pos(p.x, p.y + 1, p.z + 10)))
      if type(t) == LadderD:
        if type(self.gmap.g.loct(Pos(p.x + 1, p.y, p.z - 10))) == LadderU:
          t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 2, p.y, p.z - 10)).name)
        if type(self.gmap.g.loct(Pos(p.x - 1, p.y, p.z - 10))) == LadderU:
          t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x - 2, p.y, p.z - 10)).name)
        if type(self.gmap.g.loct(Pos(p.x, p.y + 1, p.z - 10))) == LadderU:
          t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x, p.y + 2, p.z - 10)).name)
        if type(self.gmap.g.loct(Pos(p.x, p.y - 1, p.z - 10))) == LadderU:
          t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x, p.y - 2, p.z - 10)).name)
      if type(t) == VVault:
        if s3 == Bounded:
          ab = type(self.gmap.g.loc(Pos(p.x + 1, p.y, p.z - 10))).mro()[1]
          if ab == Bounded:
            t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 1, p.y, p.z - 10)).name)
          else:
            if type(self.gmap.g.loc(Pos(p.x + 2, p.y, p.z - 10))).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 2, p.y, p.z - 10)).name)
            else:
              if type(self.gmap.g.loc(Pos(p.x + 2, p.y + 1, p.z - 10))).mro()[1] == Bounded:
                t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 2, p.y + 1, p.z - 10)).name)
              else:
                t.add_con(self.gmap.g.loc(l).name, self.gmap.g.loc(Pos(p.x + 2, p.y - 1, p.z - 10)).name)
        elif s4 == Bounded:
          ab = type(self.gmap.g.loc(Pos(p.x - 1, p.y, p.z - 10))).mro()[1]
          if ab == Bounded:
            t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x - 1, p.y, p.z - 10)).name)
          else:
            if type(self.gmap.g.loc(Pos(p.x - 2, p.y, p.z - 10))).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x - 2, p.y, p.z - 10)).name)
            else:
              if type(self.gmap.g.loc(Pos(p.x - 2, p.y + 1, p.z - 10))).mro()[1] == Bounded:
                t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x + 2, p.y + 1, p.z - 10)).name)
              else:
                t.add_con(self.gmap.g.loc(r).name, self.gmap.g.loc(Pos(p.x + 2, p.y - 1, p.z - 10)).name)
        elif s1 == Bounded:
          ab = type(self.gmap.g.loc(Pos(p.x, p.y + 1, p.z - 10))).mro()[1]
          if ab == Bounded:
            t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x, p.y + 1, p.z - 10)).name)
          else:
            if type(self.gmap.g.loc(Pos(p.x, p.y + 2, p.z - 10))).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x, p.y + 2, p.z - 10)).name)
            else:
              if type(self.gmap.g.loc(Pos(p.x + 1, p.y + 2, p.z - 10))).mro()[1] == Bounded:
                print(u, s1, self.gmap.g.loc(Pos(44,33,10)))
                t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x + 1, p.y + 2, p.z - 10)).name)
              else:
                t.add_con(self.gmap.g.loc(u).name, self.gmap.g.loc(Pos(p.x - 1, p.y + 2, p.z - 10)).name)
        elif s2 == Bounded:
          ab = type(self.gmap.g.loc(Pos(p.x, p.y - 1, p.z - 10))).mro()[1]
          if ab == Bounded:
            t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x, p.y - 1, p.z - 10)).name)
          else:
            if type(self.gmap.g.loc(Pos(p.x, p.y - 2, p.z - 10))).mro()[1] == Bounded:
              t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x, p.y - 2, p.z - 10)).name)
            else:
              if type(self.gmap.g.loc(Pos(p.x + 1, p.y - 2, p.z - 10))).mro()[1] == Bounded:
                t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x + 1, p.y - 2, p.z - 10)).name)
              else:
                t.add_con(self.gmap.g.loc(d).name, self.gmap.g.loc(Pos(p.x - 1, p.y - 2, p.z - 10)).name)
      # if type(t) == RappelU:
      #   if type(self.gmap.g.loc(p.zz(p.z+10))) == RappelD:
      #     print(self.gmap.g.loc(p), self.gmap.g.loc(p.zz(p.z+10)))

  def prep_phase(self):
      walls = []
      cc = {}
      nrs = []
      for t in self.filtertrn(self.gmap.g.objs.a, Wall, WallStatus.DEFAULT):
        if t.con[0] != self.gmap.g.objs.b and t.con[1] != self.gmap.g.objs.b:
          walls.append(t)
      for t in self.filtertrn(self.gmap.g.objs.b, Wall, WallStatus.DEFAULT):
        if t.con[0] != self.gmap.g.objs.a and t.con[1] != self.gmap.g.objs.a:
          walls.append(t)
      d = 20 - len(walls)
      if d < 0:
        f = [self.find_wall_grp(i) for i in [self.gmap.g.objs.a, self.gmap.g.objs.b]]
        # if walls connect a  and b, dont reinforce
      if d >= 0:
        for i in walls:
          i.status = WallStatus.REINFORCED
        if d > 0:
          aa, bb = (self.getnearestrooms(self.gmap.g.objs.a), self.getnearestrooms(self.gmap.g.objs.b))
          for k in aa.keys():
            if k != self.gmap.g.objs.a and k != self.gmap.g.objs.b:
              if aa[k] < bb[k]:
                cc[k] = aa[k]
              else:
                cc[k] = bb[k]
        # one wall takes up ~2 grid cells generally, 5 * 2 * 2 = 20
        mv = min(cc.items())
        for k in cc.keys():
          if cc[k] == mv[1]:
            nrs.append(k)
        f = [self.find_wall_grp(i) for i in nrs]
        g = []
        for i in f:
          if i == []:
            f.remove(i)
        for i in f[:-1]:
          for j in i:
            if len(j) == d:
              g.append(j)
        for w in choice(g):
          w.status = WallStatus.REINFORCED

  def get_adj_bnds(self, s):
    d = []
    x = self.getnearestbnds(s)
    y = self.getnearesttrns(s)
    for i in x:
      for j in y:
        if j.con == (i[1], s) or j.con == (s, i[1]) and i[1] != s:
          d.append(i)
    dd = list(set(d))
    for i in dd:
      if i[1] == s:
        dd.remove(i)
    return dd
  
  def check_adj(self, s1, s2):
    for i in self.get_adj_bnds(s1):
      print(i)
      if i[1] == s2:  return True
    return False

  def find_path(self, a, b, k=None):
    visited = defaultdict(list)
    q = deque()
    for i in self.getnearestbnds(self.gmap.g.getbndposs(a)[0]):
      visited[i[1]] = 0
    visited[a] = 1
    q.append(a)
    while len(q) > 0:
      n = q.pop()
      for i in range(len(visited.keys())):
        

    x = self.get_adj_bnds(a)
    y = self.get_adj_bnds(b)
    for i in x:
      for j in y:
        if b == i[1]:
          return
        if a == j[1]:
          return
        k[i[1]].append(j[1])
        # self.find_path(i, j, k)
    return k

  def find_all_paths(self, a, b):
    pass