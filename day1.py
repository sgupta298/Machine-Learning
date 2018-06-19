x=[]
y=[]
z=[]
for i in range(0,3):
   x.append(input())
for i in range(0,3):
    y.append(input())
for i in range(0,3):
    z.append(int(x[i])+int(y[i]))
    print(z[i])
def add(a,b):
    return(int(a) + int(b))
a=input("enter a:-")
b=input("enter b:-")
c=add(a,b)
print("sum is ", c)
x=[3,67,89,34]
x.sort()
print(x)
x.reverse()
print(x)
print(x.index(3))
y=x.copy()
print(y)
class students:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno


p2 = students("sanjay", 51)
print(p2.name)
