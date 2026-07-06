## Linear Regression and Least Squares in Matrix Form: A Salmon Farm Example

This is a fantastic question because **salmon farming** (aquaculture) is a perfect real-world example for regression! It involves biology, environment, and economics all of which are messy and require mathematical modeling.

Here is a step-by-step **"Concept to Farm"** guide to understanding regression and least squares using matrices, tailored specifically to how it is used in the salmon industry.

---

### Part 1: The "Weight Scale" Concept (Understanding the Math)

Imagine we are trying to guess a salmon's weight. We have a **digital scale** (the environment) and a **set of weights** (the variables).

| Concept | Description |
| :--- | :--- |
| **The Data ($X$)** | Our data points. In a spreadsheet, each **row** is one fish or one cage, and each **column** is a measurement (e.g., Length, Water Temp, Feed Amount) |
| **The Outcome ($y$)** | The salmon's final weight or harvest biomass |
| **The Coefficients ($\beta$)** | These are the "multipliers" that tell us *how much* each measurement matters |

**The Core Problem:**

Nature is noisy. If we put the exact same weight on a scale 10 times, we get 10 slightly different readings.

**Least Squares** is the mathematical way of saying: *"Find the multipliers ($\beta$) that make the total guessing error as small as possible."*

When we write it in **matrix form**, we are just compressing thousands of fish measurements into a single, elegant equation so a computer can calculate the answer in milliseconds.

---

### Part 2: The Salmon Farm Example Setup

We are the biologist at a salmon farm. We harvest 5 fish and record:

- **$X_1$**: Length of the fish (cm)
- **$X_2$**: Water temperature during the growth period (°C)
- **$y$**: Final weight of the fish (kg)

**The Data ($n = 5$ fish):**

| Fish | Length (cm) | Temp (°C) | Weight (kg) |
| :--- | :--- | :--- | :--- |
| 1 | 60 | 12 | 3.5 |
| 2 | 65 | 13 | 4.2 |
| 3 | 55 | 11 | 2.8 |
| 4 | 70 | 14 | 5.1 |
| 5 | 62 | 12 | 4.0 |

---

### Part 3: Building the Matrix Equation

We want to predict Weight using Length and Temp.

The linear equation is:

$$\text{Weight} = \beta_0 + \beta_1(\text{Length}) + \beta_2(\text{Temp})$$

To use matrices, we must add a column of **1s** to represent the intercept ($\beta_0$).

**Step 1: Define the Matrices**

Our **Design Matrix** ($X$) is 5 rows (fish) $\times$ 3 columns (Intercept, Length, Temp):

$$X = \begin{bmatrix}
1 & 60 & 12 \\
1 & 65 & 13 \\
1 & 55 & 11 \\
1 & 70 & 14 \\
1 & 62 & 12
\end{bmatrix}$$

Our **Outcome Vector** ($y$) is $5 \times 1$:

$$y = \begin{bmatrix} 3.5 \\ 4.2 \\ 2.8 \\ 5.1 \\ 4.0 \end{bmatrix}$$

Our **Unknown Coefficients** ($\beta$) are $3 \times 1$:

$$\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{bmatrix}$$

---

### Part 4: The Matrix Math (Step-by-Step)

We want to find $\beta$ so that $X\beta$ is as close to $y$ as possible.

**Step 1: Multiply $X^T$ (X transpose) by $X$**

This creates a $3 \times 3$ matrix. Think of this as "summarizing" all the length and temperature data.

$$X^T X = \begin{bmatrix}
5 & 312 & 62 \\
312 & 19594 & 3880 \\
62 & 3880 & 774
\end{bmatrix}$$

**Step 2: Multiply $X^T$ by $y$**

This summarizes the relationship between the predictors and the weight.

$$X^T y = \begin{bmatrix} 19.6 \\ 1231.1 \\ 244.0 \end{bmatrix}$$

**Step 3: The "Least Squares" Solution (The Normal Equation)**

The magic formula for the best coefficients is:

$$\hat{\beta} = (X^T X)^{-1} X^T y$$

When we plug our numbers in and solve this (using a calculator or Python), we get:

$$\hat{\beta} = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{bmatrix} = \begin{bmatrix} -6.2 \\ 0.14 \\ 0.25 \end{bmatrix}$$

---

### Part 5: Interpreting the Results (The Farm Insight)

Here is what these numbers mean for our salmon farm:

| Coefficient | Value | Interpretation |
| :--- | :--- | :--- |
| **$\beta_0$** | -6.2 | The mathematical baseline (a fish of zero length would weigh -6.2 kg—this doesn't make sense biologically, but mathematically it anchors the line) |
| **$\beta_1$** | 0.14 | **For every 1 cm increase in length, the fish gains 0.14 kg.** (This is our genetic growth indicator) |
| **$\beta_2$** | 0.25 | **For every 1°C increase in temperature, the fish gains an extra 0.25 kg.** (This is huge! It tells us that temperature heavily impacts growth) |

---

### Part 6: Making Predictions (Using the Model)

We just measured a new fish: **Length = 68 cm, Temp = 13°C**.

Plug it into the equation:

$$\hat{y} = \beta_0 + \beta_1(68) + \beta_2(13)$$

$$\hat{y} = -6.2 + (0.14 \times 68) + (0.25 \times 13)$$

$$\hat{y} = -6.2 + 9.52 + 3.25$$

$$\hat{y} = 6.57 \text{ kg}$$

Our model predicts this fish weighs **6.57 kg**.

---

### Part 7: How Salmon Farmers ACTUALLY Use This

In real life, salmon farmers don't just use 5 fish; they use thousands of data points across multiple pens over several years. Here is how they apply this matrix regression:

| Application | Description |
| :--- | :--- |
| **1. Dynamic Feeding** | The regression model tells them exactly how much weight a fish will gain per kg of feed given the current water temperature. They use this to automate feeders, saving millions in feed costs |
| **2. Optimal Harvest Timing** | They run the model forward. If the sea temperature is dropping in autumn, the matrix regression calculates the exact date when the cost of feeding outweighs the weight gained, telling them *exactly* when to harvest to maximize profit |
| **3. Sea Lice Management** | They add a variable to the matrix for "Sea Lice count". The resulting negative coefficient ($\beta$) tells them exactly how many kilograms of weight they lose per lice. This justifies spending money on anti-lice treatments |
| **4. Selective Breeding** | They put the "Parents" as $X$ and the "Offspring weight" as $y$. The matrix regression tells them which families of fish have the best genetic growth coefficient ($\beta_1$), allowing them to breed bigger salmon |

---

### Part 8: The "Math-to-Farm" Translation Cheat Sheet

| Matrix Term | Salmon Farm Translation |
| :--- | :--- |
| **$y$ (Outcome)** | Total Biomass, Average Weight, or Survival Rate |
| **$X$ (Design Matrix)** | The farm logbook (Temperature, Feed given, Stocking density, Lice count) |
| **$\beta$ (Coefficients)** | The "price" of each factor. *How much weight do we lose per degree of cold?* |
| **Residuals ($e$)** | The unexpected. If a fish weighs less than predicted, it might be sick or bullied. Farmers track residuals to spot disease outbreaks early! |
| **$R^2$ (Fit)** | How reliable the model is. An $R^2$ of 0.90 means the model explains 90% of the weight variation |

---

### Part 9: Quick Python Code for Our Farm

If we want to do this ourselves:

```python
import numpy as np

# Our Farm Data
X = np.array([[1, 60, 12],
              [1, 65, 13],
              [1, 55, 11],
              [1, 70, 14],
              [1, 62, 12]])
y = np.array([3.5, 4.2, 2.8, 5.1, 4.0])

# Calculate Coefficients (The Normal Equation)
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y

print("Intercept:", beta_hat[0])
print("Length effect:", beta_hat[1])  # Should be ~0.14
print("Temp effect:", beta_hat[2])    # Should be ~0.25

# Predict new fish
new_fish = np.array([1, 68, 13])
predicted_weight = new_fish @ beta_hat
print("Predicted weight:", predicted_weight, "kg")
```

## Fitted Values and Residuals: The "Signal" vs. "Noise" of Regression

This is the absolute heart of understanding regression! If we understand fitted values and residuals, we truly understand what regression is doing.

Let's connect this directly back to our salmon farm.

---

### The Core Concept: "Signal" vs. "Noise"

When we weigh a salmon, that number is made up of two parts:

1. **The Predictable Part (Signal):** The weight that comes from its length, temperature, and feed.
2. **The Unpredictable Part (Noise):** The weight from its unique genetics, how much it actually bothered to eat, or measurement error.

In math, we write this as:

> **Actual Value = Fitted Value + Residual**

Here is what that means on the farm:

| Term | Definition | Farm Interpretation |
| :--- | :--- | :--- |
| **Fitted Value ($\hat{y}$)** | The **Farm Manager's Best Guess** | The weight our regression equation *predicts* the fish *should* be, based solely on our matrix math |
| **Residual ($e$)** | The **Mystery Factor** | The difference between what the fish *actually* weighed and what the equation predicted |

---

### Part 1: Fitted Values (The "Expected" Weight)

**The Concept:**

The fitted value is the dot product of our fish's data and our calculated coefficients ($\beta$). It is the **"Signal"** extracted from our matrix.

**The Matrix Math:**

Remember our coefficients from the last example: $\beta_0 = -6.2$, $\beta_1 = 0.14$, $\beta_2 = 0.25$.

To get the fitted values for ALL our fish at once, we just multiply our Design Matrix ($X$) by our coefficient vector ($\beta$):

$$\text{Fitted Values} = \hat{y} = X\hat{\beta}$$

---

**The Salmon Farm Example:**

Let's calculate the Fitted Value for **Fish 1** (Length 60cm, Temp 12°C):

- Actual weight = 3.5 kg
- Fitted Value = $-6.2 + (0.14 \times 60) + (0.25 \times 12)$
- Fitted Value = $-6.2 + 8.4 + 3.0 = \mathbf{5.2 \text{ kg}}$

**What this means on the farm:**

Based on the overall data, our matrix says: *"A perfectly average 60cm fish in 12°C water should weigh 5.2 kg."*

---

### Part 2: Residuals (The "Error" or "Mystery")

**The Concept:**

The residual is the **"Noise"**. It is everything our matrix *failed* to capture.

**The Matrix Math:**

We simply subtract the Fitted Values from the Actual Weights:

$$\text{Residuals} = e = y - \hat{y}$$

---

**The Salmon Farm Example (Continuing Fish 1):**

- Actual Weight = 3.5 kg
- Fitted Value = 5.2 kg
- **Residual = 3.5 - 5.2 = -1.7 kg**

**What this means on the farm:**

Our model overestimated this fish by 1.7 kg! This fish is **underperforming**.

But *why*?

Maybe this specific fish was bullied by others and didn't eat enough. Maybe it has poor genetics. Maybe the scale was dirty. The regression doesn't know *why*; it just knows this fish is an "outlier" that doesn't fit the mathematical pattern.

---

### Part 3: The Matrix Table for All 5 Fish

Let's calculate the Fitted Values and Residuals for all our fish using the coefficients we found ($\beta = [-6.2, 0.14, 0.25]$):

| Fish | Length | Temp | Actual ($y$) | Fitted ($\hat{y}$) | Residual ($y - \hat{y}$) | Farm Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 60 | 12 | 3.5 | 5.2 | **-1.7** | **Underperformer.** Check if it's sick |
| 2 | 65 | 13 | 4.2 | 5.45 | **-1.25** | **Underperformer.** Slightly small for its size |
| 3 | 55 | 11 | 2.8 | 3.75 | **-0.95** | Underperformer, but not drastically |
| 4 | 70 | 14 | 5.1 | 6.3 | **-1.2** | Underperformer |
| 5 | 62 | 12 | 4.0 | 5.48 | **-1.48** | Underperformer |

**Wait a second!** Look at this table. All the residuals are negative. That means *all* our fish weighed less than the model predicted.

**This is a huge farming insight!**

It tells the farm manager: *"Our matrix model is biased. It thinks these fish are bigger than they actually are."*

Why might this happen? Maybe the feed quality dropped last month, or there was a hidden algae bloom. The residuals just alerted us to a farm-wide problem!

---

### Part 4: The "Least Squares" Connection

Remember the "Least Squares" name?

**The Concept:**

"Least Squares" doesn't try to make every single residual zero (that's impossible). Instead, it finds the exact $\beta$ coefficients that make the **sum of the squared residuals as small as possible**.

In matrix math, the objective is:

$$\text{Minimize } e^T e = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

**The Salmon Farm Translation:**

The matrix shuffles the numbers for $\beta_0, \beta_1, \beta_2$ millions of times until it finds the combination where:

> $$(\text{Underperformers})^2 + (\text{Overperformers})^2$$ is at its absolute minimum.

**Why square them?**

Because if we just added them up normally, a -1.7 and a +1.7 would cancel out to zero, making us *think* our model is perfect when it isn't! Squaring makes sure big mistakes (like a 5kg error) are heavily punished.

---

### Part 5: How Farmers Use Residuals Daily

| Application | Description |
| :--- | :--- |
| **1. Early Warning System** (The "Canary in the Coal Mine") | Farmers calculate residuals weekly. If residuals suddenly turn highly **negative** (fish are smaller than expected), it alerts the team 2 weeks before the fish look visibly sick. They can increase oxygen or change feed immediately |
| **2. Identifying "Superstar" Fish for Breeding** | If a fish has a massive **positive residual** (e.g., Actual = 7kg, but Fitted = 5kg), that fish grew way better than the environment predicted. Farmers tag these fish for breeding because they have excellent genetics (low noise, high signal)! |
| **3. Checking if our Matrix is Missing a Variable** | If we plot the residuals on a graph and see a **curved pattern** (e.g., small fish are overestimated, big fish are underestimated), it tells the biologist: *"Our matrix needs an $X^2$ (squared length) term! Growth isn't linear!"* |

---

### The Ultimate Takeaway (Keep this in our heads)

| Term | Matrix Math | Farm Reality |
| :--- | :--- | :--- |
| **Fitted Value ($\hat{y}$)** | $X\hat{\beta}$ | The **Standard Growth Chart** based on our math |
| **Residual ($e$)** | $y - \hat{y}$ | The **"Surprise Factor"**. The gap between the chart and reality |
| **Sum of Squared Residuals** | $e^T e$ | The **Total Farm Mistake**. Least Squares finds the multipliers ($\beta$) that make this number as tiny as possible |

If we understand that **Fitted Values = The Rule**, and **Residuals = The Exceptions to the Rule**, we understand 90% of regression!

## Ordinary Least Squares (OLS) Regression: From Intuition to Matrix Algebra

This is the ultimate question that ties everything together! Let's build this from the ground up—from the intuitive farm-level concept all the way to the elegant matrix algebra.

---

### Part 1: What is OLS (Ordinary Least Squares)?

**The One-Sentence Definition:**

> OLS is a mathematical method that finds the line (or hyperplane) that minimizes the sum of the squared vertical distances between our actual data points and our predicted values.

**The "Ordinary" Part:**

- "Ordinary" means we're using the basic version—no fancy weighting, no regularization, just pure, classic regression.

**The Core Idea:**

Imagine we're drawing a line through a scatterplot of salmon weights vs. feed amounts. OLS finds the **one specific line** where:

- The total error (distance from each point to the line) is as small as possible
- Big errors are heavily penalized (because we square them)
- Positive and negative errors don't cancel out (again, because we square them)

---

### Part 2: The OLS Model

**The Statistical Model:**

$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + ... + \beta_p x_{ip} + \epsilon_i$$

Where:

| Symbol | Meaning |
|--------|---------|
| $y_i$ | Outcome for observation $i$ (e.g., salmon weight) |
| $x_{ij}$ | Predictor $j$ for observation $i$ (e.g., feed, temperature, density) |
| $\beta_j$ | Unknown coefficients we want to estimate |
| $\epsilon_i$ | Random error (the "noise") |

**The OLS Objective:**

$$\text{Minimize } S = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n e_i^2$$

Where $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_{i1} + ... + \hat{\beta}_p x_{ip}$

---

### Part 3: OLS in Vector Notation

Let's build the matrix form step by step.

#### Step 1: Define the Matrices

**Design Matrix ($X$):** $n \times (p+1)$ matrix

$$X = \begin{bmatrix}
1 & x_{11} & x_{12} & \cdots & x_{1p} \\
1 & x_{21} & x_{22} & \cdots & x_{2p} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n1} & x_{n2} & \cdots & x_{np}
\end{bmatrix}$$

*(The column of 1s captures the intercept $\beta_0$)*

**Outcome Vector ($y$):** $n \times 1$

$$y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}$$

**Coefficient Vector ($\beta$):** $(p+1) \times 1$

$$\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_p \end{bmatrix}$$

**Residual Vector ($e$):** $n \times 1$

$$e = y - X\beta$$

#### Step 2: The OLS Objective in Matrix Form

The sum of squared residuals:

$$S(\beta) = e^t e = (y - X\beta)^t (y - X\beta)$$

Expanding:

$$S(\beta) = y^t y - 2\beta^t X^t y + \beta^t X^t X \beta$$

#### Step 3: Finding the Minimum (Calculus)

Take the derivative with respect to $\beta$:

$$\frac{\partial S}{\partial \beta} = -2X^t y + 2X^t X \beta = 0$$

Set to zero and solve:

$$X^t X \beta = X^t y$$

**The Normal Equations:**

$$\boxed{\hat{\beta} = (X^t X)^{-1} X^t y}$$

---

### Part 4: Geometric Interpretation in Vector Space

This is where the magic happens! Let's visualize what's actually going on.

### The Column Space Perspective

Think of the columns of $X$ as arrows (vectors) in an $n$-dimensional space:

- Column 1: The intercept (all 1s) → points straight up along the diagonal
- Column 2: The predictor $x_1$
- Column 3: The predictor $x_2$
- etc.

**The Goal:**

Find the linear combination of these column vectors that comes **closest** to the actual $y$ vector.

**The Solution:**

The OLS estimate $\hat{\beta}$ finds the combination:

$$\hat{y} = X\hat{\beta}$$

This $\hat{y}$ is the **orthogonal projection** of $y$ onto the column space of $X$.

### Visual Analogy (2D)

Imagine shining a flashlight straight down onto a table:

- $y$ = The actual point in 3D space (floating above the table)
- Column space of $X$ = The table surface
- $\hat{y}$ = The shadow of $y$ on the table
- $e = y - \hat{y}$ = The vertical distance from the point to the table (perpendicular!)

**Key Properties:**

1. The residual $e$ is **perpendicular** to every column of $X$
2. $X^t e = 0$ (orthogonality condition)
3. This is exactly the same as the normal equations!

---

### Part 5: The Matrix Projection (The Hat Matrix)

The fitted values can be written as:

$$\hat{y} = X(X^t X)^{-1} X^t y$$

Let $\mathbf{H} = X(X^t X)^{-1} X^t$

**$\mathbf{H}$ is the "Hat Matrix"** because it puts the hat on $y$:

$$\hat{y} = \mathbf{H}y$$

**Properties of $\mathbf{H}$:**

| Property | Description |
|----------|-------------|
| Symmetric | $\mathbf{H}^t = \mathbf{H}$ |
| Idempotent | $\mathbf{H}^2 = \mathbf{H}$ |
| Trace | $tr(\mathbf{H}) = p+1$ (number of parameters) |
| Projection | It's a projection matrix! |

**The Residuals:**

$$e = y - \hat{y} = (I - \mathbf{H})y$$

And $(I - \mathbf{H})$ is also a projection matrix—it projects onto the space **orthogonal** to the column space of $X$.

---
### Part 6: Full Salmon Farming Application

Now let's bring this to life with a real aquaculture scenario!

#### The Problem

We manage a salmon farm with 100 pens. We want to predict harvest weight to optimize feeding schedules.

#### Step 1: Define Our Variables

**Outcome ($y$):**

- Final weight of salmon at harvest (kg)

**Predictors ($X$):**

- $x_1$: Feed amount (kg per day)
- $x_2$: Water temperature (°C)
- $x_3$: Stocking density (fish per m³)
- $x_4$: Oxygen level (mg/L)
- Column of 1s for intercept

#### Step 2: Collect Data

| Pen | Weight (kg) | Feed (kg) | Temp (°C) | Density | O₂ (mg/L) |
|-----|-------------|-----------|-----------|---------|-----------|
| 1   | 4.2         | 2.5       | 12        | 15      | 8.5       |
| 2   | 3.8         | 2.3       | 11        | 18      | 7.8       |
| 3   | 5.1         | 3.0       | 14        | 12      | 9.0       |
| ... | ...         | ...       | ...       | ...     | ...       |
| 100 | 4.5         | 2.7       | 13        | 14      | 8.2       |

#### Step 3: Set Up the Matrices

$$X = \begin{bmatrix}
1 & 2.5 & 12 & 15 & 8.5 \\
1 & 2.3 & 11 & 18 & 7.8 \\
1 & 3.0 & 14 & 12 & 9.0 \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
1 & 2.7 & 13 & 14 & 8.2
\end{bmatrix}, \quad
y = \begin{bmatrix}
4.2 \\ 3.8 \\ 5.1 \\ \vdots \\ 4.5
\end{bmatrix}$$

#### Step 4: Compute OLS Coefficients

$$\hat{\beta} = (X^t X)^{-1} X^t y$$

Let's say the results are:

$$\hat{\beta} = \begin{bmatrix}
\beta_0 \\
\beta_1 \\
\beta_2 \\
\beta_3 \\
\beta_4
\end{bmatrix} = \begin{bmatrix}
-2.5 \\
1.8 \\
0.15 \\
-0.08 \\
0.35
\end{bmatrix}$$

#### Step 5: Interpret the Results (The "Farm Translation")

| Coefficient | Value | Interpretation |
|-------------|-------|----------------|
| $\hat{\beta}_0$ | -2.5 kg | Baseline weight when all predictors are 0 (not realistic, but mathematically necessary) |
| $\hat{\beta}_1$ (Feed) | **1.8 kg per kg feed** | **Every extra kg of feed adds 1.8 kg to harvest weight** → Critical for feeding decisions! |
| $\hat{\beta}_2$ (Temp) | **0.15 kg per °C** | **Warmer water increases growth** → Helps plan optimal harvest seasons |
| $\hat{\beta}_3$ (Density) | **-0.08 kg per fish/m³** | **Higher density reduces growth** → Tells us optimal stocking levels |
| $\hat{\beta}_4$ (O₂) | **0.35 kg per mg/L** | **More oxygen boosts growth** → Justifies aeration system investments |

#### Step 6: Make Predictions

A new pen has:
- Feed: 2.8 kg/day
- Temperature: 13°C
- Density: 16 fish/m³
- O₂: 8.0 mg/L

**Predicted weight:**

$$\hat{y} = -2.5 + 1.8(2.8) + 0.15(13) - 0.08(16) + 0.35(8.0)$$

$$= -2.5 + 5.04 + 1.95 - 1.28 + 2.8 = 6.01 \text{ kg}$$

The model predicts **6.01 kg** at harvest.

#### Step 7: The Business Impact

| OLS Finding | Business Decision |
|-------------|-------------------|
| Feed has the biggest impact (1.8 kg/kg) | Invest in precision feeding systems |
| Temperature matters (0.15 kg/°C) | Use warmer sites or adjust harvest timing |
| Density hurts growth (-0.08 kg per fish) | Reduce stocking density to improve profits |
| Oxygen helps (0.35 kg per mg/L) | Install emergency aeration to prevent losses |

---

### Part 7: The Matrix Properties in Salmon Terms

| Matrix Concept | What It Represents | Salmon Example |
|----------------|-------------------|----------------|
| **Design Matrix $X$** | Our farm logbook (all data collected) | Every measurement across all pens |
| **Coefficient $\beta$** | The "prices" of each factor | How much weight each variable adds |
| **Fitted $\hat{y}$** | Our best predictions | Expected harvest weights |
| **Residuals $e$** | The "mystery factor" | Unexplained variation (genetics, disease, measurement error) |
| **Hat Matrix $\mathbf{H}$** | "Leverage" of each observation | Pens with unusual conditions that strongly influence our model |
| **Projection** | Fitting the model geometrically | Finding the sweet spot that minimizes all errors at once |
| **$X^t X$** | Sum of squares and cross-products | How variables relate to each other (e.g., feed and temperature correlation) |
| **$(X^t X)^{-1}$** | The "scale" of uncertainty | How precise our estimates are (used for confidence intervals) |

---
### Part 8: Summary - The Complete Picture

### Intuitive View (Farm Level):

> OLS is like being a master fish farmer who observes past pens, figures out exactly how much feed, temperature, density, and oxygen affect growth, and uses that formula to predict future harvests while automatically balancing out the unavoidable randomness of nature.

### Mathematical View:

> OLS finds the $\beta$ vector that minimizes the squared Euclidean distance between $y$ and the column space of $X$.

### Matrix View:

> $\hat{\beta} = (X^t X)^{-1} X^t y$ projects $y$ onto the space spanned by the columns of $X$, giving the best linear unbiased estimate (BLUE) under the Gauss-Markov theorem.

### Geometric View:

> The residual $e$ is orthogonal to every column of $X$, meaning the "shadow" $\hat{y}$ is the closest point to $y$ in the column space.

### Business View:

> OLS turns data into dollars by quantifying exactly what drives salmon growth, enabling precision farming decisions that maximize profit per pen.

---

### Quick Reference Card

| Aspect | Formula/Notation | Farm Translation |
|--------|------------------|------------------|
| Model | $y = X\beta + \epsilon$ | Growth = (Factors × Impacts) + Random Noise |
| Objective | Minimize $e^t e$ | Make total mistakes as small as possible |
| Solution | $\hat{\beta} = (X^t X)^{-1} X^t y$ | The best multipliers for our factors |
| Fitted Values | $\hat{y} = X\hat{\beta}$ | Our predicted harvests |
| Residuals | $e = y - \hat{y}$ | The surprises (good or bad) |
| Hat Matrix | $\mathbf{H} = X(X^t X)^{-1} X^t$ | Which pens "pull" the model |

---

## Multivariate Regression: The Complete Guide

Now we're moving from **univariate** (one outcome) to **multivariate** (multiple outcomes)! This is a significant step up in power and complexity.

---

### Part 1: What is Multivariate Regression?

**The One-Sentence Definition:**

> Multivariate regression models **multiple outcome variables** simultaneously using the same set of predictors.

**Univariate vs. Multivariate:**

| | Univariate Regression | Multivariate Regression |
|---|----------------------|------------------------|
| **Outcomes** | 1 outcome variable | 2+ outcome variables |
| **Predictors** | Multiple predictors | Multiple predictors |
| **Coefficients** | 1 vector $\beta$ | A **matrix** $B$ |
| **Example** | Predict salmon weight | Predict salmon weight, length, and fat content simultaneously |

**The Key Insight:**

Instead of fitting separate models for each outcome, multivariate regression fits them **together**, accounting for the **correlations between outcomes**.

---

### Part 2: The Multivariate Model

#### Statistical Form

For $n$ observations, $q$ outcomes, and $p$ predictors:

$$\mathbf{Y} = \mathbf{X}\mathbf{B} + \mathbf{E}$$

Where:

| Symbol | Dimensions | Description |
|--------|------------|-------------|
| $\mathbf{Y}$ | $n \times q$ | Matrix of outcomes (each column is a different outcome) |
| $\mathbf{X}$ | $n \times (p+1)$ | Design matrix (includes intercept) |
| $\mathbf{B}$ | $(p+1) \times q$ | Matrix of coefficients |
| $\mathbf{E}$ | $n \times q$ | Matrix of errors |

#### Expanded Form

### Part 3: The OLS Solution (Matrix Form)

#### The Objective

Minimize the **sum of squared errors** across ALL outcomes:

$$S(\mathbf{B}) = \text{tr}\left[(\mathbf{Y} - \mathbf{X}\mathbf{B})^t(\mathbf{Y} - \mathbf{X}\mathbf{B})\right]$$

Where $\text{tr}$ is the trace (sum of diagonal elements).

#### The Solution

$$\boxed{\hat{\mathbf{B}} = (\mathbf{X}^t\mathbf{X})^{-1}\mathbf{X}^t\mathbf{Y}}$$

**Key Observation:**

> The coefficients for each outcome are estimated **independently**! Column $j$ of $\hat{\mathbf{B}}$ is exactly the univariate OLS solution for outcome $j$.

#### The Fitted Values

$$\hat{\mathbf{Y}} = \mathbf{X}\hat{\mathbf{B}} = \mathbf{X}(\mathbf{X}^t\mathbf{X})^{-1}\mathbf{X}^t\mathbf{Y} = \mathbf{H}\mathbf{Y}$$

---

### Part 4: Salmon Farm Example

#### The Problem

We manage a salmon farm and want to predict **three outcomes** simultaneously:

1. **Weight** (kg)
2. **Length** (cm)
3. **Fat content** (%)

Using predictors:

- Feed amount (kg/day)
- Water temperature (°C)
- Stocking density (fish/m³)

#### Step 1: Set Up the Data

| Pen | Weight (kg) | Length (cm) | Fat (%) | Feed (kg) | Temp (°C) | Density |
|-----|-------------|-------------|---------|-----------|-----------|---------|
| 1   | 4.2         | 65          | 18      | 2.5       | 12        | 15      |
| 2   | 3.8         | 62          | 16      | 2.3       | 11        | 18      |
| 3   | 5.1         | 72          | 22      | 3.0       | 14        | 12      |
| 4   | 4.5         | 68          | 19      | 2.7       | 13        | 14      |
| ... | ...         | ...         | ...     | ...       | ...       | ...     |

#### Step 2: Define the Matrices

**Outcome Matrix $\mathbf{Y}$ ($n \times 3$):**

$$\mathbf{Y} = \begin{bmatrix}
4.2 & 65 & 18 \\
3.8 & 62 & 16 \\
5.1 & 72 & 22 \\
4.5 & 68 & 19 \\
\vdots & \vdots & \vdots
\end{bmatrix}$$

**Design Matrix $\mathbf{X}$ ($n \times 4$):**

$$\mathbf{X} = \begin{bmatrix}
1 & 2.5 & 12 & 15 \\
1 & 2.3 & 11 & 18 \\
1 & 3.0 & 14 & 12 \\
1 & 2.7 & 13 & 14 \\
\vdots & \vdots & \vdots & \vdots
\end{bmatrix}$$

#### Step 3: Compute Coefficients

$$\hat{\mathbf{B}} = (\mathbf{X}^t\mathbf{X})^{-1}\mathbf{X}^t\mathbf{Y}$$

Results:

$$\hat{\mathbf{B}} = \begin{bmatrix}
\text{Intercept} & -2.5 & 20 & 5 \\
\text{Feed} & 1.8 & 12 & 3 \\
\text{Temp} & 0.15 & 0.8 & 0.2 \\
\text{Density} & -0.08 & -0.3 & -0.1
\end{bmatrix}$$

#### Step 4: Interpretation

| Predictor | Weight (kg) | Length (cm) | Fat (%) | Farm Meaning |
|-----------|-------------|-------------|---------|--------------|
| **Intercept** | -2.5 | 20 | 5 | Baseline when all predictors = 0 |
| **Feed** | **+1.8** | **+12** | **+3** | More feed increases all three! |
| **Temp** | **+0.15** | **+0.8** | **+0.2** | Warmer water improves all metrics |
| **Density** | **-0.08** | **-0.3** | **-0.1** | Crowding hurts everything |

#### Step 5: Make Predictions

New pen: Feed = 2.8kg, Temp = 13°C, Density = 16

$$\hat{\mathbf{y}}_{new} = \mathbf{x}_{new}^t \hat{\mathbf{B}}$$

$$\mathbf{x}_{new}^t = \begin{bmatrix} 1 & 2.8 & 13 & 16 \end{bmatrix}$$

**Weight:** $-2.5 + 1.8(2.8) + 0.15(13) - 0.08(16) = 6.01$ kg

**Length:** $20 + 12(2.8) + 0.8(13) - 0.3(16) = 69.2$ cm

**Fat:** $5 + 3(2.8) + 0.2(13) - 0.1(16) = 14.4$ %

---

### Part 5: Why Use Multivariate Regression?

#### 1. Accounting for Correlations Between Outcomes

| Aspect | Separate Models | Multivariate Model |
|--------|----------------|-------------------|
| Weight vs. Length | Ignored | Accounts for their correlation |
| Confidence intervals | Separate | Joint confidence regions |
| Hypothesis testing | Separate tests | **Multivariate tests** (MANOVA) |

#### 2. Improved Efficiency

When outcomes are correlated, multivariate models borrow strength across outcomes, yielding **more efficient estimates**.

#### 3. Interpretability

Instead of saying "feed affects weight, length, and fat separately," we can say "feed affects the **entire growth profile**."

---

### Part 6: The Residual Covariance Structure

#### The Magic of Multivariate Regression

The errors are assumed to be:

$$\text{Var}(\boldsymbol{\epsilon}_i) = \boldsymbol{\Sigma}$$

Where $\boldsymbol{\Sigma}$ is a $q \times q$ **covariance matrix** of the outcomes.

$$\boldsymbol{\Sigma} = \begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \cdots & \sigma_{1q} \\
\sigma_{12} & \sigma_2^2 & \cdots & \sigma_{2q} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{1q} & \sigma_{2q} & \cdots & \sigma_q^2
\end{bmatrix}$$

**Estimated by:**

$$\hat{\boldsymbol{\Sigma}} = \frac{1}{n - p - 1} (\mathbf{Y} - \mathbf{X}\hat{\mathbf{B}})^t(\mathbf{Y} - \mathbf{X}\hat{\mathbf{B}})$$

**Salmon Farm Translation:**

| Symbol | Meaning |
|--------|---------|
| $\sigma_1^2$ | Variance in weight |
| $\sigma_2^2$ | Variance in length |
| $\sigma_3^2$ | Variance in fat content |
| $\sigma_{12}$ | Covariance between weight and length (bigger fish are longer) |
| $\sigma_{13}$ | Covariance between weight and fat (bigger fish have more fat) |
| $\sigma_{23}$ | Covariance between length and fat (longer fish have more fat) |

---

### Part 7: Hypothesis Testing in Multivariate Regression

#### Test for Overall Significance (MANOVA)

$$H_0: \mathbf{B}_{\text{predictors}} = \mathbf{0}$$

**Test Statistics:**

| Test | Formula |
|------|---------|
| **Wilks' Lambda** | $\Lambda = \frac{|\mathbf{E}|}{|\mathbf{H} + \mathbf{E}|}$ |
| **Pillai's Trace** | $V = \text{tr}(\mathbf{H}(\mathbf{H} + \mathbf{E})^{-1})$ |
| **Hotelling-Lawley Trace** | $T = \text{tr}(\mathbf{H}\mathbf{E}^{-1})$ |
| **Roy's Largest Root** | $\lambda_{\text{max}}$ |

Where:
- $\mathbf{H}$ = Hypothesis sum of squares matrix
- $\mathbf{E}$ = Error sum of squares matrix

#### Salmon Farm Example

**Question:** *Does feed, temperature, and density jointly affect weight, length, and fat?*

Use MANOVA to test if the entire coefficient matrix $\mathbf{B}$ (excluding intercept) is zero.

---

### Part 8: Relationship to Univariate Models

#### Important Result

The coefficients for each outcome in a multivariate regression are **exactly the same** as fitting separate univariate regressions!

$$\hat{\boldsymbol{\beta}}_j = (\mathbf{X}^t\mathbf{X})^{-1}\mathbf{X}^t\mathbf{y}_j$$

**So why bother with multivariate?**

| Reason | Benefit |
|--------|---------|
| **Joint inference** | Testing multiple outcomes together |
| **Borrowing information** | Across outcomes (in some advanced methods) |
| **Handling missing data** | Imputation using correlations |
| **Dimension reduction** | Like Principal Component Analysis on outcomes |

---

### Part 9: Reduced Rank Regression

#### Extension: Constraining the Coefficient Matrix

Instead of estimating all $p \times q$ coefficients freely, we can impose a **rank constraint**:

$$\hat{\mathbf{B}} = \mathbf{A}\mathbf{C}^t$$

Where:
- $\mathbf{A}$ is $p \times r$
- $\mathbf{C}$ is $q \times r$
- $r < \min(p, q)$

**This reduces dimensionality and can improve predictions!**

#### Salmon Farm Application

Imagine we have 10 outcomes and 20 predictors. We believe there are only 2 underlying "factors" driving everything:

1. **Growth factor** (affects weight, length, fat)
2. **Health factor** (affects survival, disease resistance)

Reduced rank regression finds these latent factors!

---

### Part 10: Full Matrix Math Summary

#### The Model
$$\mathbf{Y} = \mathbf{X}\mathbf{B} + \mathbf{E}$$

#### The Solution
$$\hat{\mathbf{B}} = (\mathbf{X}^t\mathbf{X})^{-1}\mathbf{X}^t\mathbf{Y}$$

#### Fitted Values
$$\hat{\mathbf{Y}} = \mathbf{X}\hat{\mathbf{B}} = \mathbf{H}\mathbf{Y}$$

#### Residuals
$$\mathbf{E} = \mathbf{Y} - \hat{\mathbf{Y}} = (\mathbf{I} - \mathbf{H})\mathbf{Y}$$

#### Covariance Estimate
$$\hat{\boldsymbol{\Sigma}} = \frac{1}{n - p - 1} \mathbf{E}^t\mathbf{E}$$

#### Predictions for New Data
$$\hat{\mathbf{y}}_{new} = \mathbf{x}_{new}^t \hat{\mathbf{B}}$$

#### Variance of Predictions
$$\text{Var}(\hat{\mathbf{y}}_{new}) = \mathbf{x}_{new}^t (\mathbf{X}^t\mathbf{X})^{-1} \mathbf{x}_{new} \cdot \hat{\boldsymbol{\Sigma}}$$

---

### Part 11: Quick Reference Card

| Aspect | Univariate | Multivariate |
|--------|-----------|--------------|
| Outcomes | 1 ($n \times 1$) | Multiple ($n \times q$) |
| Coefficients | Vector $\boldsymbol{\beta}$ | Matrix $\mathbf{B}$ |
| Errors | Vector $\boldsymbol{\epsilon}$ | Matrix $\mathbf{E}$ |
| Covariance | $\sigma^2$ (scalar) | $\boldsymbol{\Sigma}$ (matrix) |
| OLS Solution | $(X^tX)^{-1}X^t y$ | $(X^tX)^{-1}X^t Y$ |
| Hypothesis tests | t-test, F-test | Wilks' Lambda, Pillai's Trace |
| R function | `lm()` | `lm()` (but with matrix Y!) |

---

### Part 12: R Code Example

```r
# Simulate salmon farm data
n <- 100
set.seed(123)

# Predictors
Feed <- rnorm(n, 2.5, 0.5)
Temp <- rnorm(n, 12, 2)
Density <- rnorm(n, 15, 3)

# Create design matrix
X <- cbind(1, Feed, Temp, Density)

# True coefficients (3 outcomes: Weight, Length, Fat)
B <- matrix(c(-2.5, 1.8, 0.15, -0.08,   # Weight
              20,   12,  0.8,  -0.3,    # Length
              5,    3,   0.2,  -0.1),   # Fat
            nrow=4, ncol=3)

# Generate outcomes with correlated errors
library(MASS)
Sigma <- matrix(c(0.25, 0.15, 0.05,   # Covariance matrix
                  0.15, 0.30, 0.08,
                  0.05, 0.08, 0.20), nrow=3)

E <- mvrnorm(n, mu=c(0,0,0), Sigma=Sigma)
Y <- X %*% B + E

# Fit multivariate model
library(mvtnorm)
fit <- lm(Y ~ Feed + Temp + Density)

# View coefficients
summary(fit)

# Predictions for new pen
new_data <- data.frame(Feed=2.8, Temp=13, Density=16)
predict(fit, newdata=new_data)

# MANOVA test
summary(manova(fit))

# Extract coefficient matrix
coef(fit)  # This gives B_hat!
