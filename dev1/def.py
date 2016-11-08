def al(x):
    b=5+ x
    return b
b = al (6)
print (b)

def bl (age) :
    if age >= 20:
        print('your age is', age)
        print('adult')
    else:
        print('your age is ', age)
        print('teenager')
bl(15)
def cl (name,gander,age=6,city='beijing') :
    print('name:',name)
    print('gander:',gander)
    print('age:',age)
    print('city:',city)
cl('bob','7')
def dl(n) :
    if n==1 :
        return 1
    return n * dl(n-1)
dl(2)


