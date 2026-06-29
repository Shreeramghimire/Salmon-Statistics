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
- Null mean: $\mu_0 = 5.0$ kg
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

