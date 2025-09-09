# ===== WATERFALL MODEL IMPLEMENTATION =====

# Step 1: Requirements -> define formula
def quadratic_weather_model(a, b, c, time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# Step 2: System Design -> choose coefficients
a = -0.2
b = 1.5
c = 24

# Step 3: Implementation -> test at different times (0 to 24 hours)
print("=== WATERFALL MODEL ===")
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(a, b, c, hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")
