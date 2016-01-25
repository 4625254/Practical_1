integer = int(input("Enter an integer between 0 to 1000:"))

a = 0

while integer != 0:
              a = a + integer % 10
              integer //= 10

print("Sum of its digits is:",a)
