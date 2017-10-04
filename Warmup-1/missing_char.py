#Given Solution
def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

# Solution #1

def missing_char(str, n):
  return str[0:n] + [n+1:]

#Solution #2

def missing_char(str, n):
  return str[0:n] + [n+1:]

#
