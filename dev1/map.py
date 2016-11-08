def f(x) :
    return x*x
r = map (f,[ 1,2,3,4,5,6,7,8,9])
list(r)
#for
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
    #把这个list所有数字转为字符串：
    list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))