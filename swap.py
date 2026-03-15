a=10 #without using a 3rd variable
b=20
a,b=b,a
print("value of a is: ",a)
print("value of b is: ",b)

c=30 #with using a third variable
d=40
temp=c
c=d
d=temp
print("the value of c is: ",c)
print("the value of d is: ",d)