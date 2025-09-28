number = 5
factorial = 1
print(f"Вычисление факториала {number}!:")

for i in range(number, 0, -1):
    factorial *= i
    print(f"{i} × ", end="")

print(f"= {factorial}")
