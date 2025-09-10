# INCREMENTAL MODEL - WEATHER PREDICTION

def quadratic_weather_model(a, b, c, t):
    """Predict temperature using quadratic equation."""
    return a * (t ** 2) + b * t + c


# ========== INCREMENT 1: Hardcoded values ==========
print("=== INCREMENT 1: Hardcoded Values ===")
a, b, c, t = 0.5, -3, 28, 5
temp = quadratic_weather_model(a, b, c, t)
print(f"Hardcoded -> a={a}, b={b}, c={c}, t={t} => T={temp:.2f}°C\n")


# ========== INCREMENT 2: Keyboard Input ==========
print("=== INCREMENT 2: Keyboard Input ===")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))

temp = quadratic_weather_model(a, b, c, t)
print(f"Keyboard Input -> a={a}, b={b}, c={c}, t={t} => T={temp:.2f}°C\n")


# ========== INCREMENT 3: File Input (Single Set) ==========
print("=== INCREMENT 3: File Input (Single Set) ===")
with open("inputs_single.txt", "r") as f:
    lines = f.readlines()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

temp = quadratic_weather_model(a, b, c, t)
print(f"File Input (Single) -> a={a}, b={b}, c={c}, t={t} => T={temp:.2f}°C\n")


# ========== INCREMENT 4: File Input (Multiple Sets) ==========
print("=== INCREMENT 4: File Input (Multiple Sets) ===")
with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        temp = quadratic_weather_model(a, b, c, t)
        print(f"a={a}, b={b}, c={c}, t={t} => T={temp:.2f}°C")
