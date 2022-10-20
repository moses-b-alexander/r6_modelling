class Strategy:
  """ repr of player strategies"""
  def __init__(self, desc, goal):
    self.desc = desc
    self.goal = goal
    self.tactics = []

  def __str__(self):
    return f"{self.desc} @ {self.goal}: {str(self.tactics)}"

  def add_tactic(self, t):
    self.tactics.append(t)

  def exec():
    pass


class Tactic:
  """ repr of player tactics"""
  def __init__(self, desc, goal, actions):
    self.desc = desc
    self.goal = goal
    self.actions = actions

  def __str__(self):
    return f"{self.desc} @ {self.goal}: {str(self.actions)}"

  def add_action(self, a):
    self.actions.append(a)

  def exec():
    pass