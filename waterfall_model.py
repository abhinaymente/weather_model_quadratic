# ===== VERSION 1: WATERFALL MODEL =====
import matplotlib.pyplot as plt
import numpy as np

print("=== WATERFALL MODEL ===")

# Coefficients (U-shape parabola)
a, b, c = 0.02, -0.5, 20

# Hours (every 6 hrs - sequential like waterfall)
hours = np.arange(0, 25, 6)
temps = []

# Predictions
for i, hour in enumerate(hours):
    temp = a * (hour ** 2) + b * hour + c
    temps.append(temp)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

# Plot the graph
plt.figure(figsize=(8,5))
plt.plot(hours, temps, marker='o', linestyle='-', color='b', label="Predicted Temp")
plt.title("Version 1: Waterfall Model - Weather Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save instead of show
plt.savefig("waterfall_model_v4.png")
plt.close()

print("\nGraph saved as 'waterfall_model_v4.png' in your repository.")
