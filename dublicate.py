n = int(input("enter no"))
array = []
for i in range(n):
    elm=int(input())
    array.append(elm)
    array.sort()
    var=array[i+1]
    if i==var:
        print("dublicate =",i)
    else:
        print("-1")