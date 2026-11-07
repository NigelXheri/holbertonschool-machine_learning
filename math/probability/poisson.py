#!/usr/bin/env python3
"""Define the Poisson distribution."""


class Poisson:
    """Represent a Poisson distribution with an expected count."""

    def __init__(self, data=None, lambtha=1.):
        """Set lambtha directly or estimate it from the sample mean."""
        if data is None:
            if not lambtha > 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Return the probability of exactly k occurrences."""
        k = int(k)
        if k < 0:
            return 0

        factorial = 1
        for value in range(2, k + 1):
            factorial *= value

        e = 2.7182818285
        return e ** (-self.lambtha) * self.lambtha ** k / factorial

    def cdf(self, k):
        """Return the probability of at most k occurrences."""
        k = int(k)
        if k < 0:
            return 0

        probability = 0.0
        for count in range(k + 1):
            probability += self.pmf(count)
        return probability
