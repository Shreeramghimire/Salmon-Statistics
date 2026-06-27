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
