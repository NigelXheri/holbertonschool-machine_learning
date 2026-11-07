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
