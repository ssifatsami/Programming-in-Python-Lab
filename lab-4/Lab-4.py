numbers = [10 , 20 ,30 , 40 , 50]

for number in numbers:
    print(number)

n = int(input("Enter a Number : "))

while n >= 0:
    print(n)
    n = n-1

print("CountDown finished .")


base = float(input("Enter the Base : "))

exponent = int(input("Enter the exponent : "))

result = base ** exponent

print("Result : " , result)


total = 0

for num in range(2, 20):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        total += num

print("Sum of all prime numbers below 1000:", total)




n = int(input("Enter N: "))

a = 0
b = 1

while a < n:
    print(a, end=" ")
    a, b = b, a + b