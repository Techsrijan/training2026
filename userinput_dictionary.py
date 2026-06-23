# Create an empty dictionary
user_data = {}

# Ask how many items to add
entries = int(input("How many entries do you want to add? "))

for _ in range(entries):
    key = input("Enter the key (e.g., username): ").strip()
    value = input("Enter the value (e.g., age): ").strip()

    # Map the value to the key
    user_data[key] = value

print("\nYour created dictionary:")
print(user_data)