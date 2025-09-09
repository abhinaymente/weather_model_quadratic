# ===== ITERATIVE MODEL IMPLEMENTATION =====

# Formula function
def quadratic_weather_model(a, b, c, time):
    return a * (time ** 2) + b * time + c

# Coefficients
a = -0.2
b = 1.5
c = 24

print("=== ITERATIVE MODEL ===")

# Iteration 1: basic output (every 12 hours)
print("Iteration 1:")
for hour in range(0, 25, 12):
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
print("---")

# Iteration 2: same outputs, improved formatting
print("Iteration 2:")
for hour in range(0, 25, 12):
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"[Better Output] Time={hour} hrs | Temp={temp:.2f}°C")
print("---")

# Iteration 3: more frequent checks
print("Iteration 3:")
for hour in range(0, 25, 6):
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
print("---")
