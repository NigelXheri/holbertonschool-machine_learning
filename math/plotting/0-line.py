#!/usr/bin/env python3
"""Plots the line graph"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plots the line graph"""

    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.xlim(0, 10)
    plt.xlim(0, 10)
    plt.plot(y, color='red')
