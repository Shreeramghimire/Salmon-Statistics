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




