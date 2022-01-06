"""
Dispersion refers to measure of how spread out the data is.
@date 05/01/22
@author Imran and Joel Grus
"""
from typing import List
from Statistics_Central_Tendencies import mean, quantile
from vector_functions import sum_of_squares 
import math

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

assert data_range([9, 2, 3, 4]) == 7


"""Variance"""

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean o)"""
    x_bar = mean(xs)
    return [x- x_bar for x in xs]
    
def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two variables"

    n = len(xs)
    deviation = de_mean(xs)
    return sum_of_squares(deviation) / (n - 1) # n - 1 as we are dealing with a sample mean of the population

assert variance([80, 100, 90, 50, 30, 70, 65, 63, 59, 50]) > 423

def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))

assert 20.57 < standard_deviation([80, 100, 90, 50, 30, 70, 65, 63, 59, 50]) < 20.58

def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range([80, 100, 90, 50, 30, 70, 65, 63, 59, 50]) == 30


