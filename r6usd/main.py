from gamemap.pos import Pos
from match.match import Match
from player.player import Player


if __name__ == '__main__':
  m1 = Match("BORDER", ["Thermite", "Thatcher", "Zofia", "Jackal", "Iq", "Rook", "Caveira", "Mira", "Lesion", "Smoke"])
  # print(m.cansee(Pos(88,49,10)))
  # for i in m1.gmap.g.trns:
  #   if type(i) == :
  #     if i.con == ():
  #       print(i)

  # for i, j in m1.getnearestbnds(Pos(54, 30, 0)):
  #   print(i, j)

  m1.prep_phase()
  for i in m1.players:
    i.plan_prep()
    print(i.strat)


  print()

# for j in [m1.gmap.g.roms, m1.gmap.g.hals, m1.gmap.g.strs, m1.gmap.g.otsd]:
#   for k in j:
#     for i in m1.getnearesttrns(k.name):
#       print(i)
#       print()
#       print("abcdefghi")
#       print()
