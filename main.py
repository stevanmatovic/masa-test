
class MyClass:

    def __init__(self):
        self.value = 6
        print("Initialized")
    
    def method1(self):
        self.value -= 1
        print(f"Value is now {self.value}")

    def method2(self):
        print("Fucking git")

myObject = MyClass()
myObject.method1()
myObject.method2()