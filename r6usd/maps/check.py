# funcs for checking map strings and catching common errors

def chk1(s):
  for i in s.split(' '):
    if i.count("*_*") > 1 or i[0] == "*":
        return False
  return True

def chk2(s):
  ss = ["R ", "Rf ", "H ", "Hf ", "Q ", "0 ", "RI ", "RJ ", "0I ", "0J ", "RC ", "HC ", "0C ", "RfC ", "HfC "]
  for i in s.split('\n'):
    for x in ss:
      if x in i:
        return False
  return True

def chk3(s):
  for i in s.split('\n'):
    if "  " in i or "   " in i or "    " in i or "     " in i:
      return False
  return True

def chk(s):
  fns = [chk1, chk2, chk3] # more to be added?
  for f in fns:
    if not f(s):
      return False
  return True