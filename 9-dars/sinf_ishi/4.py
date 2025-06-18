from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

class Manager(Employee):

    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department=department

    def get_details(self) -> str:
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}" 

    def calculate_bonus(self) -> float:
        return self.salary * 0.1

class Department(Employee):
    
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.programming_language           #tugatilmagan!

manager = Manager(name="Alice", salary=120000, department="Sales")
print(manager.get_details())
print(manager.calculate_bonus())
