def fi(): print("I")
def fl(): print("L")
def fr(): print("R")
def fv(): print("V")

is_running = True

funcs=[fi,fl,fr,fv]
while is_running:
  for f in funcs:
    f()
  exit()
