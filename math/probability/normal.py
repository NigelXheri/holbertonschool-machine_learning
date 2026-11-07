#!/usr/bin/env python3
"""Define the normal distribution."""


class Normal:
    """Represent a normal distribution with a mean and standard deviation."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Set parameters directly or estimate them from the data."""
        if data is None:
            if not stddev > 0:
                raise ValueError('stddev must be a positive value')
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            self.mean = float(sum(data) / len(data))
            squared_errors = sum((value - self.mean) ** 2 for value in data)
            self.stddev = float((squared_errors / len(data)) ** 0.5)

    def z_score(self, x):
        """Return the number of standard deviations x is from the mean."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Return the value corresponding to the given z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Return the probability density at x."""
        pi = 3.1415926536
        e = 2.7182818285
        z = self.z_score(x)
        return e ** (-0.5 * z * z) / (self.stddev * (2 * pi) ** 0.5)

    def cdf(self, x):
        """Return the cumulative probability at x using the erf polynomial."""
        pi = 3.1415926536
        z = self.z_score(x) / 2 ** 0.5
        erf = (2 / pi ** 0.5) * (
            z - z ** 3 / 3 + z ** 5 / 10 - z ** 7 / 42 + z ** 9 / 216
        )
        return (1 + erf) / 2
