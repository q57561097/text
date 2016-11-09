class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
#>>> s = Student('Michael')
#>>> s() # self参数不要传入
#My name is Michael.
