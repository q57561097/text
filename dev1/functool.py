int('1234567')
int('12345',base=8)
int('12345',base=16)

#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值
import functools
int2=functools.partial(int,base=2)
