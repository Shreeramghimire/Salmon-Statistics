# Salmon-Statistics
In this repository, statistical phenomena are explained in reference to metrics from aqauculture activities related to salmon.

# Probability Functions
## Random variable
A random variable is a numerical value assigned to the outcome of a random experiment or phenomenon.
1. A discrete random variable takes on a finite or countable number of possible values. The probability associated with each possible value is described by a Probability Mass Function (PMF), which assigns a probability to every individual outcome. In mathematical terms, probabilities are obtained by counting the occurrence of specific outcomes.
2. A continuous random variable can take any value within a given range or interval, resulting in infinitely many possible values. The probability distribution is described by a Probability Density Function (PDF). For continuous variables, probabilities are determined by calculating the area under the density curve over a given interval, rather than at a single point. This area represents the likelihood of the variable falling within that range of values.

## Cumulative Distribution Function (CDF)
The Cumulative Distribution Function (CDF) calculates the probability that a random variable is less than or equal to a specific value.
While individual probabilities tell the chance of a single outcome, the CDF gives the accumulated (running total) probability up to a certain point. 
The output is always between 0 and 1.

## One-Tailed Test Vs. Two-Tailed Test
### One-Tailed Test (The "Is it better?" Test)
One uses a one-tailed test when the research question is: "Is the new treatment strictly better (or strictly worse) than the old one?"

It is assumed to be completely confident that the effect cannot go in the opposite direction, or we simply don't care about the opposite direction. We pile your entire 5% alpha into just one tail of the distribution.
1. The Hypothesis: H0: New ≤ Old Vs. H1: New > Old (This is a "greater than" test)
2. Where does the rejection region go? : The entire 5% (α = 0.05) is put in the right tail only.
3. Confidence Interval: Crucially, a one-tailed test gives us a one-sided confidence bound. Instead of 
±, we get either:
a. An upper bound: $\bar{x} + t_{0.05} \times SE$ (meaning: "We are 95% confident the true mean is less than this number").
b. A lower bound: $\bar{x} - t_{0.05} \times SE$ (meaning: "We are 95% confident the true mean is greater than this number").

#### Example: A company develops a new, cheaper medicine to kill sea lice. They only care if the new medicine kills more lice than the old expensive medicine. If it kills the same amount, they will switch to the cheaper one. If it kills fewer, they won't use it. They don't care if it kills way more than the old one (that's just a bonus); they are only testing for superiority. 

### Two-Tailed Test ((The "Is it different?" Test)
We use a two-tailed test when our research question is: "Is the new treatment different from the old one?"

We are looking for an effect in either direction. The new drug could be better (lower lice count) or worse (higher lice count). We just want to know if it has any effect at all. 
1. The Hypothesis: H0: New = Old Vs. H1: New $\neq$ Old.
2. Where does the rejection region go? We split your 5% alpha (α=0.05) equally between both tails of the distribution. So, 2.5% in the left tail, and 2.5% in the right tail.
3. Confidence Interval: When calculating a 95% confidence interval, we use the t-critical value that leaves 2.5% in each tail. We get a range: Estimate±Margin of Error.

#### Example: A company develops a new feed. We want to know if salmon fed this new feed grow to a different average weight than salmon fed the standard feed. We don't care if it's heavier or lighter (though heavier is nice); We just need to know if the feed changes growth at all. 

## Pivotal Quanity Method: 
This method is the mathematical engine behind every classical confidence interval. It is a brilliant 3-step trick statisticians use to turn a random sample into a reliable confidence interval. We create a random number (the pivot) that contains the unknown parameter, but whose probability distribution is completely known and does NOT depend on that parameter. Then, we solve for the parameter.
### Step 1: Create a Pivot (A statistic that depends on the parameter, but has a fixed distribution)
A pivot (or pivotal quantity) is a function of three things:

1. The sample data (which is random).
2. The unknown parameter you care about (let's call it θ).
3. Known constants (like sample size n).

The magic property of a pivot is that even though it contains θ, its probability distribution is completely known and has no θ in it.
Let’s say we want the confidence interval for the true average weight (μ) of all salmon in a pen. We take a small sample (n=5) and calculate the sample mean ($\bar{x}$) and sample standard deviation (s). 

We create this pivot:
**Pivot** = $\frac{\bar{x} - \mu}{s/\sqrt{n}}$

1. Does it contain the unknown parameter? Yes, it contains μ.
2. What is its distribution? Gosset proved that this exact formula follows a t-distribution with n−1 degrees of freedom.
3. Does the t-distribution depend on μ? Absolutely not! Whether the true salmon weight is 5 lbs or 10 lbs, this pivot always follows the exact same t-distribution.

### Step 2: Solve the probability that the pivot lies between two fixed bounds
Because we know the exact distribution of the pivot, we can look up two numbers (percentiles) that trap the pivot with a certain probability, say 95%.
Let’s call the lower bound of the t-distribution $$-t_{0.025}$$ and the upper bound $$+t_{0.025}$$. We write: 
$$P\left(-t_{0.025} \leq \frac{\bar{x} - \mu}{s/\sqrt{n}} \leq +t_{0.025}\right) = 0.95$$

What does this mean in words?
"If I repeat this sampling process thousands of times, in 95% of those samples, my calculated pivot will fall between these two fixed numbers."

### Step 3: Rearrange (Solve) the inequality for the parameter μ
Now comes the algebraic magic. We have a probability statement about the pivot. We want a probability statement about the unknown parameter μ.

We manipulate the inequality to isolate μ in the middle:
We start with:
$-t \leq \frac{\bar{x} - \mu}{s/\sqrt{n}} \leq +t$

Multiply all sides by the standard error $(s/\sqrt{n})$:
$-t s/\sqrt{n} \leq \bar{x} - \mu \leq t s/\sqrt{n}$

Subtract ($\bar{x}$) from all sides:
$-\bar{x} - t\frac{s}{\sqrt{n}} \leq -\mu \leq -\bar{x} + t\frac{s}{\sqrt{n}}$

Multiply all sides by -1 (which flips the inequality signs):
$\bar{x} - t\frac{s}{\sqrt{n}} \leq \mu \leq \bar{x} + t\frac{s}{\sqrt{n}}$

The Final Result
We have just derived the confidence interval!

$P(\bar{x} - t \cdot SE \leq \mu \leq \bar{x} + t \cdot SE) = 0.95$

### Example: We will calculate a 95% confidence interval for the true average weight of Atlantic salmon in a massive net-pen, using a tiny sample of just 5 fish.
The Scenario
You randomly catch 5 salmon, weigh them (in kg), and get the following results:

Data: 
4.8, 5.1, 5.3, 5.5, 5.8

Sample size (n): 5

Sample mean ($\bar{x}$): 
(4.8+5.1+5.3+5.5+5.8)/5=5.3 kg

Sample standard deviation (s): 0.39 kg 

We want to know: What is the true average weight (μ) of all 10,000 salmon in the pen?

For $n-1=4$ degrees of freedom.

The standard error ($SE$) = $\frac{s}{\sqrt{n}} = \frac{0.39}{\sqrt{5}} = \frac{0.39}{2.236} \approx 0.174$.

So our specific pivot is: $\frac{5.3 - \mu}{0.174}$. This random number will follow a $t$-distribution with $df=4$.

### Step 2: Solve the probability that the pivot lies between fixed bounds

We want 95% confidence. So we ask: "Between which two fixed numbers does this pivot fall 95% of the time?"

We look up the t-table for $df=4$. For 95% confidence, we put 2.5% in the left tail and 2.5% in the right tail. The critical value is $t_{0.025} = 2.776$.

So, we write:

$$P\left(-2.776 \leq \frac{5.3 - \mu}{0.174} \leq 2.776\right) = 0.95$$

**Translation:** "Before we caught these fish, there was a 95% chance that our random sample would produce a pivot number between -2.776 and +2.776."

### Step 3: Solve the inequality for the parameter $\mu$

Now we do algebra to isolate $\mu$ in the middle of the inequality.

Start with:

$$-2.776 \leq \frac{5.3 - \mu}{0.174} \leq 2.776$$

Multiply all sides by 0.174 (the Standard Error):

$$-2.776 \times 0.174 \leq 5.3 - \mu \leq 2.776 \times 0.174$$

$$-0.483 \leq 5.3 - \mu \leq 0.483$$

Subtract 5.3 from all sides:

$$-5.3 - 0.483 \leq -\mu \leq -5.3 + 0.483$$

$$-5.783 \leq -\mu \leq -4.817$$

Multiply all sides by -1 (and remember to flip the inequality signs):

$$5.783 \geq \mu \geq 4.817$$

Rewrite it properly (lowest to highest):

$$4.817 \leq \mu \leq 5.783$$

### The Final Result

Your 95% confidence interval is **4.82 kg to 5.78 kg**.

**What do you tell the farm manager?**

> *"Based on our sample of 5 fish, we are 95% confident that the true average weight of every salmon in this pen is between 4.82 kg and 5.78 kg."*

### What if you had caught 100 fish instead?

Let's say $n = 100$, $\bar{x} = 5.3$, $s = 0.39$.

Standard Error = $\frac{0.39}{\sqrt{100}} = 0.039$.

$df = 99$. The t-critical value is $\approx 1.98$ (almost identical to the Normal $1.96$).

Our interval would be:

$$5.3 \pm (1.98 \times 0.039) = 5.22 \text{ to } 5.38$$

With more data, our pivot becomes incredibly precise, the interval shrinks, and the t-distribution automatically converges to the Normal distribution. This perfectly demonstrates **asymptotics**.

## Chi-Squared distribution
Imagine we take a standard normal distribution (mean 0, variance 1), reach in, and grab a random number (like +0.5). We square it. Now we grab another, square it, and add it to the first. You do this $k$ times.

The distribution of that sum of squared normal variables is the **Chi-Squared distribution** with $k$ degrees of freedom.

$$\chi^2_k = Z_1^2 + Z_2^2 + \cdots + Z_k^2$$

Where $Z_i \sim N(0, 1)$ are independent standard normal random variables.
### Why is it skewed and stuck at 0?

Because we are **squaring numbers**!

| Feature | Explanation |
|---------|-------------|
| **Stuck at 0** | We can never get a negative number (hence support starts at $0$) |
| **Pile-up near 0** | Most $Z$-scores are small (between $-1$ and $1$), so their squares are between $0$ and $1$. We get a massive pile-up of data just above $0$ |
| **Right skew** | Occasionally, we randomly grab a $Z$-score of $+2.5$, square it to $6.25$, which drags the mean to the right. This creates that long right-skewed tail (stretching to infinity) |

**Example:**

$$Z = 0.5 \rightarrow Z^2 = 0.25 \quad \text{(small)}$$
$$Z = 1.0 \rightarrow Z^2 = 1.00 \quad \text{(moderate)}$$
$$Z = 2.5 \rightarrow Z^2 = 6.25 \quad \text{(large, rare)}$$

### The "Degrees of Freedom" (df) and its Mean/Variance

We noted: Mean = df, Variance = 2 × df.

**Why does this matter?** It tells you the "spread" of the distribution.

- If $df = 2$, the mean is $2$, and the variance is $4$ (standard deviation = $2$). It is highly skewed.

- If $df = 100$, the mean is $100$, and the variance is $200$ (standard deviation $\approx 14.14$).

**Crucial observation:** As the degrees of freedom get larger, the mean and variance both grow, but the relative spread (the coefficient of variation) shrinks. The Chi-Squared distribution slowly morphs from a highly skewed lopsided blob into a shape that looks exactly like a Normal distribution (thanks to the Central Limit Theorem!). This is why we use it for small samples, but for huge samples, it behaves normally.

### The Famous Pivot: $\frac{(n-1)s^2}{\sigma^2}$

We wrote the formula perfectly:

$$\chi^2_{n-1} = \frac{(n-1) \times s^2}{\sigma^2}$$

Let's break this down into plain English, piece by piece, using salmon weights.

- **$\sigma^2$** = The true population variance. This is the "ground truth" of how much all salmon in the entire ocean weigh differently from each other. (We will never, ever know this number).

- **$s^2$** = The sample variance. This is the spread we calculated from our 5 randomly caught salmon.

- **$n-1$** = Our degrees of freedom.

- **$\frac{(n-1)s^2}{\sigma^2}$** = The ratio of "What we observed in our tiny sample" divided by "The hidden truth of the universe."

---

### What does this ratio actually mean?

- If our sample variance ($s^2$) happens to be exactly equal to the true population variance ($\sigma^2$), then the ratio equals $n-1$ (which is the mean of the distribution).

- If our sample, by bad luck, contains 5 salmon that are all almost exactly the same weight ($s^2$ is very small), then the ratio becomes small (less than $n-1$). The pivot falls into the left tail (near 0).

- If our sample, by bad luck, contains one giant salmon and one tiny salmon ($s^2$ is huge), then the ratio becomes large. The pivot falls into the far right tail.

### How we use this to build a Confidence Interval for Variance

Remember the 3-step process we used for the t-distribution? We do exactly the same thing here, but because the Chi-Squared distribution is **skewed**, we can't use a symmetric $\pm$ like we did for the mean. We have to grab two different percentiles from the table.

---

#### Step 1: The Pivot

$$\text{Pivot} = \frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$$

---

#### Step 2: Trap the pivot between two fixed bounds with 95% probability

Because it's skewed, we cut off 2.5% in the left tail (call this $\chi^2_{0.975}$) and 2.5% in the right tail (call this $\chi^2_{0.025}$).

We write:

$$P\left(\chi^2_{0.975} \leq \frac{(n-1)s^2}{\sigma^2} \leq \chi^2_{0.025}\right) = 0.95$$

---

#### Step 3: Solve the inequality for $\sigma^2$ (The true variance)

Using algebra, we flip the fractions to isolate $\sigma^2$ in the middle:

$$\frac{(n-1)s^2}{\chi^2_{0.025}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{0.975}}$$

---

### Salmon Example (Confidence Interval for Weight Variance)

We caught 5 salmon ($df = 4$). We calculate the sample variance: $s^2 = 0.152$ (which is $0.39^2$).

We want a 95% confidence interval for the true variance of salmon weights ($\sigma^2$).

Look up the Chi-Squared table for $df = 4$:

- The 2.5% quantile (left tail, $\chi^2_{0.975}$) = **0.484**
- The 97.5% quantile (right tail, $\chi^2_{0.025}$) = **11.143**

Plug these into our formula:

**Lower bound:** 
$$\frac{4 \times 0.152}{11.143} = \frac{0.608}{11.143} \approx 0.054$$

**Upper bound:** 
$$\frac{4 \times 0.152}{0.484} = \frac{0.608}{0.484} \approx 1.256$$

---

### Final Result

We are **95% confident** that the true variance of salmon weights in the entire pen is between **0.054 kg** and **1.256 kg**.

Notice how massive that interval is (0.054 to 1.256)? **It's huge!**

That is the harsh reality of the Chi-Squared distribution. It is incredibly volatile for small samples.

To get a precise estimate of variance, you need massive sample sizes. The Chi-Squared distribution has a variance of $2 \times df$. For $df = 4$, the standard deviation is $\sqrt{8} \approx 2.8$, which is almost as large as the mean ($4$)! The uncertainty is enormous.

## At what conditions do we use n as degree of freedom and use n-1 as degree of freedom?
It depends entirely on whether We are using the **true population mean** ($\mu$) or if we had to **estimate the mean** ($\bar{x}$) from our data.

Here is the **golden rule**:

> **We use $df = n$** when we are working with the **TRUE** population mean ($\mu$) and we know it in advance.

> **We use $df = n - 1$** when we have to **ESTIMATE** the population mean ($\bar{x}$) from our sample first.

Let's break down exactly why this happens using your salmon farm.
### 1. The Condition for df = n (We know the true mean $\mu$)

Imagine you are a salmon farmer, and you have a magical, perfect scale that tells you the true average weight of every salmon in the ocean is exactly $\mu = 5.0$ kg.

You randomly catch $n = 5$ salmon to test how much their weights vary around this known 5.0 kg mark. You calculate the variance using this formula:

$$\text{Variance} = \frac{\sum_{i=1}^n (X_i - \mu)^2}{n}$$

Because we are using the known center ($\mu$), none of our data points are "wasting" information. Every single one of the 5 salmon is completely free to be any weight it wants. They are all independent.

**Degrees of freedom = n = 5.**

In this case, if we square these 5 deviations and add them up, the resulting pivot strictly follows a Chi-Squared distribution with df = n.

---

### 2. The Condition for df = n - 1 (You estimate the mean $\bar{x}$)

Now, let's be realistic. We do not know the true population mean ($\mu$). We have to catch 5 salmon, weigh them, and calculate the sample mean ($\bar{x}$) to guess what $\mu$ is.

We calculate the sample variance using this formula:

$$s^2 = \frac{\sum_{i=1}^n (X_i - \bar{x})^2}{n-1}$$

**Why do we divide by $n-1$ here, and why does the Chi-Squared pivot use $n-1$?**

Because we have lost a piece of information.

**The Mathematical Proof:**

When we calculate $\bar{x}$, you impose a constraint on your data:

$$\sum_{i=1}^n (X_i - \bar{x}) = 0$$

This means:
- We have $n$ observations
- But they must satisfy 1 constraint (the sum of deviations is zero)
- Therefore, only $n-1$ observations are free to vary

**The Salmon Example:**

We catch 5 salmon. Their weights are: 4.8, 5.1, 5.3, 5.5, and ?

We calculate the average of the first 4 weights:

$$\frac{4.8 + 5.1 + 5.3 + 5.5}{4} = 5.175$$

We want total sample mean to be exactly $\bar{x} = 5.3$ kg.

**Question:** What must the weight of the 5th salmon be?

**Answer:** It is forced. It must be exactly 5.8 kg. It cannot vary freely.

In a sample of 5, once you know the sample mean ($\bar{x}$) and 4 of the weights, the 5th weight is completely determined. Only 4 of the salmon are truly free to vary.

**Degrees of freedom = n - 1 = 4.**

Because we lost that freedom, your sample variance ($s^2$) will, on average, be slightly smaller than the true population variance ($\sigma^2$). To fix this, we divide by $n-1$ (which makes $s^2$ a tiny bit bigger), and we use the Chi-Squared distribution with df = n - 1.

---

### Why Dividing by $n-1$ Fixes the Problem

$$E[s^2] = E\left[\frac{\sum (X_i - \bar{x})^2}{n-1}\right] = \sigma^2$$

Dividing by $n-1$ makes $s^2$ an **unbiased estimator** of $\sigma^2$!

### The Same Rule Applies to the t-distribution!

This rule isn't just for Chi-Squared; it applies everywhere.

- **t-distribution for a single mean:** You have to estimate $\mu$ using $\bar{x}$. Therefore, you lose 1 degree of freedom. **$df = n - 1$.**

- **Comparing two independent means (two-sample t-test):** You have to estimate two means ($\bar{x}_1$ and $\bar{x}_2$). You lose 2 degrees of freedom. **$df = n_1 + n_2 - 2$.**

- **Linear Regression (Estimating a slope and intercept):** You have to estimate two parameters (the slope and the intercept) to draw your best-fit line. You lose 2 degrees of freedom. **$df = n - 2$.**

### Why Use MLE (Dividing by $n$) Instead of $n-1$?

If $n-1$ gives us an unbiased estimate, why would anyone ever use the MLE (which divides by $n$)?

**Because of Asymptotics (large samples)!**

- When $n$ is small (e.g., $n=5$): The difference is huge. Dividing by $n$ gives you only $0.8$ of the truth (bad bias). Dividing by $n-1$ gives you the exact truth on average.

- When $n$ is huge (e.g., $n=1,000$): Dividing by $n$ gives you $\frac{999}{1000} = 0.999$ of the truth. The bias is practically zero!

Statisticians prefer the MLE (dividing by $n$) for large samples because it has better **"asymptotic properties"** (it is more efficient and consistent). But for small samples, we absolutely must use $n-1$ to avoid grossly underestimating our true variance!

**Golden Rule: When we calculate variance, we have $n$ data points. But we already **"spent"** 1 piece of information to calculate $\bar{x}$. Therefore, only $n-1$ of our data points are actually free to vary. Because only $n-1$ pieces of information are contributing to the variance, we divide by $n-1$. Dividing by $n$ would be like saying we have more information than we actually do, which makes our estimate falsely precise (and biased).**

## Gamma Distribution
Gamma distribution is the bigger, more flexible parent of the Chi-Squared distribution.

If the Chi-Squared distribution is a specific sports car, the Gamma distribution is the SUV that can be configured to do a hundred different things.
### The Physical Meaning: "The Waiting Time" Distribution
The Gamma distribution is the ultimate "waiting time" distribution.

Imagine you are a salmon farmer, and you are waiting for sea lice to attach to a fish. Lice arrive randomly at a constant average rate (say, 2 lice per hour).

How long do you wait for exactly 1 louse to arrive? That follows an Exponential distribution.

How long do you wait for exactly 5 lice to arrive? That sum of 5 independent waiting times follows a Gamma distribution!

In fact, the Exponential distribution is just a special case of the Gamma distribution (when the "shape" parameter equals 1).

### The Parameters (The "Knobs" we can turn)

The Gamma distribution has two parameters that control its shape, scale, and location. Statisticians use two different common parameterizations.

The parameters are: **Shape ($\alpha$)** and **Rate ($\beta$)**.

- **Shape ($\alpha$):** This dictates the "number of events" you are waiting for. It must be a positive number.

- **Rate ($\beta$):** This dictates the "speed" at which events happen. A higher rate means events happen faster, so the waiting time shrinks.

### The Probability Density Function (PDF)

Here is the mathematical formula for the Gamma PDF (using the Shape/Rate parameterization):

$$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \quad \text{for } x > 0$$

Let's decode this scary-looking equation:

- **$x^{\alpha-1}$** : This controls the initial rise of the curve.
  - If $\alpha = 1$, it's flat at the start (Exponential).
  - If $\alpha > 1$, the curve starts at 0, rises to a peak, and then falls.

- **$e^{-\beta x}$** : This is the "decay" factor that eventually drags the curve down to zero as $x$ gets large.

- **$\Gamma(\alpha)$** : This is the **Gamma Function** (the distribution's namesake). It is just a mathematical constant in the denominator that ensures the total area under the curve equals 1. (Think of it as the factorial function for non-integers: $\Gamma(n) = (n-1)!$).

### The Mean and Variance

Just like the Chi-Squared distribution, the Gamma distribution is right-skewed (starts at 0, stretches to infinity). Its mean and variance are beautifully simple:

$$\text{Mean} = \frac{\alpha}{\beta}$$

$$\text{Variance} = \frac{\alpha}{\beta^2}$$

---

### Check this against the Chi-Squared

A Chi-Squared distribution with $k$ degrees of freedom is actually a **Gamma distribution** with:

$$\alpha = \frac{k}{2} \quad \text{and} \quad \beta = \frac{1}{2}$$

Let's verify:

**Mean:**
$$\frac{\alpha}{\beta} = \frac{k/2}{1/2} = k$$

(Matches the Chi-Squared mean of $k$!)

**Variance:**
$$\frac{\alpha}{\beta^2} = \frac{k/2}{(1/2)^2} = \frac{k/2}{1/4} = 2k$$

(Matches the Chi-Squared variance of $2k$!)
### How the Shape ($\alpha$) Changes the Graph

This is the coolest part. The Gamma distribution can look completely different depending on the shape parameter:

- **$\alpha = 1$:** The curve is a perfect Exponential decay. Highest at 0, drops off quickly. (Waiting for the first event).

- **$\alpha = 2$:** The curve starts at 0, shoots up to a peak, and falls slowly. (Waiting for the second event. You cannot get 2 events at exactly time 0, so the curve starts at 0).

- **$\alpha = 10$:** The curve looks almost perfectly like a Normal distribution (bell curve)! This is due to the Central Limit Theorem—summing up 10 waiting times gives you a symmetrical blob.

### The Gamma Distribution and Your Salmon Data (The Connection!)

Remember the Chi-Squared pivot we used for the confidence interval of variance?

$$\frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$$

Since a Chi-Squared is just a Gamma with $\alpha = (n-1)/2$ and $\beta = 1/2$, we can actually say:

> **The sampling distribution of your sample variance follows a Gamma distribution!**

This means:

If you collected thousands of salmon samples, calculated the variance for each, and plotted them, the histogram would perfectly match a Gamma curve (which is heavily right-skewed for small samples, but looks Normal for large samples).

This perfectly explains why your confidence intervals for variance are so wide for small samples—the Gamma/Chi-Squared distribution has a long tail stretching out to the right, meaning your sample variance can occasionally be wildly larger than the true variance.

### Real-World Uses of Gamma (Outside of Variance)

Because the Gamma distribution models positive, continuous, right-skewed data, it is used everywhere:

- **Rainfall:** The amount of daily rainfall is never negative, often has many days with 0 rain, and occasionally has massive downpours. Gamma models this perfectly.

- **Insurance claims:** Most claims are small, but occasionally there is a catastrophic, massive claim.

- **Salmon growth rates:** If you measure how long it takes for a salmon to reach 5 kg, the times are positive, skewed (most take average time, a few take forever), and fit a Gamma distribution beautifully.

## Gaussian Data and Gaussian Distribution
A Gaussian distribution is the famous **"bell curve"** (also called the **Normal distribution**).

Gaussian data simply means data that, when plotted on a histogram, roughly follows that bell-shaped curve.

### 1. What does Gaussian Data actually look like?

If our data is Gaussian (Normally distributed), it follows three strict rules:

- **It is Symmetric:** The left half of the histogram is a perfect mirror image of the right half. The mean, median, and mode are all exactly the same number.

- **It follows the 68-95-99.7 Rule:**
  - 68% of our data falls within $\pm 1$ standard deviation of the mean.
  - 95% falls within $\pm 2$ standard deviations.
  - 99.7% falls within $\pm 3$ standard deviations.

- **It has no "tails":** The curve smoothly approaches zero as we go to infinity in both directions (meaning extreme outliers are incredibly rare).

---

### Example of Gaussian Data

The weights of 1,000 adult salmon raised in the exact same pen, eating the exact same feed, at the exact same age.

- Most will cluster around the average (say, 5.0 kg).
- A few will be slightly lighter (4.5 kg) or slightly heavier (5.5 kg).
- A very tiny fraction will be freakishly small (3.0 kg) or freakishly huge (7.0 kg).

If we plot this, we get a beautiful, symmetric bell curve.

---

### 2. The Catch: Not everything is Gaussian!

In nature and aquaculture, many things are not bell-shaped. Here are classic examples of non-Gaussian (often called "heavy-tailed" or "skewed") data in our salmon farm:

- **Sea lice counts per fish:** Most fish have 0 or 1 louse, but a few fish are absolutely covered in 50 lice. The histogram is slammed against zero with a massive right tail. (This follows a Negative Binomial or Poisson distribution, not Gaussian!).

- **Time until a fish dies:** We put a disease in a tank. Most fish die around day 5, but some die immediately, and a few tough fish survive for 20 days. The curve is skewed right. (This follows a Weibull or Gamma distribution).

- **Daily revenue:** Most days we sell average fish, but once a month we sell a massive bulk order to a giant grocery chain. The data is full of extreme spikes.

---

### 3. Why does "Gaussian Data" matter so much?

This is the most important part of our question. If our data is Gaussian, we get to use parametric tests (t-tests, ANOVAs, and the Chi-Squared variance tests we just discussed).

- The math for these tests is easy and powerful.
- The confidence intervals we calculated earlier rely on the assumption that our sample mean comes from a Gaussian distribution.

But here is the magic (and why we don't need to panic!):

> **Thanks to the Central Limit Theorem (Asymptotics!), our sample mean will become Gaussian even if our raw data is horribly non-Gaussian, as long as our sample size is large enough (usually $n > 30$).**

- Raw sea lice counts (non-Gaussian): Weird, slammed against zero.
- The average lice count from 100 samples (Gaussian): Perfectly bell-shaped!

Because of this, we don't actually require the raw data to be Gaussian for most tests—we just require the sample means to be Gaussian, which happens automatically when $n$ is large.

---

### 4. How to check if our data is Gaussian (The Tools)

Before we blindly use a t-test or a Chi-Squared test for variance on a small sample (say, $n = 10$), we should check if our data is roughly Gaussian. Here is how:

**Method 1: The Histogram (Visual)**

Plot our data. Does it look like a symmetric bell? Or is it squished to one side?

**Method 2: The Q-Q Plot (The Statistician's Favorite)**

This is a scatterplot where we plot our actual data against the theoretical quantiles of a perfect Gaussian distribution.

- If the points fall roughly along a straight diagonal line → Our data is Gaussian.
- If the points curve upwards like a J-shape, or form an S-shape → Our data is not Gaussian.

**Method 3: The Shapiro-Wilk Test (Statistical)**

This is a formal hypothesis test.

$$H_0: \text{The data is Gaussian}$$

- If the p-value is high ($> 0.05$), we fail to reject the null—we assume it is Gaussian.
- If the p-value is low ($< 0.05$), we reject the null—our data is not Gaussian.

---

### 5. What do we do if our data is NOT Gaussian?

If our raw data is violently non-Gaussian (like sea lice counts) and we have a small sample size (so the Central Limit Theorem can't save us), we have two choices:

1. **Transform the data:** Take the logarithm (log) or square root of every data point. Often, log-transforming sea lice counts turns a skewed blob into a beautiful bell curve. We then run our t-test on the logged data.

2. **Use a Non-Parametric test:** These are "distribution-free" tests (like the Wilcoxon test) that don't assume Gaussian data at all. They work by ranking our data instead of using the raw numbers. They are safer, but slightly less powerful.

## t-distribution
The t-distribution is a bell-shaped curve, just like the Normal distribution. However, it has one crucial difference: **It has fatter tails.**

Imagine two archers:

- The **Normal distribution** is a perfect, world-class archer. Their arrows always land within a tight 2-inch circle.

- The **t-distribution** is a good, but inexperienced, archer. Their arrows usually land close to the bullseye, but because they are less consistent, they occasionally shoot an arrow wildly off into the 10-point ring or completely miss the target.

Because the t-distribution has fatter tails, it pulls probability away from the center and pushes it out to the extremes. This means:

> To capture 95% of the data, the t-distribution requires a wider interval than the Normal distribution.

Mathematically, the t-distribution is the ratio of two things:

1. A Standard Normal variable ($Z$).
2. The square root of a Chi-Squared variable divided by its degrees of freedom ($\chi^2_{df}/df$).

The formula looks like this:

$$t = \frac{Z}{\sqrt{\chi^2_{df}/df}}$$

### What does this mean in plain English?

It means the t-distribution naturally arises whenever we are trying to estimate the mean of a population, but we don't know the true standard deviation ($\sigma$) and have to guess it using our sample's standard deviation ($s$).

Because $s$ is a random guess (based on our sample), it introduces extra "noise" into our calculation. The t-distribution mathematically accounts for that extra noise by stretching out the tails.

### The "Degrees of Freedom" (df) Knob

The t-distribution has one single parameter: the Degrees of Freedom ($df$).

- When $df$ is small (like $df = 2$): The tails are massively fat, and the peak is very flat. The curve looks more like a squashed, wide blob than a bell.

- When $df$ gets larger (like $df = 30$): The tails shrink, the peak gets taller, and the curve looks almost exactly like a Normal distribution.

- When $df = \infty$ (infinity): The t-distribution becomes identical to the Standard Normal distribution (mean 0, variance 1).
### How it connects to your Salmon Farm (The Pivot)

Remember the pivotal quantity we built for the confidence interval of the mean?

$$\text{Pivot} = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

This exact formula follows Gosset's t-distribution with $df = n - 1$.

Because of this, we use the t-distribution to build confidence intervals for small samples:

$$\bar{x} \pm t_{n-1, \alpha/2} \times \frac{s}{\sqrt{n}}$$

---

### The Salmon Example

You catch $n = 5$ salmon, so $df = 4$.

- If you wrongly used the Normal distribution, your 95% critical value would be **1.96**.
- Because you correctly use Gosset's t-distribution with $df = 4$, your critical value is **2.776**.

**Result:** The t-distribution forces you to build a much wider, more honest confidence interval. It basically says:

## Standard Normal Distribution (Z value) (N(0,1))
When a Normal distribution has a mean of $0$ and a standard deviation of $1$, we give it a special name: the **Standard Normal Distribution** (often called the **$Z$-distribution**).

### 1. What does a "Mean of 0" actually mean?

A mean of 0 does not mean that all your values are zero or negative. It simply means that **zero is the center of the universe** for this measurement.

Imagine a weighing scale that is perfectly calibrated to measure change rather than total weight:

- We weigh a salmon before the experiment (5.0 kg).
- We feed it your new diet.
- We weigh it after the experiment (5.5 kg).
- We calculate the difference: $5.5 - 5.0 = +0.5$ kg.

Now, imagine we do this for 1,000 salmon. You plot the differences on a histogram.

- Some salmon gained weight ($+0.2, +0.8$).
- Some salmon lost weight ($-0.3, -0.1$).

If the new feed does absolutely nothing, the gains and losses will cancel out. The average of all these differences will be exactly 0.

**In plain English:** A mean of 0 means that 0 is the "baseline" or "no-effect" point. Values above 0 represent an increase; values below 0 represent a decrease. The bell curve is perfectly centered right on that baseline.

---

### 2. What does a "Standard Deviation of 1" actually mean?

A standard deviation of 1 is just a ruler that we artificially created to make math easier.

In the real world, salmon weights might have a standard deviation of 0.8 kg, and sea lice counts might have a standard deviation of 5.2 lice. These are different "rulers" (units).

When we subtract the mean and divide by the standard deviation (which is called **standardizing** or calculating a **Z-score**), we are throwing away the original units (kg, lice, dollars) and converting everything into a universal ruler called **"standard deviations away from the mean."**

- A value of $+1$ means it is exactly 1 standard deviation above the mean.
- A value of $-2$ means it is exactly 2 standard deviations below the mean.
- A value of $0$ means it is exactly equal to the mean.

---

### 3. The "Standard Normal" Distribution $N(0,1)$

When we write $X \sim N(0,1)$, we are saying:

> *"X follows a Normal distribution that is perfectly centered at zero, and the units on the x-axis are measured in 'standard deviations.'"*

**Why do statisticians love this so much?**

Because every single Normal distribution in the universe can be turned into $N(0,1)$ using a simple formula:

$$Z = \frac{X - \mu}{\sigma}$$

---

### Salmon Example

Let's say the weights of your adult salmon follow a Normal distribution with a mean of 5.0 kg and a standard deviation of 1.5 kg. You catch a random salmon that weighs 6.5 kg.

What is its Z-score?

$$Z = \frac{6.5 - 5.0}{1.5} = \frac{1.5}{1.5} = 1$$

**Translation:** A 6.5 kg salmon is exactly 1 standard deviation above the average.

Instead of carrying around the messy numbers "5.0" and "1.5" for every calculation, we just say it's a $Z$ of 1, and we look up "1" in our standard Normal table to find that about 84% of salmon are lighter than it.

---

### 4. The Boring (But mathematically true) Facts about $N(0,1)$

**The PDF:**

$$f(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$$

Notice that the mean ($\mu$) and standard deviation ($\sigma$) have completely vanished from the formula! They are replaced by 0 and 1.

**Symmetry:** Because the mean is 0, the curve is perfectly symmetric. The probability of getting a value less than $-1.96$ is exactly the same as getting a value greater than $+1.96$ (which is 2.5% each).

**The 68-95-99.7 Rule:**

- 68% of the data lies between $-1$ and $+1$.
- 95% lies between $-2$ and $+2$ (actually 1.96, but roughly 2).
- 99.7% lies between $-3$ and $+3$.

---

### 5. Can a "mean" actually be zero in real life?

Yes! But only if we are measuring **relative** things, not **absolute** things.

- **Absolute measurements** (like salmon weight in kg, or human height in cm) can never have a mean of zero, because you can't have negative height or negative weight.

- **Relative measurements** (like weight gain, profit/loss, temperature in Celsius, or standardized Z-scores) can and do have a mean of zero all the time!

**For example:**

- The daily change in the S&P 500 stock index over a long period has a mean of roughly 0.
- The difference in blood pressure before and after taking a placebo pill has a mean of 0.
- If we standardize the exam scores of your entire class, the resulting Z-scores will have a mean of exactly 0 and a standard deviation of exactly 1 by construction.

### Cohen's *d* (the standardized effect size)

The ratio:

$$\frac{\text{Population Mean}}{\text{Standard Deviation}} = \frac{\mu}{\sigma}$$

...is the **Signal-to-Noise Ratio**.

It tells us how big our "discovery" is, relative to the natural chaos of our system. It strips away the units (kg, dollars, lice) and tells us the practical size of an effect, completely independent of our sample size.

Let me break down exactly what this ratio means in plain English, and why it is arguably more important than the p-value.

---

### 1. The Intuition: The "Whisper in a Hurricane"

Imagine we are standing in a crowded salmon processing plant.

- **The Signal ($\mu$):** Our friend whispers something to us from 2 feet away. That whisper has a certain volume (say, 20 decibels).

- **The Noise ($\sigma$):** The machines, the water pumps, and the workers are creating a constant roar of background noise (say, 100 decibels).

What is our chance of hearing the whisper? It is almost zero. The noise completely drowns out the signal. The ratio of $\mu/\sigma$ is $20/100 = 0.2$. Very small.

Now, imagine our friend uses a megaphone (Signal = 120 decibels) in the exact same factory (Noise = 100 decibels). The ratio is $120/100 = 1.2$.

That ratio is exactly what $\mu/\sigma$ is! It measures how far the "center" of our effect is from zero, measured in units of the natural background noise.

---

### 2. Let's translate this to our Salmon Farm

**Scenario A (A Tiny Effect):**

We test a new vitamin supplement. We find that it increases salmon growth by 0.1 kg ($\mu = 0.1$).

However, salmon naturally have a huge variation in weight—some are just naturally big eaters, some are small. The standard deviation is 1.0 kg ($\sigma = 1.0$).

$$\frac{\mu}{\sigma} = \frac{0.1}{1.0} = 0.1$$

**What does 0.1 mean?**

It means the average growth from our supplement is only 0.1 standard deviations away from zero. The "signal" is completely buried inside the natural randomness of the fish. If we feed 100 fish this supplement, we will barely notice the difference because a random, untreated fish varies more than that on its own.

**Scenario B (A Massive Effect):**

We test a miracle growth hormone. It increases salmon growth by 1.5 kg ($\mu = 1.5$). The natural standard deviation is still 1.0 kg ($\sigma = 1.0$).

$$\frac{\mu}{\sigma} = \frac{1.5}{1.0} = 1.5$$

**What does 1.5 mean?**

It means our "signal" is 1.5 times bigger than the natural "noise." The effect is massive. If we feed this to fish, we can literally look at the tank and see that these fish are giants compared to the others. The effect is so large it punches through the randomness.

---

### 3. The Two Faces of this Ratio (The Catch!)

Here is where things get incredibly subtle. The exact same ratio $\mu/\sigma$ does two completely different jobs depending on how we use it:

**Role 1: The Non-Centrality Parameter (Signal we expect to see)**

When we are designing an experiment (before we collect data), this ratio is the true, real-world effect we are trying to catch. We call this $\delta$.

| $\delta$ | Interpretation |
|----------|----------------|
| $\delta = 0.2$ | A tiny, barely noticeable effect |
| $\delta = 0.5$ | A moderate, noticeable effect |
| $\delta = 0.8$ | A large, obvious effect |

We use this to calculate **Statistical Power**: *"How many fish do we need to catch to be sure we detect this 0.5 effect?"*

**Role 2: The "Z-score" (Signal we observed in our data)**

When we have already collected our data, we calculate the sample mean ($\bar{x}$) and sample standard deviation ($s$). The ratio $\bar{x}/s$ tells us how many standard deviations our observed result is away from zero. This is our observed effect size.

**But wait!** We usually divide by the Standard Error ($s/\sqrt{n}$) for a t-test, not just $s$:

| Ratio | What it tells us |
|-------|------------------|
| $\frac{\bar{x}}{s}$ | How big is the effect in the population? |
| $\frac{\bar{x}}{s/\sqrt{n}}$ | How confident are we that this effect isn't due to random luck? (This is the **t-statistic**) |

---

### 4. The Golden Rule of Statistics (Why this ratio saves us)

There is a famous saying in statistics: **"Statistical significance is not the same as practical significance."**

**If our sample size ($n$) is huge:**
- We can get a statistically significant p-value (e.g., $p < 0.0001$) even when $\mu/\sigma = 0.01$.
- We proved the feed works, but it adds 0.01 kg per fish. Who cares? It's not worth the money.

**If our sample size ($n$) is tiny:**
- We might get a p-value of 0.08 (not significant) even when $\mu/\sigma = 1.5$.
- We failed the math test, but the effect is so massive that any farmer looking at the tank knows it works.

The ratio $\mu/\sigma$ protects us from these traps. It forces us to ask: *"Forget the p-value. Is this effect actually large enough to matter in the real world?"*

---

### Summary Table

| Effect Size ($d$) | Interpretation | Real-World Example |
|-------------------|----------------|-------------------|
| $d = 0.2$ | Small | Barely noticeable |
| $d = 0.5$ | Medium | Noticeable |
| $d = 0.8$ | Large | Obvious |
| $d = 1.5$ | Very Large | Massive, can't miss it |

**The Bottom Line:** Cohen's $d$ tells us the **practical significance** of our results. It strips away sample size and tells us: *"Is this effect big enough to care about?"*

## Parameter in Statistics
A parameter is a fixed, usually unknown number that describes the entire population you are studying.

It is the "DNA" of the population. We cannot see it, we cannot measure every single individual to find it, but it is the underlying truth that governs how your data behaves.

### Salmon Example:

- **Parameter ($\mu$):** The true average weight of all 1,000,000 salmon in the ocean. We will never catch all of them. It is a fixed number (say, 5.0 kg), but we don't know it.

- **Statistic ($\bar{x}$):** The average weight of the 20 salmon we just caught in our net (say, 4.8 kg). We do know this number. We use 4.8 kg as our estimate (guess) for the hidden parameter $\mu$.

Every probability distribution is defined by its **parameters**. The parameters are the **"knobs"** that change the shape, center, and spread of the distribution.

| Distribution | Parameters (The Unknown Truths) | What they control |
|--------------|--------------------------------|-------------------|
| **Normal (Gaussian)** | $\mu$ (mean) and $\sigma$ (standard deviation) | $\mu$ = where the bell curve sits. $\sigma$ = how wide the bell curve is. |
| **Binomial** | $n$ (trials) and $p$ (probability of success) | $p$ = the true underlying chance of something happening (e.g., the true mortality rate of salmon). |
| **Poisson** | $\lambda$ (rate) | The true average number of events (e.g., sea lice) per unit of time/space. |
| **Gamma** | $\alpha$ (shape) and $\beta$ (scale) | Controls the skewness and the spread of waiting times. |
| **Linear Regression** | $\beta_0$ (intercept) and $\beta_1$ (slope) | The true relationship between two variables (e.g., how much weight increases for every extra cm of length). |

In the **Frequentist** school of statistics (which we have been learning with t-tests and confidence intervals), we believe that **parameters are fixed, unchanging numbers**.

The true average weight of the salmon is 5.0 kg. It doesn't change. It is a single, solid rock of truth.

The only reason we don't know it is because we can't catch all the salmon. The randomness comes from our **sampling**, not from the parameter itself. If we catch a different set of 20 fish, our statistic ($\bar{x}$) changes, but the parameter ($\mu$) stays exactly the same.

When we use a statistic to guess a parameter, we put a **"hat"** (^) on the Greek letter to show it is an estimate.

- $\mu$ = The true, unknown average.
- $\hat{\mu}$ (read as **"mu-hat"**) = Our best guess for the average (which is usually just $\bar{x}$, the sample mean).

---

### Salmon Example

We want to know the true sea lice infestation rate ($p$). We sample 100 fish and find 10 have lice.

- **The Parameter:** $p$ = The true proportion of all fish in the pen with lice. (Hidden).
- **The Estimate:** $\hat{p} = 10/100 = 0.10$. We guess that 10% of all fish have lice.

In modern machine learning or computer science, people often use the word **"parameter"** differently.

- **In statistics:** A parameter is a fixed, hidden truth about nature.

- **In AI (like neural networks):** A "parameter" is just a weight or a number inside the algorithm that gets updated as the computer learns. There might be billions of them, and they don't necessarily represent a biological "truth"—they are just mathematical knobs to make the computer spit out the right answer.

**Golden rule: The parameter is the target. The statistic is the arrow you shoot at it. You never hit the bullseye perfectly, but you try to get as close as possible.** 

## Maximum Likelihood Estimation (MLE)
### Maximum Likelihood Estimation (MLE)

It is the single most important tool in a statistician's toolbox. If statistics is about finding the "hidden truth" (the parameters) from our data, MLE is the mathematical search engine that finds the most plausible value for that truth.

MLE is a method that finds the value of the unknown parameter (e.g., the true average weight) that makes the data we actually observed as likely as possible.

---

### The Intuition: The Blindfolded Archer

Imagine we are blindfolded and throw a dart at a wall. We hear it hit the wall. We take off the blindfold and see the dart stuck in the wall.

Now, someone asks us: *"Where do you think the bullseye (the center of the target) is located?"*

We would point directly at the dart.

**Why?** Because if the bullseye were anywhere else, the probability of our dart landing exactly where it did would be lower. The spot where the dart landed is the Maximum Likelihood Estimate for the bullseye.

**In statistics:**

- **The dart** = Our sample data (the 5 salmon we caught).
- **The bullseye** = The unknown parameter (the true average weight of all salmon).
- **The MLE** = The value of the parameter that places the highest probability on the data we actually observed.

---

### How MLE Works (The Step-by-Step Process)

Let's say we catch 5 salmon and their average weight is 5.3 kg. We want to know the true population mean ($\mu$).

**Step 1: Write the Likelihood Function**

We write a mathematical formula that answers: *"If the true mean is $\mu$, how likely is it that I would get a sample average of 5.3 kg?"*

This creates a curve (the Likelihood Function).

**Step 2: Find the Peak (Maximize)**

We use calculus (or a computer) to find the peak of that curve—the single value of $\mu$ that makes our observed 5.3 kg the most probable.

**Step 3: The Answer**

The peak will always be at $\mu = 5.3$ kg. The MLE for the population mean is simply the sample mean ($\bar{x}$).

---

### The Mathematical Definition

Formally, if we have a likelihood function $L(\theta \mid \text{data})$, the MLE (written as $\hat{\theta}$) is:

$$\hat{\theta}_{MLE} = \underset{\theta}{\arg\max} \, L(\theta \mid \text{data})$$

**Translation:** *"Find the value of $\theta$ that makes the likelihood function as big as possible."*

---

### Why We Use Log-Likelihood

Because likelihood functions often involve multiplying many small probabilities (which creates tiny numbers), statisticians usually maximize the **Log-Likelihood** ($\log L$) instead.

The logarithm turns multiplication into addition, making the math vastly easier—but it gives the exact same answer because the logarithm is a strictly increasing function.

$$\log L(\theta \mid \text{data}) = \sum_{i=1}^n \log f(x_i \mid \theta)$$

---

### MLEs for Common Parameters

| Parameter | What it represents | The MLE (The Best Guess) |
|-----------|-------------------|--------------------------|
| **Mean ($\mu$)** | True average weight of all salmon | The sample average: $\hat{\mu} = \bar{x}$ |
| **Variance ($\sigma^2$)** | True spread of salmon weights | $\hat{\sigma}^2 = \frac{1}{n}\sum (x_i - \bar{x})^2$ (Divides by $n$, not $n-1$!) |
| **Proportion ($p$)** | True fraction of salmon with sea lice | $\hat{p} = \frac{\text{Number with lice}}{\text{Total sampled}}$ |
| **Poisson Rate ($\lambda$)** | True average number of lice per fish | $\hat{\lambda} = \bar{x}$ |

---

### The Three Magical Properties of MLE (Asymptotics!)

Remember our discussion about Asymptotics (what happens when sample size gets huge)? MLE has three magical properties that make it the gold standard of statistics:

| Property | Meaning | Salmon Example |
|----------|---------|----------------|
| **Consistency** | As we catch more fish, MLE gets closer to the true parameter | Catch 1,000 fish, and $\hat{\mu}$ is almost certainly 5.000 kg |
| **Efficiency** | Among all estimators, MLE has the smallest possible variance | No other estimator gives a tighter, more precise guess |
| **Normality** | As $n \to \infty$, MLE becomes Normally distributed | We can easily build confidence intervals! |

---

### The MLE vs. Unbiased Estimator Trade-off

Notice in the table above that the MLE for variance divides by $n$, not $n-1$.

| Estimator | Formula | Bias | Consistency |
|-----------|---------|------|-------------|
| **MLE for variance** | $\hat{\sigma}^2 = \frac{1}{n}\sum (x_i - \bar{x})^2$ | Biased (underestimates) | Consistent |
| **Unbiased estimate** | $s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$ | Unbiased | Consistent |

This means the MLE for variance is **biased**. On average, it slightly underestimates the true population variance (because it doesn't account for the fact that we estimated the mean using the same data).

**MLE for variance:**
$$\hat{\sigma}^2 = \frac{1}{n}\sum (x_i - \bar{x})^2 \quad \text{(Biased, but consistent)}$$

**Unbiased estimate:**
$$s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2 \quad \text{(Unbiased, but not the MLE)}$$

---

### The Classic Trade-off

| | MLE | Unbiased Estimator |
|--|-----|-------------------|
| **Variance** | Divides by $n$ | Divides by $n-1$ |
| **Bias** | Biased (slightly underestimates) | Unbiased |
| **Variance of estimator** | Smaller | Larger |
| **Best for** | Large samples | Small samples |

MLE gives you the absolute peak of the likelihood curve, but if you want an unbiased estimate, you have to tweak the denominator.

---

### Summary

It is the single most important tool in a statistician's toolbox. If statistics is about finding the "hidden truth" (the parameters) from our data, MLE is the mathematical search engine that finds the most plausible value for that truth.

MLE is a method that finds the value of the unknown parameter (e.g., the true average weight) that makes the data we actually observed as likely as possible.

**The Bottom Line:** MLE is the gold standard for estimation. It's consistent, efficient, and asymptotically Normal. But for small samples, the unbiased estimator (dividing by $n-1$) is safer for variance estimation!

## t Confidence Intervals

To understand t confidence intervals, we have to combine three things we already know:

1. **Gosset's t-distribution** (the bell curve with fatter tails for small samples).
2. **The Pivot** $\frac{\bar{x} - \mu}{s/\sqrt{n}}$ (which follows that t-distribution).
3. **The Pivotal Quantity Method** (trapping the pivot between two bounds and solving for $\mu$).

A t confidence interval is simply the practical result of that 3-step process. It is the formula we plug our numbers into to get a range of plausible values for the true population mean ($\mu$) when we are working with a small sample and don't know the true standard deviation.

Here is the formula, followed by a plain-English breakdown:

$$\bar{x} \pm t_{n-1, \alpha/2} \times \frac{s}{\sqrt{n}}$$

---

### 1. Breaking Down the Formula

Let's translate each piece into salmon-farming language.

| Component | Symbol | Meaning | Salmon Example |
|-----------|--------|---------|----------------|
| **Sample Mean** | $\bar{x}$ | Our best single guess | 5.3 kg |
| **Sample Std Dev** | $s$ | How much our fish vary from each other | 0.39 kg |
| **Sample Size** | $n$ | How many fish we caught | 5 |
| **Standard Error** | $\frac{s}{\sqrt{n}}$ | The "margin of error" from random sampling | $0.39/\sqrt{5} \approx 0.174$ |
| **t-Critical Value** | $t_{n-1, \alpha/2}$ | Multiplier accounting for small sample size | 2.776 |

---

#### The Standard Error

This is the "margin of error" caused by random sampling. It tells us how much our sample mean (5.3 kg) typically bounces around from sample to sample.

$$\frac{s}{\sqrt{n}} = \frac{0.39}{\sqrt{5}} \approx 0.174$$

#### The t-Critical Value

This is the multiplier that accounts for our small sample size. We look this up in a t-table.

- For $n = 5$, degrees of freedom ($df$) = $4$
- For 95% confidence, $\alpha = 0.05$, so $\alpha/2 = 0.025$
- The t-critical value for $df = 4$ is **2.776**

---

#### Plugging it in

$$\bar{x} \pm t_{n-1, \alpha/2} \times \frac{s}{\sqrt{n}}$$

$$5.3 \pm 2.776 \times 0.174$$

$$5.3 \pm 0.483$$

**Final Interval:** $(4.817 \text{ kg}, 5.783 \text{ kg})$

---

### 2. What does this interval actually mean?

This is the tricky philosophical part.

| Statement | Correct? | Why? |
|-----------|----------|------|
| "There is a 95% probability that the true mean is between 4.817 and 5.783 kg." | **Incorrect** | The true mean is a fixed number; it's either in there or it isn't. Probability doesn't apply to a fixed number. |
| "We are 95% confident that the true mean lies between 4.817 and 5.783 kg." | **Correct** | Confidence refers to the method, not the parameter. |

---

#### What does "95% confident" mean?

It means that if we repeated this exact experiment 100 times (catching 5 new salmon each time, calculating the mean and standard deviation, and building a new interval each time), **95 of those 100 intervals** would successfully capture the true population mean, and **5 of them would miss it**.

We don't know if this specific interval is one of the 95 that hit or the 5 that miss. But our method is reliable 95% of the time.

---

### 3. Why "t" instead of "Z" (Normal)?

This is the core of Gosset's genius.

| Distribution | When to Use | Problem |
|--------------|-------------|---------|
| **Normal (Z)** | We know $\sigma$ (true population std dev) | We never know $\sigma$ in real life! |
| **t-distribution** | We estimate $\sigma$ with $s$ | Correctly accounts for extra uncertainty |

**The t-distribution has fatter tails** than the Normal distribution. This forces the critical value (2.776) to be much larger than the Normal value (1.96).

**The Result:** The t-interval is **wider** than the Normal interval. It forces us to be honest about our uncertainty when we only have a few data points.

---

### 4. The "Degrees of Freedom" (Why $n-1$?)

We might wonder why we use $n-1$ instead of $n$.

When we calculate the sample standard deviation ($s$), we first have to calculate the sample mean ($\bar{x}$). Once we know $\bar{x}$ and $n-1$ of the data points, the $n$-th data point is forced (it cannot vary freely).

We have effectively **"lost" 1 degree of freedom**. So, for a sample of 5 fish, we have $5-1=4$ degrees of freedom. We use the t-table row for $df = 4$.

$$\text{df} = n - 1 = 5 - 1 = 4$$

---

### 5. The "Magic" of Large Samples (Asymptotics)

What happens if we catch 1,000 salmon instead of 5?

- Degrees of freedom = 999
- The t-critical value for 999 df is 1.962—almost identical to the Normal value of 1.96
- The Standard Error ($s/\sqrt{n}$) becomes tiny because $n$ is huge

Our interval becomes:

$$5.3 \pm 1.962 \times \frac{0.39}{\sqrt{1000}} = 5.3 \pm 1.962 \times 0.0123$$

$$5.3 \pm 0.024 \rightarrow (5.276, 5.324)$$

With 1,000 fish, we are incredibly certain the true mean is around 5.3 kg. The t-distribution automatically **"grows up"** to become the Normal distribution as our sample size increases.

This is why we love the t-interval: **We can use it for any sample size.**

- If $n$ is small, it gives us wide, honest intervals.
- If $n$ is huge, it automatically gives us the same result as the Normal distribution.

---

### Summary: The t Confidence Interval Cheat Sheet

| Step | Action | Salmon Example |
|------|--------|----------------|
| 1 | Calculate the sample mean ($\bar{x}$) | 5.3 kg |
| 2 | Calculate the sample std dev ($s$) | 0.39 kg |
| 3 | Find the Standard Error ($s/\sqrt{n}$) | 0.174 kg |
| 4 | Find the t-critical value ($df = n-1$, 95% confidence) | 2.776 |
| 5 | Multiply the critical value by the SE | $2.776 \times 0.174 = 0.483$ |
| 6 | Add and subtract from the mean | $5.3 \pm 0.483$ |

**Final Answer:** We are 95% confident the true mean is between **4.817 kg** and **5.783 kg**.

## The Pooled Estimator

To understand a pooled estimator, imagine we are a salmon farmer with two separate pens.

- **Pen A** gets the standard, cheap feed.
- **Pen B** gets our expensive, experimental feed.

We want to know if the experimental feed makes the fish grow heavier. We catch 10 fish from Pen A and 10 fish from Pen B.

Now we have two separate sample variances ($s_1^2$ and $s_2^2$).

- Pen A's variance might be 0.8 kg².
- Pen B's variance might be 1.2 kg².

**Which one do we use to calculate our standard error?** Do we use Pen A's? Pen B's? An average?

A **pooled estimator** is the mathematical answer to this problem. It is a weighted average that combines the information from both samples into one single, super-reliable estimate of the common population variance.

---

### 1. The Formula for the Pooled Variance ($s_p^2$)

When we assume that both populations have the same underlying variance ($\sigma_1^2 = \sigma_2^2$), we **"pool"** our samples together to get the best possible guess for that single $\sigma^2$.

The formula is:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

Let's decode this:

| Component | Meaning |
|-----------|---------|
| $n_1 - 1$ and $n_2 - 1$ | The degrees of freedom for each sample |
| $(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2$ | The sum of the squared deviations from both groups added together (total "evidence" of spread from both pens) |
| $n_1 + n_2 - 2$ | The total degrees of freedom (we lose 1 df estimating the mean of Pen A, and 1 df estimating the mean of Pen B) |

---

### 2. Salmon Example (Plugging in the Numbers)

Let's put real numbers to it.

| Pen | Feed | Sample Size ($n$) | Sample Variance ($s^2$) |
|-----|------|-------------------|------------------------|
| **Pen A** | Standard | $n_1 = 10$ | $s_1^2 = 0.8$ |
| **Pen B** | Experimental | $n_2 = 10$ | $s_2^2 = 1.2$ |

Plug them into the formula:

$$s_p^2 = \frac{(10 - 1) \times 0.8 + (10 - 1) \times 1.2}{10 + 10 - 2}$$

$$s_p^2 = \frac{(9 \times 0.8) + (9 \times 1.2)}{18}$$

$$s_p^2 = \frac{7.2 + 10.8}{18} = \frac{18}{18} = 1.0$$

**The Pooled Variance is exactly 1.0 kg².**

The pooled standard deviation (which we use in our formulas) is:

$$s_p = \sqrt{1.0} = 1.0 \text{ kg}$$

**What did we just do?** Instead of trusting the weird 0.8 from Pen A or the 1.2 from Pen B (which were based on only 10 fish each), we combined them. By pooling, we effectively have a variance estimate based on **18 degrees of freedom**, which is much more reliable!

---

### 3. Where do we use the Pooled Estimator?

We use the pooled variance to calculate the **Standard Error for the two-sample t-test** (when we assume equal variances).

The formula for the pooled standard error is:

$$SE_{\text{pooled}} = s_p \times \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

Using our numbers:

$$SE_{\text{pooled}} = 1.0 \times \sqrt{\frac{1}{10} + \frac{1}{10}} = 1.0 \times \sqrt{0.2} \approx 0.447$$

We would then use this 0.447 to build a confidence interval for the difference between the two pen means, or to calculate our t-statistic!

---

### 4. The Intuition: Why do we "weight" it?

Notice the formula does not just add the two variances and divide by 2 (a simple average).

It is a **weighted average**.

| Scenario | Result |
|----------|--------|
| Pen A has 100 fish, Pen B has 10 fish | The pooled variance will be pulled much closer to Pen A's variance, because Pen A has more information (more degrees of freedom). |

**The group with more data "deserves" to have more say in the final estimate.**

---

### 5. The Big Assumption (The Catch!)

We can only use the pooled estimator if we are willing to assume that the two populations have **equal variances**.

In statistics, this is called the **assumption of homogeneity of variance**.

| Situation | What to Do |
|-----------|------------|
| Variances are equal (e.g., 0.8 and 1.2) | **Use pooled estimator** ✅ |
| Variances are wildly different (e.g., 5.0 and 0.5) | **Do NOT pool** ❌ |

If Pen A's fish weights vary wildly (variance = 5.0) and Pen B's fish weights are incredibly consistent (variance = 0.5), pooling them together into one single number would be mathematically wrong.

If the variances are wildly different, we have to use **Welch's t-test**, which does not pool the variances. Instead, it uses a complicated formula (the Satterthwaite approximation) to calculate the degrees of freedom and keeps the variances separate.

---

### 6. Pooled Estimator in Linear Regression (The Big Picture)

The pooled estimator isn't just for comparing two groups.

When we run a **linear regression** (e.g., predicting salmon weight based on length, temperature, and feed type), the computer calculates a single **Residual Standard Error**.

That Residual Standard Error is actually a **giant pooled variance**! It pools together the variation from all the data points around the regression line, across all values of our predictors, to give us one single, powerful estimate of the **"noise"** in our system.

### The Test Statistic that uses the Pooled Estimator

When we want to compare the means of two groups (e.g., Pen A vs. Pen B), we calculate a two-sample t-statistic:

$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

Notice that the pooled standard deviation ($s_p$) is sitting in the denominator.

Now, here is the crucial part:

| Scenario | Distribution | Center |
|----------|--------------|--------|
| **Null hypothesis is TRUE** ($\mu_1 = \mu_2$) | Central (regular) t-distribution | Centered at 0 |
| **Null hypothesis is FALSE** ($\mu_1 \neq \mu_2$) | Non-central t-distribution | Shifted by $\delta$ |

If the null hypothesis is **TRUE** ($\mu_1 = \mu_2$): This test statistic follows a central (regular) t-distribution with $n_1 + n_2 - 2$ degrees of freedom.

If the null hypothesis is **FALSE** ($\mu_1 \neq \mu_2$): This test statistic follows a **non-central t-distribution** with the same degrees of freedom, but with a non-centrality parameter ($\delta$).

---

### The Non-Centrality Parameter for the Pooled Test

When there is a true difference between the two pens, the numerator of our t-statistic doesn't center at 0 anymore. It centers at the true difference ($\mu_1 - \mu_2$).

The non-centrality parameter ($\delta$) for this two-sample t-test is:

$$\delta = \frac{\mu_1 - \mu_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

Let's decode this:

| Component | Meaning |
|-----------|---------|
| **Numerator** ($\mu_1 - \mu_2$) | The true, real-world difference between the average weights of the two pens. (The **"Signal"**). |
| **Denominator** ($\sigma \sqrt{1/n_1 + 1/n_2}$) | The standard error of that difference. (The **"Noise"**). |

---

### The Big Picture

This non-centrality parameter ($\delta$) measures **how detectable our effect is**.

| Effect Size | $\delta$ | Detectability |
|-------------|----------|---------------|
| **Large effect** (e.g., feed adds 2 kg) | $\delta$ is large | The non-central t-distribution is shoved far to the right, far away from the central t-distribution. **Power is HIGH** — we are very likely to detect the difference. |
| **Small effect** (e.g., feed adds 0.1 kg) | $\delta$ is tiny | The non-central t-distribution sits almost exactly on top of the central t-distribution. **Power is LOW** — we are unlikely to detect the difference unless we have a massive sample size. |

---

### Example for salmon

**The Setup:**

| Pen | Feed | True Mean ($\mu$) |
|-----|------|-------------------|
| **Pen A** | Standard | $\mu_1 = 5.0$ kg |
| **Pen B** | Experimental | $\mu_2 = 5.5$ kg |

So the true difference is $\mu_1 - \mu_2 = -0.5$ kg (Pen B is heavier).

- The true standard deviation of weights in both pens is $\sigma = 1.0$ kg.
- We catch $n_1 = 10$ fish from Pen A, and $n_2 = 10$ fish from Pen B.

---

**Calculate the Non-Centrality Parameter:**

$$\delta = \frac{-0.5}{1.0 \times \sqrt{1/10 + 1/10}} = \frac{-0.5}{1.0 \times \sqrt{0.2}} = \frac{-0.5}{0.447} \approx -1.12$$

---

**What does $\delta = -1.12$ mean?**

It means the true effect (the feed makes fish 0.5 kg lighter) is **1.12 standard errors away from zero**.

| Scenario | Distribution | Center |
|----------|--------------|--------|
| **If the feed actually does nothing** | Central t-distribution | Centered at 0 |
| **If the feed adds 0.5 kg** | Non-central t-distribution | Shifted to the left, centered at -1.12 |

If we run a t-test, our observed t-statistic will be a random draw from a **non-central t-distribution** that is shifted to the left, centered at -1.12.

If the feed actually did nothing ($\delta = 0$), our t-statistic would be a random draw from the central t-distribution (centered at 0).

---

### The Connection to Power

The area under the non-central t-curve (with $\delta = -1.12$) that falls past the critical rejection region (e.g., $t < -2.10$) is our **statistical power**.

Because $\delta$ is only -1.12, our power might be around **30%** — meaning we only have a 30% chance of actually catching this 0.5 kg difference with only 10 fish per pen.

---

### Summary Table

| Concept | Formula | Use Case |
|---------|---------|----------|
| **Pooled Variance** | $s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$ | Combining two sample variances |
| **Pooled SE** | $SE_{\text{pooled}} = s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$ | Standard error for two-sample t-test |
| **Degrees of Freedom** | $df = n_1 + n_2 - 2$ | Total df for pooled t-test |

**The Big Idea:** Pooling combines information from multiple groups to get a more reliable estimate of the common variance. But it only works if we can assume the variances are equal!



## Test Statistics

A **test statistic** is a single number calculated from our sample data that measures how far our observed results are from what we would expect if the null hypothesis were true.

It is the **"distance"** between our data and our assumption, measured in units of standard error.

---

### The Salmon Feed Example

Imagine we are a salmon farmer. We have always used Standard Feed, and our fish average 5.0 kg.

A salesperson sells us a new **"Super-Growth"** feed, claiming it makes fish heavier. We try it on 10 fish and get an average of 5.3 kg.

We ask ourselves: *"Is 5.3 kg genuinely heavier, or is this just random luck because I happened to catch a few big fish?"*

A test statistic is the mathematical tool that answers this question.

| Test Statistic | Meaning |
|----------------|---------|
| **Small (close to 0)** | Our data is perfectly consistent with the null hypothesis (the feed does nothing). The difference is just noise. |
| **Large (far from 0)** | Our data is screaming that the null hypothesis is wrong. The difference is a real signal. |

---

### The Signal/Noise Template

Every single test statistic we will ever encounter follows this exact same **"Signal/Noise"** template:

$$\text{Test Statistic} = \frac{\text{Observed Effect} - \text{Expected Effect under } H_0}{\text{Standard Error of the Effect}}$$

Let's decode this:

| Component | Meaning |
|-----------|---------|
| **Numerator (Signal)** | How far our sample result is from the null hypothesis value |
| **Denominator (Noise)** | How much random variation we would expect just by chance (the standard error) |

---

### The Golden Rule

> **The bigger the numerator (the effect), or the smaller the denominator (the noise), the larger our test statistic becomes. A large test statistic means strong evidence against the null hypothesis.**

---

### Common Test Statistics

| Test | Test Statistic Formula | What it measures | Distribution |
|------|----------------------|------------------|--------------|
| **One-sample t-test** | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | How many standard errors our sample mean is from the hypothesized mean ($\mu_0$) | Central $t$ (if $H_0$ is true) |
| **Two-sample t-test (Pooled)** | $t = \frac{(\bar{x}_1 - \bar{x}_2) - 0}{s_p \sqrt{1/n_1 + 1/n_2}}$ | How many standard errors apart the two group means are | Central $t$ (if $H_0$ is true) |
| **Chi-Squared test** | $\chi^2 = \sum \frac{(O - E)^2}{E}$ | How far our observed counts ($O$) are from our expected counts ($E$) | Chi-Squared (if $H_0$ is true) |

---

### Super-Growth Feed Example (Walkthrough)

**Null Hypothesis ($H_0$):** The new feed does nothing. The true mean is still $\mu_0 = 5.0$ kg.

**Our sample:** 10 fish, average $\bar{x} = 5.3$ kg, standard deviation $s = 0.5$ kg.

**Standard Error:**

$$SE = \frac{s}{\sqrt{n}} = \frac{0.5}{\sqrt{10}} \approx 0.158$$

**Calculate the test statistic ($t$):**

$$t = \frac{5.3 - 5.0}{0.158} = \frac{0.3}{0.158} \approx 1.90$$

---

### What does $t = 1.90$ actually mean?

> *"Our observed average (5.3 kg) is **1.90 standard errors** away from the hypothesized average (5.0 kg)."*

Now, we look up the $t$-distribution with 9 degrees of freedom. We find that 95% of random samples fall between $t = -2.26$ and $t = +2.26$.

Because our test statistic (1.90) falls **inside** this range, we conclude:

> *"There is not enough evidence to reject the null hypothesis. The 0.3 kg gain could easily be due to random chance."*

---

### The "Z-Score" vs. "T-Statistic" Connection

| Concept | What it measures |
|---------|------------------|
| **Z-score** | How many **standard deviations** an individual data point is from the mean |
| **Test Statistic (t)** | How many **standard errors** our sample estimate is from the null hypothesis |

---

### The Non-Central t-Distribution Connection

Remember our discussion about the non-central $t$-distribution?

| Scenario | Distribution | Center | Meaning |
|----------|--------------|--------|---------|
| **Null hypothesis is TRUE** | Central $t$-distribution | Centered at 0 | The average test statistic is 0 |
| **Null hypothesis is FALSE** | Non-central $t$-distribution | Shifted right or left | The average test statistic is the non-centrality parameter ($\delta$) |

---

### The Real-World Application

We calculate our test statistic (e.g., $t = 1.90$). We compare it to the central $t$-distribution to get our **p-value**.

| Test Statistic | What It Means | Decision |
|----------------|---------------|----------|
| **$t$ is huge** (say, 4.5) | Falls in the extreme tail. Probability if null were true is tiny ($p < 0.01$) | **Reject the null** — the feed works! |
| **$t$ is tiny** (say, 0.5) | Falls right in the middle of the central distribution | **Fail to reject the null** — no evidence the feed works |

---

## Summary

A test statistic is a single number calculated from our sample data that measures how far our observed results are from what we would expect if the null hypothesis were true.

**The Bottom Line:** A test statistic is the "distance" between our data and our assumption, measured in units of standard error. The larger the test statistic, the stronger the evidence against the null hypothesis!

### Bootstrapping

Bootstrapping is the statistical magic trick that lets us create **"fake"** new samples from our single, real sample, allowing us to estimate how wrong our estimate might be—**without catching a single additional fish!**

To understand bootstrapping, imagine we are a salmon farmer who wants to know the true average weight of all 10,000 fish in our pen.

We have a problem: We can only afford to catch and weigh 20 fish.

We calculate the average of those 20 fish (say, 5.2 kg). But we know that if we caught a different set of 20 fish, the average would be slightly different. We want to know how much our estimate bounces around—but we refuse to catch more fish because it's too expensive.

---

### The Name and the Idea

The name comes from the old phrase **"to pull yourself up by your bootstraps"**—doing the impossible with nothing but what you already have.

In statistics, bootstrapping does exactly this. It uses our existing 20 fish as a **"pretend population."** Then, it reaches into this pretend population, pulls out a fish, records its weight, puts it back, and pulls again. This is called **sampling with replacement**.

Because we put the fish back each time, we can catch the exact same fish multiple times in our "fake" sample. A fake sample of 20 fish might look like this:

> Fish #3, Fish #3, Fish #7, Fish #1, Fish #3, Fish #12, Fish #12, Fish #12, Fish #5, ... (with repeats and some fish left out).

This fake sample is called a **bootstrap sample**. It is the exact same size (20) as our original sample, but it is a random "reshuffling" of our original data.

---

### The Bootstrap Algorithm

Here is exactly how a statistician performs a bootstrap:

**Step 1: The Original Sample**

We catch 20 salmon. We have their weights: [4.8, 5.1, 5.3, 5.5, 5.8, ...]. The average is 5.2 kg.

**Step 2: Create a Bootstrap Sample (Resample)**

We randomly select 20 fish **with replacement** from our original 20. Because of replacement, some fish are picked multiple times, some not at all. We calculate the average of this fake sample. Let's say it's 5.1 kg.

**Step 3: Repeat, Repeat, Repeat**

We do Step 2 a massive number of times—say, **10,000 times**. We now have 10,000 different "fake" averages (5.1, 5.3, 4.9, 5.4, 5.0, ...).

**Step 4: Use the Fake Averages to Understand the Real One**

We look at the spread of these 10,000 fake averages.

- The **standard deviation** of these 10,000 averages is our **Bootstrap Standard Error**. It tells us exactly how much our original 5.2 kg average bounces around.
- The **2.5th and 97.5th percentiles** of these 10,000 averages give us a **95% Bootstrap Confidence Interval**. (e.g., 4.8 kg to 5.6 kg).

**The Result:** We have built a confidence interval and estimated our uncertainty **without ever catching a single additional fish**, without knowing the true population standard deviation, and without relying on the Normal distribution!

---

### A Concrete Salmon Example

| Sample | Data | Mean |
|--------|------|------|
| **Original Sample (n=5)** | [4.8, 5.1, 5.3, 5.5, 5.8] | **5.3 kg** |
| Bootstrap Sample #1 | [5.1, 5.3, 5.3, 5.5, 5.8] | 5.4 kg |
| Bootstrap Sample #2 | [4.8, 4.8, 5.1, 5.5, 5.8] | 5.2 kg |
| Bootstrap Sample #3 | [5.3, 5.5, 5.5, 5.5, 5.8] | 5.52 kg |

We do this 10,000 times. We sort all 10,000 means from smallest to largest.

- The **250th** smallest mean is 4.9 kg (the lower bound).
- The **9,750th** smallest mean is 5.7 kg (the upper bound).

**Final Answer:** We are 95% confident that the true average weight of all salmon in the pen is between **4.9 kg** and **5.7 kg**.

---

### Why Bootstrapping is Revolutionary

Bootstrapping is one of the most important statistical inventions of the 20th century (introduced by Bradley Efron in 1979). Here is why:

| Advantage | Explanation |
|-----------|-------------|
| **It makes no assumptions** | We don't have to assume our data is Normally distributed. We don't need to know the true variance. The data speaks for itself. |
| **It works for anything** | It doesn't just work for averages. It works for **any** statistic—the median, the standard deviation, the correlation coefficient, the slope of a regression line, or even a complex machine learning model. |
| **It is computationally simple** | With modern computers, resampling 10,000 times takes seconds. |

---

### Two Types of Bootstrapping

| Type | Description | When to Use |
|------|-------------|-------------|
| **Non-Parametric Bootstrap** | We resample directly from our raw data. We make no assumptions about the underlying distribution. | **Most common and safest method** |
| **Parametric Bootstrap** | We fit a specific distribution to our data (say, we assume it's Normal, estimate the mean and variance, and then draw new samples from that fitted Normal distribution). | Less common; relies on the assumption that our chosen distribution is correct |

---

### The Golden Rule: "The Bootstrap is not a cure-all"

Bootstrapping is magical, but it has one fatal flaw: **It cannot create information out of thin air.**

If our original sample of 20 fish is completely biased (e.g., we accidentally only caught fish from the shallow, warm end of the pen), bootstrapping will just give us 10,000 fake samples that are all equally biased.

> **Garbage in = Garbage out.** The bootstrap only tells us about the **random sampling error**; it cannot fix systematic errors in how we collected our data.

---

### Summary Table

| Step | Action | Result |
|------|--------|--------|
| 1 | Collect original sample | 20 fish, mean = 5.2 kg |
| 2 | Resample with replacement (10,000 times) | 10,000 bootstrap samples |
| 3 | Calculate statistic for each | 10,000 bootstrap means |
| 4 | Compute standard deviation | Bootstrap Standard Error |
| 5 | Find 2.5th and 97.5th percentiles | 95% Bootstrap Confidence Interval |

**The Bottom Line:** Bootstrapping lets us estimate uncertainty without additional data, without distributional assumptions, and without complex math. But it cannot fix biased data—garbage in, garbage out!

### The Jackknife

The Jackknife is a simple, brilliant, old-school trick (invented in 1949, decades before the computer-heavy Bootstrap) to answer exactly this question. It systematically answers: **"How much does each individual data point influence our final estimate?"**

To understand the Jackknife, imagine we are a salmon farmer who caught 10 fish to estimate the average weight.

We calculate the average: 5.2 kg.

But we have a nagging worry: *"What if Fish #3 (which weighed 6.5 kg) is a freakishly large outlier that is pulling our average upward? How much does this single fish actually change our result?"*

---

### 1. The Intuition: "Leave One Out"

The name "Jackknife" comes from the folding pocketknife. It is a **"rough and ready"** tool that is simple, reliable, and can cut through tough problems.

The process is beautifully simple:

| Step | Action |
|------|--------|
| 1 | We have $n$ data points (say, 10 salmon). |
| 2 | We calculate our statistic (e.g., the average) using all 10 fish. We call this $\hat{\theta}$. |
| 3 | We leave out the first fish and calculate the average of the remaining 9 fish. |
| 4 | We leave out the second fish and calculate the average of the remaining 9 fish. |
| 5 | We do this for **every single fish**. We end up with 10 different **"leave-one-out"** averages. |
| 6 | We look at how much these 10 averages bounce around. |

**The Result:**
- If all 10 leave-one-out averages are very close to 5.2 kg, our estimate is **stable and robust**.
- If one of them drops to 4.5 kg when we remove that 6.5 kg fish, we know that single fish is a **"leverage point"** (an outlier) that is driving our results.

---

### 2. The Step-by-Step Salmon Example

Let's do it with 5 fish to keep it simple.

**Original sample (n=5):**

| Fish | Weight (kg) |
|------|-------------|
| Fish 1 | 4.8 |
| Fish 2 | 5.1 |
| Fish 3 | **6.5** (The outlier!) |
| Fish 4 | 5.5 |
| Fish 5 | 5.8 |

---

**Step 1: Calculate the full-sample mean.**

$$\bar{x}_{all} = \frac{4.8 + 5.1 + 6.5 + 5.5 + 5.8}{5} = \frac{27.7}{5} = 5.54 \text{ kg}$$

---

**Step 2: Calculate the "Leave-One-Out" (Jackknife) means.**

| Leave Out | Remaining Data | Mean |
|-----------|----------------|------|
| Fish 1 (4.8) | [5.1, 6.5, 5.5, 5.8] | $22.9 / 4 = 5.725$ |
| Fish 2 (5.1) | [4.8, 6.5, 5.5, 5.8] | $22.6 / 4 = 5.65$ |
| **Fish 3 (6.5)** | [4.8, 5.1, 5.5, 5.8] | **$21.2 / 4 = 5.30$** (Notice how much lower this is!) |
| Fish 4 (5.5) | [4.8, 5.1, 6.5, 5.8] | $22.2 / 4 = 5.55$ |
| Fish 5 (5.8) | [4.8, 5.1, 6.5, 5.5] | $21.9 / 4 = 5.475$ |

---

**Step 3: Analyze the spread.**

The leave-one-out means range from **5.30** to **5.725**. That is a spread of **0.425 kg**.

This tells us that our estimate (5.54 kg) is **heavily influenced** by that single 6.5 kg fish. If we remove it, the average drops from 5.54 to 5.30.

---

### 3. The Jackknife Formula for Standard Error

Just like the Bootstrap, the Jackknife can give us a standard error for our estimate.

The formula for the Jackknife standard error is:

$$SE_{\text{Jackknife}} = \sqrt{\frac{n-1}{n} \sum_{i=1}^{n} \left( \hat{\theta}_{(i)} - \hat{\theta}_{(\cdot)} \right)^2}$$

Where:

| Symbol | Meaning |
|--------|---------|
| $\hat{\theta}_{(i)}$ | The statistic (e.g., mean) calculated with the $i$-th observation removed |
| $\hat{\theta}_{(\cdot)}$ | The average of all the leave-one-out statistics |

**What this formula does:** It measures the variance of the leave-one-out estimates and scales it appropriately to estimate the standard error of our full-sample estimate.

---

### 4. Jackknife vs. Bootstrap

| Feature | Jackknife (1949) | Bootstrap (1979) |
|---------|------------------|------------------|
| **When invented** | 1949 | 1979 |
| **Computational cost** | $n$ replications (cheap) | Thousands of replications (more expensive) |
| **What it does** | Systematically leaves out each observation | Randomly resamples with replacement |
| **Best for** | Quick assessment of influence | General uncertainty estimation |
| **Works for** | Simple statistics | Any statistic |

---

### Summary Table

| Step | Action | Result |
|------|--------|--------|
| 1 | Calculate full-sample statistic | $\hat{\theta} = 5.54$ kg |
| 2 | Leave out each observation one at a time | 5 leave-one-out means |
| 3 | Look at the spread | Range: 5.30 to 5.725 (spread = 0.425 kg) |
| 4 | Identify influential points | Fish #3 (6.5 kg) is pulling the mean up! |

**The Bottom Line:** The Jackknife is a simple, elegant tool that tells us **which data points are driving our results** and gives us a quick estimate of our uncertainty without the computational burden of the Bootstrap!

### Pseudo-Observations

A **pseudo-observation** is a mathematically constructed number that represents the exclusive contribution of a single data point to our overall estimate. It is the **"opinion"** of that one fish about what the population parameter should be.

To understand pseudo-observations (often called pseudo-values), we have to go back to the Jackknife and ask one deep question:

> *"If we remove one fish and the average drops from 5.54 kg to 5.30 kg, what does that single fish think the true average should be?"*

---

### 1. The Intuition: The "Imaginary" Contribution

Imagine we have a team of 5 salmon, and together they give us an average weight of 5.54 kg.

We want to know how much credit (or blame) each individual fish deserves for that final number.

The pseudo-observation for Fish $i$ is calculated by taking the overall estimate and adjusting it upward or downward based on how much the estimate changed when Fish $i$ was removed.

**The Formula:**

$$\text{Pseudo-Value}_i = n \times (\text{Full Estimate}) - (n-1) \times (\text{Leave-One-Out Estimate}_{(-i)})$$

Where:

| Symbol | Meaning |
|--------|---------|
| $n$ | Our total sample size |
| Full Estimate | The statistic calculated using all our data |
| Leave-One-Out Estimate | The statistic calculated without Fish $i$ |

---

### 2. A Salmon Example (Putting numbers to it)

Let's use the 5 fish from the Jackknife example:

**Full Mean (all 5 fish):** 5.54 kg

**Leave-One-Out Means:**

| Remove | Mean |
|--------|------|
| Without Fish 1 (4.8 kg) | 5.725 kg |
| Without Fish 2 (5.1 kg) | 5.65 kg |
| Without Fish 3 (6.5 kg) | 5.30 kg |
| Without Fish 4 (5.5 kg) | 5.55 kg |
| Without Fish 5 (5.8 kg) | 5.475 kg |

---

**Calculate the pseudo-observation for Fish 3 (the 6.5 kg outlier):**

$$\text{Pseudo}_3 = 5 \times (5.54) - 4 \times (5.30)$$

$$\text{Pseudo}_3 = 27.7 - 21.2 = 6.5$$

**Look at that!** The pseudo-observation for Fish 3 is exactly **6.5 kg**—which is its actual weight!

---

**Now calculate the pseudo-observation for Fish 1 (the 4.8 kg fish):**

$$\text{Pseudo}_1 = 5 \times (5.54) - 4 \times (5.725)$$

$$\text{Pseudo}_1 = 27.7 - 22.9 = 4.8$$

**Mind blown!** In the case of the mean, every pseudo-observation is exactly equal to the original data point!

---

### 3. The Magic: Pseudo-Observations for Complex Statistics

If the pseudo-observation is just the original data point for a mean, why do we even care?

> **Because for complex statistics, the pseudo-observation is NOT the original data point!**

Imagine we are calculating the **median**, the **variance**, the **correlation**, or the **slope of a regression line**. When we remove a single fish, the statistic changes in a nonlinear, complicated way.

The pseudo-observation formula gives us a single number that represents how that specific fish **"wants"** the statistic to be.

---

**Example: The Median**

Take 5 fish: [4.8, 5.1, 5.3, 5.5, 5.8]. The median is 5.3.

| Remove | New Median | Pseudo-Value |
|--------|------------|--------------|
| Fish 1 (4.8) | 5.3 | $5 \times 5.3 - 4 \times 5.3 = 5.3$ |
| Fish 2 (5.1) | 5.3 | $5 \times 5.3 - 4 \times 5.3 = 5.3$ |
| **Fish 3 (5.3)** | **5.5** | **$5 \times 5.3 - 4 \times 5.5 = 26.5 - 22.0 = 4.5$** |
| Fish 4 (5.5) | 5.3 | $5 \times 5.3 - 4 \times 5.3 = 5.3$ |
| Fish 5 (5.8) | 5.3 | $5 \times 5.3 - 4 \times 5.3 = 5.3$ |

**What does this 4.5 mean?**

It means that Fish 3 (which was exactly the median) is actually **pulling the median downward** relative to the other fish. The pseudo-observation (4.5) is completely different from the actual data point (5.3)! It tells us the **"hidden influence"** of that fish.

---

### 4. Why are Pseudo-Observations so Useful?

Once we calculate the pseudo-observations for all our fish, we now have a new dataset (the pseudo-values).

Here is the genius part: **These pseudo-values behave like independent, identically distributed (i.i.d.) data points**, even if our original statistic is wildly complicated!

| Application | How It Works |
|-------------|--------------|
| **Calculate the Standard Error** | Take the standard deviation of the pseudo-values and divide by $\sqrt{n}$ to get a standard error for any statistic—without using complicated calculus! |
| **Detect Outliers** | If one pseudo-observation is wildly different from the others, that data point is exerting outsized leverage on our result. |
| **Regression Analysis** | Run a linear regression on the pseudo-values to see which variables (like fish length or water temperature) are driving our statistic. |

---

### 5. Pseudo-Observations vs. Bootstrapping

This is the final piece of the puzzle!

| Feature | Pseudo-Observations (Jackknife) | Bootstrap Samples |
|---------|--------------------------------|-------------------|
| **What it creates** | Exactly $n$ pseudo-values (one per data point) | Thousands of resampled datasets |
| **Interpretation** | The "opinion" of each single data point about the parameter | The distribution of the statistic across fake universes |
| **Computational cost** | Very cheap ($n$ calculations) | Expensive (10,000+ calculations) |
| **What it gives us** | A fast, deterministic estimate of standard error and bias | Full, flexible confidence intervals and percentile distributions |

---

### The Golden Rule

> **The Jackknife pseudo-observation is the "influence score" of a single data point. The Bootstrap is the "universe of possibilities" for our statistic. The Jackknife is faster and simpler; the Bootstrap is more powerful and flexible.**

---

### Summary Table

| Concept | Definition | Formula |
|---------|------------|---------|
| **Pseudo-Observation** | The "opinion" of a single data point about the parameter | $\text{Pseudo}_i = n\hat{\theta} - (n-1)\hat{\theta}_{(-i)}$ |
| **Jackknife SE** | Standard error from pseudo-values | $SE = \sqrt{\frac{1}{n(n-1)} \sum (\text{Pseudo}_i - \bar{\text{Pseudo}})^2}$ |
| **Interpretation** | Each pseudo-value represents the contribution of one observation | High leverage = pseudo-value far from others |

**The Bottom Line:** Pseudo-observations let us see the **hidden influence** of each data point on any statistic—mean, median, variance, correlation, or regression slope—without complex math!

### Confidence Intervals for Binomial Proportions

Let's dive into confidence intervals for binomial parameters (specifically, the population proportion $p$).

When we flip a coin, survey 100 farmers, or check how many salmon in a sample have sea lice, we are dealing with binomial data. The goal is to estimate the true underlying probability $p$ of "success" (e.g., a fish having lice).

We have two main ways to build a confidence interval for $p$:

1. **The Wald Interval** (the standard "textbook" method, based on the Normal approximation).
2. **The Wilson Interval** (the smarter, more accurate method, often called the "plus-four" interval).

There is also the Exact (Clopper-Pearson) interval, but we will focus on the two most common approaches.

---

### 1. The Wald Interval (Normal Approximation)

If we have $n$ trials and $X$ successes, our estimate for $p$ is:

$$\hat{p} = \frac{X}{n}$$

By the Central Limit Theorem, $\hat{p}$ is approximately Normal with mean $p$ and variance $\frac{p(1-p)}{n}$.

**The Wald 95% Confidence Interval is:**

$$\hat{p} \pm 1.96 \times \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

---

**Salmon Example:**

We sample 20 fish and find 4 have lice. $\hat{p} = 4/20 = 0.20$.

$$0.20 \pm 1.96 \times \sqrt{\frac{0.20 \times 0.80}{20}} = 0.20 \pm 1.96 \times 0.089 = 0.20 \pm 0.175$$

**Result:** $[0.025, 0.375]$. We are 95% confident the true infection rate is between 2.5% and 37.5%.

---

**The Catch (The "Wald" Problem):**

If $p$ is near 0 or 1, or if $n$ is small, this interval **fails miserably**. The Normal approximation breaks down.

**Example:** If we sample 10 fish and find 0 lice ($\hat{p} = 0$), the Wald interval gives $0 \pm 0$, which is $[0, 0]$. That implies we are 100% certain there are no lice in the entire pen—**which is nonsense!**

---

### 2. The Wilson Interval (The "Score" Method)

To fix the flaws of the Wald interval, we use the Wilson interval. It is more complicated to calculate by hand, but it gives much better coverage, especially for small samples or extreme probabilities.

Instead of centering the interval at $\hat{p}$, the Wilson interval solves for the two values of $p$ that satisfy:

$$\frac{|\hat{p} - p|}{\sqrt{p(1-p)/n}} \leq 1.96$$

**The closed-form formula for the 95% Wilson interval is:**

$$\frac{\hat{p} + \frac{1.96^2}{2n} \pm 1.96 \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{1.96^2}{4n^2}}}{1 + \frac{1.96^2}{n}}$$

---

**Salmon Example:** $n = 20$, $\hat{p} = 0.20$:

$$\text{Wilson Interval} \approx [0.073, 0.414]$$

Notice this is shifted upwards compared to the Wald interval ($[0.025, 0.375]$) and performs better in practice.

---

### 3. The "Plus-Four" Rule (Agresti-Coull)

This is a quick and dirty approximation to the Wilson interval. It is incredibly simple and works surprisingly well.

We add **2 successes and 2 failures** to our data (hence "plus-four"):

$$\tilde{n} = n + 4$$

$$\tilde{p} = \frac{X + 2}{n + 4}$$

Then we use the Wald formula with these adjusted numbers:

$$\tilde{p} \pm 1.96 \times \sqrt{\frac{\tilde{p}(1-\tilde{p})}{\tilde{n}}}$$

---

**Salmon Example** ($n = 20, X = 4$):

$$\tilde{p} = (4 + 2) / (20 + 4) = 6/24 = 0.25$$

$$SE = \sqrt{0.25 \times 0.75 / 24} = 0.088$$

$$\text{Interval: } 0.25 \pm 1.96 \times 0.088 = 0.25 \pm 0.173$$

**Result:** $[0.077, 0.423]$, which is remarkably close to the proper Wilson interval!

---

### Summary Table: Which interval should we use?

| Method | Formula | When to Use |
|--------|---------|-------------|
| **Wald** | $\hat{p} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ | Avoid if possible. Only use if $n$ is huge and $p$ is not near 0 or 1. |
| **Wilson (Score)** | Complex formula (see above) | **The gold standard.** Works well for any $n$ and any $p$. |
| **Plus-Four (Agresti-Coull)** | $\tilde{p} \pm z \sqrt{\frac{\tilde{p}(1-\tilde{p})}{n+4}}$ | The best "quick" method. Use for teaching or quick hand calculations. Prevents the zero-variance issue. |

---

### The One-Liner to Memorize

> *"The Wald interval is dangerous for small samples or extreme probabilities because the Normal approximation fails. The Wilson interval fixes this, and the Plus-Four interval is a simple trick that mimics it by adding 2 successes and 2 failures to your data."*

---
## What is Bayesian Statistics?

To understand Bayesian statistics, forget about p-values, confidence intervals, and "repeating the experiment infinitely many times."

Bayesian statistics is built on a single, radical, and deeply intuitive idea:

> **"Uncertainty is a belief, and beliefs can be updated with data."**

Instead of treating the unknown truth (like the true average weight of our salmon) as a single, fixed number, Bayesian statistics treats it as a **random variable** that has a distribution of plausible values.

---

### 1. The Core Philosophy: "Prior" + "Data" = "Posterior"

Bayesian statistics is governed by one elegant equation: **Bayes' Theorem**.

$$\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$$

In plain English, this means:

| Component | Meaning |
|-----------|---------|
| **Prior** | What we believed **before** we saw the data. (Our gut feeling, historical knowledge, or expert opinion). |
| **Likelihood** | How well the new data fits our prior belief. (This is the same likelihood function we discussed for MLE!). |
| **Posterior** | What we should believe **after** seeing the data. (Our updated, combined belief). |

---

### 2. A Salmon Example (Step-by-Step)

Let's say we want to know the true proportion ($p$) of salmon in a pen that are infected with sea lice.

---

**Step 1: The Prior (Our initial belief)**

We have farmed this pen for years. Historically, the infection rate is around 10%. We are fairly confident it's near 10%, but we aren't 100% sure.

In Bayesian stats, we encode this belief as a **prior distribution**. We might use a **Beta distribution** with parameters $\alpha = 1, \beta = 9$, which peaks at 10%.

---

**Step 2: The Data (The Likelihood)**

We catch 20 fish and find that 4 have lice (20% infection rate).

We calculate the likelihood: *"Given a true infection rate of $p$, how likely is it that we would see 4 infected fish out of 20?"*

---

**Step 3: The Posterior (Our updated belief)**

We plug the Prior and the Likelihood into Bayes' Theorem. The math is beautifully simple for the Beta distribution:

$$\text{Posterior} = \text{Beta}(\alpha + \text{successes}, \beta + \text{failures})$$

$$\text{Posterior} = \text{Beta}(1 + 4, 9 + 16) = \text{Beta}(5, 25)$$

---

**The Result:**

Our prior (centered at 10%) and our data (showing 20%) combine to give a posterior distribution centered around **16.7%**.

Instead of saying, *"There is a 95% confidence interval between X and Y,"* we can say: *"There is a 95% probability that the true infection rate is between 6% and 32%."* This is a **direct, probabilistic statement** about our parameter—which Frequentist statistics strictly forbids!

---

### 3. Bayesian vs. Frequentist (The Ultimate Showdown)

| Feature | Frequentist (Classical) | Bayesian |
|---------|------------------------|----------|
| **What is a parameter?** | A fixed, unknown constant. (The true mean weight is exactly 5.0 kg, period). | A random variable with a distribution. (The mean weight could be 4.9 or 5.1, with varying probabilities). |
| **What is probability?** | The long-run frequency of events. (If we repeat this experiment 1,000 times...). | A degree of belief or certainty. (We are 95% certain the mean is between X and Y). |
| **Does it use prior knowledge?** | No. It relies purely on the data in our hand. | Yes. It formally combines prior knowledge with the current data. |
| **What do we get?** | A confidence interval (about the procedure, not the parameter). | A credible interval (a direct probability statement about the parameter). |
| **Computational cost** | Fast (closed-form math). | Slow (requires computers to simulate the posterior, e.g., MCMC sampling). |

---

### 4. The "Priors" Controversy (The Catch)

The biggest criticism of Bayesian statistics is the **Prior**.

- If we have a strong, incorrect prior belief, it can **"bias"** our results.
- If we have no prior knowledge, we use a **"non-informative"** prior (like Beta(1,1), which is flat), allowing the data to speak entirely for itself. In this case, the Bayesian credible interval ends up looking almost exactly like the Frequentist confidence interval!

**The Defense:**

Bayesians argue that everyone has a prior, even Frequentists. When a Frequentist says, *"We assume the null hypothesis is true,"* that is a prior belief! Bayesian statistics just makes that assumption explicit and mathematically rigorous.

---

### 5. Why is Bayesian Statistics so Popular NOW?

If Bayes' Theorem was invented in the 1700s, why did it take so long to catch on?

Because the math is **brutally hard**. To find the Posterior, we often have to solve incredibly complex integrals in the denominator (the "Evidence").

In the 1990s, computers got fast enough to run **Markov Chain Monte Carlo (MCMC)** algorithms. These algorithms allow computers to **"sample"** from the posterior distribution without doing the impossible calculus. Suddenly, Bayesian statistics became the dominant force in:

- **Machine Learning** (Google, Amazon, Netflix use it for recommendations)
- **A/B Testing** (Which website layout converts better?)
- **Pharmaceutical Trials** (Adaptive trial designs that update beliefs mid-study)

---

### Summary Cheat Sheet

| Concept | Explanation | Salmon Example |
|---------|-------------|----------------|
| **Prior** | Our initial belief about the parameter. | "We believe the sea lice rate is around 10%." (Beta(1,9)) |
| **Likelihood** | How well the new data fits the parameter. | "We saw 4 infected fish out of 20." |
| **Posterior** | Our updated belief after seeing the data. | "The infection rate is most likely around 16.7%." (Beta(5,25)) |
| **Credible Interval** | The Bayesian version of a confidence interval. | "There is a 95% probability the true rate is between 6% and 32%." |

---

### The Golden Rule

> *"Bayesian statistics is about updating your beliefs, not making binary 'reject/fail to reject' decisions. It gives us a full distribution of plausible truths, not just a single p-value."*

---

### The One-Liner to Memorize

> *"Bayesian statistics is the formal mathematical process of updating your beliefs. It combines what we thought before the experiment (the Prior) with what we observed during the experiment (the Likelihood) to give us a complete picture of what we should think after the experiment (the Posterior)."*
