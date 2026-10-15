"""
CSC 4162 | Programming in Python Laboratory Manual
Lab 02: Python Installation and First Programs
"""

# ======================================================================
# Problem 1. Demonstrate the installation steps of Python
# ======================================================================
# Steps (Windows):
#  1. Open https://www.python.org/downloads/ and click "Download Python 3.x.x".
#  2. Run the downloaded installer (python-3.x.x-amd64.exe).
#  3. IMPORTANT: tick "Add python.exe to PATH" at the bottom of the first screen.
#  4. Click "Install Now" (or "Customize installation" to choose features/location).
#  5. Wait for the progress bar, then click "Close" at "Setup was successful".
#  6. Verify: open Command Prompt and run
#         python --version        -> e.g. Python 3.13.0
#         pip --version           -> shows the pip version
#  7. Open IDLE from the Start menu (it is installed together with Python).
#
# macOS: download the .pkg installer and follow the wizard; verify with python3 --version.
# Linux: sudo apt update && sudo apt install python3 python3-pip idle3

# ======================================================================
# Problem 2. Introduction with IDLE and other coding environments
# ======================================================================
# IDLE          : Bundled with Python. Has an interactive shell (>>>) and a script
#                 editor (File > New File, run with F5). Best for beginners.
# PyCharm       : Full IDE by JetBrains. Debugger, code completion, project/venv
#                 management. Best for large projects.
# Spyder        : Scientific IDE (comes with Anaconda). Variable explorer, IPython
#                 console. Popular in data science.
# Jupyter       : Browser-based notebook of code/text cells. Run cell by cell
#   Notebook      (Shift+Enter). Great for analysis and visualisation.
# Google Colab  : Free, cloud-hosted Jupyter notebook (colab.research.google.com).
#                 Needs only a Google account and a browser, no installation.

# ======================================================================
# Problem 3. Explore IDLE and Google Colab (basic programs)
# ======================================================================
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
print(type(username))          # input() always returns a str

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
