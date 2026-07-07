#In this example: we have 500 salmon being grown in a feed trial station located at west coast of Norway. This is a synthetic data.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.plotly as plt

np.random.seed(42)

N = 500

true_length = np.random.normal(loc=68, scale=6, size=N)
true_length = np.clip(true_length, 45, 95)

a, b = 0.0125, 3.05
true_weight = (a * (true_length ** b)) / 1000

distance = np.random.uniform(1, 4, size=N)
swim_angle = np.abs(np.random.normal(0, 15, size=N))

df = pd.DataFrame({
    "fish_id": range(N),
    "true_length_cm": true_length,
    "true_weight_kg": true_weight,
    "distance_m": distance,
    "swim_angle_deg": swim_angle,
})

df.head()

angle_rad = np.radians(df["swim_angle_deg"])
foreshortening_factor = np.cos(angle_rad)

clean_noise = np.random.normal(0, 0.8, size=N)  # ordinary camera noise, cm
df["measured_length_cm"] = df["true_length_cm"] * foreshortening_factor + clean_noise
df["measured_weight_kg"] = (a * (df["measured_length_cm"] ** b)) / 1000

print("Naive mean measured length:", df["measured_length_cm"].mean().round(2))
print("True mean length:          ", df["true_length_cm"].mean().round(2))
print("Naive mean measured weight:", df["measured_weight_kg"].mean().round(3))
print("True mean weight:          ", df["true_weight_kg"].mean().round(3))

# KDE mode instead of mean
kde = stats.gaussian_kde(df["measured_length_cm"], bw_method=0.25)

x_grid = np.linspace(df["measured_length_cm"].min() - 5,
                      df["measured_length_cm"].max() + 5, 2000)
density = kde(x_grid)
kde_mode = x_grid[np.argmax(density)]

print(f"KDE-estimated mode (peak) length: {kde_mode:.2f} cm")
print(f"True mean length:                 {df['true_length_cm'].mean():.2f} cm")
print(f"Naive mean measured length:       {df['measured_length_cm'].mean():.2f} cm")
print(f"\nError vs naive mean: {abs(df['measured_length_cm'].mean() - df['true_length_cm'].mean()):.2f} cm")
print(f"Error vs KDE mode:   {abs(kde_mode - df['true_length_cm'].mean()):.2f} cm")

#Visualization
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df["measured_length_cm"], bins=40, density=True, alpha=0.4,
        color="steelblue", label="Measured length (raw, angle-contaminated)")
ax.plot(x_grid, density, color="black", lw=2, label="KDE estimate")
ax.axvline(df["measured_length_cm"].mean(), color="red", ls="--", lw=2,
           label=f"Naive mean = {df['measured_length_cm'].mean():.1f} cm")
ax.axvline(kde_mode, color="green", ls="-", lw=2,
           label=f"KDE mode = {kde_mode:.1f} cm")
ax.axvline(df["true_length_cm"].mean(), color="gray", ls=":", lw=2,
           label=f"True mean = {df['true_length_cm'].mean():.1f} cm")
ax.set_xlabel("Length (cm)")
ax.set_ylabel("Density")
ax.set_title("Problem: KDE mode recovers true size despite bent-fish noise tail")
ax.legend()
plt.tight_layout()
plt.show()

