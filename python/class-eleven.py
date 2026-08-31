class UserForm:
  def __init__(self, name, age, password):
    # creating the attributes of the class
    self.name = name
    self.age = age
    self.password = password
  
  def printName(self):
    print(self.name)
    return self.name

  def check_password(self):
    if len(self.password) < 6:
      print("Password length should be valid")
    else:
      print("Password is valid")


my_info = UserForm("Ali", 25, "ABCDEFGHIK")
print(my_info.name)
print(my_info.age)
my_info.check_password()
