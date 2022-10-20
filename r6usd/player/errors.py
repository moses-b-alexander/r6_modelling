
class Error:
  """ model errors"""
  def __init__(self, s):
    assert s in err_types
    self.err = s

  def __str__(self):
    return f"{self.err}"

err_types = ["Out of ammo", "No gadgets remaining", "Impossible movement",
  "Impossible action", "Not enough time", "Illegal action"]