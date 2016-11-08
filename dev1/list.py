classmates = ['Michael', 'Bob', 'Tracy']
classmates
len(classmates)
L = [ ]
n = 1
while n<=99 :
    L.append(n)
    n=n+2
L
r = [ ]
n=3
for i in range (n):
    r.append(L[i])
#切片
L[1:3]
L[-2:-1]
#前10个数，每两个取一个：
L[:10:2]
#迭代

for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)
#列表生成式
list(range(1,11)) #生成[1x1, 2x2, 3x3, ..., 10x10]
f = [ ]
for x in range(1,11):
    f.append(x*x)
[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0 ] #筛选出仅偶数的平方
#使用两层循环，可以生成全排列
[m+n for m in 'ABC' for n in 'EFG']
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
g ={ 'x':'a','y':'b','z':'c'}
for k,v in g.items():
    print(k,'=',v)
    #列表生成式也可以使用两个变量来生成list
    [k+'='+ v for k,v in g.items()]
    #把一个list中所有的字符串变成小写
    h = [ 'BB','CC','DD']
[s.lower() for s in h]
#生成器
ll = [ x*x for x in range(10)]
gg = ( x*x for x in range(10))
for n in gg :
    print(n)
#斐波拉契数列:除第一个和第二个数外，任意一个数都可由前两个数相加得到1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n,a,b = 0,0,1
    while n<max :
        print(b)
        a,b=b,a+b  #t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]

        n=n+1
        return 'done'
def fib(max):
    n,a,b =0,0,1
    while n<max :
        yield b
        a,b=b,a+b
        return 'done'
        for n in fib(6):
            print(n)
    #但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
ggg = fib(6)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break