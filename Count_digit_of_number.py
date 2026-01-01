# sum of first n natural numbers
num = int(input("Enter a number: "))
total = 0
for i in range (1, num+1):
    total += i
print("Sum of all numbers: ", total)
