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
