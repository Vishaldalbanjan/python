n=int(input("enter no"))
array=[]
for i in range(n-1):
    elm=int(input())
    array.append(elm)
    array.sort()
for i in range(0,n+1):
    if i==array[i+1]:
        print(array)
    else:
        var=array[i+1]
        print(var)
print(array)