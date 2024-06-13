
array=[]
n=int(input("enter no"))
x=6
count=0
for i in range(0,n):
    elm=int(input())
    array.append(elm)
    if elm==x:
        count += 1

print("output is=",count)
