from functools import  reduce
def add(x,y):
    return x+y
reduce(add,[1,3,5,7,9])
#[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10 + y
reduce(fn,[1,3,5,7,9])
