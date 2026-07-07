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
