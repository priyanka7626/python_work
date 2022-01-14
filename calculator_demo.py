
class Demo:
    def add(self):
        print("This is add function")
    def m(self):
        Demo.a=10
        print(Demo.a)

    def n(self):
        print(a)  # 'a' is local variable of m()
    def sub(self):
        print('hi')

d = Demo()
d.m()