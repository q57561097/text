class Student(object):
    pass
s=Student()
s.name='bob'
print(s.name)
def set_age(self,age):
    self.age=age
    from types import MappingProxyType
    s.set_age=MappingProxyType(set_age,s)
    s.set_age(25)
    s.age
def set_score(self,score):
    self.score=score
Student.set_score=set_score
class Student(object):
    __slots__=('name','age')
s = Student()
s.age=100
s.name='bob'
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来