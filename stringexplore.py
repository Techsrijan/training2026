age=input("enter your age")

if age.isdigit():
    print(age)
else:
    print("You have entered invalid age")


st="Welcome to pythton me to"
print(st)
print(st.endswith('m'))
print(st.count('to'))
print(st.find('me'))
print(st.lower())
print(st.upper())
print(st.capitalize())
print(st.swapcase())
print(st.title())

name=input("enter your  name")
print(name,end='')
print()
print(name.rstrip(),end='')
print('test')
print(name)
# if name.isalpha():
#     print(name)
# else:
#     print("You have entered invalid name")