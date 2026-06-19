# 1. Sea-lice Count:
The Norwegian Food Safety Authority records the weekly number of salmon lice in aquaculture facilities. Regulations require fish farms to maintain an average of 0.5 or fewer adult female lice per fish. To comply with this requirement, farms conduct weekly sampling of salmon from net pens and count the number of lice present. The number of adult female lice serves as the primary indicator in salmon lice monitoring and control programs, as it reflects the reproductive potential of the parasite population. This is an example of discrete data. And we use Probability Mass Function (PMF) to calculate the probability of a specific count. 
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



