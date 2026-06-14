from  array import *

arr=array('i',[1,2,3,4,9])
print(arr)
print(arr.typecode)
print(arr.buffer_info())

print(len(arr))
print(arr[0])
print(arr[-1])

i=0
while i<len(arr):
    print(arr[i],end='')
    i=i+1
print()
for i in arr:
    print(i)

for i in range(len(arr)):
    print(arr[i])

