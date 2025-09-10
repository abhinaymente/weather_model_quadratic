# ===== ITERATIVE MODEL =====
import matplotlib.pyplot as plt
import numpy as np

print("=== ITERATIVE MODEL ===")

# Quadratic model function
def quadratic_weather_model(hour):
    a, b, c = -0.02, 0.5, 15
    return a * (hour ** 2) + b * hour + c

# Iterations
iterations = 3
hours = np.arange(0, 25, 12)  # checking every 12 hours
all_temps = []

for iteration in range(1, iterations + 1):
    print(f"Iteration {iteration}:")
    temps = []
    for hour in hours:
        temp = quadratic_weather_model(hour)
        temps.append(temp)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")
    all_temps.append(temps)

# Plot the graph
plt.figure(figsize=(8,5))

for i, temps in enumerate(all_temps, start=1):
    plt.plot(hours, temps, marker='o', linestyle='-', label=f"Iteration {i}")

plt.title("Iterative Model - Weather Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save graph as PNG
plt.savefig("iterative_graph.png")

print("\nGraph saved as 'iterative_graph.png' in your repository.")