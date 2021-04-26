
class MyClass:

    def __init__(self, a, b):
        self.value = 0
        self.a = a
        self.b = b
        print("Initialized")
    
    def method1(self):
        self.value += 1
        print(f"Value is now {self.value}")

    def method2(self):
        print(f"Method 2 called {self.a + self.b}")

myObject = MyClass()
myObject.method1()
myObject.method2()