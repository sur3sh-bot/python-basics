a=float(input("enter 1st operand: "))
b=float(input("enter 2nd operand: "))
op=input("enter operator: ")
if op=="+":
    print("result: ", a+b)
elif op=="-":
    print("result: ", a-b)
elif op=="*":
    print("result: ", a*b)
elif op=="/":
    print("result: ", a/b)
else:
    print("invalid")
