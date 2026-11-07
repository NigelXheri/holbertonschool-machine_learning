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
