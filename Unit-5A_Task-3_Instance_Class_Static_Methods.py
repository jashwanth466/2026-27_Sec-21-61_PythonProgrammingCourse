# Example solution: instance, class, and static methods
class Demo:
    college = "RVRJC"

    def set_name(self, name):
        self.name = name
        print("Instance:", self.name)

    @classmethod
    def show_college(cls):
        print("Class:", cls.college)

    @staticmethod
    def info():
        print("Static: utility message")


obj = Demo()
obj.set_name("Anu")
Demo.show_college()
Demo.info()