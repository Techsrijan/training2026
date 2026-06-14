from array import *
arr=array('i',[])
print(type(arr))

n=int(input("how many students in class"))
print("no of students=",n)

for i in range(n):
    marks=int(input("enter the marks"))
    arr.append(marks)

for i in arr:
    print(i)
