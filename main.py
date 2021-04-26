
class MyClass:

    def __init__(self):
        self.value = 0
        print("Initialized")
    
    def method1(self):
        self.value += 1
        print(f"Value is now {sekf.value}")

    def method2(self):
        print("Method 2 called")

myObject = MyClass()
myObject.method1()
myObject.method2()