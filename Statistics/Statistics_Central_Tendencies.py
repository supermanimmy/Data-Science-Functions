"""
Central Tendencies of data
@date 05/01/22
@author Imran and Joel Grus
"""


from typing import Counter, List


def mean(xs: List[float]) -> float:
    """The mean or average"""
    return sum(xs)/ len(xs)

assert mean([1,2,3,4,5]) == 3

def _median_odd(xs: List[float]) -> float:
    """if len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs)//2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of two middle elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) //2
    return (sorted_xs[hi_midpoint -1] + sorted_xs[hi_midpoint])/2

def median(v: List[float]) -> float:
    """Finds the middle-most value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1,2,3,4]) == (2+3)/2
assert median([1, 5, 9, 2, 3]) == 3


def quantile(xs: List[float], p:float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p* len(xs))
    return sorted(xs)[p_index]

assert quantile([1,2,4,3,5], 0.1) == 1


def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

assert set(mode([1,1,3,3,2,3,2,2])) == {2,3}
