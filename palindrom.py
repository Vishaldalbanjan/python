
print("for string")
a="racecar"
b=""

for i in a:
    b=i+b

if a==b:
    print("palindrom")
else:
    print("not palindrom")

print("for numbers")
num=121
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10

if num==rev:
    print("palindrom")
else:
    print("not palindrom")