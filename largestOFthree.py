a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter thrid number: "))
if a>=b and a>=c:
    print("the largest is",a)
elif b>=a and b>=c:
    print("the largest is",b)
else:
    print("the largest is",c)
