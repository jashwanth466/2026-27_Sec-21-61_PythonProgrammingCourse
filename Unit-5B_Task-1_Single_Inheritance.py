# Example solution: single inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


s = Student("Anu", "Python")
s.show()
s.show_course()