#Given

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 
  
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.
  
 #solution  01

def front3(str):
  if len(str) <= 3:
    return str*3
  front = str[:3]
  
  return front*3


#Solution 02
def front3(str):
  if len(str) < 3:
    return str+str+str
  else:
    return str[:3] + str[:3] + str[:3]
  
  #Solution 03
  
  
