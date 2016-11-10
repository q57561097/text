import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)
ns = itertools.takewhile(lambda x: x<=10,natuals)
list(ns)
#通过takewhile()等函数根据条件判断来截取出一个有限的序列
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC','XYZ'):
    print(c)
## 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
 