class People:

  def create_identity(self, name):
    self.name = name;
    print("Name: ", name)

  def printer(self):
      print(self.name)

person1 = People();
person2 = People();

person1.create_identity("Walter")
person2.create_identity("Aron")

person1.printer();
