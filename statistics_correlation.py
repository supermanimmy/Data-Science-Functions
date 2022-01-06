"""
Relationship between two metrics
@date 05/01/22
@author Imran and Joel Grus
"""

from typing import List

from statistics_dispersion import de_mean, standard_deviation
from vector_functions import dot


def covariance(xs: List[float], ys: List) -> float:
    assert len(xs) == len(ys), "xs and ys must have the same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) -1)

height = [150, 160, 180, 190]
weight = [50, 55, 80, 85]

assert 316 < covariance(height, weight) < 317

def correlations(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)

    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x /stdev_y
    else:
        return 0 #no varation, correlation is zero
    
"""
Correlation is unitless and always lies between -1 (perfect anticorrelation
and 1 (perfect correlation). A number like 0.25 represents a relatively weak psitive correlation.
Correlation can be very sensitive to outliers.

Simpson's Paradox: correlations can be misleading when confounding variables are ignored.
Correlation is measuring relationship between two variables, all else being equal.
All else being equal can be an terrible assumption to make.
You need to know your data and check for possible confounding factors. If

Other Correlational Caveats:
    Correlation of 0 does not always mean no  correlation. 
    Each element of variable y can be the absolute value of element x, cancelling out to 0.25

    Correlation doesn't tell you anything about how large the relationship is between two variables.
    Example: x = [-2, -1, 0, 1, 2], y = [99.89, 99.99, 100, 100.01, 100.02] are perfectly correalted. 

Correlation and Causation:
    "Correlation is not causation". If x and y are correlated strongly, that might mean that x causes y,
     that y causes x, that that each causes the other, that some third factor causes both, or nothing at all. 
"""

assert 0.98 < correlations(height, weight) < 0.99


