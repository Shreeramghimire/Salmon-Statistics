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
Example: A company develops a new, cheaper medicine to kill sea lice. They only care if the new medicine kills more lice than the old expensive medicine. If it kills the same amount, they will switch to the cheaper one. If it kills fewer, they won't use it. They don't care if it kills way more than the old one (that's just a bonus); they are only testing for superiority. 

### Two-Tailed Test ((The "Is it different?" Test)
We use a two-tailed test when our research question is: "Is the new treatment different from the old one?"

We are looking for an effect in either direction. The new drug could be better (lower lice count) or worse (higher lice count). We just want to know if it has any effect at all. 
1. The Hypothesis: H0: New = Old Vs. H1: New $\neq$ Old.
2. Where does the rejection region go? We split your 5% alpha (α=0.05) equally between both tails of the distribution. So, 2.5% in the left tail, and 2.5% in the right tail.
3. Confidence Interval: When calculating a 95% confidence interval, we use the t-critical value that leaves 2.5% in each tail. We get a range: Estimate±Margin of Error.
Example: A company develops a new feed. We want to know if salmon fed this new feed grow to a different average weight than salmon fed the standard feed. We don't care if it's heavier or lighter (though heavier is nice); We just need to know if the feed changes growth at all. 
