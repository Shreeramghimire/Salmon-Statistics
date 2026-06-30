## Example 1. Sea-lice Count:
The Norwegian Food Safety Authority records the weekly number of salmon lice in aquaculture facilities. Regulations require fish farms to maintain an average of 0.5 or fewer adult female lice per fish. To comply with this requirement, farms conduct weekly sampling of salmon from net pens and count the number of lice present. The number of adult female lice serves as the primary indicator in salmon lice monitoring and control programs, as it reflects the reproductive potential of the parasite population. This is an example of discrete data. And we use the Probability Mass Function (PMF) to calculate the probability of a specific count. 
The PMF is the mathematical function that describes the probability that a single, randomly selected fish from that net pen will have exactly k lice on it.
If X = the number of adult female lice on a single fish, then the PMF is: P(X = k), where k = 0, 1, 2, 3, ...
Because lice are randomly distributed across thousands of fish in a net pen, and the average is very low (≤ 0.5), biologists and statisticians almost always model this using the Poisson distribution.

The Poisson PMF is perfect here because it models the probability of several events (lice) occurring in a fixed space (one fish) when the average rate is low. The PMF is:
P(X = k) = (e^(-λ) * λ^k) / k!
Where: λ (lambda) is the average number of lice per fish (which the regulation says must be ≤ 0.5).
Let’s plug the regulation limit (λ = 0.5) into the PMF. This tells a fish farmer exactly what their weekly sample should look like if they are right at the legal limit:

P(X = 0) = (e^(-0.5) * 0.5^0) / 0! = 60.7% (About 61 out of 100 fish will have zero lice).

P(X = 1) = (e^(-0.5) * 0.5^1) / 1! = 30.3% (About 30 fish will have exactly 1 louse).

P(X = 2) = (e^(-0.5) * 0.5^2) / 2! = 7.6% (About 8 fish will have 2 lice).

P(X = 3) = (e^(-0.5) * 0.5^3) / 6 = 1.3% (About 1 fish will have 3 lice).

We use the PMF to define Event A = "The farm exceeds the legal limit."

Let's say they sample 20 fish. If the true average is exactly 0.5 (the legal limit), then the total number of lice in their 20-fish sample should follow a Poisson distribution with an average of 20 * 0.5 = 10 total adult female lice.

You use the PMF to calculate the probability of exceeding the limit:

P(Compliant) = P(Total lice in 20 fish ≤ 10).

P(Non-compliant / Event A) = P(Total lice in 20 fish > 10).

## Example 2
### Salmon Growth Diet Experiment: 95% Confidence Interval for Difference in Means

Researchers are studying the effect of a new experimental diet on the growth of Atlantic salmon. They measure the natural logarithm of the ratio of final weight to initial weight (a standard measure of specific growth rate) for 8 salmon fed the experimental diet and 8 salmon fed the standard control diet.

The log-growth measurements resulted in:

- **Experimental diet group:** Mean log-growth = 6 (log grams per day)
- **Control diet group:** Mean log-growth = 4 (log grams per day)
- Sample variance in the experimental group: 3
- Sample variance in the control group: 5

Assuming equal variances, create a 95% confidence interval for the difference in the population means of log-growth between the experimental diet and control diet (Experimental - Control).

---

### Step 1: Identify the given information

**Experimental Diet (Group 1):**
- Sample size: $n_1 = 8$
- Sample mean: $\bar{x}_1 = 6$
- Sample variance: $s_1^2 = 3$

**Control Diet (Group 2):**
- Sample size: $n_2 = 8$
- Sample mean: $\bar{x}_2 = 4$
- Sample variance: $s_2^2 = 5$

**Confidence level:** 95% ($\alpha = 0.05$)

**Degrees of freedom:**
$$df = n_1 + n_2 - 2 = 8 + 8 - 2 = 14$$

---

### Step 2: Calculate the Pooled Variance ($s_p^2$)

Since we assume equal variances, we pool the two sample variances:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

Plug in the numbers:

$$s_p^2 = \frac{(8 - 1) \times 3 + (8 - 1) \times 5}{8 + 8 - 2}$$

$$s_p^2 = \frac{(7 \times 3) + (7 \times 5)}{14}$$

$$s_p^2 = \frac{21 + 35}{14} = \frac{56}{14} = 4$$

So the pooled variance is **4**.

The pooled standard deviation is:

$$s_p = \sqrt{4} = 2$$

---

### Step 3: Calculate the Standard Error of the Difference

The standard error for the difference between two independent means (with equal variances) is:

$$SE(\bar{x}_1 - \bar{x}_2) = s_p \times \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

Plug in the numbers:

$$SE = 2 \times \sqrt{\frac{1}{8} + \frac{1}{8}}$$

$$SE = 2 \times \sqrt{\frac{2}{8}} = 2 \times \sqrt{0.25} = 2 \times 0.5 = 1$$

So the Standard Error is **1.0** (log grams per day).

---

### Step 4: Find the t-critical value

We need the t-value for a 95% confidence interval with $df = 14$.

For 95% confidence, $\alpha = 0.05$, so $\alpha/2 = 0.025$.

Looking up $t_{14, 0.025}$ in a t-table (or using software), we get:

$$t_{critical} = 2.145$$

---

### Step 5: Calculate the Confidence Interval

The formula for the confidence interval is:

$$(\bar{x}_1 - \bar{x}_2) \pm t_{critical} \times SE$$

First, calculate the difference in sample means:

$$\bar{x}_1 - \bar{x}_2 = 6 - 4 = 2$$

Now, calculate the margin of error:

$$\text{Margin of Error} = 2.145 \times 1 = 2.145$$

Finally, construct the interval:

$$2 \pm 2.145$$

**Lower bound:** $2 - 2.145 = -0.145 \approx -0.14$

**Upper bound:** $2 + 2.145 = 4.145 \approx 4.14$

---

### Answer 

The 95% confidence interval for the difference in population mean log-growth rates (Experimental Diet - Control Diet) is:

$$[-0.14, \; 4.14] \text{ (log grams per day)}$$

---

### Interpretation for the Salmon Farmer

We are **95% confident** that the true difference in mean log-growth rate between salmon fed the experimental diet and those fed the control diet is between **-0.14** and **4.14** log grams per day.

**What does this mean for the farmer?**

- Because this interval contains **0**, we **cannot conclude with 95% confidence** that the experimental diet significantly changes growth rates compared to the control diet.

- The experimental diet could be:
  - Slightly worse (down to -0.14)
  - Have no effect (0)
  - Or be substantially better (up to 4.14)

- The **wide interval** (spanning over 4 units) tells us that with only 8 fish per group, our estimate is **very imprecise**. To get a narrower, more definitive answer, the farmer would need to sample many more fish (increase $n$) to shrink the standard error and pin down the true effect of the new diet.

---

### Summary Table

| Step | Calculation | Result |
|------|-------------|--------|
| 1 | $df = n_1 + n_2 - 2$ | $df = 14$ |
| 2 | $s_p^2 = \frac{(7)(3) + (7)(5)}{14}$ | $s_p^2 = 4$ |
| 3 | $SE = 2 \times \sqrt{1/8 + 1/8}$ | $SE = 1.0$ |
| 4 | $t_{14, 0.025}$ | $t = 2.145$ |
| 5 | $2 \pm 2.145 \times 1$ | $[-0.14, 4.14]$ |

**The Bottom Line:** With only 8 fish per group, we can't conclude the diet works. We need a larger sample size to get a precise estimate!

## Example 3 Delta Method
Here is the **definitive version** of the Delta Method applied to two-sample binomial statistics, **completely integrated with the salmon farm example**. 

We will use a consistent 2x2 table throughout to make every formula tangible.

---

### Data

We run a trial comparing a new feed to an old feed to see if it reduces sea lice.

| | **Sea Lice (Disease)** | **No Sea Lice** | **Total** |
| :--- | :--- | :--- | :--- |
| **Old Feed (Group 1)** | 40 (a) | 60 (b) | 100 |
| **New Feed (Group 2)** | 20 (c) | 80 (d) | 100 |

From this table:
- **Group 1 (Old):** \( \hat{p}_1 = 40/100 = 0.40 \)
- **Group 2 (New):** \( \hat{p}_2 = 20/100 = 0.20 \)
- **Risk Difference (RD):** \( 0.40 - 0.20 = 0.20 \)
- **Relative Risk (RR):** \( 0.40 / 0.20 = 2.0 \)
- **Odds Ratio (OR):** \( (40 \times 80) / (60 \times 20) = 3200 / 1200 = 2.67 \)

---

### Part 1: The Delta Method (The Mathematical Engine)

**The Problem:** 
We have a statistic \( \hat{\theta} \) (like \( \hat{p} \)) that is asymptotically Normal. We want the distribution of a transformed version \( g(\hat{\theta}) \) (like \( \log(\hat{p}) \)). 

**The Delta Method Formula:**
\[
\text{Var}(g(\hat{\theta})) \approx \left( g'(\theta) \right)^2 \times \text{Var}(\hat{\theta})
\]

**In plain English:** 
The variance of a transformed statistic is approximately the variance of the original statistic multiplied by the **square of the slope** of the transformation.

---

### Part 2: Three Key Transformations (Applied to Salmon)

Here are the three most common transformations in epidemiology, with their derivatives and final formulas.

| Transformation \( g(p) \) | Derivative \( g'(p) \) | Variance Formula (Delta Method) |
| :--- | :--- | :--- |
| **Linear (\( p \))** | \( 1 \) | \( \text{Var}(p) \) |
| **Log (\( \log(p) \))** | \( 1/p \) | \( \text{Var}(p) / p^2 \) |
| **Logit (\( \log(p/(1-p)) \))** | \( 1/(p(1-p)) \) | \( \text{Var}(p) / (p(1-p))^2 \) |

---

### Part 3: Two-Sample Binomial Methods (Complete Salmon Examples)

Because we have *two* independent groups, the variance of any difference (or ratio) is the **sum** of the individual variances. 

---

#### A. Risk Difference (RD = \( p_1 - p_2 \))

This is the simplest; it is perfectly linear, so the Delta Method is exact.

- **Point Estimate:** \( \hat{p}_1 - \hat{p}_2 = 0.40 - 0.20 = \mathbf{0.20} \)
- **Asymptotic SE (Delta Method):**
\[
SE(\hat{p}_1 - \hat{p}_2) = \sqrt{ \frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2} }
\]
\[
SE = \sqrt{ \frac{0.40(0.60)}{100} + \frac{0.20(0.80)}{100} } = \sqrt{ 0.0024 + 0.0016 } = \sqrt{0.004} = 0.0632
\]
- **95% Confidence Interval:** 
\[
0.20 \pm 1.96(0.0632) = 0.20 \pm 0.124
\]
- **Final CI:** **\[0.076, \ 0.324\]**

**Salmon Interpretation:** We are 95% confident that the new feed reduces the sea lice infection rate by between **7.6% and 32.4%**. Since this interval does not contain 0, it is statistically significant.

---

#### B. Log Relative Risk (log RR = \( \log(p_1 / p_2) \))

Relative risk is a ratio. We use the Delta Method because the ratio is non-linear.

- **Point Estimate (RR):** \( 2.0 \)
- **Point Estimate (log RR):** \( \log(2.0) = \mathbf{0.693} \)
- **Derivation of SE (Delta Method):**
For a single proportion, \( \text{Var}(\log(\hat{p})) = \frac{1-p}{n p} \). Because \( \log(RR) = \log(p_1) - \log(p_2) \), we add the variances:

\[
SE(\log RR) = \sqrt{ \frac{1-\hat{p}_1}{n_1 \hat{p}_1} + \frac{1-\hat{p}_2}{n_2 \hat{p}_2} }
\]
\[
SE = \sqrt{ \frac{0.60}{100 \times 0.40} + \frac{0.80}{100 \times 0.20} } = \sqrt{ 0.015 + 0.04 } = \sqrt{0.055} = 0.2345
\]
- **95% CI (on the log scale):** 
\[
0.693 \pm 1.96(0.2345) = 0.693 \pm 0.460
\]
- **95% CI (Exponentiate to get back to RR):**
\[
[e^{0.233}, \ e^{1.153}] = \mathbf{[1.26, \ 3.17]}
\]

**Salmon Interpretation:** Fish on the old feed are between **1.26 and 3.17 times more likely** to get sea lice than fish on the new feed. Since this interval does not contain 1.0, it is significant.

---

#### C. Log Odds Ratio (log OR = \( \log \left( \frac{p_1/(1-p_1)}{p_2/(1-p_2)} \right) \))

This is the most common output of logistic regression. 

- **Point Estimate (OR):** \( 2.67 \)
- **Point Estimate (log OR):** \( \log(2.67) = \mathbf{0.982} \)
- **Derivation of SE (Delta Method):**
For a single proportion, \( \text{Var}(\text{logit}(p)) = \frac{1}{n p (1-p)} \). Because log OR is the difference of two logits, we add the variances:

\[
SE(\log OR) = \sqrt{ \frac{1}{n_1 \hat{p}_1 (1-\hat{p}_1)} + \frac{1}{n_2 \hat{p}_2 (1-\hat{p}_2)} }
\]
\[
SE = \sqrt{ \frac{1}{100(0.40)(0.60)} + \frac{1}{100(0.20)(0.80)} } = \sqrt{ \frac{1}{24} + \frac{1}{16} } = \sqrt{ 0.04167 + 0.0625 } = \sqrt{0.10417} = 0.3227
\]

*(If you use the shortcut formula using cell counts: \( SE = \sqrt{ \frac{1}{40} + \frac{1}{60} + \frac{1}{20} + \frac{1}{80} } = \sqrt{0.1042} = 0.3227 \))*

- **95% CI (on the log scale):** 
\[
0.982 \pm 1.96(0.3227) = 0.982 \pm 0.632
\]
- **95% CI (Exponentiate):**
\[
[e^{0.350}, \ e^{1.614}] = \mathbf{[1.42, \ 5.03]}
\]

**Salmon Interpretation:** The odds of sea lice on the old feed are between **1.42 and 5.03 times higher** than on the new feed. 

---

### Part 4: The Asymptotic Summary (The Fine Print)

| Concept | Definition | Salmon Example |
| :--- | :--- | :--- |
| **Asymptotic Mean** | The mean of the transformed statistic converges to the true transformed value. | The mean of \( \log(OR) \) converges to \( \log(2.67) \). |
| **Asymptotic Variance** | The variance we calculate using the Delta Method. | \( \text{Var}(\log OR) \approx 0.1042 \) |
| **Asymptotic SE** | The square root of the asymptotic variance. | \( SE(\log OR) \approx 0.3227 \) |
| **When does it fail?** | If cell counts are zero (e.g., a=0), the SE blows up. | Add 0.5 to all cells (Haldane correction) to fix this. |
| **The Golden Rule** | The Delta Method requires large samples. For small samples, use **exact methods** (Clopper-Pearson, Fisher's Exact Test). | Our sample size (100 per group) is large enough. |

---

### The One-Liner to Memorize

> **"The Delta Method draws a straight tangent line through a curved statistic. It tells us that the variance of a log(OR) or log(RR) is just the sum of the variances of the individual logits or logs, multiplied by the square of their slopes. This gives us reliable standard errors and confidence intervals for any ratio—as long as our sample size is large and no cell counts are zero."**
