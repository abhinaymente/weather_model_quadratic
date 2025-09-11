import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

with open("input2.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * t**2 + b * t + c
        print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")

        # Curve across 0–24 hours
        times = np.arange(0, 25, 1)
        temps = a * times**2 + b * times + c

        # Plot curve
        plt.plot(times, temps, label=f"a={a}, b={b}, c={c}")
        # Highlight specific t
        plt.scatter(t, T, s=80, color='red', zorder=5)

# Graph formatting
plt.title("Quadratic Weather Prediction (Multiple Inputs)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG (for GitHub Codespaces)
plt.savefig("file_input_multiple_weather.png")
plt.close()

print("\nGraph saved as 'file_input_multiple_weather.png' in your repository.")


