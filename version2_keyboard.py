a = float(input("enter a value: "))
b = float(input("enter b value: "))
c = float(input("enter c value: "))
t = float(input("enter t value: "))

temp = a * t**2 + b * t + c
print(f"Temp at t={t}: {temp:.2f}°C")
