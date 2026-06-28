x = []
y = []

n = int(input("Kitne points enter karne hain? "))

for i in range(n):
    x_value = float(input(f"Enter X{i+1}: "))
    y_value = float(input(f"Enter Y{i+1}: "))

    x.append(x_value)
    y.append(y_value)

with open("graph_data.txt", "w") as file:
    for i in range(n):
        file.write(f"{x[i]},{y[i]}\n")

print("Data successfully saved.")