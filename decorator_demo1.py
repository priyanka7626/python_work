def star(func):
    def inner(*n):
        print('*'*30)
        func()
        print('*'*30)
    return inner
def hash(func):
    def inner(*n):
        print('#'*30)
        func()
        print('#'*30)
    return inner
@star
@hash
def buisness():
    print('Inside buisness logic')
buisness()
def event():
    pass

def welcome():
    pass





import sys
sys.exit(0)
def star(func):
    def inner(*n):
        print('*' * 30)
        func()
        print('*' * 30)
    return inner

def hash(func):
    def inner(*n):
        print('#' * 30)
        func()
        print('#' * 30)
    return inner

def dash(func):
    def inner(*n):
        print('-' * 30)
        func()
        print('-' * 30)
    return inner
@star
@hash
@dash
def bussiness_fun():
    print("Inside Bussiness Function")

bussiness_fun()