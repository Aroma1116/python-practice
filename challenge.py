class Square:
  square_list = []

  def __init__(self, l):
    self.len = l
    self.square_list.append(self)

  def __repr__(self):
    print("{} by {} by {} by {}".format(self.len, self.len,self.len,self.len))

  s1 = Square(29)
  print(s1)