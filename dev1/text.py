def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
fact(2)

def dl(n):
   return dl(n,1)
def el(num,product):
    if num == 1:
        return product
    return el(num-1,num*product)
el(5,1)