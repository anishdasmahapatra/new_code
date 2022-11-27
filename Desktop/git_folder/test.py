

nums=[4,6,1,2,7,8]
def _even(nums):
    for num in nums:
        if num%2==0:
            print(num)
            yield

s=(_even(nums))
print(next(s))
print(next(s))
print(next(s))



def _abs(func):
    def wrapper(*args,**kwargs):
        result=func(*args)
        return abs(result)
    return wrapper


@_abs   
def _value(a,b):
    return a-b

print(_value(10,20))


class Bank:
    def __init__(self,name):
        self.name=name
        

    def deposit(self,amount):
        self.amount=amount

class Bank1():
        
    def withdraw(self,amount):
        self.amount=amount

class Bank2(Bank,Bank1):

    def __init__(self,name,amount):
        super().__init__(amount)
        super().__init__(amount)
        self.tran=[]
        

    def deposit(self,amount):
        self.amount=amount
        

B=Bank2("Anish",5000)

w="rama"
from re import findall
print(findall(r"[^r^m]",w))


d={
"id":"0001",
"type":"donut",
"name":"Cake",
"ppu":0.55,
"batters":{
"batter":[
 { "id":"1001",
"type":"Regular"
 }
,{"id":"1002",
"type":"Chocolate"
}, {"id":"1003",
"type":"Blueberry" },

{"id":"1004",
"type":"Devil's Food" } ]},

"topping":[{"id":"5001",
"type":"None" },{"id":"5002","type":"Glazed" }, {
"id":"5005",
"type":"Sugar" },
{"id":"5007","type":"Powdered Sugar"
 },
           {"id":"5006", "type":"Chocolate with Sprinkles"
 }, {"id":"5003",
"type":"Chocolate"
  },  {"id":"5004","type":"Maple"
 }]
}

s="Hi how are you"
res=" "
k=s.split()
print(k[::-1])

for words in s:
    res =words+res

print(res)

print([words[::-1] for words in k])
l=[]
for item,value in d.items():
    if item=="topping":
        print(value[6]["id"])


d={'a':10,'b':20,'c':{"Anish":27,"Vivek":28}}
for item,value in d.items():
    if item=='c':
        print(value["Anish"])


s="hi how are you python is good programming language for you"
k=s.split()
from collections import defaultdict
dd=defaultdict(list)
for word in k:
    dd[word[0]].append(word)
print(dd)


d={0:0,1:2,2:4,3:6,4:8,5:10,6:12,7:14,8:16,9:18}
dd=[0,1,2,3,4,5,6,7,8,9]
print({item:item*2 for item in dd})

_sequence= lambda seq,n : seq[-n:]
print(_sequence("hello hai",3))

_txt = "apple#banana#cherry#orange"
from re import findall
print(findall(r"\w+",_txt))

f={42:'covid',12:'anish',32:'bangalore'}
print(sorted(f.items(), key= lambda item: item[0]))


a = [1, 2, 3, 4, 5]
ra = [ a[index] for index in range(len(a)-1, -1, -1) ]


d={"a":1,"b":"hello","c":85,"d":12.3}
d1={}
for i in d:
    if isinstance(d[i],int):
        d1[i]=d[i]
print(d1)

sequence="hello"
for ele in sequence[::-1]:
    print(ele,end="")

for i in range(len(sequence)):
    print((i, sequence[i]))

ite=["apple","google","walmart","flipkart","gmail"]
for i in range(len(ite)):
    print(i, ite[i])

l=lambda s: (word, len(word))
print(list(map(l,"MY NAME IS ANISH")))

dial={86:"china",91:"India",1:"usa",62:"Indonesia",55:"Brazil"}
print(sorted(dial.items(),key=lambda items:len(items[1]))[::-1])

prices={"IBM":{'current':90.1, 'low':88.3,'high':92.7},"Hp":{'Name':'Anish','Age': 27, 'Degree':'B.tech'}}

for key, value in prices. items():
    if  key=="IBM":
        print(value['current'])

for key, value in prices.items():
    if key=="Hp":
        print(value["Age"])

_dict={"a":4,"b":3,"c":5}
print(sorted(_dict.items(), key=lambda item: item[1]))

p={"ACME": 45.23,"AAPL":"ANISH","IBM":26.78}
print(sorted(p.items(),key=lambda i:i[0]))

a = [1, 2, 3, 4, 5]
ra = [ a[index] for index in range(len(a)-1, -1, -1) ]
print(ra)


s="hi how are you python is good programming language for you"
k=s.split()
from collections import defaultdict
dd=defaultdict(list)
for word in k:
    dd[word[0]].append(word)
print(dd)









        
        
    
    
        




   
    
