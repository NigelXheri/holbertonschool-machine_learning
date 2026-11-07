#!/usr/bin/env python3
"""Define the exponential distribution."""


class Exponential:
    """Represent an exponential distribution with a rate parameter."""

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
            self.lambtha = 1.0 / (sum(data) / len(data))

    def pdf(self, x):
        """Return the probability density at time x."""
        if x < 0:
            return 0

        e = 2.7182818285
        return self.lambtha * e ** (-self.lambtha * x)
