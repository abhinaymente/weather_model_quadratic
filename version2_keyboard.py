import matplotlib.pyplot as plt
import numpy as np

# Take user input
a = float(input("enter a value: "))
b = float(input("enter b value: "))
c = float(input("enter c value: "))
t = float(input("enter t value: "))

# Calculate temperature at given t
temp = a * t**2 + b * t + c
print(f"Temp at t={t}: {temp:.2f}°C")

# Function
def quadratic_weather_model(x):
    return a * x**2 + b * x + c

# Range of time values (0–24 hours)
times = np.arange(0, 25, 1)  # every 1 hour
temps = [quadratic_weather_model(x) for x in times]

# Plot graph
plt.figure(figsize=(8,5))
plt.plot(times, temps, marker='o', linestyle='-', color='b', label="Temperature Curve")
plt.scatter(t, temp, color='r', s=100, zorder=5, label=f"t={t}, Temp={temp:.2f}°C")  # highlight user point
plt.title("Quadratic Weather Prediction Model")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG (for GitHub Codespaces)
plt.savefig("user_input_weather.png")
plt.close()

print("\nGraph saved as 'user_input_weather.png' in your repository.")
