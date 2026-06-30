## What is Hypothesis Testing?

Hypothesis testing is a formal statistical procedure to decide whether the evidence in our sample is strong enough to reject a claim about the population.

**The Process:**
1. We make a claim (The Null Hypothesis).
2. We collect data.
3. We calculate a **test statistic** (which measures how far our data is from our claim, in standard error units).
4. We calculate the probability of getting our data *if* our claim were true (the p-value).
5. If that probability is tiny, we reject the claim.

---

### The Two Hypotheses

We always set up two competing statements:

- **Null Hypothesis ($H_0$):** The "status quo" or "no effect" claim. This is what we assume to be true until proven otherwise. It always contains an equality ($=, \leq, \geq$).
  - *Salmon Example:* "The new feed does not change growth. The true mean weight is still $\mu = 5.0$ kg."

- **Alternative Hypothesis ($H_A$ or $H_1$):** The "effect exists" claim. This is what we want to prove. It always contains an inequality ($\neq, >, <$).
  - *Salmon Example:* "The new feed changes growth. The true mean weight is $\mu \neq 5.0$ kg" (Two-tailed).

---

### The Three Conditions for Rejecting the Null ($\bar{x} \neq \mu$)

Our sample mean ($\bar{x}$) will almost **never** exactly equal the population mean ($\mu$) just by random chance. We reject $H_0$ when the difference is **too large to be explained by random luck**.

There are exactly **three reasons** our sample mean differs from the population mean:

| Reason | Description | Action |
|--------|-------------|--------|
| 1. **Random Sampling Error (Pure Chance)** | We just happened to catch a few big fish. The feed does nothing. | **Do not reject $H_0$** |
| 2. **Bias in Sampling** | Our sampling method is flawed (e.g., we only caught fish near the feeder, which are heavier) | Might falsely reject $H_0$, but for the wrong reason |
| 3. **A True Effect** | The feed actually works! The population mean has genuinely changed | **Correctly reject $H_0$** |

Hypothesis testing is designed to distinguish between Reason 1 (luck) and Reason 3 (a real effect).

---

### The Test Statistic (The "Measuring Stick")

A test statistic is a single number that measures how many **standard errors** our sample estimate is away from the null hypothesis value.

For a sample mean, the test statistic is the **z-score** (or t-score):

$$z = \frac{\bar{x} - \mu_0}{SE} = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

**Salmon Example:**
- Null mean: $\mu_0 = 5.0$ kg (population mean)
- Sample mean: $\bar{x} = 5.3$ kg
- Standard Error: $SE = 0.15$ kg

$$z = \frac{5.3 - 5.0}{0.15} = \frac{0.3}{0.15} = 2.0$$

**Translation:** Our sample mean is **2.0 standard errors** above the hypothesized mean.

---
### The "Alpha" Level ($\alpha$) – Type I Error

**Definition:** Alpha ($\alpha$) is the **threshold** we set for rejecting the null hypothesis. It is the probability of making a **Type I Error**.

| Concept | Definition | Salmon Example |
|---------|------------|----------------|
| **Type I Error (False Positive)** | We reject $H_0$ when it is actually *true* | We declare the feed works, but it actually does nothing |
| **Alpha ($\alpha$)** | The risk we are willing to take of making a Type I Error | Usually set to **0.05** (5%) |

**How it works:**

We compare our test statistic ($z = 2.0$) to the critical value for $\alpha = 0.05$ (which is $\pm 1.96$ for a two-tailed test).

- If $|z| > 1.96$ → Reject $H_0$
- If $|z| < 1.96$ → Fail to reject $H_0$

Since $2.0 > 1.96$, we reject $H_0$. We conclude the feed works, but there is a 5% chance we are wrong (Type I Error).

---

### "Beta" ($\beta$) and Type II Error

**Definition:** Beta ($\beta$) is the probability of making a **Type II Error**.

| Concept | Definition | Salmon Example |
|---------|------------|----------------|
| **Type II Error (False Negative)** | We **fail** to reject $H_0$ when it is actually *false* | The feed *does* work, but our sample was too small or too noisy to detect it |
| **Beta ($\beta$)** | The probability of a Type II Error | Depends on effect size, sample size, and alpha |
| **Power ($1 - \beta$)** | The probability that we *correctly* reject a false null hypothesis | Power = 80% means we have an 80% chance of catching the effect if it truly exists |

**Beta ($\beta$) depends on:**
1. The **true effect size** (how big the real difference is)
2. Our **sample size** ($n$)
3. Our **alpha level** ($\alpha$)

---

### The Interplay of Alpha, Beta, and Sample Size

These three are locked in an eternal triangle:

| What we change | Effect on $\alpha$ (Type I) | Effect on $\beta$ (Type II / Power) |
|----------------|----------------------------|-------------------------------------|
| **Increase $n$ (Sample Size)** | No effect (we set $\alpha$) | $\beta$ **decreases** (Power increases) |
| **Decrease $\alpha$** (e.g., 0.05 to 0.01) | Stricter threshold | $\beta$ **increases** (Power decreases). Harder to find effects |
| **Increase the true effect size** | No effect | $\beta$ **decreases** (huge effects are easy to spot) |
---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example |
|---------|------------|----------------|
| **Null Hypothesis ($H_0$)** | The "no effect" claim | Feed does nothing: $\mu = 5.0$ kg |
| **Alternative ($H_A$)** | The "effect exists" claim | Feed changes weight: $\mu \neq 5.0$ kg |
| **Test Statistic (z-score)** | Signal / Noise. How many SEs away from $H_0$ | $z = (5.3 - 5.0) / 0.15 = 2.0$ |
| **Alpha ($\alpha$)** | The risk of a False Positive (Type I Error). Usually 5% | We are willing to wrongly declare the feed works 5% of the time |
| **Type I Error** | Rejecting $H_0$ when it is *true* | Declaring the feed works when it actually doesn't |
| **Beta ($\beta$)** | The risk of a False Negative (Type II Error) | Declaring the feed doesn't work when it actually does |
| **Power ($1 - \beta$)** | The probability of correctly detecting a real effect | 80% power = 80% chance we catch the real weight gain if it exists |
| **The Golden Rule** | To reduce $\beta$ (increase power), increase our sample size ($n$) or accept a higher $\alpha$ | Catch more fish to make sure we don't miss a real effect! |

---

### The One-Liner to Memorize

> *"Alpha is the risk of a false alarm (Type I), Beta is the risk of missing the truth (Type II). Increasing our sample size is the only cure to lower Beta without raising Alpha."*

### Applying t critical value and p-value in testing hypothesis

To understand how we use the **t-critical value** to decide whether to reject the null hypothesis, we have to look at the **"Courtroom Analogy"** of hypothesis testing.

We are the judge. The **Null Hypothesis ($H_0$)** is the defendant, who is presumed "innocent" (no effect). The **Alternative Hypothesis ($H_A$)** is the prosecutor, claiming "guilty" (there is an effect).

The **t-critical value** is the **"burden of proof"** line. It is the minimum amount of evidence we need to convict the defendant.

Here is the exact step-by-step process of how we use it to make the final decision.

---
### 1. The Two Numbers We Calculate

In a t-test, we have two numbers:

| Number | Symbol | What It Is | How We Get It |
|--------|--------|------------|---------------|
| **t-critical value** | $t^*$ | The **threshold** | Look up in a t-table *before* looking at our data. Depends on $\alpha$, $df$, and whether the test is one-tailed or two-tailed |
| **t-statistic** | $t_{obs}$ | The **evidence** | Calculate *from our data*. Measures how many standard errors our sample mean is away from the null hypothesis mean |

---
### 2. The Decision Rule (The "Line in the Sand")

Once we have both numbers, the rule is brutally simple:
> **If our observed t-statistic is MORE EXTREME than the t-critical value, we REJECT the null hypothesis.**

Let's look at how this works in the two different scenarios.

---
### Scenario 1: The Two-Tailed Test (Checking for ANY difference)

**The Question:** *"Does the new feed change weight? (It could be heavier OR lighter)."*

| Component | Value |
|-----------|-------|
| **Null ($H_0$)** | $\mu = 5.0$ kg |
| **Alternative ($H_A$)** | $\mu \neq 5.0$ kg |
| **Alpha ($\alpha$)** | 0.05 (split into 2.5% left tail + 2.5% right tail) |
| **Degrees of Freedom** | $df = 9$ |
| **t-critical value ($t^*$)** | $\pm 2.262$ (from t-table) |

**Visualizing the Graph:**

Imagine a t-distribution (bell curve). We draw vertical lines at **-2.262** and **+2.262**.

| Region | Range | Probability | Meaning |
|--------|-------|-------------|---------|
| **Innocence Zone** | Between -2.262 and +2.262 | 95% | Fail to reject $H_0$ |
| **Rejection Zones** | Outside -2.262 and +2.262 | 5% | Reject $H_0$ |


**Our Decision:**

| Scenario | $t_{obs}$ | Result | Meaning |
|----------|-----------|--------|---------|
| **Case 1** | $t_{obs} = 1.5$ | Falls between -2.262 and +2.262 (Innocence Zone) | **Fail to reject $H_0$.** The evidence is too weak; we cannot convict the feed of working |
| **Case 2** | $t_{obs} = 2.8$ | Is greater than +2.262 (Rejection Zone) | **Reject $H_0$.** The evidence is overwhelming; we conclude the feed works! |

---

### Scenario 2: The One-Tailed Test (Checking if it is GREATER)

**The Question:** *"Does the new feed make fish HEAVIER?"* (We only care about weight gain, not weight loss).

| Component | Value |
|-----------|-------|
| **Null ($H_0$)** | $\mu \leq 5.0$ kg |
| **Alternative ($H_A$)** | $\mu > 5.0$ kg |
| **Alpha ($\alpha$)** | 0.05 (ALL in the right tail) |
| **Degrees of Freedom** | $df = 9$ |
| **t-critical value ($t^*$)** | $+1.833$ (from t-table) |

**Visualizing the Graph:**
We draw a vertical line at **+1.833**.

| Region | Range | Probability | Meaning |
|--------|-------|-------------|---------|
| **Innocence Zone** | Left of 1.833 | 95% | Fail to reject $H_0$ |
| **Rejection Zone** | Right of 1.833 | 5% | Reject $H_0$ |


**Our Decision:**

| Scenario | $t_{obs}$ | Result | Meaning |
|----------|-----------|--------|---------|
| **Case 1** | $t_{obs} = 1.9$ | Greater than 1.833 (Rejection Zone) | **Reject $H_0$.** We conclude the fish are heavier! |
| **Case 2** | $t_{obs} = 1.5$ | Less than 1.833 (Innocence Zone) | **Fail to reject $H_0$.** Not enough evidence |

---

### 3. The "P-value" Shortcut (Modern Software)

Almost all modern statistical software (R, Python, SPSS) bypasses the t-critical value and gives us the **p-value** instead.

| Concept | Definition | Rule |
|---------|------------|------|
| **p-value** | The exact probability of getting our specific $t_{obs}$ (or something more extreme) if the null hypothesis were true | If **p-value < $\alpha$** (e.g., 0.05) → **Reject $H_0$** |
| **Connection** | A p-value of 0.03 means there is a 3% chance of seeing our data by pure luck | Since 3% < 5% (alpha), we reject the null |

The t-critical value method is the **"old-school"** way of doing this without computers.

---

### Summary Table: The Decision Matrix

| Test Type | Condition | Result | Meaning |
|-----------|-----------|--------|---------|
| **Two-tailed ($\alpha = 0.05$)** | $t_{obs}$ is between -2.262 and +2.262 | **Fail to Reject $H_0$** | Not enough evidence to say the feed changes weight |
| **Two-tailed ($\alpha = 0.05$)** | $t_{obs} < -2.262$ or $t_{obs} > +2.262$ | **Reject $H_0$** | Strong evidence that the feed changes weight |
| **One-tailed ($\alpha = 0.05$)** | $t_{obs} < +1.833$ | **Fail to Reject $H_0$** | Not enough evidence to say the feed *increases* weight |
| **One-tailed ($\alpha = 0.05$)** | $t_{obs} > +1.833$ | **Reject $H_0$** | Strong evidence that the feed *increases* weight |

---

### The One-Liner to Memorize

> *"The t-critical value is the 'finish line.' If our calculated t-statistic crosses that line (is more extreme), we reject the null hypothesis. If it stays behind the line, we admit the evidence is too weak to convict."*

## The p-Value: A Measure of Surprise

The **p-value** is the probability of obtaining a test statistic as extreme as (or more extreme than) the one observed, **assuming that the null hypothesis ($H_0$) is true**.

- It is **not** the probability that $H_0$ is true.
- It is **not** the probability that the alternative hypothesis ($H_A$) is true.
- It is purely a measure of **surprise**: *"How surprised would we be to see this data if nothing were really going on?"*

---

### The Courtroom Analogy

To understand the **p-value**, we have to go back to our courtroom analogy from hypothesis testing.

Imagine we are a judge, and the **Null Hypothesis ($H_0$)** is the defendant, who is presumed "innocent" (meaning: there is no effect, no difference, no relationship).

The **p-value** is the exact answer to this question:

> *"If the defendant is truly innocent (if $H_0$ is true), what is the probability that we would see evidence as extreme as (or more extreme than) what we just observed, purely by random chance?"*

---

### A Salmon Example (Putting numbers to it)

We are testing a new feed. We want to know if it makes salmon heavier.

| Component | Value |
|-----------|-------|
| **Null Hypothesis ($H_0$)** | The feed does nothing. The true mean weight is $\mu = 5.0$ kg |
| **Alternative ($H_A$)** | The feed makes them heavier. $\mu > 5.0$ kg |
| **Sample** | 100 fish, $\bar{x} = 5.3$ kg, $SE = 0.15$ kg |
| **Test Statistic** | $z = \frac{5.3 - 5.0}{0.15} = 2.0$ |

**The p-value:**

We ask: *"If the feed actually does nothing (true mean = 5.0), what is the probability of randomly catching 100 fish with an average of 5.3 kg or higher?"*

We look at the standard Normal distribution. The area to the right of $z = 2.0$ is **0.025** (2.5%).

> **The p-value = 0.025**

---

### How to use the p-value to make a decision

We compare the p-value to our pre-set **Alpha level ($\alpha$)**, which is our tolerance for false alarms (Type I error). Usually, $\alpha = 0.05$.

**The Decision Rule:**

| Condition | Meaning | Decision |
|-----------|---------|----------|
| **p-value < $\alpha$** (e.g., 0.025 < 0.05) | *"This is too unlikely to be a coincidence. The evidence is strong enough to reject the null hypothesis."* | **Statistically Significant** → Reject $H_0$ |
| **p-value > $\alpha$** (e.g., 0.10 > 0.05) | *"This is plausible under the null hypothesis. We do not have enough evidence to convict."* | **Not Statistically Significant** → Fail to reject $H_0$ |

---

### The Golden Rule of p-values (What they DO NOT mean)

This is the single most misunderstood concept in statistics. Memorize these:

| **True Statement** | **False Statement (Common Misinterpretation)** |
| :--- | :--- |
| A p-value of 0.03 means there is a 3% chance of seeing this data (or more extreme) **if $H_0$ is true** | A p-value of 0.03 means there is only a 3% chance that $H_0$ is true |
| A p-value of 0.06 means we do not have enough evidence to reject $H_0$ | A p-value of 0.06 means there is a 94% chance that $H_A$ is true |
| A small p-value indicates that the data are **incompatible** with the null hypothesis | A small p-value indicates the **effect size** is large or practically important |

---

### The "P-Value" Fallacy (A Cautionary Tale)

Imagine we test a new feed on **1,000,000 salmon**. The feed increases weight by a microscopic **0.001 kg**.

- The sample size is so huge that our standard error is tiny.
- The test statistic becomes gigantic.
- We get a **p-value of 0.0001**.

We reject the null hypothesis. We declare the feed works. **But does it matter?**

- 0.001 kg is less than a drop of water. It is completely useless to the farmer, even though it is "statistically significant."

> **The Golden Rule of Application:** A p-value tells us about **statistical significance** (is it likely a coincidence?). It does **NOT** tell us about **practical significance** (does it actually matter?). Always report the **effect size** and **confidence interval** alongside the p-value!

---

### Real-World Applications of p-values

| Application | Example | Interpretation |
|-------------|---------|----------------|
| **Medical Trials** | p-value = 0.04 | Only a 4% chance the observed drug effect is due to random luck. FDA approves the drug |
| **Salmon Farming** | p-value = 0.60 | 60% chance the difference in growth is just noise. Stick with the cheaper feed |
| **A/B Testing (Websites)** | p-value = 0.01 | Only 1% chance the increase in clicks was random. Switch to the new layout |

---
### The Most Important Rule: p-value is a continuous measure

The p-value is not a binary "significant / not significant" switch.

- A p-value of **0.049** and **0.051** are almost identical in reality, but one is considered "significant", and the other is not if we use a strict 0.05 cutoff.
- **Best Practice:** Report the exact p-value (e.g., $p = 0.048$) and let the reader decide.

---

### Summary Cheat Sheet

| Concept | Explanation |
| :--- | :--- |
| **p-value** | The probability of seeing our data (or more extreme) **assuming $H_0$ is true** |
| **Small p-value** | Strong evidence against $H_0$. The data are unlikely to be a coincidence |
| **Large p-value** | Weak evidence against $H_0$. The data are consistent with random chance |
| **Alpha ($\alpha$)** | The threshold we set (usually 0.05). If $p < \alpha$, we reject $H_0$ |
| **The Catch** | p-value is **not** the probability that $H_0$ is true. It is the probability of the data *given* $H_0$ |
| **Practical Significance** | A tiny p-value does not mean a huge effect. Always check the effect size! |

---

### The One-Liner to Memorize

> *"The p-value is a measure of surprise, not a measure of truth. It tells us how unlikely our data would be if nothing were really happening. The smaller the p-value, the louder our data screams, 'This is not a coincidence!'"*

### The Score Statistic

To understand the **Score Statistic**, we have to look under the hood of **Maximum Likelihood Estimation (MLE)**.

Remember, the MLE finds the parameter value that makes our data the most likely. The **Score Statistic** is the mathematical "engine" that drives that search. It tells us **which direction to go** and **how steep the hill is** to reach the top of the likelihood mountain.

Here is the intuitive, step-by-step breakdown.

---

### 1. The Intuition: The "Treasure Hunter" on a Hill

Imagine we are blindfolded on a mountain, and we are trying to find the **absolute peak** (the Maximum Likelihood Estimate). We can't see the top, but we can feel the slope beneath our feet.

- If we are standing on the **left side** of the peak, the ground slopes **upward to the right**.
- If we are standing on the **right side** of the peak, the ground slopes **downward to the right**.
- If we are standing **exactly at the peak**, the ground is **perfectly flat** (slope = 0).

The **Score Statistic** is simply a mathematical measurement of that **slope** at any given point.

- It is the **first derivative** (the slope) of the log-likelihood function.

---

### 2. The Mathematical Definition

Let $\ell(\theta)$ be the **log-likelihood function** (the log of the likelihood).

The Score Statistic, often written as $U(\theta)$ or $S(\theta)$, is defined as:

$$U(\theta) = \frac{d}{d\theta} \ell(\theta)$$

**What this tells us:**

| Value of $U(\theta)$ | Meaning |
|---------------------|---------|
| **$U(\theta) > 0$** | The slope is positive. The likelihood increases as $\theta$ increases. We need to move **right** to find the peak. |
| **$U(\theta) < 0$** | The slope is negative. The likelihood decreases as $\theta$ increases. We need to move **left** to find the peak. |
| **$U(\theta) = 0$** | The slope is flat. We have found the **Maximum Likelihood Estimate (MLE)**! |

---

### 3. A Salmon Example (The Score in action)

Let's go back to estimating the sea lice infection rate $p$.

We sample 20 fish and find 4 have lice. The log-likelihood for a Binomial proportion is:

$$\ell(p) = x \log(p) + (n-x) \log(1-p) + \text{constant}$$

The Score statistic (the slope) is the derivative of this with respect to $p$:

$$U(p) = \frac{x}{p} - \frac{n-x}{1-p}$$

---

**Let's test the slope at different guesses for $p$:**

| Guess for $p$ | Calculation | $U(p)$ | Meaning |
|---------------|-------------|--------|---------|
| **$p = 0.10$** | $U(0.10) = \frac{4}{0.10} - \frac{16}{0.90} = 40 - 17.78 = 22.22$ | **Positive** | The hill is still going up to the right. Our guess of 10% is too low; the true MLE is higher. |
| **$p = 0.30$** | $U(0.30) = \frac{4}{0.30} - \frac{16}{0.70} = 13.33 - 22.86 = -9.53$ | **Negative** | The hill is going down to the right. Our guess of 30% is too high; the true MLE is lower. |
| **$p = 0.20$** (The MLE) | $U(0.20) = \frac{4}{0.20} - \frac{16}{0.80} = 20 - 20 = 0$ | **Zero** | We are standing exactly at the peak! This is our MLE. |

---

### 4. The "Score Test" (The Rao Score Test)

The Score Statistic isn't just for finding the MLE; it also forms the basis of a powerful hypothesis test called the **Score Test** (or Rao's Score Test).

| Component | Explanation |
|-----------|-------------|
| **The Problem** | We want to test $H_0: \theta = \theta_0$ |
| **The Logic** | If the null hypothesis is true, the slope ($U(\theta_0)$) should be close to zero. If the slope is extremely steep (very positive or very negative), it means the data is screaming that $\theta_0$ is not the peak, so we should reject $H_0$ |

**The Formula for the Score Test Statistic:**

$$\text{Score Test Statistic} = \frac{U(\theta_0)^2}{\text{Var}(U(\theta_0))}$$

Under the null hypothesis, this statistic follows a **Chi-squared distribution** with 1 degree of freedom.

---

### 5. The "Big Three" Hypothesis Tests (Where the Score fits in)

In statistics, there are three classic tests for evaluating parameters. They are mathematically equivalent in large samples, but they use different "views" of the likelihood:

| Test | What it looks at | The "Treasure Hunter" Analogy |
|------|------------------|-------------------------------|
| **Likelihood Ratio Test (LRT)** | Looks at the *height* of the likelihood mountain | Compares how tall the mountain is at the null hypothesis vs. at the peak |
| **Wald Test** | Looks at the *horizontal distance* from the null to the peak | Measures how far our guess is from the peak in standard errors |
| **Score Test (Rao)** | Looks at the *slope* of the mountain at the null | Checks how steep the hill is at our starting point |

---

### 6. Why use the Score Test?

The Score Test has two massive advantages:

| Advantage | Explanation |
|-----------|-------------|
| **1. It is fast** | We only have to calculate the likelihood under the **null hypothesis** ($\theta_0$). We do not need to find the MLE (the peak). This makes it very computationally efficient, especially in complex models |
| **2. It is invariant** | It often performs better than the Wald test for small sample sizes because it doesn't rely as heavily on a perfect estimate of the variance |

**Salmon Application:**

Imagine we are testing whether a new gene is linked to sea lice resistance in salmon. Fitting the full model (finding the MLE) takes hours of computer time. With the Score Test, we just fit the model *without* the gene (under $H_0$), calculate the slope, and test if that slope is steep enough to reject $H_0$. It saves massive amounts of time!

---

### Summary Cheat Sheet

| Concept | Explanation |
|---------|-------------|
| **Score Statistic $U(\theta)$** | The slope (first derivative) of the log-likelihood at a given parameter value |
| **If $U = 0$** | We are at the MLE (the peak of the likelihood) |
| **If $U > 0$** | The likelihood increases as $\theta$ increases (move right) |
| **If $U < 0$** | The likelihood decreases as $\theta$ increases (move left) |
| **Score Test** | A hypothesis test that uses the steepness of the slope under $H_0$ to decide if the null is plausible |
| **Advantage** | No need to calculate the MLE; fast and computationally efficient |
| **The Analogy** | The Score Statistic is our "slope sensor" on a foggy mountain, telling us exactly which way to walk to find the peak |

---

### The One-Liner to Memorize

> *"The Score Statistic is the slope of the likelihood hill. If the slope at our null hypothesis is steep, the data is screaming that we are nowhere near the peak—so we reject the null."*

## Hypothesis Testing for Binomial Proportions: Wald, Score, and Agresti-Coull

Let's dive into **hypothesis testing for binomial proportions** using the three most common approaches: the **Score Test**, the **Wald Test**, and the **Agresti-Coull Interval**.

We'll use a consistent example throughout: We sample **100 fish** and find **40 have sea lice**. We want to test if the true infection rate is **50%** ($H_0: p = 0.5$).

---

### Part 1: The Wald Test (The "Standard" but Flawed Test)

The Wald test is the most straightforward. It uses the sample proportion $\hat{p} = x/n$ and its standard error, calculated *at the estimated proportion*.

**The Logic:** How many standard errors is our observed $\hat{p}$ away from the null value $p_0$?

**The Formula:**

$$Z_{Wald} = \frac{\hat{p} - p_0}{\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}}$$

---

**Our Example:**

| Component | Value |
|-----------|-------|
| $\hat{p}$ | $40/100 = 0.40$ |
| $p_0$ | 0.50 |
| Standard Error | $SE = \sqrt{0.40 \times 0.60 / 100} = \sqrt{0.0024} \approx 0.049$ |
| Test Statistic | $Z = \frac{0.40 - 0.50}{0.049} \approx -2.04$ |

**The Result:** The two-sided p-value is $2 \times P(Z < -2.04) \approx 0.041$. At $\alpha = 0.05$, we **reject** $H_0$.

**The Catch (The "Wald" Problem):**

The Wald test uses $\hat{p}$ in the standard error. If $p$ is near 0 or 1, or if $n$ is small, the standard error is poorly estimated. It also fails completely if $\hat{p} = 0$ (it gives a zero standard error).

---

### Part 2: The Score Test (Rao's Test – The "Gold Standard")

The Score test fixes the Wald test's flaw by calculating the standard error **under the null hypothesis** ($p_0$), not under the estimate.

**The Logic:** *"If the null is true, how much 'slope' or 'score' do we have pulling us away from it?"*

**The Formula:**

$$Z_{Score} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1-p_0)}{n}}}$$

---

**Our Example:**

| Component | Value |
|-----------|-------|
| $\hat{p}$ | 0.40 |
| $p_0$ | 0.50 |
| Standard Error under $H_0$ | $SE_0 = \sqrt{0.50 \times 0.50 / 100} = \sqrt{0.0025} = 0.05$ |
| Test Statistic | $Z = \frac{0.40 - 0.50}{0.05} = -2.0$ |

**The Result:** The two-sided p-value is $2 \times P(Z < -2.0) \approx 0.0455$. We still reject $H_0$, but the test statistic is slightly different from the Wald test.

**Why the Score Test is better:**

It is more reliable for small samples and extreme probabilities. It is the foundation of the **Wilson Confidence Interval** (which we will see in a moment).

---

### Part 3: The Agresti-Coull Interval (The "Quick Fix")

The **Agresti-Coull interval** is a simple modification of the Wald interval that makes it perform almost as well as the Wilson (Score) interval, without the complex formula.

**The Logic:** We add **2 successes** and **2 failures** to our data (the "Plus-Four" rule), then use the Wald formula.

**The Adjusted Numbers:**

$$\tilde{n} = n + 4 = 104$$

$$\tilde{p} = \frac{x + 2}{n + 4} = \frac{40 + 2}{104} = \frac{42}{104} \approx 0.4038$$

**The 95% Confidence Interval Formula:**

$$\tilde{p} \pm 1.96 \times \sqrt{\frac{\tilde{p}(1-\tilde{p})}{\tilde{n}}}$$

---

**Our Example:**

| Component | Value |
|-----------|-------|
| $\tilde{p}$ | 0.4038 |
| Standard Error | $SE = \sqrt{0.4038 \times 0.5962 / 104} = \sqrt{0.00231} \approx 0.0481$ |
| Margin of Error | $1.96 \times 0.0481 \approx 0.0943$ |

**The Interval:**

$$0.4038 \pm 0.0943 = [0.3095, \ 0.4981]$$

**Interpretation:** We are 95% confident that the true infection rate is between **31.0% and 49.8%**. Since 0.50 falls *just outside* the upper bound, it confirms the result of the hypothesis test (reject $H_0$).

---

### Side-by-Side Summary Table

| Test/Interval | Formula | Standard Error uses... | Performance | When to use |
| :--- | :--- | :--- | :--- | :--- |
| **Wald Test / CI** | $\hat{p} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ | The estimated $\hat{p}$ | **Unreliable** for small $n$ or $p$ near 0/1. Sometimes gives impossible bounds (<0 or >1) | Quick, rough estimates with large $n$ and $p$ around 0.5 |
| **Score Test / Wilson CI** | Complex (solve for $p$ where | $\hat{p}-p$ | $\leq z \sqrt{p(1-p)/n}$) | The null $p_0$ (for testing) or solves for $p$ (for CI) | **Excellent.** Works well for any $n$ and any $p$. Never gives impossible bounds | The **gold standard** for proportions. Use in scientific reporting |
| **Agresti-Coull CI** | $\tilde{p} \pm z \sqrt{\frac{\tilde{p}(1-\tilde{p})}{\tilde{n}}}$, with $\tilde{p} = \frac{x+2}{n+4}$ | The adjusted $\tilde{p}$ | **Very Good.** A simple hack that mimics the Wilson interval perfectly | Great for teaching, quick hand calculations, or when we want a simple formula that actually works |

---

### The Ultimate Recommendation

1. **For Hypothesis Testing:** Use the **Score Test**. It controls the Type I error rate much better than the Wald test, especially when $p$ is near 0 or 1.

2. **For Confidence Intervals:** Use the **Wilson Interval** (the inverted Score test) or the **Agresti-Coull** interval. **Never** use the Wald interval for proportions in practice—it is dangerously misleading for small samples.

---

### The One-Liner to Memorize

> *"The Wald test gambles by guessing the variance from the data; the Score test plays it safe by using the null hypothesis. And if we want a confidence interval that actually works, use the Wilson method or the Agresti-Coull quick-fix—never trust the Wald interval for proportions!"*

## Pearson Interval and Clopper-Pearson Interval
### The Pearson Interval (The "Classic" Wald Interval)

**What it is:**

This is the standard, textbook interval we learn in introductory statistics. It is also called the Wald Interval (named after Abraham Wald). It uses the Normal approximation to the Binomial distribution.

**The Formula:**

$$\hat{p} \pm Z_{1-\alpha/2} \times \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Salmon Example ($n = 20$, $x = 4$, $\hat{p} = 0.20$):**

$$SE = \sqrt{0.20 \times 0.80 / 20} = 0.089$$

$$95\% \text{ CI: } 0.20 \pm 1.96 \times 0.089 = 0.20 \pm 0.175$$

**Result:** $[0.025, 0.375]$

---

**The Pros:**

- Incredibly easy to calculate by hand.
- Works fine if $n$ is huge (e.g., $> 100$) and $p$ is not near 0 or 1.

**The Cons (The "Pearson" Problem):**

- It is based on the Central Limit Theorem, which assumes $n$ is large.
- If $p$ is near 0 or 1, or if $n$ is small, the Normal approximation breaks down.
- **Worst Offense:** It can produce impossible intervals. If we have 0 successes out of 10 ($\hat{p} = 0$), the Wald interval gives $0 \pm 0$, which is $[0, 0]$. This says we are 100% certain the true proportion is zero—which is statistically nonsense!

---

### The Clopper-Pearson Interval (The "Exact" Interval)

**What it is:**

Named after Charles Clopper and Egon Pearson (Karl Pearson's son), this is the **exact** binomial interval. Instead of using a Normal approximation, it uses the actual Binomial distribution to find two values of $p$ that satisfy a strict probability statement.

**The Philosophy:**

It finds a lower bound $p_L$ and an upper bound $p_U$ such that:

$$P(X \geq x \mid p = p_L) = \alpha/2 \quad \text{and} \quad P(X \leq x \mid p = p_U) = \alpha/2$$

**In plain English:**

- The lower bound $p_L$ is the value of $p$ where observing $x$ or more successes becomes too unlikely (only 2.5% chance).
- The upper bound $p_U$ is the value of $p$ where observing $x$ or fewer successes becomes too unlikely (only 2.5% chance).

**Salmon Example ($n = 20$, $x = 4$):**

Using the Clopper-Pearson method (which requires looking up the F-distribution or using software):

$$95\% \text{ CI: Approximately } [0.064, 0.414]$$

**Notice:** This interval is **wider** than the Pearson interval ($[0.025, 0.375]$). It is shifted upward and is asymmetric.

---

**The Pros:**

- It is **exact**. It guarantees that the true coverage probability is at least 95% for any sample size and any value of $p$.
- It never produces impossible bounds (it will never go below 0 or above 1).

**The Cons (The "Clopper-Pearson" Problem):**

- It is **conservative** (overly wide). Because it uses discrete binomial probabilities, it forces the coverage to be at least 95%, which often means it is actually greater than 95%.
- For small samples, this interval can be ridiculously wide. (If we flip a coin 3 times and get 0 heads, the 95% Clopper-Pearson CI for the true probability of heads is $[0, 0.708]$—a massive range!).

---

### The Side-by-Side Showdown

Let's compare them head-to-head for our salmon data ($n = 20$, $x = 4$):

| Feature | Pearson (Wald) Interval | Clopper-Pearson Interval |
| :--- | :--- | :--- |
| **Method** | Normal approximation to the Binomial | Exact Binomial calculation |
| **Formula** | $\hat{p} \pm z \times SE$ | Uses the F-distribution or Beta quantiles |
| **95% CI for n=20, x=4** | $[0.025, 0.375]$ | $[0.064, 0.414]$ |
| **Coverage Guarantee** | Approximate (only works well if $n$ is large) | **Exact** (guarantees at least 95% coverage) |
| **Can it go below 0 or above 1?** | Yes (e.g., if $x = 0$, gives $[0, 0]$) | **No.** It respects the $[0, 1]$ bounds |
| **Is it symmetric?** | Symmetric around $\hat{p}$ | **Asymmetric** (accounts for skewness) |
| **Best for...** | Quick, large-sample back-of-the-envelope calculations | Scientific reporting, small samples, or when $p$ is near 0 or 1 |

---

### The "Practical" Truth (What to actually use)

**Forget the Pearson (Wald) interval for proportions.** It is dangerously misleading for small samples or extreme probabilities. Many statisticians argue it should never be taught.

| Recommendation | Method | Why |
| :--- | :--- | :--- |
| **Default** | **Wilson (Score) interval** | Excellent compromise: simple enough to compute, gives good coverage, and never goes outside $[0, 1]$ |
| **When you need an exact guarantee** | **Clopper-Pearson interval** | For regulatory submissions (e.g., FDA) or reporting serious health risks. Just be aware it is intentionally conservative (wide) |

---

### The Connection to the Beta Distribution

Here is a beautiful piece of math that ties everything together:

The Clopper-Pearson interval is exactly the Bayesian Credible Interval we get when we use the **Beta(0.5, 0.5) prior** (Jeffreys' prior) and then force it to have frequentist coverage properties!

$$\text{Beta}(0.5, 0.5) + \text{Data} \rightarrow \text{Beta}(0.5 + x, 0.5 + n - x)$$

The quantiles of this posterior distribution give us the exact Clopper-Pearson bounds!

---

### The One-Liner to Memorize

> *"The Pearson (Wald) interval is dangerously misleading for small samples or extreme proportions. Use the Clopper-Pearson interval when you need an exact guarantee, but for everyday use, the Wilson (Score) interval is the gold standard—it never gives impossible bounds and works for any sample size!"*

## Bayesian and likelihood inference for two binomial proportions


To understand **Bayesian and likelihood inference for two binomial proportions**, we are moving from the "Frequentist" world (p-values, Z-tests, and confidence intervals) into the **likelihood** and **Bayesian** frameworks.

Instead of asking *"What is the probability of seeing this data if the null is true?"*, we ask: **"Given the data we observed, what is the relative plausibility of different values for the true difference between the two proportions?"**

We will stick with our salmon example:

| Group | Sample Size | Lice Count | Proportion |
| :--- | :--- | :--- | :--- |
| **Group 1 (Old Feed)** | $n_1 = 100$ | $x_1 = 40$ | $\hat{p}_1 = 0.40$ |
| **Group 2 (New Feed)** | $n_2 = 120$ | $x_2 = 36$ | $\hat{p}_2 = 0.30$ |

**Parameter of interest:** The true difference $\delta = p_1 - p_2$.

Let's break down how **Likelihood** and **Bayesian** inference handle this.

---

### Part 1: Likelihood Inference (The "Pure Data" Approach)

Likelihood inference is the bridge between Frequentist and Bayesian. It uses only the data to create a **likelihood function** for the parameter $\delta$, without using prior beliefs.

**Step 1: Write the Likelihood**

For two independent binomial groups, the likelihood is the product of the two individual binomial likelihoods:

$$\mathcal{L}(p_1, p_2) \propto p_1^{x_1} (1-p_1)^{n_1 - x_1} \times p_2^{x_2} (1-p_2)^{n_2 - x_2}$$

**Step 2: Profile Likelihood for $\delta = p_1 - p_2$**

We don't care about the individual $p_1$ and $p_2$; we care about their **difference** $\delta$.

To get the likelihood for $\delta$ alone, we use the **Profile Likelihood**. For every possible value of $\delta$, we mathematically "maximize out" $p_1$ and $p_2$ to find the absolute highest likelihood.

**Step 3: The Profile Likelihood Curve**

If we plot this profile likelihood against $\delta$, we get a curve that:
- Peaks at $\hat{\delta} = \hat{p}_1 - \hat{p}_2 = 0.10$ (the MLE).
- Falls off as $\delta$ moves away from 0.10.

**The Likelihood Ratio Test (LRT):**

To test $H_0: \delta = 0$, we compare the height of the likelihood at $\delta = 0$ to the height at the peak ($\delta = 0.10$):

$$\text{Likelihood Ratio} = \frac{\mathcal{L}(\delta = 0)}{\mathcal{L}(\delta = \hat{\delta})}$$

- If this ratio is very small (i.e., the likelihood at 0 is much lower than at the peak), we reject $H_0$.
- In large samples, $-2 \log(\text{Likelihood Ratio})$ follows a Chi-squared distribution (giving us a p-value).

**The "Likelihood Interval" (Similar to a CI):**

A 95% likelihood-based confidence interval is the set of $\delta$ values for which:

$$-2 \log\left( \frac{\mathcal{L}(\delta)}{\mathcal{L}(\hat{\delta})} \right) < 3.84$$

(This is the Chi-squared 1 df critical value).

**Result:** For our salmon data, the profile likelihood interval for $\delta = p_1 - p_2$ is approximately **[-0.025, 0.225]**.

**Interpretation:** This is very close to the Agresti-Caffo interval we calculated earlier. It does not contain 0, so we fail to reject the null (no significant difference).

---

### Part 2: Bayesian Inference (Updating with Priors)

Bayesian inference adds a **prior distribution** to the mix. For two binomial proportions, the **conjugate prior** is the Beta distribution.

**Step 1: Choose Priors for $p_1$ and $p_2$**

| Prior Type | Distribution | Description |
| :--- | :--- | :--- |
| **Non-informative (Jeffreys) prior** | $p_1 \sim \text{Beta}(0.5, 0.5)$ and $p_2 \sim \text{Beta}(0.5, 0.5)$ | Lets the data speak entirely for itself |
| **Informative prior** | $p_1 \sim \text{Beta}(10, 90)$ | Belief that the old feed has ~10% infection rate (based on historical data) |

**Step 2: Calculate the Posterior**

Because the Beta is conjugate to the Binomial, the posterior for each proportion is just:

- $p_1 \mid \text{data} \sim \text{Beta}(\alpha_1 + x_1, \ \beta_1 + n_1 - x_1)$
- $p_2 \mid \text{data} \sim \text{Beta}(\alpha_2 + x_2, \ \beta_2 + n_2 - x_2)$

For Jeffreys prior ($\alpha = \beta = 0.5$):

- Posterior for $p_1$: Beta(40.5, 60.5)
- Posterior for $p_2$: Beta(36.5, 84.5)

**Step 3: Get the Posterior for $\delta = p_1 - p_2$**

This is the tricky part. The difference of two Beta distributions does not have a simple closed-form formula.

**How we do it today (MCMC):**

We use a computer to take **thousands of random draws** from the posterior of $p_1$ and $p_2$, subtract them, and plot the histogram of the differences. This histogram is the **posterior distribution of $\delta$**.

**Step 4: The Bayesian Credible Interval**

We look at the histogram of $\delta$ and find the 2.5th percentile and the 97.5th percentile.

**Result (Using Jeffreys prior):**

The 95% credible interval for $\delta$ is approximately **[-0.023, 0.223]**.

**Interpretation:**

We can say: *"There is a 95% probability that the true difference in infection rates is between -2.3% and 22.3%."*

*(Notice: this is a direct probabilistic statement, which is strictly forbidden in Frequentist statistics!)*

---

### Part 3: The Grand Comparison (Frequentist vs. Likelihood vs. Bayesian)

Let's put all three side-by-side for the same salmon data:

| Method | Interval for $\delta = p_1 - p_2$ | Interpretation |
| :--- | :--- | :--- |
| **Frequentist (Agresti-Caffo)** | [-0.0265, 0.2239] | *"If we repeated this experiment infinitely, 95% of these intervals would contain the true $\delta$."* |
| **Likelihood (Profile)** | [-0.025, 0.225] | *"These are the values of $\delta$ most compatible with the data."* |
| **Bayesian (Jeffreys Prior)** | [-0.023, 0.223] | *"There is a 95% **probability** that $\delta$ lies in this range."* (The most intuitive!) |

---

### The Role of the Prior (The Bayesian Superpower)

Here is where Bayesian inference shines (and gets criticized).

| Prior Type | Effect | Result |
| :--- | :--- | :--- |
| **Jeffreys Prior (Beta(0.5, 0.5))** | Almost identical to likelihood/Frequentist intervals | The data completely drives the result |
| **Strong Informative Prior** | Imagine 10 years of data showing the old feed has a 10% infection rate. Use $p_1 \sim \text{Beta}(50, 450)$ | The prior "pulls" the estimate of $p_1$ toward 0.10. The resulting credible interval for $\delta$ might shrink and shift, perhaps becoming **[-0.05, 0.12]** |

**The Bayesian Superpower:** We are now formally combining historical knowledge with new data!

---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **Likelihood Inference** | Uses the profile likelihood to find plausible values of $\delta$. No priors | Profile likelihood interval: [-0.025, 0.225] |
| **Bayesian Inference** | Uses priors + data = posterior. Gives direct probability statements | Posterior for $p_1$: Beta(40.5, 60.5) |
| **Jeffreys Prior** | A non-informative prior (Beta(0.5, 0.5)). Lets data speak | Credible interval: [-0.023, 0.223] |
| **Informative Prior** | Uses real prior knowledge (e.g., historical data) | Shrinks the interval toward historical values |
| **The Key Difference** | Frequentist = "Long-run coverage." Bayesian = "Direct probability of the parameter" | Bayesian gives the intuitive answer most people actually want! |

---

### The One-Liner to Memorize

> *"Likelihood inference listens only to the data; Bayesian inference combines the data with prior knowledge. When we use a non-informative prior, they shake hands and give nearly identical results—but only Bayesian allows us to say, 'There is a 95% chance the true difference lies in this interval.'"*

## Monte Carlo Simulation for Bayesian Inference

Ah, we are asking about the **engine** that makes modern Bayesian statistics actually work!

If the Beta-Binomial model is the *recipe* (Prior + Data = Posterior), then **Monte Carlo simulation** is the *oven* that bakes the cake.

When we have two independent Beta posteriors (like $p_1 \sim \text{Beta}(40.5, 60.5)$ and $p_2 \sim \text{Beta}(36.5, 84.5)$), the math to figure out the difference ($\delta = p_1 - p_2$) by hand is nearly impossible.

**Monte Carlo simulation is the brute-force trick we use to approximate the posterior distribution without doing any advanced calculus.**

---

### Part 1: What is Monte Carlo Simulation? (The Intuition)

The name "Monte Carlo" comes from the famous casino in Monaco. It is all about **using random numbers** to solve problems that are too hard to solve with pure math.

Imagine we want to know the probability of winning a very complicated card game. Instead of calculating the exact probability (which might take a genius years to figure out), we simply **play the game 1,000,000 times** on a computer and count how many times we win.

That is Monte Carlo simulation: *"If we can't calculate the answer, we will just simulate it a million times and look at the histogram."*

---

### Part 2: How we use Monte Carlo for Bayesian Inference (The Step-by-Step)

Let's walk through the exact computer code (in our head) for our salmon example.

**The Goal:** Find the 95% credible interval for the true difference in infection rates ($\delta = p_1 - p_2$).

**The Inputs:**
- Posterior for the Old Feed: $p_1 \sim \text{Beta}(40.5, 60.5)$
- Posterior for the New Feed: $p_2 \sim \text{Beta}(36.5, 84.5)$

---

**The Monte Carlo Algorithm:**

| Step | Action | Example Draw |
| :--- | :--- | :--- |
| **1** | Draw a random value from Beta(40.5, 60.5) | $p_1 = 0.41$ |
| **2** | Independently, draw a random value from Beta(36.5, 84.5) | $p_2 = 0.29$ |
| **3** | Calculate the difference | $\delta = 0.41 - 0.29 = 0.12$ |
| **4** | Write down this number | $0.12$ |
| **5** | Repeat Steps 1–4 a massive number of times | Do this 10,000 or 100,000 times |

**The Result:**

We now have 100,000 different values of $\delta$ written down. We sort them from smallest to largest.

- To find the 95% credible interval, we look at the **2.5th percentile** (the 2,500th smallest value) and the **97.5th percentile** (the 97,500th smallest value).
- The computer spits out: **[-0.023, 0.223]**.

---

### Part 3: Why do we use Monte Carlo instead of math?

In our simple Beta-Binomial example, we *could* technically calculate the distribution of the difference using calculus (it involves a complex integral called the "Beta-binomial convolution").

But in **real-world Bayesian statistics**:

| Challenge | Why Monte Carlo Helps |
| :--- | :--- |
| **10 different parameters, not just 2** | Monte Carlo scales easily to high dimensions |
| **Weird prior that isn't a neat Beta distribution** | Monte Carlo works for any prior |
| **Hierarchical model** (infection rate depends on water temperature and fish age) | Monte Carlo handles complex dependencies |

In those cases, the math is **impossible** to solve by hand. Monte Carlo simulation is the universal hammer that smashes through these complex problems.

---

### Part 4: The Difference between Monte Carlo and MCMC

This is a crucial distinction that often confuses students:

| Method | When do we use it? | How it works |
| :--- | :--- | :--- |
| **Monte Carlo (Direct Sampling)** | When we can easily draw independent samples directly from the posterior | We just tell the computer to draw random numbers from a known distribution (like Beta). It is fast and perfectly accurate |
| **Markov Chain Monte Carlo (MCMC)** | When the posterior is too weird to sample from directly | The computer takes a "random walk" through the parameter space, gradually building a histogram of the posterior. It takes longer, but it handles insane complexity |

**In our Beta-Binomial example:** We use **Direct Monte Carlo** because the Beta distribution is built into every statistical software. We just hit "draw random sample" and go.

**In complex models:** We use **MCMC** (e.g., software like JAGS, Stan, or PyMC) to simulate the posterior.

---

### Part 5: Seeing the Law of Large Numbers in Action (Asymptotics!)

Remember the **Law of Large Numbers** we discussed? It applies perfectly here!

| Number of Draws | Result | Quality |
| :--- | :--- | :--- |
| **10 draws** | Wildly inaccurate (e.g., [-0.10, 0.35]) | **Useless** |
| **10,000 draws** | Stabilizes to [-0.023, 0.223] | **Good** |
| **1,000,000 draws** | Exactly the same as the math would give us | **Perfect** |

The LLN guarantees that as our number of Monte Carlo draws goes to infinity, our simulated histogram converges perfectly to the true mathematical posterior distribution.

---

### Summary Cheat Sheet

| Concept | Explanation | Salmon Example |
| :--- | :--- | :--- |
| **Monte Carlo Simulation** | Using random draws to approximate a complex distribution | Drawing 100,000 values from Beta(40.5, 60.5) and Beta(36.5, 84.5) |
| **Direct Sampling** | Sampling directly from a known distribution | Using a computer's built-in `rbeta()` function |
| **The Difference ($\delta$)** | Subtract each draw of $p_1$ from each draw of $p_2$ | 100,000 values of $p_1 - p_2$ |
| **The 95% Credible Interval** | The 2.5th and 97.5th percentiles of the simulated differences | [-0.023, 0.223] |
| **The Law of Large Numbers** | As we increase the number of simulations, our answer gets more precise | 10 draws = useless; 1,000,000 draws = perfect |

---

### The One-Liner to Memorize

> *"Monte Carlo simulation replaces impossible calculus with brute-force random numbers. Instead of solving a complex integral for the difference of two Betas, we just draw a million random samples from each, subtract them, and look at the histogram."*

## Relative Risk and Odds Ratios

To understand **Relative Risk** and **Odds Ratios**, we have to go back to the salmon farm and look at a **2x2 contingency table**.

We want to know: *Does the new feed reduce the risk of sea lice?*

These two numbers—Relative Risk and Odds Ratios—are the standard tools for answering this. They both measure the **strength of association** between an exposure (New Feed) and an outcome (Sea Lice). However, they do it in completely different ways, and one is vastly more popular in medical research.

Here is the definitive guide.

---

### The Setup: A 2x2 Contingency Table

We run a trial with 100 fish on the old feed and 100 fish on the new feed. Here are the results:

| | **Sea Lice (Disease)** | **No Sea Lice (No Disease)** | **Total** |
| :--- | :--- | :--- | :--- |
| **Old Feed (Exposed)** | 40 (a) | 60 (b) | 100 (a+b) |
| **New Feed (Unexposed)** | 20 (c) | 80 (d) | 100 (c+d) |

- **Risk (Incidence) in Old Feed:** $40/100 = 0.40$ (40%)
- **Risk (Incidence) in New Feed:** $20/100 = 0.20$ (20%)

---

### Part 1: Relative Risk (The "Risk Ratio")

**Definition:** Relative Risk (RR) is the **ratio** of the risk of an event happening in the exposed group compared to the unexposed group.

**The Formula:**

$$RR = \frac{\text{Risk in Exposed}}{\text{Risk in Unexposed}} = \frac{a / (a+b)}{c / (c+d)}$$

**Salmon Example:**

$$RR = \frac{40 / 100}{20 / 100} = \frac{0.40}{0.20} = 2.0$$

**Interpretation:**

Fish on the old feed are **2.0 times more likely** to get sea lice than fish on the new feed. Alternatively, the new feed cuts the risk in half (since $1 - 0.50 = 50\%$ reduction).

**The Golden Rule of RR:**

| RR Value | Meaning |
| :--- | :--- |
| **RR = 1** | No association. The exposure does not affect risk |
| **RR > 1** | The exposure **increases** risk (risk factor) |
| **RR < 1** | The exposure **decreases** risk (protective factor) |

**The Catch:** Relative Risk is **only valid** in prospective studies (cohort studies, clinical trials) where we follow people forward in time. It does not work in retrospective studies (case-control studies) because we artificially fix the number of cases, so we can't calculate the true risk.

---

### Part 2: Odds Ratio (The "Cross-Product" Ratio)

**Definition:** An Odds Ratio (OR) is the ratio of the **odds** of an event happening in one group to the odds of it happening in another group.

*Remember:* Odds = $\frac{\text{Probability of happening}}{\text{Probability of not happening}}$.

**The Formula:**

$$\text{Odds in Exposed} = \frac{a}{b}, \quad \text{Odds in Unexposed} = \frac{c}{d}$$

$$OR = \frac{a / b}{c / d} = \frac{a \times d}{b \times c}$$

**Salmon Example:**

- Odds of lice on **Old Feed**: $40 / 60 = 0.667$
- Odds of lice on **New Feed**: $20 / 80 = 0.25$
- **Odds Ratio:** $0.667 / 0.25 = \mathbf{2.67}$

**Interpretation:**

The odds of having sea lice are **2.67 times higher** on the old feed compared to the new feed.

**The Golden Rule of OR:**

| OR Value | Meaning |
| :--- | :--- |
| **OR = 1** | No association |
| **OR > 1** | The exposure is associated with **higher odds** of the outcome |
| **OR < 1** | The exposure is associated with **lower odds** of the outcome |

---

### Part 3: Relative Risk vs. Odds Ratio (The Showdown)

Here is where it gets tricky. For rare diseases (e.g., less than 10% incidence), the Odds Ratio is a **very good approximation** of the Relative Risk.

In our example, the incidence was 40% and 20% (not rare). Notice the difference:

| Measure | Value |
| :--- | :--- |
| **Relative Risk** | 2.0 |
| **Odds Ratio** | 2.67 |

They are different! The OR is always "further from 1" than the RR.

| Feature | Relative Risk (RR) | Odds Ratio (OR) |
| :--- | :--- | :--- |
| **What it calculates** | Ratio of *probabilities* (risks) | Ratio of *odds* (not probabilities) |
| **Range** | 0 to infinity | 0 to infinity |
| **Interpretation** | Intuitive: "X times more likely to happen" | Counterintuitive: "X times higher odds" (Most people don't think in odds) |
| **When is it used?** | Randomized trials, cohort studies | **Case-control studies** (retrospective) |
| **When does OR ≈ RR?** | Only when the disease is **rare** (<10%) | Always, but approximates RR when rare |
| **The "Constant" Rule** | RR is a direct comparison | OR is **asymmetric**—the OR of disease vs. non-disease is the same, but RR is not |

---

### Part 4: The "Rare Disease" Rule (Crucial!)

Imagine sea lice is rare (say, 2% vs. 1%).

- **Risk:** $0.02 / 0.01 = \mathbf{RR = 2.0}$
- **Odds:** $(0.02/0.98) / (0.01/0.99) \approx \mathbf{OR = 2.02}$

**When the outcome is rare, OR ≈ RR.** This is why medical researchers love the OR: they study rare diseases using case-control designs, and the OR gives them a perfect estimate of the RR without having to do a massive, expensive trial.

---

### Part 5: Why does the Odds Ratio dominate statistics? (Logistic Regression)

We will see Odds Ratios everywhere in advanced statistics (like Logistic Regression). Why?

| Reason | Explanation |
| :--- | :--- |
| **1. Symmetry** | The OR is "symmetric." The OR of getting the disease is $a \times d / (b \times c)$. The OR of *not* getting the disease is $b \times c / (a \times d)$. They are just reciprocals. This makes it mathematically elegant |
| **2. No Bounds on Odds** | Odds can range from 0 to infinity without being restricted by probability boundaries. This allows statisticians to use the **logit** transformation ($\log(\text{odds})$), which forms the backbone of logistic regression, without worrying about probabilities going below 0 or above 1 |

---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example | Interpretation |
| :--- | :--- | :--- | :--- |
| **Relative Risk (RR)** | $\frac{\text{Risk in Exposed}}{\text{Risk in Unexposed}}$ | $0.40 / 0.20 = 2.0$ | Old feed = **2.0 times more likely** to get lice |
| **Odds Ratio (OR)** | $\frac{\text{Odds in Exposed}}{\text{Odds in Unexposed}} = \frac{a \times d}{b \times c}$ | $40 \times 80 / (60 \times 20) = 2.67$ | Odds of lice are **2.67 times higher** on old feed |
| **When to use RR** | Cohort studies, clinical trials | Testing a new feed prospectively | - |
| **When to use OR** | Case-control studies, Logistic Regression | Retrospectively comparing fish with/without lice to see which feed they ate | - |
| **The Golden Rule** | If the disease is **rare**, OR ≈ RR | If 1% vs. 2% infection, OR ≈ 2.0 | - |

---

### The One-Liner to Memorize

> *"Relative Risk tells us how much more **likely** something is to happen; Odds Ratios tell us how much higher the **odds** are. For rare events, they are almost identical—but only the Odds Ratio can be used in case-control studies and logistic regression."*

## Standard Error and Confidence Intervals for Log Odds Ratio and Log Relative Risk

To understand the **standard error and confidence intervals for the log Odds Ratio (OR) and log Relative Risk (RR)**, we have to tackle a fundamental problem: **These ratios are not Normally distributed.**

- An Odds Ratio can range from 0 to $\infty$.
- It is highly skewed. An OR of 2.0 (showing increased risk) and an OR of 0.5 (showing decreased risk) are mathematically symmetric *on the log scale*, but they are not symmetric on the raw scale.

**The Fix:** We do all our math on the **natural log (ln) scale**, calculate the standard error and confidence interval there, and then **exponentiate** (take $e^{\text{bound}}$) the final bounds to get back to the interpretable OR/RR scale.

Here is the exact step-by-step guide.

---

### Part 1: The Setup (The 2x2 Table)

Let's use our salmon data comparing the old feed to the new feed:

| | **Lice (Disease)** | **No Lice** | **Total** |
| :--- | :--- | :--- | :--- |
| **Old Feed** | 40 (a) | 60 (b) | 100 |
| **New Feed** | 20 (c) | 80 (d) | 100 |

- **Risk Old:** $p_1 = 40/100 = 0.40$
- **Risk New:** $p_2 = 20/100 = 0.20$
- **Odds Old:** $40/60 = 0.667$
- **Odds New:** $20/80 = 0.25$

---

### Part 2: Standard Error and CI for the Log Odds Ratio (OR)

**Step 1: Calculate the Odds Ratio.**

$$OR = \frac{a \times d}{b \times c} = \frac{40 \times 80}{60 \times 20} = \frac{3200}{1200} = 2.67$$

**Step 2: Calculate the log(OR).**

$$\log(OR) = \log(2.67) \approx 0.982$$

**Step 3: Calculate the Standard Error of the log(OR).**

This is a beautiful, simple formula (developed by Woolf). The variance of the log(OR) is simply the sum of the reciprocals of the four cell counts:

$$SE(\log OR) = \sqrt{ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} }$$

Plug in our numbers:

$$SE(\log OR) = \sqrt{ \frac{1}{40} + \frac{1}{60} + \frac{1}{20} + \frac{1}{80} }$$

$$SE(\log OR) = \sqrt{ 0.025 + 0.0167 + 0.05 + 0.0125 } = \sqrt{0.1042} \approx 0.323$$

**Step 4: Build the 95% Confidence Interval on the log scale.**

$$\log(OR) \pm 1.96 \times SE(\log OR)$$

$$0.982 \pm 1.96(0.323) = 0.982 \pm 0.633$$

- **Lower log bound:** $0.982 - 0.633 = 0.349$
- **Upper log bound:** $0.982 + 0.633 = 1.615$

**Step 5: Exponentiate to get back to the Odds Ratio scale.**

- **Lower bound:** $e^{0.349} \approx 1.42$
- **Upper bound:** $e^{1.615} \approx 5.03$

**Final 95% CI for OR:** **$[1.42, 5.03]$**

**Interpretation:** We are 95% confident that the true odds of sea lice on the old feed are between **1.42 and 5.03 times higher** than on the new feed. Since this interval does not contain 1.0, it is statistically significant.

---

### Part 3: Standard Error and CI for the Log Relative Risk (RR)

The RR is slightly trickier because it involves dividing two probabilities, but the logic is identical.

**Step 1: Calculate the Relative Risk.**

$$RR = \frac{a / (a+b)}{c / (c+d)} = \frac{40/100}{20/100} = 2.0$$

**Step 2: Calculate the log(RR).**

$$\log(RR) = \log(2.0) \approx 0.693$$

**Step 3: Calculate the Standard Error of the log(RR).**

The variance of the log(RR) is a bit more complex because it depends on the probabilities:

$$SE(\log RR) = \sqrt{ \frac{1 - p_1}{n_1 \times p_1} + \frac{1 - p_2}{n_2 \times p_2} }$$

Where $p_1$ and $p_2$ are the risks in the two groups.

Plug in our numbers:

$$SE(\log RR) = \sqrt{ \frac{1 - 0.40}{100 \times 0.40} + \frac{1 - 0.20}{100 \times 0.20} }$$

$$SE(\log RR) = \sqrt{ \frac{0.60}{40} + \frac{0.80}{20} } = \sqrt{ 0.015 + 0.04 } = \sqrt{0.055} \approx 0.2345$$

**Step 4: Build the 95% CI on the log scale.**

$$0.693 \pm 1.96(0.2345) = 0.693 \pm 0.460$$

- **Lower log bound:** $0.693 - 0.460 = 0.233$
- **Upper log bound:** $0.693 + 0.460 = 1.153$

**Step 5: Exponentiate.**

- **Lower bound:** $e^{0.233} \approx 1.26$
- **Upper bound:** $e^{1.153} \approx 3.17$

**Final 95% CI for RR:** **$[1.26, 3.17]$**

**Interpretation:** We are 95% confident that the true risk of sea lice on the old feed is between **1.26 and 3.17 times higher** than on the new feed.

---

### Part 4: Why the Odds Ratio CI is wider than the RR CI

Look at the intervals:

| Measure | 95% CI | Width |
| :--- | :--- | :--- |
| **Odds Ratio (OR)** | $[1.42, 5.03]$ | 3.61 |
| **Relative Risk (RR)** | $[1.26, 3.17]$ | 1.91 |

The OR interval is much wider and more skewed. This is because the OR is always more extreme than the RR when the disease is common (like 20% and 40%). If sea lice were a rare disease (say, 2% and 1%), the OR and RR would be almost identical, and their CIs would look the same.

---

### Summary Cheat Sheet

| Measure | Formula for SE (on the log scale) | 95% CI (on log scale) | Final CI (Exponentiate) |
| :--- | :--- | :--- | :--- |
| **Odds Ratio (OR)** | $\sqrt{ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} }$ | $\log(OR) \pm 1.96 \times SE$ | $e^{\text{lower}}, e^{\text{upper}}$ |
| **Relative Risk (RR)** | $\sqrt{ \frac{1-p_1}{n_1 p_1} + \frac{1-p_2}{n_2 p_2} }$ | $\log(RR) \pm 1.96 \times SE$ | $e^{\text{lower}}, e^{\text{upper}}$ |
| **The Golden Rule** | **Always** do the math on the **log scale** first | Add/subtract the margin on the log scale | **Exponentiate** the bounds to get the final interval. If the interval contains **1**, the result is not significant |

---

### The One-Liner to Memorize

> *"Odds Ratios and Relative Risks are highly skewed. To build a proper confidence interval, we must convert them to logs, calculate the standard error, add/subtract 1.96, and then exponentiate the bounds. If the final interval doesn't contain 1, we have a significant result."*

## The Delta Method: The Grand Unification of Asymptotic Statistics

This is the **grand unification** of asymptotic statistics! We are asking for the mathematical engine that allows us to approximate the distribution of almost any complicated statistic—the **Delta Method**.

Let's break this down into four parts: **What the Delta Method is**, **the mathematical derivation**, and **how we apply it to two-sample binomial statistics (like Risk Difference, Relative Risk, and Odds Ratio)**.

---

### Part 1: What is the Delta Method? (The Intuition)

The Delta Method is a mathematical trick that says:

> *"If we have a statistic that is Normally distributed (like $\hat{p}$), then any smooth function of that statistic (like $\log(\hat{p})$, or $\hat{p}_1 / \hat{p}_2$) is also approximately Normally distributed, as long as our sample size is large enough."*

**The Analogy:**

Imagine we are looking at a curved mountain slope through a microscope. If we zoom in close enough to any single point on the curve, the curved line starts to look perfectly **straight** (a tangent line). The Delta Method uses this tangent line to approximate the variance of a transformed statistic.

---

### Part 2: The Mathematical Derivation (The "Slope" Trick)

Let's say we have a statistic $\hat{\theta}$ that is asymptotically Normal:

$$\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} N(0, \sigma^2)$$

Now we want to know the distribution of a transformed version $g(\hat{\theta})$.

**Step 1: The Taylor Expansion (First-Order).**

We expand $g(\hat{\theta})$ around the true value $\theta$:

$$g(\hat{\theta}) \approx g(\theta) + g'(\theta)(\hat{\theta} - \theta)$$

**Step 2: Subtract the true transformed value.**

$$g(\hat{\theta}) - g(\theta) \approx g'(\theta)(\hat{\theta} - \theta)$$

**Step 3: Scale by $\sqrt{n}$ and find the variance.**

If $\text{Var}(\hat{\theta}) = \sigma^2$, then:

$$\text{Var}(g(\hat{\theta})) \approx \left( g'(\theta) \right)^2 \times \text{Var}(\hat{\theta})$$

**The Delta Method Formula (Asymptotic Variance):**

$$\boxed{\text{Var}(g(\hat{\theta})) \approx \left( g'(\theta) \right)^2 \times \sigma^2}$$

---

### Part 3: The Delta Method applied to Two Binomial Proportions

We have two independent groups:

- Group 1: $\hat{p}_1$ with variance $\frac{p_1(1-p_1)}{n_1}$
- Group 2: $\hat{p}_2$ with variance $\frac{p_2(1-p_2)}{n_2}$

Because they are independent, the variance of the difference (or any combination) is the sum of their individual variances.

---

### A. Risk Difference (RD = $p_1 - p_2$)

This is the easiest because it is a **linear** function. The derivative of $g(p_1, p_2) = p_1 - p_2$ is 1 for both variables.

| Component | Formula |
| :--- | :--- |
| **Point Estimate** | $\hat{p}_1 - \hat{p}_2$ |
| **Asymptotic SE** | $SE(\hat{p}_1 - \hat{p}_2) = \sqrt{ \frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2} }$ *(We estimate $p_1$ and $p_2$ with $\hat{p}_1$ and $\hat{p}_2$)* |
| **95% CI** | $(\hat{p}_1 - \hat{p}_2) \pm 1.96 \times SE$ |

---

### B. Log Relative Risk (log RR = $\log(p_1 / p_2)$)

This is a non-linear function. We need the derivative of $g(p) = \log(p)$, which is $1/p$.

The variance of the log of a single proportion is:

$$\text{Var}(\log(\hat{p})) \approx \left( \frac{1}{p} \right)^2 \times \frac{p(1-p)}{n} = \frac{1-p}{n p}$$

Because $\log(p_1/p_2) = \log(p_1) - \log(p_2)$, the variance of the difference is the sum of the two variances:

| Component | Formula |
| :--- | :--- |
| **Asymptotic Variance** | $\text{Var}(\log RR) = \frac{1-p_1}{n_1 p_1} + \frac{1-p_2}{n_2 p_2}$ |
| **Asymptotic SE** (plugging in estimates) | $SE(\log RR) = \sqrt{ \frac{1-\hat{p}_1}{n_1 \hat{p}_1} + \frac{1-\hat{p}_2}{n_2 \hat{p}_2} }$ |
| **95% CI for log RR** | $\log(RR) \pm 1.96 \times SE(\log RR)$ |
| **95% CI for RR** | Exponentiate the bounds |

*(Note: This matches the exact formula we derived in the previous question!)*

---

### C. Log Odds Ratio (log OR = $\log \left( \frac{p_1/(1-p_1)}{p_2/(1-p_2)} \right)$)

This is the most common use of the Delta Method in logistic regression.

For a single proportion, the variance of the log-odds $\log\left( \frac{p}{1-p} \right)$ is derived using the Delta Method with $g(p) = \log(p) - \log(1-p)$. The derivative is $\frac{1}{p(1-p)}$.

- **Variance of log-odds for one group:**

$$\text{Var}\left( \log\left( \frac{\hat{p}}{1-\hat{p}} \right) \right) \approx \frac{1}{n p (1-p)}$$

Since the log OR is the difference of the two log-odds, its variance is the sum of the two:

| Component | Formula |
| :--- | :--- |
| **Asymptotic Variance** | $\text{Var}(\log OR) = \frac{1}{n_1 p_1 (1-p_1)} + \frac{1}{n_2 p_2 (1-p_2)}$ |
| **Asymptotic SE** (plugging in estimates) | $SE(\log OR) = \sqrt{ \frac{1}{n_1 \hat{p}_1 (1-\hat{p}_1)} + \frac{1}{n_2 \hat{p}_2 (1-\hat{p}_2)} }$ |
| **Classic Formula** (using cell counts) | $SE(\log OR) = \sqrt{ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} }$ *(Where $a, b, c, d$ are the cell counts in the 2x2 table)* |
| **95% CI for log OR** | $\log(OR) \pm 1.96 \times SE(\log OR)$ |
| **95% CI for OR** | Exponentiate the bounds |

---

### Part 4: Summary Table – Two-Sample Binomial Methods

| Measure | Transformation $g(p_1, p_2)$ | **Asymptotic Variance (Delta Method)** | **Asymptotic SE (Plug-in)** |
| :--- | :--- | :--- | :--- |
| **Risk Difference (RD)** | $p_1 - p_2$ | $\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}$ | $\sqrt{ \frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2} }$ |
| **Log Relative Risk (log RR)** | $\log(p_1) - \log(p_2)$ | $\frac{1-p_1}{n_1 p_1} + \frac{1-p_2}{n_2 p_2}$ | $\sqrt{ \frac{1-\hat{p}_1}{n_1 \hat{p}_1} + \frac{1-\hat{p}_2}{n_2 \hat{p}_2} }$ |
| **Log Odds Ratio (log OR)** | $\log\left( \frac{p_1}{1-p_1} \right) - \log\left( \frac{p_2}{1-p_2} \right)$ | $\frac{1}{n_1 p_1(1-p_1)} + \frac{1}{n_2 p_2(1-p_2)}$ | $\sqrt{ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} }$ |

---

### The "Asymptotic" Conditions (The Fine Print)

| Condition | Requirement |
| :--- | :--- |
| **Asymptotic Mean** | The mean of the transformed statistic is approximately $g(\theta)$. This means $\log RR$ is approximately unbiased for the true log RR |
| **Asymptotic Variance** | The variance we derived above |
| **When is it valid?** | The Delta Method requires **large sample sizes** |
| **Critical Failure** | If $p_1$ or $p_2$ is exactly 0 or 1, or the cell counts are zero, the asymptotic variance blows up to infinity. This is why we often add 0.5 to all cells (the "Haldane" correction) before calculating logs! |

---

### The One-Liner to Memorize

> *"The Delta Method draws a straight tangent line to a curved function. It tells us that the variance of a transformed statistic is approximately the variance of the original statistic multiplied by the square of the slope ($g'(\theta)^2$). This gives us the standard errors for logs, odds, and risks without doing any complex calculus."*

## Fisher's Exact Test, Hypergeometric Distribution, and Monte Carlo Simulation

This is the **trifecta of "small sample" statistics**.

When our sample size is tiny (like the 4 people in the Coke vs. Pepsi taste test), the Normal approximation (Z-tests) and Chi-Squared tests break down. They become unreliable.

To fix this, we use **Fisher's Exact Test**, which relies on the **Hypergeometric Distribution**. And when the math for Fisher's test gets too complicated to do by hand, we use **Monte Carlo simulation** to approximate the answer.

Here is the complete, step-by-step breakdown.

---

### Part 1: The Hypergeometric Distribution (The Engine)

The **Hypergeometric distribution** is the probability distribution that describes **sampling without replacement**.

Imagine we have a finite population of $N$ objects:
- $m$ of them are "successes" (e.g., prefer Coke).
- $N - m$ of them are "failures" (prefer Pepsi).

We randomly draw $n$ objects *without replacement*. The probability of getting exactly $x$ successes is:

$$P(X = x) = \frac{\binom{m}{x} \binom{N-m}{n-x}}{\binom{N}{n}}$$

**Salmon Example:**

We have 10 fish in a tank. 4 are infected with lice (successes), 6 are healthy (failures). We randomly catch 3 fish *without putting them back*. The probability that exactly 2 of them have lice is:

$$P(X=2) = \frac{\binom{4}{2} \binom{6}{1}}{\binom{10}{3}} = \frac{6 \times 6}{120} = 0.30$$

**Key Difference from Binomial:**

| Feature | Binomial | Hypergeometric |
| :--- | :--- | :--- |
| **Population** | Infinite (or sampling *with* replacement) | Finite population |
| **Sampling** | With replacement | **Without replacement** |
| **Convergence** | - | As the population gets huge, the Hypergeometric converges to the Binomial |

---

### Part 2: Fisher's Exact Test (The Test)

**Fisher's Exact Test** is a statistical test used to determine if there is a **non-random association** between two categorical variables in a **2x2 contingency table**, specifically when sample sizes are **small**.

Instead of relying on the Normal approximation (like the Chi-Squared test), Fisher's test calculates the **exact** probability of observing our data (or something more extreme) using the Hypergeometric distribution.

**The Logic:**

1. We have a 2x2 table with fixed marginal totals (row totals and column totals are fixed).
2. We calculate the probability of observing that exact table using the Hypergeometric formula.
3. We then calculate the probabilities of all other tables that are "more extreme" (i.e., show even stronger association).
4. We add them all up to get the **p-value**.

**The Formula for the probability of a specific 2x2 table:**

$$P = \frac{(a+b)! (c+d)! (a+c)! (b+d)!}{a! b! c! d! N!}$$

---

**Coke vs. Pepsi Example (n=4, 3 chose Coke):**

| | Coke | Pepsi | Total |
| :--- | :--- | :--- | :--- |
| **Chose** | 3 | 1 | 4 |
| **Did not choose** | 0 | 0 | 0 |
| **Total** | 3 | 1 | 4 |

Under the null hypothesis ($p = 0.5$), the probability of exactly 3 out of 4 choosing Coke is:

$$P(X=3) = \frac{\binom{4}{3} \binom{0}{0}}{\binom{4}{3}} = \frac{4}{16} = 0.25$$

*(The p-value is the probability of getting 3 or more out of 4 under $H_0$, which is 0.3125 for a one-sided test.)*

---

### Part 3: Monte Carlo Simulation (The "Brute Force" Approximation)

**Monte Carlo simulation** is used in Fisher's Exact Test when the table is larger than 2x2 (e.g., 3x3 or 5x4).

In a 2x2 table, the math is easy. But in a 5x4 table with fixed margins, there are **thousands or millions** of possible tables. Calculating the exact probability of every single table by hand (or even by computer) can be computationally impossible.

**The Monte Carlo Solution:**

Instead of enumerating all possible tables, the computer does this:

| Step | Action |
| :--- | :--- |
| **1** | Generates thousands (e.g., 10,000) of random tables that have the exact same row and column totals as our observed table |
| **2** | For each random table, it calculates the test statistic (e.g., the Chi-Square or the exact probability) |
| **3** | It counts how many of these simulated tables have a statistic **as extreme as** (or more extreme than) our observed data |
| **4** | **The P-value = (Number of extreme simulated tables) / (Total number of simulations)** |

**Why we use it:**

- It is **exact** in the limit (as the number of simulations goes to infinity, it converges to the true exact p-value).
- It is **fast** and works for any size of contingency table.

---

### Part 4: The Grand Connection (Putting it all together)

| Concept | Definition | Role in Fisher's Test |
| :--- | :--- | :--- |
| **Hypergeometric Distribution** | The probability of getting exactly $x$ successes in $n$ draws *without replacement* from a finite population | **This is the mathematical engine.** It calculates the exact probability of our specific 2x2 table |
| **Fisher's Exact Test** | A statistical test that computes the exact p-value for a 2x2 table by summing the hypergeometric probabilities of all tables as extreme as the observed one | **This is the hypothesis test.** It gives us a valid p-value even when sample sizes are tiny |
| **Monte Carlo Simulation** | A computational method that uses random sampling to approximate a complex probability distribution | **This is the "cheat code."** Used when the table is too large (e.g., 5x4) to enumerate all possible tables. It simulates thousands of random tables to approximate the exact p-value |

---

### Summary Cheat Sheet

| Concept | Definition | Coke vs. Pepsi (n=4, x=3) |
| :--- | :--- | :--- |
| **Hypergeometric Formula** | $P(X=x) = \frac{\binom{m}{x} \binom{N-m}{n-x}}{\binom{N}{n}}$ | $P(X=3) = \frac{\binom{4}{3} \binom{0}{0}}{\binom{4}{3}} = 0.25$ |
| **Fisher's Exact P-value (One-sided)** | Sum of probabilities of all tables with $X \geq 3$ | $P(X=3) + P(X=4) = 0.25 + 0.0625 = 0.3125$ |
| **Fisher's Exact P-value (Two-sided)** | Sum of probabilities of all tables as extreme as $X=3$ in *either direction* | $P(X \leq 1) + P(X \geq 3) = 0.3125 + 0.3125 = 0.625$ |
| **Monte Carlo** | Simulate 10,000 random tables under $H_0$, count how many have $X \geq 3$ | Approximates 0.3125 |

---

### The One-Liner to Memorize

> *"The Hypergeometric distribution calculates exact probabilities for small, finite populations. Fisher's Exact Test uses it to get exact p-values for 2x2 tables. When the table gets too big to calculate by hand, Monte Carlo simulates thousands of random tables to approximate the same exact p-value."*

## The Chi-Squared Test: Goodness-of-Fit, Independence, and Generalizations

We have just asked about the **most versatile workhorse** in all of categorical data analysis.

The **Chi-Squared test** is actually a **family of tests**, not just one test. At its core, it is a **"goodness-of-fit"** measure: it answers the question:

> *"How far are our observed counts from what we would expect to see if nothing interesting were happening?"*

Let's break this down into three parts: **The Basic Test**, **Goodness-of-Fit**, and **Generalizations** (testing for independence in larger tables).

---

### Part 1: The Chi-Squared Test Statistic (The Core Engine)

Whether we are testing a single proportion, a 2x2 table, or a complex model, the Chi-Squared test statistic always follows the same fundamental formula:

$$\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}$$

**The Intuition:**

| Result | $\chi^2$ Value | Decision |
| :--- | :--- | :--- |
| Observed counts are **very close** to expected counts | Small $\chi^2$ | Fail to reject the null hypothesis |
| Observed counts are **very different** from expected counts | Large $\chi^2$ | Reject the null hypothesis |

**The Distribution:** Under the null hypothesis, this test statistic follows a **Chi-Squared distribution** with $df$ degrees of freedom.

---

### Part 2: The Chi-Squared Goodness-of-Fit Test (One Categorical Variable)

This is the simplest version of the test. We have **one categorical variable** and we want to test if the observed proportions match a theoretical (or known) distribution.

**Salmon Example:**

We suspect that sea lice are randomly distributed across three different pens (Pen A, B, and C) in a 1:1:1 ratio. We sample 300 fish and find:

| Pen | Observed | Expected (if equal) |
| :--- | :--- | :--- |
| A | 120 | 100 |
| B | 90  | 100 |
| C | 90  | 100 |

**Step 1: Calculate the Chi-Squared statistic.**

$$\chi^2 = \frac{(120-100)^2}{100} + \frac{(90-100)^2}{100} + \frac{(90-100)^2}{100} = \frac{400}{100} + \frac{100}{100} + \frac{100}{100} = 4 + 1 + 1 = 6$$

**Step 2: Find the degrees of freedom.**

$$df = \text{Number of categories} - 1 = 3 - 1 = 2$$

**Step 3: Find the p-value.**

For $\chi^2 = 6$ with $df = 2$, the p-value is approximately **0.05**.

We would fail to reject the null hypothesis at the 5% level—there is not enough evidence to say the lice are unevenly distributed.

---

### Part 3: The Chi-Squared Test of Independence (Two Categorical Variables)

This is the **generalization** to a **contingency table** (e.g., a 2x2, 3x3, or 3x4 table).

Here, we have **two categorical variables**, and we want to know if they are **independent** of each other (i.e., does knowing the value of one variable tell us anything about the other?).

**Salmon Example:**

We want to know if infection status (Lice / No Lice) is independent of feed type (Old / New). We collect data on 200 fish:

| | **Lice** | **No Lice** | **Total** |
| :--- | :--- | :--- | :--- |
| **Old Feed** | 40 | 60 | 100 |
| **New Feed** | 20 | 80 | 100 |
| **Total** | 60 | 140 | 200 |

**Step 1: Calculate the Expected Counts under Independence.**

The expected count for each cell is:

$$E = \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}$$

| Cell | Calculation | Expected |
| :--- | :--- | :--- |
| Old & Lice | $100 \times 60 / 200$ | 30 |
| Old & No Lice | $100 \times 140 / 200$ | 70 |
| New & Lice | $100 \times 60 / 200$ | 30 |
| New & No Lice | $100 \times 140 / 200$ | 70 |

**Step 2: Calculate the Chi-Squared statistic.**

$$\chi^2 = \frac{(40-30)^2}{30} + \frac{(60-70)^2}{70} + \frac{(20-30)^2}{30} + \frac{(80-70)^2}{70}$$

$$= \frac{100}{30} + \frac{100}{70} + \frac{100}{30} + \frac{100}{70} = 3.33 + 1.43 + 3.33 + 1.43 = 9.52$$

**Step 3: Find the degrees of freedom.**

For a contingency table:

$$df = (\text{Number of rows} - 1) \times (\text{Number of columns} - 1) = (2-1) \times (2-1) = 1$$

**Step 4: Find the p-value.**

For $\chi^2 = 9.52$ with $df = 1$, the p-value is about **0.002**.

We strongly reject the null hypothesis. The new feed is significantly reducing lice!

---

### Part 4: Generalization to Larger Tables (R x C Tables)

The same logic extends to **any size** of contingency table.

| Table Size | Degrees of Freedom | Example |
| :--- | :--- | :--- |
| **3x3 Table** | $(3-1) \times (3-1) = 4$ | Compare three feed types across three disease severity levels |
| **4x5 Table** | $(4-1) \times (5-1) = 12$ | Compare four age groups across five symptom types |

The formula for $\chi^2$ remains identical: sum the squared differences divided by the expected counts.

---

### Part 5: The "Yates' Continuity Correction" (The 2x2 Fix)

For a **2x2 table**, the Chi-Squared test can be slightly inaccurate (too liberal) when sample sizes are small. To fix this, we use **Yates' Continuity Correction**:

$$\chi^2_{Yates} = \sum \frac{(|O - E| - 0.5)^2}{E}$$

This subtracts 0.5 from the absolute difference before squaring, which reduces the Chi-Squared value and makes the test more conservative. It is the Pearson Chi-Squared equivalent of Fisher's Exact Test.

---

### Summary Table: Chi-Squared Applications

| Scenario | Test | Degrees of Freedom | Null Hypothesis |
| :--- | :--- | :--- | :--- |
| One categorical variable vs. known proportions | **Goodness-of-Fit** | $k - 1$ | The proportions match the hypothesized distribution |
| Two categorical variables (e.g., 2x2) | **Test of Independence** | $(r-1)(c-1)$ | The two variables are independent (no association) |
| Testing a specific model (e.g., Hardy-Weinberg) | **Goodness-of-Fit** | $k - 1 - m$ | The data fit the theoretical model |
| Comparing multiple proportions (e.g., 3 feeds) | **Test of Homogeneity** | $(r-1)(c-1)$ | The proportions are the same across all groups |

---

### The Golden Rule of Chi-Squared

The Chi-Squared test is a **"large-sample"** test.

- **Rule of Thumb:** All expected cell counts should be **$\geq 5$**.
- If any expected count is $< 5$, the Chi-Squared approximation fails. In that case, use **Fisher's Exact Test** (for 2x2 tables) or **Monte Carlo simulation** (for larger tables).

---

### The One-Liner to Memorize

> *"The Chi-Squared test is the ultimate 'distance detector' for categorical data. It measures how far our observed counts are from our expected counts, squares that distance, and divides by the expected count. The bigger the sum, the stronger the evidence that our variables are related or that our model is wrong."*

## Confounding, Simpson's Paradox, Weighting, and the Mantel-Haenszel Estimator


### Confounding (The "Lurking Variable")

**Definition:** A **confounder** is a third variable that is associated with **both** our exposure (e.g., feed type) and our outcome (e.g., sea lice), causing us to mistakenly think there is a direct causal relationship when there isn't.

**Three conditions for a confounder:**

| Condition | Description |
| :--- | :--- |
| 1 | It is associated with the exposure |
| 2 | It is associated with the outcome |
| 3 | It is not on the causal pathway (it's not caused by the exposure) |

**Salmon Example:**

We compare two pens:

- **Pen A (New Feed):** Low mortality.
- **Pen B (Old Feed):** High mortality.

We conclude the new feed saves lives. But wait! We realize **Pen A** is in a deep, cold fjord, and **Pen B** is in a warm, shallow bay.

- Water temperature (the confounder) affects **both** feed choice (we tried the new feed in the cold fjord) and mortality (cold water kills the disease).

**Without accounting for temperature, we falsely credit the feed!**


---

### Simpson's Paradox (The "Flip-Flop")

**Definition:** Simpson's Paradox occurs when a trend that appears in *separate* groups **disappears or reverses** when we combine the groups. It is caused entirely by ignoring a confounder.

**Salmon Example (Numbers):**

We test two treatments (New vs. Old) in **two different farms** (Cold Water vs. Warm Water).

| | **Cold Water Farm** | **Warm Water Farm** | **Combined Total** |
| :--- | :--- | :--- | :--- |
| **New Feed** | 90/100 survive (90%) | 10/100 survive (10%) | 100/200 survive (50%) |
| **Old Feed** | 80/100 survive (80%) | 20/100 survive (20%) | 100/200 survive (50%) |

---

**Looking at separate farms (Stratified):**

| Farm | New Feed | Old Feed | Winner |
| :--- | :--- | :--- | :--- |
| **Cold Water** | 90% | 80% | **New Feed** ✅ |
| **Warm Water** | 10% | 20% | **New Feed** ✅ |

**Looking at the combined table (Collapsed):**

| Feed | Survival |
| :--- | :--- |
| **New Feed** | 50% |
| **Old Feed** | 50% |

**This is Simpson's Paradox.** The combined average is misleading because the farms have different baseline mortality rates. The water temperature (confounder) is masking the true effect.

---

### Weighting (The "Fix" for Unequal Groups)

**Definition:** **Weighting** is a statistical technique where we assign different "importance" (weights) to different subgroups to correct for imbalance in a confounder.

Instead of giving every individual equal weight, we give *underrepresented* groups more weight and *overrepresented* groups less weight, so that the weighted average reflects a balanced population.

**Salmon Example:**

In the combined table above, the New Feed had 100 fish in the cold farm and 100 in the warm farm (balanced). The Old Feed also had 100 in each. In this case, a simple average works.

But what if the New Feed was tested on **150 fish in the cold farm** and **50 in the warm farm**, while the Old Feed was tested on **50 in the cold farm** and **150 in the warm farm**?

| | Cold Farm | Warm Farm |
| :--- | :--- | :--- |
| **New Feed** | 150 fish | 50 fish |
| **Old Feed** | 50 fish | 150 fish |

- If we just average the raw proportions, we are letting the cold farm dominate the New Feed result and the warm farm dominate the Old Feed result.
- **Weighting** corrects this by giving each farm equal "say" in the final average, regardless of how many fish were actually sampled from each farm.

---

### The Mantel-Haenszel Estimator (The "Grand Unifier")

**Definition:** The **Mantel-Haenszel (M-H) estimator** is a weighted average of the odds ratios (or risk ratios) across **multiple 2x2 tables** (strata). It is the gold-standard method for combining evidence from several stratified tables while controlling for a confounder.

Instead of collapsing all the data into one big, misleading table, the M-H method:

1. Calculates the odds ratio **separately** for each stratum (e.g., Cold Farm and Warm Farm).
2. Assigns a weight to each stratum based on its sample size and variability.
3. Combines them into a **single, summary odds ratio** that is free from confounding.

**The M-H Odds Ratio Formula (for each stratum $i$):**

$$OR_{MH} = \frac{\sum \left( \frac{a_i d_i}{N_i} \right)}{\sum \left( \frac{b_i c_i}{N_i} \right)}$$

Where $a, b, c, d$ are the cells of the 2x2 table for stratum $i$, and $N_i$ is the total sample size in that stratum.

| Why it's amazing | Explanation |
| :--- | :--- |
| **Automatically weights** | Gives more weight to larger, more precise strata |
| **Controls for confounders** | Controls for water temperature without building a complex regression model |
| **Computationally simple** | Widely used in epidemiology, meta-analysis, and observational studies |

---

### The Grand Connection (Putting it all together)

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **Confounding** | A third variable distorts the true relationship | Water temperature affects both feed choice and mortality |
| **Simpson's Paradox** | The combined table shows the opposite of every separate table | New feed is better in cold and warm farms, but looks equal when combined |
| **Weighting** | Giving more importance to certain subgroups to balance the confounder | Giving equal weight to cold/warm farms, regardless of sample size |
| **Mantel-Haenszel Estimator** | A weighted average of stratum-specific odds ratios | Calculates the true feed effect, controlling for temperature |

---

### The One-Liner to Memorize

> *"Confounding creates the illusion of an effect; Simpson's Paradox is that illusion on display. Weighting corrects for the imbalance, and the Mantel-Haenszel estimator sums it all up into one honest, confounder-adjusted odds ratio."*


## The Cochran-Mantel-Haenszel (CMH) Test

To understand the **Cochran-Mantel-Haenszel (CMH) Test**, we have to go back to the **Mantel-Haenszel estimator** we just discussed.

If the Mantel-Haenszel estimator gives us the *size* of the effect (the adjusted odds ratio), the **CMH Test** gives us the *p-value* for that effect.

It is the **hypothesis test** that asks: *"After controlling for the confounder, is there still a statistically significant association between the exposure and the outcome?"*

Here is the definitive guide.

---

### Part 1: The Intuition (The "Stratified" Chi-Squared)

Imagine we have a 2x2 contingency table (Exposure vs. Outcome). But we know there is a confounder (like Age, Sex, or Farm Location).

We decide to **stratify** (split) our data into $K$ separate 2x2 tables based on the levels of the confounder (e.g., one table for Cold Farms, one for Warm Farms).

The **CMH Test** is a **single, overall test** that combines all $K$ tables to answer one question:

> *"Is there a consistent association between exposure and outcome **across all strata**, after removing the effect of the confounder?"*

It is essentially a **weighted average of the differences** between observed and expected counts across all strata.

---

### Part 2: The Formula (The Mathematical Engine)

For each stratum $i$ (e.g., each farm), we have a 2x2 table:

| | Outcome + | Outcome - | Total |
| :--- | :--- | :--- | :--- |
| **Exposed +** | $a_i$ | $b_i$ | $n_{1i}$ |
| **Exposed -** | $c_i$ | $d_i$ | $n_{2i}$ |
| **Total** | $m_{1i}$ | $m_{2i}$ | $N_i$ |

**The CMH Test Statistic:**

$$Q_{CMH} = \frac{ \left( \sum_{i=1}^{K} (a_i - E[a_i]) \right)^2 }{ \sum_{i=1}^{K} \text{Var}(a_i) }$$

Where:

- **$E[a_i]$** = The expected count of $a_i$ under the null hypothesis of no association (calculated using row and column margins, just like in a regular Chi-squared test):

$$E[a_i] = \frac{n_{1i} \times m_{1i}}{N_i}$$

- **$\text{Var}(a_i)$** = The variance of $a_i$ under the null hypothesis:

$$\text{Var}(a_i) = \frac{n_{1i} n_{2i} m_{1i} m_{2i}}{N_i^2 (N_i - 1)}$$

**The Distribution:**

Under the null hypothesis, $Q_{CMH}$ follows a **Chi-Squared distribution** with **1 degree of freedom** (for a 2x2 table). For larger tables (R x C), it has $(R-1) \times (C-1)$ df.

---

### Part 3: A Salmon Example (Putting numbers to it)

Let's use the confounded data from the previous section:

**Cold Farm (Stratum 1):**

| | Survive | Die | Total |
| :--- | :--- | :--- | :--- |
| **New Feed** | 90 (a1) | 10 (b1) | 100 |
| **Old Feed** | 80 (c1) | 20 (d1) | 100 |
| **Total** | 170 | 30 | 200 |

**Warm Farm (Stratum 2):**

| | Survive | Die | Total |
| :--- | :--- | :--- | :--- |
| **New Feed** | 10 (a2) | 90 (b2) | 100 |
| **Old Feed** | 20 (c2) | 80 (d2) | 100 |
| **Total** | 30 | 170 | 200 |

---

**Step 1: Calculate the expected and variance for each stratum.**

**Stratum 1 (Cold Farm):**
- $E[a_1] = \frac{100 \times 170}{200} = 85$
- $\text{Var}(a_1) = \frac{100 \times 100 \times 170 \times 30}{200^2 \times 199} = \frac{51,000,000}{7,960,000} \approx 6.407$

**Stratum 2 (Warm Farm):**
- $E[a_2] = \frac{100 \times 30}{200} = 15$
- $\text{Var}(a_2) = \frac{100 \times 100 \times 30 \times 170}{200^2 \times 199} = 6.407$ (Symmetric, same variance)

---

**Step 2: Calculate the CMH Statistic.**

$$Q_{CMH} = \frac{ \left( (90 - 85) + (10 - 15) \right)^2 }{ 6.407 + 6.407 }$$

$$Q_{CMH} = \frac{ (5 - 5)^2 }{ 12.814 } = \frac{0}{12.814} = 0$$

**Step 3: The P-value.**

A Chi-Squared of 0 with 1 df gives a P-value of **1.0**.

**Interpretation:**

After controlling for water temperature (the confounder), there is **absolutely no evidence** that the new feed affects survival. The apparent effect in the raw data was entirely due to the imbalance in the farms!

---

### Part 4: The Connection to the Mantel-Haenszel Estimator

| Method | What it gives | Our Example |
| :--- | :--- | :--- |
| **Mantel-Haenszel Estimator** | The **adjusted odds ratio** (the size of the effect) | M-H OR = **1.0** (no effect) |
| **CMH Test** | The **p-value** for that adjusted effect | p-value = **1.0** (not significant) |

They are two sides of the same coin. The M-H estimator tells us *how much*; the CMH test tells us *how sure*.

---

### Part 5: When to Use the CMH Test

| Application | Description |
| :--- | :--- |
| **Case-Control Studies** | Control for age, sex, or other categorical confounders |
| **Meta-Analysis** | Combining results from multiple studies (each study is a "stratum") |
| **Longitudinal Data** | Repeated measures across time (each time point is a stratum) |
| **Large R x C Tables** | Extended to handle tables larger than 2x2, testing for general association across multiple strata |

---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **CMH Test** | A stratified Chi-squared test that controls for a confounder | Testing feed effect while controlling for water temperature |
| **Null Hypothesis** | No association between exposure and outcome **after** stratifying by the confounder | The feed does not affect survival, regardless of temperature |
| **Formula** | $Q_{CMH} = \frac{(\sum (a_i - E_i))^2}{\sum \text{Var}(a_i)}$ | - |
| **Distribution** | Chi-Squared with 1 df (for 2x2 tables) | - |
| **The Golden Rule** | If CMH is significant, the association persists even after removing the confounder. If CMH is not significant, the apparent effect was likely due to confounding | In our example, CMH = 0, p = 1.0 → No true feed effect |

---

### The One-Liner to Memorize

> *"The Cochran-Mantel-Haenszel test is the 'truth serum' for 2x2 tables. It stratifies by the confounder, calculates the expected values in each stratum, and tests if the overall association is still significant after adjusting for the lurking variable."*

## Case-Control Studies: Odds Ratios, Exact Inference, and Fisher's Exact Test

We have just stepped into the **heart of epidemiology**—the case-control study.

A **case-control study** is retrospective. We start with the *outcome* (e.g., "Has disease") and look *backward* to see who was exposed. Because we deliberately sample a fixed number of cases and a fixed number of controls, **we cannot calculate risk** (incidence). However, we **can** calculate the **Odds Ratio (OR)** to estimate the strength of association.

When sample sizes are small, the Normal approximation (Wald test) fails, so we use **exact inference** (Fisher's Exact Test) based on the **Hypergeometric distribution**.

Here is the complete, step-by-step guide.

---

### Part 1: Case-Control Sampling (The 2x2 Table)

In a case-control study, we fix the number of cases and controls. The data are arranged as:

| | **Cases (Disease +)** | **Controls (Disease -)** | **Total** |
| :--- | :--- | :--- | :--- |
| **Exposed (e.g., New Feed)** | $a$ | $b$ | $n_1$ |
| **Unexposed (Old Feed)** | $c$ | $d$ | $n_2$ |
| **Total** | $m_1$ | $m_2$ | $N$ |

**Salmon Case-Control Example:**

We hypothesize that a new feed causes sea lice. We sample **40 salmon with lice (cases)** and **40 salmon without lice (controls)**. We look back at their feed history:

| | **Lice (Cases)** | **No Lice (Controls)** | **Total** |
| :--- | :--- | :--- | :--- |
| **New Feed (Exposed)** | 30 (a) | 10 (b) | 40 |
| **Old Feed (Unexposed)** | 10 (c) | 30 (d) | 40 |
| **Total** | 40 | 40 | 80 |

- **Exposure rate among cases:** $30/40 = 75\%$
- **Exposure rate among controls:** $10/40 = 25\%$

---

### Part 2: The Odds Ratio (The Measure of Association)

Since we cannot calculate risk (because we fixed the number of cases/controls), we calculate the **Odds Ratio (OR)**:

$$OR = \frac{a \times d}{b \times c} = \frac{30 \times 30}{10 \times 10} = \frac{900}{100} = 9.0$$

**Interpretation:** The odds of being exposed to the new feed are **9 times higher** among salmon with lice than among those without lice. This strongly suggests the new feed is a risk factor.

---

### Part 3: The Problem with Small Samples (Why exact inference?)

In our example, we have 80 fish. A large-sample Wald test (Z-test) works fine.

But what if we only had 10 cases and 10 controls?

- If any cell count is very small (e.g., $< 5$), the Normal approximation used by the Wald test **breaks down**.
- The p-value becomes unreliable, and the confidence intervals may include impossible values (e.g., below 0).

**The Solution:** Use **Exact Inference** based on the **Hypergeometric Distribution**.

---

### Part 4: Exact Inference for the Odds Ratio (Fisher's Exact Test)

In a case-control study, the margins (row totals and column totals) are considered **fixed**:

- Column totals (number of cases and controls) are fixed by design.
- Row totals (exposed/unexposed) are random, but we condition on them for the exact test.

Under the null hypothesis ($OR = 1$, i.e., no association), the probability of observing a specific table (with cell $a$) is given by the **Hypergeometric distribution**:

$$P(a) = \frac{\binom{n_1}{a} \binom{n_2}{m_1 - a}}{\binom{N}{m_1}}$$

Where:
- $\binom{n_1}{a}$ = ways to choose $a$ exposed cases from $n_1$ exposed total
- $\binom{n_2}{m_1 - a}$ = ways to choose unexposed cases
- $\binom{N}{m_1}$ = total ways to choose $m_1$ cases from $N$ total

---

### Step-by-Step Salmon Example (Small Sample)

Imagine a smaller case-control study:

| | **Cases** | **Controls** | **Total** |
| :--- | :--- | :--- | :--- |
| **Exposed** | 4 (a) | 1 (b) | 5 |
| **Unexposed** | 1 (c) | 4 (d) | 5 |
| **Total** | 5 | 5 | 10 |

- **OR = $4 \times 4 / (1 \times 1) = 16$** (Strong effect)
- But is it statistically significant?

**Step 1: Calculate the probability of the observed table.**

$$P(a=4) = \frac{\binom{5}{4} \binom{5}{1}}{\binom{10}{5}} = \frac{5 \times 5}{252} = \frac{25}{252} \approx 0.0992$$

**Step 2: Identify more extreme tables (One-sided test).**

We are testing if exposure *increases* risk (alternative: OR > 1).

"More extreme" means even *more* exposed cases ($a$ larger).

The only possible table with $a = 5$ is:

| | Cases | Controls | Total |
| :--- | :--- | :--- | :--- |
| **Exposed** | 5 | 0 | 5 |
| **Unexposed** | 0 | 5 | 5 |
| **Total** | 5 | 5 | 10 |

$$P(a=5) = \frac{\binom{5}{5} \binom{5}{0}}{\binom{10}{5}} = \frac{1 \times 1}{252} \approx 0.00397$$

**Step 3: One-sided P-value.**

$$P_{\text{one-sided}} = P(a=4) + P(a=5) = 0.0992 + 0.00397 \approx 0.1032$$

**Conclusion:** With a p-value of $\sim 0.10$, we **fail to reject** the null hypothesis. There is not enough evidence to say exposure is associated with disease in this tiny sample.

---

### Part 5: Confidence Interval for the Odds Ratio (Exact)

Exact confidence intervals for the OR are based on the **Cornfield method** or the **Fisher exact method** (inverting the test). They are asymmetric and guarantee 95% coverage even for small samples.

In R, we would run:

```r
matrix <- matrix(c(4,1,1,4), nrow=2)
fisher.test(matrix, alternative="two.sided")

	Fisher's Exact Test for Count Data
p-value = 0.2065
95 percent confidence interval:
  0.6229 745.1493
sample estimates:
odds ratio: 11.248




Notice the massively wide confidence interval: $[0.62, 745]$. This reflects the extreme uncertainty with such a small sample.

---

### Part 6: The Connection to the Mantel-Haenszel Test

In the previous section, we discussed the **CMH test** for combining multiple 2x2 tables (stratified by a confounder).

- The **exact inference** we just did is the **single-stratum** version.
- When we have multiple strata (e.g., Cold Farm and Warm Farm), we use the **Mantel-Haenszel (MH) estimator** for the OR, and the **CMH test** for the p-value.
- For small samples across multiple strata, we can perform an **exact version of the CMH test**, which is essentially a **multivariate hypergeometric distribution**.

---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **Case-Control Study** | Sampling based on outcome (cases vs. controls), looking backward for exposure | Sampled 40 with lice, 40 without, checked feed history |
| **Odds Ratio (OR)** | Measure of association: $\frac{a \times d}{b \times c}$ | OR = 9.0 (strong risk factor) |
| **Exact Inference** | Using the Hypergeometric distribution to calculate exact p-values (Fisher's Exact Test) | For small samples, avoids relying on Normal approximation |
| **Hypergeometric Probability** | $P(a) = \frac{\binom{n_1}{a} \binom{n_2}{m_1 - a}}{\binom{N}{m_1}}$ | Calculates the probability of a specific table given fixed margins |
| **Fisher's Exact Test** | Sums hypergeometric probabilities of observed + more extreme tables | Gives exact p-value for OR $\neq$ 1 |
| **Exact Confidence Interval** | Based on inverting the Fisher test (Cornfield method) | Wide intervals for small samples |
| **The Golden Rule** | If sample sizes are small or expected counts $< 5$, **always** use exact inference (Fisher's Exact Test) instead of the Wald test | - |

---

### The One-Liner to Memorize

> *"In a case-control study, we fix the number of cases and controls, so we can't calculate risk—only odds. When sample sizes are small, the Normal approximation fails, so we must use exact inference (Fisher's Exact Test) based on the Hypergeometric distribution to get honest p-values and confidence intervals."*
