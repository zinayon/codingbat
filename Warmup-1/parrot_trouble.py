def parrot_trouble(talking, hour):
  if talking and (hour <7):
    return True
  if talking and (hour > 20):
    return True
  else:
    return False
