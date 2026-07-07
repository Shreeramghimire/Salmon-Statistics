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

#Simulate the drift
np.random.seed(7)
N2 = 3000

true_length_day30 = np.random.normal(loc=68, scale=6, size=N2)
GROWTH_CM = 3.0  # real biological growth over 30 days
true_length_day30 = np.clip(true_length_day30 + GROWTH_CM, 45, 98)

swim_angle_day30 = np.abs(np.random.normal(0, 15, size=N2))
foreshortening_day30 = np.cos(np.radians(swim_angle_day30))

DRIFT_BIAS_CM = -1.8  # unknown to the system: camera rig has physically shifted
clean_noise_day30 = np.random.normal(0, 0.8, size=N2)

measured_length_day30 = (true_length_day30 * foreshortening_day30
                          + clean_noise_day30 + DRIFT_BIAS_CM)

# Re-simulate day 1 at matching N for a fair comparison
np.random.seed(42)
true_length_day1 = np.clip(np.random.normal(68, 6, N2), 45, 95)
swim_angle_day1 = np.abs(np.random.normal(0, 15, size=N2))
foreshortening_day1 = np.cos(np.radians(swim_angle_day1))
clean_noise_day1 = np.random.normal(0, 0.8, size=N2)
measured_length_day1 = true_length_day1 * foreshortening_day1 + clean_noise_day1

kde_day1 = stats.gaussian_kde(measured_length_day1, bw_method=0.25)
kde_day30 = stats.gaussian_kde(measured_length_day30, bw_method=0.25)

x_grid2 = np.linspace(40, 100, 3000)
mode_day1 = x_grid2[np.argmax(kde_day1(x_grid2))]
mode_day30 = x_grid2[np.argmax(kde_day30(x_grid2))]

print(f"Day 1 KDE peak:  {mode_day1:.2f} cm")
print(f"Day 30 KDE peak: {mode_day30:.2f} cm")
print(f"Observed shift: {mode_day30 - mode_day1:+.2f} cm")

# Real growth vs. camera drift
peak_shift = mode_day30 - mode_day1
expected_growth_cm = 3.0  # from an independent feed-intake / day-degree growth model
unexplained_shift = peak_shift - expected_growth_cm

ks_stat, ks_pvalue = stats.ks_2samp(measured_length_day1, measured_length_day30)

print(f"Expected biological growth: +{expected_growth_cm:.2f} cm")
print(f"Actual observed shift:      {peak_shift:+.2f} cm")
print(f"Unexplained shift:          {unexplained_shift:+.2f} cm")
print(f"KS test: stat={ks_stat:.4f}, p={ks_pvalue:.6f}")

if abs(unexplained_shift) > 1.0 and ks_pvalue < 0.01:
    print(">>> FLAG: shift exceeds what biology explains -> recommend camera check.")
else:
    print(">>> No flag: shift consistent with expected growth.")

# Drift visualization
fig, ax = plt.subplots(figsize=(9, 5))
density_day1 = kde_day1(x_grid2)
density_day30 = kde_day30(x_grid2)

ax.plot(x_grid2, density_day1, color="steelblue", lw=2, label="Day 1 (baseline) KDE")
ax.plot(x_grid2, density_day30, color="darkorange", lw=2, label="Day 30 KDE")
ax.axvline(mode_day1, color="steelblue", ls="--", label=f"Day 1 peak = {mode_day1:.1f} cm")
ax.axvline(mode_day30, color="darkorange", ls="--", label=f"Day 30 peak = {mode_day30:.1f} cm")
ax.fill_between(x_grid2, density_day1, density_day30, color="red", alpha=0.08)
ax.set_xlabel("Length (cm)")
ax.set_ylabel("Density")
ax.set_title("Problem: Comparing daily KDE distributions to flag camera drift")
ax.legend()
plt.tight_layout()
plt.show()
