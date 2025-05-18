class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"{self.name}, {self.age}"

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def displayStudent(self):
        return super().display()+f', {self.major}.'

student = Student(name='ali', age='22', major='computer science')
print(student.displayStudent())
