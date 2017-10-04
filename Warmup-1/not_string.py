def not_string(str):
  if len(str) >= 3 and str [:3] == "not":     # len(str) = lenth of the string  and [:3] count of string from the begining
    return str
  else:
    return "not "+str  
  
  #####
