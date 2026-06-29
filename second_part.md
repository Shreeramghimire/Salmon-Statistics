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

e alarm (Type I), Beta is the risk of missing the truth (Type II). Increasing our sample size is the only cure to lower Beta without raising Alpha."*

