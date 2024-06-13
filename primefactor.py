array=[2,3,5,7]
m=len(array)
n=23
var=0
for i in range(m):
    if n%array[i]==0:
        var=array[i]
print(var)