#要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
f.write('')
f.write('world!')
print(f.getvalue())
#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
     s = f.readline()
     if s == '':
        break
     print(s.strip())
    #BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
     from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())