n=int(input("enter no"))

if n==0 or n==1:
    print("not prime")
elif n==2:
    print("prime")
while n>2:
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        print("not prime")
        break
    else:
        print("prime")
        break