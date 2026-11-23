# Exercise 01 - User Information
# Learning: variables, input and output

print("=== USER INFORMATION ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print("\n--- INFORMATION ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")
