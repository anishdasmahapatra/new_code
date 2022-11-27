names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
for i in range(len(names)):
    if len(names)>6:
        print(i,names[i])

for name,index in enumerate(names):
    print(name,index)

names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
for name in names:
    if len(name)>6:
        print(name)


def prime_(num):
    for i in range(num):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
                
            else:
                print(i)
prime_(20)

def _prime(num):
    for i in range(2,num):
        if num%i!=0:
            return(f"{num} is not prime number")
            break
    else:
        print("not prime")
print(_prime(13))

l = ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"]
d={}

for item in l:
    if len(item) not in d:
        d[len(item)]=[item]
    else:
        d[len(item)]+=[item]
print(d)


def fibo(num):
    a=0
    b=1
    for i in range(10):
        c=a+b
        a,b=b,c
        print(c)
    print()

print(fibo(10))
    
s="python is a programming language and programming is fun"
long=[]
new=s.split()
for word in new:
    if len(word)>len(long) and new.count(word)==1:
        long=word
print(long)

s="hello world"
print([{letter,ord(letter)}for index,letter in enumerate(s)])



class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

s=Son("Anish","Nisith","Aswini")
s.print_name()


class Grandfather:
    def __init__(self,gfname):
        self.gfname=gfname


class Father(Grandfather):
    def __init__(self,gfname,fname):
        self.fname=fname
        Grandfather.__init__(self,gfname)

class son(Father):
    def __init__(self,gfname,fname,sname):
        Father.__init__(self,gfname,fname)
        self.sname=sname


    def print(self):
        print('Grandfather name :', self.gfname)
        print("Father name :", self.fname)
        print("Son name :", self.sname)
        

s=son("Aswini","Nisith","Anish")
s.print()

s="python is a programming language and programming is fun"
long=[]
new=s.split()   
for word in new:
    if len(word)>len(long) and new.count(word)==1:
        long=word
print(long)


s="python is a programming language and programming is fun"

l=[]
new=s.split()
for word in new:
    if len(word)>len(l) and word[0]  in "aeiou":
        l=word
print(l)

l1=[]
print([{word, new.count(word)} for word in new if len(word)>len(l1)])
