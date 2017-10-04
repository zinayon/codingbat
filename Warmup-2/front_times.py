#Given
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result


# Solve 01
def front_times(str, n):
  if len(str) <3:
    return str*n
  else:
    return str[:3]*n
