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
- **Group 1 (Old Feed):** \( n_1 = 100 \), \( x_1 = 40 \) lice → \( \hat{p}_1 = 0.40 \)
- **Group 2 (New Feed):** \( n_2 = 120 \), \( x_2 = 36 \) lice → \( \hat{p}_2 = 0.30 \)
- **Parameter of interest:** The true difference \( \delta = p_1 - p_2 \).

Let’s break down how **Likelihood** and **Bayesian** inference handle this.

---

### Part 1: Likelihood Inference (The "Pure Data" Approach)

Likelihood inference is the bridge between Frequentist and Bayesian. It uses only the data to create a **likelihood function** for the parameter \( \delta \), without using prior beliefs.

**Step 1: Write the Likelihood**
For two independent binomial groups, the likelihood is the product of the two individual binomial likelihoods:

\[
\mathcal{L}(p_1, p_2) \propto p_1^{x_1} (1-p_1)^{n_1 - x_1} \times p_2^{x_2} (1-p_2)^{n_2 - x_2}
\]

**Step 2: Profile Likelihood for \( \delta = p_1 - p_2 \)**
We don't care about the individual \( p_1 \) and \( p_2 \); we care about their **difference** \( \delta \). 

To get the likelihood for \( \delta \) alone, we use the **Profile Likelihood** (which you asked about earlier!). For every possible value of \( \delta \), we mathematically "maximize out" \( p_1 \) and \( p_2 \) to find the absolute highest likelihood.

**Step 3: The Profile Likelihood Curve**
If you plot this profile likelihood against \( \delta \), you get a curve that:
- Peaks at \( \hat{\delta} = \hat{p}_1 - \hat{p}_2 = 0.10 \) (the MLE).
- Falls off as \( \delta \) moves away from 0.10.

**The Likelihood Ratio Test (LRT):**
To test \( H_0: \delta = 0 \), we compare the height of the likelihood at \( \delta = 0 \) to the height at the peak (\( \delta = 0.10 \)):

\[
\text{Likelihood Ratio} = \frac{\mathcal{L}(\delta = 0)}{\mathcal{L}(\delta = \hat{\delta})}
\]

- If this ratio is very small (i.e., the likelihood at 0 is much lower than at the peak), we reject \( H_0 \).
- In large samples, \( -2 \log(\text{Likelihood Ratio}) \) follows a Chi-squared distribution (giving us a p-value).

**The "Likelihood Interval" (Similar to a CI):**
A 95% likelihood-based confidence interval is the set of \( \delta \) values for which:
\[
-2 \log\left( \frac{\mathcal{L}(\delta)}{\mathcal{L}(\hat{\delta})} \right) < 3.84
\]
(This is the Chi-squared 1 df critical value).

**Result:** For our salmon data, the profile likelihood interval for \( \delta = p_1 - p_2 \) is approximately **[-0.025, 0.225]**.

**Interpretation:** This is very close to the Agresti-Caffo interval we calculated earlier. It does not contain 0, so we fail to reject the null (no significant difference).

---

### Part 2: Bayesian Inference (Updating with Priors)

Bayesian inference adds a **prior distribution** to the mix. For two binomial proportions, the **conjugate prior** is the Beta distribution.

**Step 1: Choose Priors for \( p_1 \) and \( p_2 \).**

- **Non-informative (Jeffreys) prior:** \( p_1 \sim \text{Beta}(0.5, 0.5) \) and \( p_2 \sim \text{Beta}(0.5, 0.5) \). This lets the data speak entirely for itself.
- **Informative prior:** If you have historical data, you might use \( p_1 \sim \text{Beta}(10, 90) \) (belief that the old feed has ~10% infection rate).

**Step 2: Calculate the Posterior**
Because the Beta is conjugate to the Binomial, the posterior for each proportion is just:

- \( p_1 | \text{data} \sim \text{Beta}(\alpha_1 + x_1, \ \beta_1 + n_1 - x_1) \)
- \( p_2 | \text{data} \sim \text{Beta}(\alpha_2 + x_2, \ \beta_2 + n_2 - x_2) \)

For Jeffreys prior (\( \alpha = \beta = 0.5 \)):

- Posterior for \( p_1 \): Beta(40.5, 60.5)
- Posterior for \( p_2 \): Beta(36.5, 84.5)

**Step 3: Get the Posterior for \( \delta = p_1 - p_2 \)**
This is the tricky part. The difference of two Beta distributions does not have a simple closed-form formula. 

**How we do it today (MCMC):** 
We use a computer to take **thousands of random draws** from the posterior of \( p_1 \) and \( p_2 \), subtract them, and plot the histogram of the differences. This histogram is the **posterior distribution of \( \delta \)**.

**Step 4: The Bayesian Credible Interval**
We look at the histogram of \( \delta \) and find the 2.5th percentile and the 97.5th percentile. 

**Result (Using Jeffreys prior):** 
The 95% credible interval for \( \delta \) is approximately **[-0.023, 0.223]**.

**Interpretation:** 
We can say: *"There is a 95% probability that the true difference in infection rates is between -2.3% and 22.3%."* 
*(Notice: this is a direct probabilistic statement, which is strictly forbidden in Frequentist statistics!)*

---

### Part 3: The Grand Comparison (Frequentist vs. Likelihood vs. Bayesian)

Let’s put all three side-by-side for the same salmon data:

| Method | Interval for \( \delta = p_1 - p_2 \) | Interpretation |
| :--- | :--- | :--- |
| **Frequentist (Agresti-Caffo)** | [-0.0265, 0.2239] | *"If we repeated this experiment infinitely, 95% of these intervals would contain the true \( \delta \)."* |
| **Likelihood (Profile)** | [-0.025, 0.225] | *"These are the values of \( \delta \) most compatible with the data."* |
| **Bayesian (Jeffreys Prior)** | [-0.023, 0.223] | *"There is a 95% **probability** that \( \delta \) lies in this range."* (The most intuitive!). |

---

### The Role of the Prior (The Bayesian Superpower)

Here is where Bayesian inference shines (and gets criticized).

- **Jeffreys Prior (Beta(0.5, 0.5)):** Gives almost identical results to the likelihood/Frequentist intervals. The data completely drives the result.
- **Strong Informative Prior:** Imagine you have 10 years of data showing the old feed has a 10% infection rate. You use a strong prior \( p_1 \sim \text{Beta}(50, 450) \). 
  - Your prior "pulls" the estimate of \( p_1 \) toward 0.10.
  - The resulting credible interval for \( \delta \) might shrink and shift, perhaps becoming **[-0.05, 0.12]**. 
  - You are now formally combining historical knowledge with new data!

---

### Summary Cheat Sheet

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **Likelihood Inference** | Uses the profile likelihood to find plausible values of \( \delta \). No priors. | Profile likelihood interval: [-0.025, 0.225]. |
| **Bayesian Inference** | Uses priors + data = posterior. Gives direct probability statements. | Posterior for \( p_1 \): Beta(40.5, 60.5). |
| **Jeffreys Prior** | A non-informative prior (Beta(0.5, 0.5)). Lets data speak. | Credible interval: [-0.023, 0.223]. |
| **Informative Prior** | Uses real prior knowledge (e.g., historical data). | Shrinks the interval toward historical values. |
| **The Key Difference** | Frequentist = "Long-run coverage." <br> Bayesian = "Direct probability of the parameter." | Bayesian gives the intuitive answer most people actually want! |

---

### The One-Liner to Memorize

> **"Likelihood inference listens only to the data; Bayesian inference combines the data with prior knowledge. When you use a non-informative prior, they shake hands and give nearly identical results—but only Bayesian allows you to say, 'There is a 95% chance the true difference lies in this interval.'"**
