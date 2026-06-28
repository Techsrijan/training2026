import matplotlib.pyplot as plt

x = []
y = []

with open("graph_data.txt", "r") as file:
    for line in file:
        a, b = line.strip().split(",")
        x.append(float(a))
        y.append(float(b))

plt.plot(x, y, marker="o")
plt.title("X-Y Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

plt.show()