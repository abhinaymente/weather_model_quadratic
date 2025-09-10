import matplotlib.pyplot as plt
import numpy as np

# Coefficients
a = -0.3
b = 4.5
c = 15.0

# Function
def quadratic_weather_model(t):
    return a * t**2 + b * t + c

# Range of time values (0 to 24 hours)
times = np.arange(0, 25, 1)  # every 1 hour
temps = [quadratic_weather_model(t) for t in times]

# Specific calculation for t = 8
t = 8
temperature = quadratic_weather_model(t)

print("Weather Prediction Model")
print(f"Time (t) = {t}")
print(f"Predicted temperature: {temperature:.2f}°C")

# Plot graph
plt.figure(figsize=(8,5))
plt.plot(times, temps, marker='o', linestyle='-', color='b', label="Temperature Curve")
plt.scatter(t, temperature, color='r', zorder=5, label=f"t={t}, Temp={temperature:.2f}°C")  # highlight t=8
plt.title("Quadratic Weather Prediction Model")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG for GitHub
plt.savefig("weather_prediction.png")
plt.close()

print("\nGraph saved as 'weather_prediction.png' in your repository.")

