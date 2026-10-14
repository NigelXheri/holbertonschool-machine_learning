#!/usr/bin/env python3
"""Displays a histogram plot"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Displays a histogram plot"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.hist(student_grades, edgecolor='k', bins=np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 110, 10))
    plt.yticks(np.arange(0, 31, 5))
    plt.xlim(0, 100)
    plt.title("Project A")
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.show()
