# Given
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]


#Solution 01
#============
def front_back(str):
  if len(str) == 1:
    return str
  if len(str) == 2:
    return str[1]+str[0]
  else:
    return str[-1:]+str[1:-1]+str[:1]
  
  #Solution 02
  #_____________________
  
  def front_back(str):
  if len(str) == 0 or len(str) == 1:
    return str
  return str[-1] + str[1:-1] + str[0]
############
