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







