from numpy import *
arr=array([5,6,89,416,9,88])
for i in arr:
    print(i)

print("data Type=",arr.dtype)
print("Dimension=",arr.ndim)
print("Size=",arr.size)
print("shape=",arr.shape)
print("reshape=",arr.reshape(3,2))
print("Flatten=",arr.flatten())
print(arr)
print(arr*5)
