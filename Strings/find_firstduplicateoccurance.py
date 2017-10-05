def find_firstoccurance(string):
  dic = {}
  for char in string:
    try:
      if dic[char]==1:
        return char
    except:
      dic[char] = 1
  return None