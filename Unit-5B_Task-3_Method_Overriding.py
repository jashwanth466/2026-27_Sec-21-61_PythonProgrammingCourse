# Example solution: method overriding
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal()
d = Dog()
a.sound()
d.sound()