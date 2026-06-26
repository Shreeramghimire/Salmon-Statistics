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
| **Right skew** | Occasionally, you randomly grab a $Z$-score of $+2.5$, square it to $6.25$, which drags the mean to the right. This creates that long right-skewed tail (stretching to infinity) |

**Example:**

$$Z = 0.5 \rightarrow Z^2 = 0.25 \quad \text{(small)}$$
$$Z = 1.0 \rightarrow Z^2 = 1.00 \quad \text{(moderate)}$$
$$Z = 2.5 \rightarrow Z^2 = 6.25 \quad \text{(large, rare)}$$




