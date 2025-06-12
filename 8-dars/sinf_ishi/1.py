class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Salom, men {self.name}")

class Student(Person):
    def __init__(self, name, rating=0):
        super().__init__(name)
        self.rating = rating        

    def say_hello(self):
        print(f"Salom, men {self.name} {self.rating}")
  

s = Student("Ali", 5)
s.say_hello()  # Salom, men Ali
