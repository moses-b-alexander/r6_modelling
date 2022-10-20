from gamemap.pos import Pos
from gamemap.wall import Wall
from player.attacker import AtkOp
from player.defender import DefOp
from player.strategy import Strategy, Tactic
from random import randint, choice

class Player:
  """ data model for players"""
  def __init__(self, op, pos, time):
    assert isinstance(op, AtkOp) or isinstance(op, DefOp)
    assert isinstance(pos, Pos)
    assert isinstance(time, int)
    self.op = op
    self.pos = pos
    self.time = time
    self.health = 100
    self.stunned = False
    self.hurt = False
    self.actions = []
    self.tactics = []
    self.match = None
    self.strat = None # use roles to determine via conditional


  def __str__(self):
    return f"{str(self.op)}\n@ {str(self.pos)}, {self.time} sec\n{self.health} health\n{self.strat}\n\n"

  def plan_prep(self):

    if isinstance(self.op, AtkOp):
      if "Hard Breacher" in self.op.roles:
        q = None
        r = choice([self.match.gmap.g.objs.a, self.match.gmap.g.objs.b])
        if r == self.match.gmap.g.objs.a:
          q = self.match.gmap.g.objs.b
        else:
          q = self.match.gmap.g.objs.a
        ws = self.match.find_wall_grp(r, True)
        wss = []
        for i in ws:
          if i[0].con == (q, r) or i[0].con == (r, q):
            pass
          else:
            wss.append(i)
        self.strat = Strategy("Breach walls", (choice(wss))[0].pos)
        # find path from current pos to walls OR control target zone and wait for other tm8s
      if "Frontliner" in self.op.roles:
        print(self.match.find_path(self.match.gmap.g.loc(self.pos).name, self.match.gmap.g.objs.a))
        # print(self.match.get_adj_bnds(self.match.gmap.g.objs.b))



    if isinstance(self.op, DefOp):
      pass