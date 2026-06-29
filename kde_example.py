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

#Lets explain histogram density digram in a basic terms. The diagram should always present the total area of all bars combined to equal exactly 1. 


# Data
[221, 221.5, 223, 226, 224, 229, 222]

# Number of bins
Number of bins can be calculated by using formula: $${\text{Sturges' Rule}} = 1 + \log_2(n)$$

And number of bins in density histogram diagram matters significantly. Choosing the wrong number of bins can create two major structural problems: over-smoothing or under-smoothing.
$$\text{Number of Optimal Bins} = 1 + \log_2(7) \approx \mathbf{3.81} = 1 + approax. 4 = 5 $$

# Bin width
$${\text{Bin Width}} = \frac{229 - 221}{5} = \mathbf{1.6\text{ grams}}$$


**The 5 Bins are:**
* $[221.0, 222.6]$
* $[222.6, 224.2]$
* $[224.2, 225.8]$
* $[225.8, 227.4]$
* $[227.4, 229.0]$

# Density count
Instead of just counting the fish, the density formula is:

$$\text{Density (Height)} = \frac{\text{Count in Bin}}{\text{Total Fish (7)} \times \text{Bin Width (1.6)}}$$

**Bin 1 $[221.0, 222.6)$:** Contains 3 fish `(221, 221.5, 222)`
$$\text{Height} = \frac{3}{7 \times 1.6} = \frac{3}{11.2} \approx \mathbf{0.2679}$$

**Bin 2 $[222.6, 224.2)$:** Contains 2 fish `(223, 224)`
$$\text{Height} = \frac{2}{7 \times 1.6} = \frac{2}{11.2} \approx \mathbf{0.1786}$$

**Bin 3 $[224.2, 225.8)$:** Contains 0 fish
$$\text{Height} = \frac{0}{7 \times 1.6} = \mathbf{0.0000}$$

**Bin 4 $[225.8, 227.4)$:** Contains 1 fish `(226)`
$$\text{Height} = \frac{1}{7 \times 1.6} = \frac{1}{11.2} \approx \mathbf{0.0893}$$

**Bin 5 $[227.4, 229.0]$:** Contains 1 fish `(229)`
$$\text{Height} = \frac{1}{7 \times 1.6} = \frac{1}{11.2} \approx \mathbf{0.0893}$$


# Calculate the total area
$$\text{Total Area} = \text{Bin Width} \times (\text{Sum of all Heights})$$

$$\text{Total Area} = 1.6 \times (0.2679 + 0.1786 + 0.0000 + 0.0893 + 0.0893)$$

$$\text{Total Area} = 1.6 \times 0.6251 \approx \mathbf{1.0}$$


