"""
Applying different vector calculations using python
@date 04/01/22
@author Imran and Joel Grus
"""

#Defining a vector in python
from typing import List

Vector = List[float]

#Creating a vector
height_weight_age = [70 , #inches,
                    170 , #pounds
                    40 ] #years

# Creating another vector
grades = [
    95, #module 1
    80, #module 2
    75, #module 3
    62  #module 4
]

def add(v: Vector, w: Vector)-> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1,2,3], [3,2,1]) == [4,4,4]  



def subtract(v: Vector, w: Vector)-> Vector:
    """Subtracts corresponding elements"""
    assert len(v)== len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert subtract([1,2,3], [3,2,1]) == [-2, 0, 2]



def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v)== num_elements for v in vectors), "different sizes!" #all() function returns true if all elements are True.

    # The i-th element of the result is the sum of every vector[i]
    return[sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1,2], [2,3], [5,1]]) == [8, 6]


def scalar_multiply(c: float, v: Vector)-> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1,2,4]) == [2, 4, 8]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... v_n* w_n"""
    assert len(v) == len(w), "Vectors must be the same length."
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1, 5, 3], [2, 1, 3]) ==  16 #1*2 + 5*1 + 3*3 = 16


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1+ ...+ v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1,2,3]) == 14 # 1*1 + 2*2 + 3*3 = 14

import math
def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5 #3*3 + 4*4 = 25 , sqrt=5




