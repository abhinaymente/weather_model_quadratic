# ===== AGILE MODEL IMPLEMENTATION =====

def quadratic_weather_model(a, b, c, time):
    return a * (time ** 2) + b * time + c

a = -0.2
b = 1.5
c = 24

print("=== AGILE MODEL ===")

# Sprint 1: quick delivery, simple output
print("Sprint 1:")
for hour in [0, 6, 12, 18, 24]:
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
print("---")

# Sprint 2: refinement, add labels
print("Sprint 2:")
for hour in [0, 6, 12, 18, 24]:
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"[Sprint 2] Time={hour} hrs | Predicted Temp={temp:.2f}°C")
print("---")
