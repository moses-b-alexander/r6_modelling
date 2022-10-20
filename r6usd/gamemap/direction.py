from gamemap.statuses import enum

directions = ['North', 'East', 'South', 'West',\
  'Northeast', 'Northwest', 'Southeast', 'Southwest']
Directions = enum(N=directions[0], E=directions[1],\
  W=directions[2], S=directions[3], NE=directions[4],\
  NW=directions[5], SE=directions[6], SW=directions[7])