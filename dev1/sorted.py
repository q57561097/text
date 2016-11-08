sorted([1,-1,-9,4])
sorted([1,-1,-9,4],key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)#略大小写的排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#进行反向排序
#不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

