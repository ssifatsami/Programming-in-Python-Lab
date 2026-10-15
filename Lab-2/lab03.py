"""
CSC 4162 | Programming in Python Laboratory Manual
Lab 03: Variables, Data Types, Operators, and Branching Statements
"""

# ----------------------------------------------------------------------
# Problem 1. Swap the values of two variables
# ----------------------------------------------------------------------
print("----- Problem 1: Swap two variables -----")
a = input("Enter value of a: ")
b = input("Enter value of b: ")
print("Before swap: a =", a, ", b =", b)

a, b = b, a                      # Pythonic swap (tuple unpacking)
print("After swap : a =", a, ", b =", b)

# Alternative using a temporary variable:
# temp = a
# a = b
# b = temp

# ----------------------------------------------------------------------
# Problem 2. Distance between two points
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
# ----------------------------------------------------------------------
print("\n----- Problem 2: Distance between two points -----")
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) = {d:.2f}")

# ----------------------------------------------------------------------
# Problem 3. Even or odd
# ----------------------------------------------------------------------
print("\n----- Problem 3: Even or Odd -----")
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

# ----------------------------------------------------------------------
# Problem 4. Vowel check
# ----------------------------------------------------------------------
print("\n----- Problem 4: Vowel or not -----")
ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")
elif ch.lower() in "aeiou":
    print(ch, "is a vowel")
else:
    print(ch, "is not a vowel (it is a consonant)")

# ----------------------------------------------------------------------
# Problem 5. Marks to grade (AIUB grading scheme)
#   90-100 A+ 4.00 | 85-89 A 3.75 | 80-84 B+ 3.50 | 75-79 B 3.25
#   70-74  C+ 3.00 | 65-69 C 2.75 | 60-64 D+ 2.50 | 50-59 D 2.25
#   0-49   F  0.00
# ----------------------------------------------------------------------
print("\n----- Problem 5: Marks to Grade -----")
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter a value between 0 and 100.")
else:
    if marks >= 90:
        grade, point = "A+", 4.00
    elif marks >= 85:
        grade, point = "A", 3.75
    elif marks >= 80:
        grade, point = "B+", 3.50
    elif marks >= 75:
        grade, point = "B", 3.25
    elif marks >= 70:
        grade, point = "C+", 3.00
    elif marks >= 65:
        grade, point = "C", 2.75
    elif marks >= 60:
        grade, point = "D+", 2.50
    elif marks >= 50:
        grade, point = "D", 2.25
    else:
        grade, point = "F", 0.00

    print(f"Marks: {marks} -> Grade: {grade} (Grade point: {point:.2f})")
