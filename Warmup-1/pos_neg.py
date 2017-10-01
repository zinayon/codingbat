def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a*b <0:
      return True
    else:
      return False
  # This solve is from Sadman Niloy 
  # A group member of PythonBD
  #https://www.facebook.com/groups/pythonbd/
