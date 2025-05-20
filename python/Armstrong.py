n = int(input("Enter a number: "))
digits = [int(d) for d in str(n)]
power = len(digits)
total = sum(d ** power for d in digits)
print(n == total)
