a=10
b=c=20
print(c)

d,e,f=1,2,3
print(e)

Name="Laxmi"
name="chaitra"  #case sensitive
print(Name)

#Data Types
Age=19 #int
_name="laxmi" #String
weight=56.5 #float
is_student=True #bool

print(type(Age))     #<class 'int'>
print(type(_name))   #<class 'str'>
print(type(weight))  #<class 'float'>
print(type(is_student))  #<class 'bool'>

is_student="yes"
print(type(is_student))  #it will show this but above is bool, it changed to str <class 'str'> Dynamically changed

age_float=float(Age)
print(age_float)
s=100
print(int(s)+Age)   #type conversion

#Arithmetec Operations

x=10
y=3
print(x+y) #13
print(x-y)  #7
print(x*y)  #30
print(x/y)  #3.3333333
print(x//y)  #3
print(x%y)   #1
print(x**y)  #1000

#Home Work practice
#swap of two numbers

m=10
n=20

temp=m
m=n
n=temp

print("m is",m)
print("n is",n)


#2nd Method
k=30
l=40

k,l=l,k
print("K is",k)
print("L is",l)

#3rd method

e=5  
f=15  

e=e+f  # 5+15=20
f=e-f   #20-15=5  
e=e-f   #20-5=15
print("e is",e)     #e is 15
print("f is",f)      #f is 5