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
