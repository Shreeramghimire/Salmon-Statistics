# In this example, we are comparing density histogram with KDE diagram. Three types of KDE curves (undersmooth, balanced, oversmooth) are drawn by altering the bandwidth parameter.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fish_biomass = np.array([221, 221.5, 223, 226, 224, 229, 222])

sns.set_theme(style="whitegrid")
fig, axes = plt. subplots(1,2, figsize=(15,6))

sns.histplot(
    x=fish_biomass,
    kde=True,
    stat="density",
    bins=5,
    color="#4C72B0",
    alpha=0.6,
    ax=axes[0]
)

sns.rugplot(x=fish_biomass, color="black", height=0.05, ax=axes[0])
axes[0].set_title("Density Histogram Vs. Default KDE Curve", fontsize=14, pad =15)
axes[0].set_xlabel("Fish Biomass", fontsize=12)
axes[0].set_ylabel("Density", fontsize =12)

sns.kdeplot(x=fish_biomass, bw_adjust=0.2, color="#C44E52", linewidth=2.5, label ="Under-Smoothed (bw_adjust=0.2)", ax=axes[1])

sns.kdeplot(x=fish_biomass, bw_adjust=0.7, color="#55A868", linewidth=2.5, label="Balanced (bw_adjust=0.7)", ax=axes[1])

sns.kdeplot(x=fish_biomass, bw_adjust=2.0, color="#8172B3", linewidth=2.5, label="Over-smoothed (bw_adjust=2.0)", ax=axes[1])

sns.rugplot(x=fish_biomass, color ="black", height =0.05, ax=axes[1])
axes[1].set_title("How Bandwidth Changes Smoothness and Density", fontsize=14, pad=15)
axes[1].set_xlabel("Fish Biomass", fontsize=12)
axes[1].set_ylabel("Density", fontsize=12)
axes[1].legend(fontsize=10, loc="upper right")

plt.tight_layout()
plt.show()



