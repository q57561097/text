#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#lambda x: x * x实际上就是
def f(x):
    return x*x
#匿名函数作为返回值返回
def b(x,y):
    return lambda :x*x+y*y