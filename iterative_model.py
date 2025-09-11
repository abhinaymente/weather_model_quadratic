# ===== VERSION 3: ITERATIVE MODEL (U-shape) =====
import matplotlib.pyplot as plt
import numpy as np

print("=== ITERATIVE MODEL ===")

# Quadratic model function (U-shape parabola)
def quadratic_weather_model(hour):
    a, b, c = 0.02, -0.5, 20   # positive a -> U shape
    return a * (hour ** 2) + b * hour + c

# Iterations
iterations = 3
check_hours = np.arange(0, 25, 12)  # checking every 12 hours
plot_hours = np.arange(0, 25, 1)    # smooth curve for plotting
all_temps = []

for iteration in range(1, iterations + 1):
    print(f"Iteration {iteration}:")
    temps = []
    for hour in check_hours:
        temp = quadratic_weather_model(hour)
        temps.append(temp)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")
    all_temps.append(temps)

# Plot graph
plt.figure(figsize=(8,5))

for i in range(iterations):
    temps = [quadratic_weather_model(h) for h in plot_hours]
    plt.plot(plot_hours, temps, linestyle='-', label=f"Iteration {i+1}")

# Highlight check points
for hour in check_hours:
    temp = quadratic_weather_model(hour)
    plt.scatter(hour, temp, color='r', s=70, zorder=5)

plt.title("Version 2: Iterative Model (U-shape)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG
plt.savefig("iterative_graph.png")

print("\nGraph saved as 'iterative_graph_v3_ushape.png' in your repository.")
