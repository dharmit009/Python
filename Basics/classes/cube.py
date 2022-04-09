class cube:

  def __init__(self, length=None, breadth=None, height=None):
      if length and breadth and height is None:
          return None;
      else:
        self.l = length;
        self.b = breadth;
        self.h = height;


  def area(self):
    out = self.l * self.b * self.h;
    return out

cube1 = cube(1,1,1);
cube2 = cube(2,2,2);

print(cube1.area())
print(cube2.area())
