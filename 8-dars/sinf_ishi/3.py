class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def set_address(yangi_manzil):
        return self.__address

    def __str__(self):
        return f"Name: {self.__name}\nManzili: {self.__address}"

person = Person("Kamila", "chilanzar")


class Student(Person):
    def __init__(self, name, address, courses, grades):
        super().__init__(name, address)
        self.courses = courses
        self.grades = grades

    def add_course_grade(course: str, grade: int)

    def print_grades(self)

    def defget_average_grade(self):
        10 // grade

    def __str__(self):
        return f"\nstuden:{super().__str__()}"
       
curslar = Student("Kamila", "chilanzar","matem", 5)


print(curslar)
class Teacher(Person):
    def __init__(self, name, address, courses, grades):
        super().__init__(name, address, courses, grades)

    