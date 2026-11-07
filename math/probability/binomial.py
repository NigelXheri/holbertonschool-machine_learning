#!/usr/bin/env python3
"""Define the binomial distribution."""


class Binomial:
    """Represent a distribution of successes over Bernoulli trials."""

    def __init__(self, data=None, n=1, p=0.5):
        """Set parameters directly or estimate them by matching moments."""
        if data is None:
            n = int(n)
            if n <= 0:
                raise ValueError('n must be a positive value')
            if not 0 < p < 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = n
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            mean = sum(data) / len(data)
            variance = sum((value - mean) ** 2 for value in data) / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = mean / self.n

    def pmf(self, k):
        """Return the probability of exactly k successes."""
        k = int(k)
        if not 0 <= k <= self.n:
            return 0

        combinations = 1
        for i in range(1, min(k, self.n - k) + 1):
            combinations = combinations * (self.n - i + 1) // i

        return combinations * self.p ** k * (1 - self.p) ** (self.n - k)

    def cdf(self, k):
        """Return the probability of at most k successes for valid counts."""
        k = int(k)
        if not 0 <= k <= self.n:
            return 0

        probability = 0.0
        for count in range(k + 1):
            probability += self.pmf(count)
        return probability
