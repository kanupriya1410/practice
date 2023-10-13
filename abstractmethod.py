from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return(self.l*self.b)
    
c=Rectangle(12,2)
print(c.area())

class Node:
    def __init__(self,data):
        self.data=data
        
#%%
class Node:
    def __init__(self,data):
        self.data=data
class stack:
    def __init__(self):
        self.top=None
    def Push(self):
        n=int(input("enter the number : "))
        n1=Node(n)
        if self.top is None:
            self.top=n1
            self.top.next=None
        else:
            n1.next=self.top
            self.top=n1
            
    def Pop(self):
        if self.top is None:
            print("Stack is emplt")
        elif self.top.next is None:
            self.top=None
        else:
            tmp=self.top
            self.top=tmp.next
            tmp=None
    def Display(self):
        if self.top is None:
            print("Empty Stack")
        else:
            
            tmp=self.top
            while(tmp):
                print(tmp.data,end="--->")
                tmp=tmp.next
s=stack()
while(1):
    print("The operation \n1 ---PUSH \n2----POP \n3-----Display \n4--EXIT)")
    opt=input("Enter the option = ")
    if opt=='1':
        s.Push()
    elif opt=='2':
        s.Pop()
    elif opt=='3':
        s.Display()
    else:
        print("exit")
        break
    
#%%
d1="radar"
c=list("radar")
d=''
for i in range(len(c)-1,-1,-1):
    
    d+=c[i]
    #print(c[i])
print(d)
if d1==d:
    print("palii")
else:
    print("Not")
#%%


n=input("enter the string =").lower()
print(n)
vowels=list("aeiou")
v=0
c=0
ls1=[]
ls2=[]
for i in n:
    if i.isalpha():
        if i in vowels:
            v+=1
            ls1.append(i)
        else:
            c+=1
            ls2.append(i)
print(f'total vowels {v}')
print(ls1)
print(f"Total consonant {c}")
print(ls2)

#%%
n=list(input("enter any string: ").lower())
print(n)
ls=[]
for i in n:
    if i not in ls:
        ls.append(i)
print(''.join(ls))
#%%
c=list(input("enter any string : ").lower())
ch=c[0]
count=0
out=""
for i in c:
    if i==ch:
        count+=1
    else:
        out=out+ch+str(count)
        count=1
        ch=i
out=out+ch+str(count)
print(out)
#%%
c=[12,23,23,1,2,25,25]
cs=[]
for i in c:
    if i not in cs and c.count(i)>2:
        cs.append(i)
print(cs)
#%%
lst = ['this', 'is', 'a', 'sample', 'sentence','jjop']
if len(lst) >= 2:
    lst[-2] = lst[-2][1:]
    lst[-1] = lst[-1][1:]

print(lst)
#%%
ls=[['ram',35],['rita',23],['meet',56],['sneha',78],['darshan',99],['mohit',35]]
dict1=dict(ls)
print(dict1)
d=sorted(dict1.values())
print(d)
second_largest=d[-2]
print(second_largest)
for ele in ls:
    print(ele)
    if ele[1]==second_largest:
        print(ele[0])
#%%
ls=[['ram',35],['rita',23],['meet',56],['sneha',78],['darshan',99],['mohit',35]]
dict1=dict(ls)
print(dict1)
d=sorted(dict1.values())
print(d)
second=d[-2]
for key,value in dict1.items():
    if value==second:
        print(key,value)
#%%
def binary(arr,x):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
    return -1
arr=[23,34,45,56,67,78]
x=23
res=binary(arr,x)
if res==-1:
    print("not found")
else:
    print("found")
#%%
arr=[23,34,44,56,67,78]
x=78
res=binary(arr,x)
if res==-1:
    print(f'{x} is not found in array')
else:
    print(f'{x} is found in {res} position in array')

#%%
d={}
d1=dict()
print(type(d))
print(type(d1))        
d1.update({"Name":["kanu"],"Age":[23]})
print(d1)   
d1.update({"salary":[1200]})
print(d1)
d1.pop('Age')
print(d1)

def add(a,b):
    '''
    Addition of two Number
    '''
    return(a+b)
print(add.__doc__)
c=add(2,3)
print(c)

k="kanupriya"
c=k[::-1]
print(c)
#%%
s="i am a python developer"
ls=[]
d=s.split()
print(d)
for i in range(len(d)-1,-1,-1):
    ls.append(d[i])
print(ls)

#%%
ls = ["python", "java", "c"]
res={}
for i in range(len(ls)):
    res[i]=ls[i]
print(res)
    
#%%  
  
ls=dict()
ls.update({"name":["kanu"]})
print(ls)

#%%
import pandas as pd
data={"id":[1],"name":["kanu"]}
df1=pd.DataFrame(data)
print(df1)
data1={"id":[1],"salary":[100]}
df2=pd.DataFrame(data1)
print(df2)

df3=df1.merge(df2,on="id")
print(df3)
df4=pd.concat([df1,df2])
print(df4)
#%%
#with file
import pandas as pd
import csv
data={"id":[1],"name":["kanu"]}
df1=pd.DataFrame(data)
df1.to_csv("c:\\python_data\\emp.csv",index=False)
# print(df1)
with open("c:\\python_data\\emp.csv","r") as file:
    #load=pd.read_csv(file)
    for i in file:
        print(i,end="")
#%%
import pandas as pd

data = {"id": [1], "name": ["kanu"]}
df1 = pd.DataFrame(data)
df1.to_csv("c:\\python_data\\emp.csv", index=False)

# Read the CSV file using with open
with open("c:\\python_data\\emp.csv", "r") as file:
    for line in file:
        print(line, end="")  # Print each line in the CSV file

    


    
#%%
import pandas as pd
data={"name":["kanu","Payal","gunjun"],"Age":[23,34,43]}
df=pd.DataFrame(data)
print(df)
df.to_csv("c:\\python_data\\emp.csv",index=True)
with open ("c:\\python_data\\emp.csv","r") as file:
    for i in file:
        print(i)
















