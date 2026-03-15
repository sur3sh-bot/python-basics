n=input("enter a number: ")#with slicing
if n==n[::-1]:
    print("it is a palindrome")
else:
    print("its not a palindrome")

x=int(input("enter a number: "))#without slicing
org=x
reverse=0
while x>0:
    digit=x%10
    reverse=reverse*10+digit
    x=x//10
if org==reverse:
    print("it is a palindrome")
else:
    print("its not a palindrome")