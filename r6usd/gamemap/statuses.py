

def enum(**enums):
  return type('Enum', (), enums)

nopestatuses = ['Neutral']
NopeStatus = enum(DEFAULT=nopestatuses[0])

doorstatuses = ['DoorDefault', 'DoorBarricaded', 'DoorBroken',\
  'DoorCastled', 'DoorShielded']
DoorStatus = enum(DEFAULT=doorstatuses[0], BARRICADED=doorstatuses[1],\
  BROKEN=doorstatuses[2], CASTLED=doorstatuses[3], SHIELDED=doorstatuses[4])

wallstatuses = ['WallDefault', 'WallDamaged', 'WallDestroyed',\
  'WallReinforced', 'WallUnbreakable']
WallStatus = enum(DEFAULT=wallstatuses[0], DAMAGED=wallstatuses[1],\
  DESTROYED=wallstatuses[2], REINFORCED=wallstatuses[3],\
  UNBREAKABLE=wallstatuses[4])

objsstatuses = ['ObjsDisarmed', 'ObjsPlanted', 'ObjsDefused', 'ObjsArmed']
ObjsStatus = enum(DEFAULT=objsstatuses[0], PLANTED=objsstatuses[1],\
  DEFUSED=objsstatuses[2], ARMED=objsstatuses[3])

gamestatuses = ['ATKItv', 'DEFItv', 'ATKWin', 'DEFWin', 'Draw']
GameStatus = enum(DEFAULT=gamestatuses[0], POSTDEFUSE=gamestatuses[1],\
  ATKWIN=gamestatuses[2], DEFWIN=gamestatuses[3], DRAW=gamestatuses[4])

# disarmed -> planting | atk has initiative
# planting failure -> disarmed | atk has initiative
# disarmed -> planting failure (repeated) -> disarmed | def wins
# planting success -> planted | def has initiative
# planted -> defusing | def has initiative
# defusing failure -> planted | def has initiative
# defusing success -> Defused | def wins
# planted -> defusing failure (repeated) -> armed | atk wins

map_names = ["TESTMAP", "BANK", "BORDER", "CHALET", "CLUBHOUSE",
  "COASTLINE", "CONSULATE", "KAFE", "KANAL", "OREGON", "SKYSCRAPER",
  "THEMEPARK"]
MAPS = enum(DEFAULT=map_names[0], BANK=map_names[1], BORDER=map_names[2],\
  CHALET=map_names[3], CLUBHOUSE=map_names[4], COASTLINE=map_names[5],\
  CONSULATE=map_names[6], KAFE=map_names[7], KANAL=map_names[8],\
  OREGON=map_names[9], SKYSCRAPER=map_names[10], THEMEPARK=map_names[11])