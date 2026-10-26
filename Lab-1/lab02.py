

# Problem 3. Explore IDLE and Google Colab (basic programs)
print("=== Declaring variables ===")
x = 5
y = "John"
print(x)
print(y)

# dynamic typing: the same name can be re-assigned to a different type
x = "Now I am a string"
print(x, "->", type(x))

# multiple assignment
a, b, c = 1, 2.5, "three"
print(a, b, c)

print("\n=== Input and output ===")
username = input("Enter username: ")
print("Username is:", username)
print("Username is: " + username)
print(type(username))         

# convert input to a number
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# simple calculator
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("Sum        :", n1 + n2)
print("Difference :", n1 - n2)
print("Product    :", n1 * n2)
print("Quotient   :", n1 / n2 if n2 != 0 else "Cannot divide by zero")
