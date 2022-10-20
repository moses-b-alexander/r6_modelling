from gamemap.transition import Transition
from gamemap.statuses import NopeStatus

class HVault(Transition):
  """ repr of horizontal vaults (vaults which don't transition floors)
  in the game map"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "I"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Horizontal Vault" + super().__str__()

class VVault(Transition):
  """ repr of vertical vaults (vaults which transition floors)
  in the game map; these vaults are one-way only generally"""
  def __init__(self, pos, con=(), status=NopeStatus.DEFAULT):
    assert status == NopeStatus.DEFAULT
    self.id = "J"
    super().__init__(pos, con, status)

  def __str__(self):
    return "Vertical Vault" + super().__str__()
