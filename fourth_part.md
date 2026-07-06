# Multivariate Statistics: From Covariance Matrices to Confidence Ellipsoids

## Part 1: Matrix Operations for Multivariate Variance/Covariance

### The Data Setup

Let's say we have **3 outcomes** for 100 salmon pens:

- **Weight (kg)**
- **Length (cm)**
- **Fat (%)**

Our data matrix $\mathbf{Y}$ is $100 \times 3$.

### The Centering Matrix (Refresher)

Remember the centering matrix? $\mathbf{H}_1 = \frac{1}{n}J_{n,n}$ (projects onto the intercept).

The centered data is:

$$\mathbf{Y}_c = (\mathbf{I} - \mathbf{H}_1)\mathbf{Y}$$

### The Covariance Matrix (The Star of the Show)

The **sample covariance matrix** ($\mathbf{S}$) captures how every variable relates to every other variable:

$$\mathbf{S} = \frac{1}{n-1} \mathbf{Y}_c^t \mathbf{Y}_c$$

Let's expand this for our 3 variables:

The sample covariance matrix is

```math
S =
\begin{bmatrix}
s_{11} & s_{12} & s_{13} \\
s_{12} & s_{22} & s_{23} \\
s_{13} & s_{23} & s_{33}
\end{bmatrix}
=
\begin{bmatrix}
\mathrm{Var}(\text{Weight}) &
\mathrm{Cov}(\text{Length},\text{Weight}) &
\mathrm{Cov}(\text{Fat},\text{Weight}) \\
\mathrm{Cov}(\text{Weight},\text{Length}) &
\mathrm{Var}(\text{Length}) &
\mathrm{Cov}(\text{Fat},\text{Length}) \\
\mathrm{Cov}(\text{Weight},\text{Fat}) &
\mathrm{Cov}(\text{Length},\text{Fat}) &
\mathrm{Var}(\text{Fat})
\end{bmatrix}
```
**The Salmon Farm Translation:**

| Component | Meaning |
|-----------|---------|
| **Diagonal ($s_{ii}$)** | How much each metric fluctuates on its own |
| **Off-diagonal ($s_{ij}$)** | The *direction* and *strength* of the relationship. Positive = bigger fish tend to be longer. Negative = fatter fish might have lower heart rates (less fit) |

---

## Part 2: The Multivariate Normal Distribution ($MVN$)

### The Concept

The univariate normal ($N(\mu, \sigma^2)$) describes a single bell curve. The **Multivariate Normal** describes a **bell-shaped cloud** in multiple dimensions.

### The Probability Density Function (PDF)

If $\mathbf{Y}$ is a $p \times 1$ random vector, it follows:

$$\mathbf{Y} \sim N_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$$

The PDF is:

f(Y) = (2π)^(-p/2) × |Σ|^(-1/2) × exp{ -1/2 × (Y - μ)^T × Σ^(-1) × (Y - μ) }

| Symbol | Description |
|--------|-------------|
| $\boldsymbol{\mu}$ ($p \times 1$) | The mean vector (e.g., average Weight, Length, Fat) |
| $\boldsymbol{\Sigma}$ ($p \times p$) | The **population** covariance matrix (our $\mathbf{S}$ is an estimate of this) |

### The Geometry (The Salmon Cloud)

Imagine plotting Weight on the X-axis and Length on the Y-axis.

- If $\text{Cov} = 0$: The cloud looks like a round circle (or a perfect ellipse aligned with the axes).
- If $\text{Cov} > 0$: The cloud is a tilted ellipse stretching from bottom-left to top-right (bigger fish are longer).

**The Matrix $\boldsymbol{\Sigma}^{-1}$** (the precision matrix) literally defines the shape and orientation of this ellipse!

---

## Part 3: The Singular Normal Distribution (The "Flat" Normal)

### What is it?

Usually, $\boldsymbol{\Sigma}$ must be **positive definite** (invertible). But sometimes, our variables are perfectly linearly related (e.g., we accidentally include Weight in kg *and* Weight in pounds).

When $\boldsymbol{\Sigma}$ is **singular** (determinant = 0, not invertible), the distribution "flattens" into a lower-dimensional subspace.

**Salmon Example:**

We measure:

1. Weight (kg)
2. Length (cm)
3. **Weight in pounds** (exactly 2.20462 × Weight)

The third variable gives us no new information. The 3D normal distribution collapses onto a 2D plane. The PDF formula breaks (because $|\boldsymbol{\Sigma}| = 0$), but the distribution still exists—we just say it's "singular" or "degenerate."

---

## Part 4: The Normal Likelihood (Estimating from Data)

**The Concept:**

Given our observed salmon data $\mathbf{Y}$, what are the most likely values for $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$?

### The Likelihood Function

For $n$ independent observations, the likelihood is the product of the individual MVN densities:

\begin{aligned}
\mathbf{S} &= 
\begin{bmatrix}
s_{11} & s_{12} & s_{13} \\
s_{12} & s_{22} & s_{23} \\
s_{13} & s_{23} & s_{33}
\end{bmatrix}
=
\begin{bmatrix}
\mathrm{Var}(\text{Weight}) &
\mathrm{Cov}(\text{Weight}, \text{Length}) &
\mathrm{Cov}(\text{Weight}, \text{Fat}) \\
\mathrm{Cov}(\text{Length}, \text{Weight}) &
\mathrm{Var}(\text{Length}) &
\mathrm{Cov}(\text{Length}, \text{Fat}) \\
\mathrm{Cov}(\text{Fat}, \text{Weight}) &
\mathrm{Cov}(\text{Fat}, \text{Length}) &
\mathrm{Var}(\text{Fat})
\end{bmatrix} \\[2em]
L(\boldsymbol{\mu}, \boldsymbol{\Sigma}) &\propto |\boldsymbol{\Sigma}|^{-n/2} \exp\left\{ -\frac{1}{2} \sum_{i=1}^n (\mathbf{y}_i - \boldsymbol{\mu})^t \boldsymbol{\Sigma}^{-1} (\mathbf{y}_i - \boldsymbol{\mu}) \right\}
\end{aligned}

### The Maximum Likelihood Estimates (MLE)

Using matrix calculus (taking derivatives and setting to zero):

| Parameter | MLE |
|-----------|-----|
| **Mean** | $\hat{\boldsymbol{\mu}} = \bar{\mathbf{y}} = \frac{1}{n}\sum \mathbf{y}_i$ (the column means) |
| **Covariance** | $\hat{\boldsymbol{\Sigma}}_{MLE} = \frac{1}{n} \sum (\mathbf{y}_i - \bar{\mathbf{y}})(\mathbf{y}_i - \bar{\mathbf{y}})^t$ *(Divides by $n$; the unbiased version divides by $n-1$)* |

---

## Part 5: Chi-squared Results for Quadratic Forms

This is the mathematical engine that powers all hypothesis testing!

### The Key Theorem

If $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{I})$ (standard independent normals), then:

$$\mathbf{Z}^t \mathbf{Z} \sim \chi^2_p$$

(A sum of $p$ squared standard normals follows a Chi-squared distribution with $p$ degrees of freedom).

### The Salmon Application (Mahalanobis Distance)

For our multivariate data:

$$(\mathbf{Y} - \boldsymbol{\mu})^t \boldsymbol{\Sigma}^{-1} (\mathbf{Y} - \boldsymbol{\mu}) \sim \chi^2_p$$

This is the **Mahalanobis Distance** squared.

**What it means on the farm:**

Instead of asking "Is this one fish heavy?" we ask "Is this fish an outlier in the *multivariate space*?" A fish might have average weight and average length, but if the combination (e.g., very long but very light) is rare, the Mahalanobis distance will be large, flagging it for a health check!

---

## Part 6: Confidence Intervals for Regression Coefficients

**The Scenario:**

We fit a univariate regression: $\text{Weight} = \beta_0 + \beta_1(\text{Feed}) + \epsilon$.

### The Matrix Result

We know $\hat{\beta} \sim N(\beta, \sigma^2 (\mathbf{X}^t\mathbf{X})^{-1})$.

### The Confidence Interval (CI) for a single coefficient $\beta_j$:

$$\hat{\beta}_j \pm t_{n-p-1, \alpha/2} \times \text{se}(\hat{\beta}_j)$$

Where:

- $\text{se}(\hat{\beta}_j) = \hat{\sigma} \sqrt{(\mathbf{X}^t\mathbf{X})^{-1}_{jj}}$
- $t$ is the critical value from the t-distribution

**Farm Translation:**

*"We are 95% confident that for every 1 kg of feed, the true weight gain is between 1.5 kg and 2.1 kg."*

---

## Part 7: The F-Distribution (Testing Groups of Coefficients)

**The Scenario:**

We want to test if *both* Feed **and** Temperature jointly have no effect on Weight (i.e., $\beta_1 = \beta_2 = 0$).

### The F-Test

We compare two models:

1. **Full Model:** Weight ~ Feed + Temp
2. **Reduced Model:** Weight ~ 1 (just intercept)

The F-statistic is:

$$F = \frac{(SSE_{reduced} - SSE_{full}) / (p_{full} - p_{reduced})}{SSE_{full} / (n - p_{full})} \sim F_{p_1 - p_0, n - p_1}$$

**Farm Translation:**

*"The F-test tells us if adding Feed AND Temperature gives us significantly better predictions than just using the average weight. If the p-value is low, we know these variables actually matter."*

---

## Part 8: Prediction Intervals (For a New Pen)

**The Scenario:**

We have a new pen with Feed = 2.8 kg. We want to predict the *exact weight* of a single fish in that pen.

### The Formula

$$\hat{y}_{new} \pm t_{n-p-1, \alpha/2} \times \hat{\sigma} \sqrt{1 + \mathbf{x}_{new}^t (\mathbf{X}^t\mathbf{X})^{-1} \mathbf{x}_{new}}$$

**Notice the "1 +" inside the square root!**

This accounts for the **variance of the new observation itself** (the irreducible noise).

**Farm Translation:**

*"We are 95% sure that this specific new fish will weigh between 5.5 kg and 6.5 kg."* (This is wider than the confidence interval for the *average* weight, which would be 5.8 to 6.2).

---

## Part 9: Confidence Ellipsoids (The Multivariate CI)

**The Scenario:**

We want a 95% confidence region for **BOTH** $\beta_1$ (Feed) and $\beta_2$ (Temp) **simultaneously**.

If we calculate separate 95% CIs for Feed and Temp, the overall chance that *both* are correct is less than 95%. The ellipsoid fixes this.

### The Formula

The set of all $\beta$ that satisfy:

$$(\hat{\beta} - \beta)^t (\mathbf{X}^t\mathbf{X}) (\hat{\beta} - \beta) \leq p \times \hat{\sigma}^2 \times F_{p, n-p, \alpha}$$

### The Geometry

| Dimension | Shape |
|-----------|-------|
| 1 coefficient | Line segment (CI) |
| 2 coefficients | **Ellipse** on the 2D plane |
| 3+ coefficients | **Ellipsoid** (a 3D football) |

**Salmon Farm Translation (2D Ellipse):**

Imagine plotting Feed coefficient on the X-axis and Temp coefficient on the Y-axis. Instead of a square box (which would be wrong), we get a tilted ellipse.

- The tilt tells us: *"If we overestimated the effect of Feed, we likely also overestimated the effect of Temp"* (because they are correlated predictors).
- The ellipse gives us the exact combinations of Feed and Temp effects that are jointly plausible.

---

## Part 10: Summary Table

| Concept | Matrix Math | Salmon Farm Translation |
| :--- | :--- | :--- |
| **Covariance Matrix** | $\mathbf{S} = \frac{1}{n-1}\mathbf{Y}_c^t\mathbf{Y}_c$ | How Weight, Length, and Fat dance together |
| **Multivariate Normal** | $N_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ | The 3D bell-shaped cloud of farm data |
| **Singular Normal** | $ |\boldsymbol{\Sigma}| = 0$ | We accidentally measured the same thing twice |
| **Likelihood** | $L(\boldsymbol{\mu}, \boldsymbol{\Sigma} \mid \mathbf{Y})$ | What are the most likely true farm averages? |
| **Chi-squared** | $(\mathbf{y}-\mu)^t\Sigma^{-1}(\mathbf{y}-\mu)$ | Flagging weird fish (Mahalanobis distance) |
| **CI for $\beta_j$** | $\hat{\beta}_j \pm t \cdot se$ | Feed adds between 1.5 and 2.1 kg per kg |
| **F-test** | $\frac{(SSE_R - SSE_F)/(df)}{\ SSE_F/(n-p)}$ | Do Feed *and* Temp jointly predict growth? |
| **Prediction Interval** | $\hat{y} \pm t \cdot \hat{\sigma} \sqrt{1 + x^t(X^tX)^{-1}x}$ | This specific fish will weigh 5.5–6.5 kg |
| **Confidence Ellipsoid** | $(\hat{\beta}-\beta)^tX^tX(\hat{\beta}-\beta) \leq p \hat{\sigma}^2 F$ | The tilted football of plausible Feed/Temp effects |
