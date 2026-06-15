'''
There are seven ways to create any array using numpy
1 array
2. linspace
3. logspace
4. arange
5. zeros
6. ones
7. empty
'''
from numpy import *
arr=array([1,2,3,4])
print(arr)
print("linspace")
arr2=linspace(1,150000,3)
print(arr2)
print("logspace")
arr3=logspace(1,15,5)
print(arr3)
print("arange")
arr4=arange(10)
print(arr4)
print(arr4[5])
print("zeros")
arr5=zeros(10,int)
print(arr5)
print("ones")
arr6=ones(10)
print(arr6)
print("empty")
arr7=empty(4)
print(arr7)