from numpy import *
arr=array([5,6,7,8])
print("arr=",arr,"Address of arr=",id(arr))
arr2=arr # aliasing
print("arr=",arr,"Address of arr=",id(arr))
print("arr2=",arr2,"Address of arr2=",id(arr2))
print("after performing operation in arr")
#print(arr+5)
arr2[2]=5000
print("arr=",arr,"Address of arr=",id(arr))
print("arr2=",arr2,"Address of arr2=",id(arr2))
print("another method view --Shallow copy")
arr3=array([55,6,99,77,8])
print("arr3=",arr3,"Address of arr3=",id(arr3))
arr4=arr3.view()
print("arr3=",arr3,"Address of arr3=",id(arr3))
print("arr4=",arr4,"Address of arr4=",id(arr4))
arr3[2]=4343
print("arr3=",arr3,"Address of arr3=",id(arr3))
print("arr4=",arr4,"Address of arr4=",id(arr4))
print("another method Deep --Deep copy")
arr5=array([554,56,54564,77,8])
print("arr5=",arr5,"Address of arr5=",id(arr5))
arr6=arr5.copy()
print("arr5=",arr5,"Address of arr5=",id(arr5))
print("arr6=",arr6,"Address of arr6=",id(arr6))
arr5[0]=1000
print("arr5=",arr5,"Address of arr5=",id(arr5))
print("arr6=",arr6,"Address of arr6=",id(arr6))