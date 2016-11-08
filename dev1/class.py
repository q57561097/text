class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
bart.name
bart.print_score()
bart.get_grade()
class Student(object):
    def __init__(self, name, score):#让内部属性不被外部访问，可以把属性的名称前加上两个下划线
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):   #外部代码要获取name和score
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):  #允许外部代码修改score
        self.__score = score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



