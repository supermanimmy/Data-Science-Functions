"""
Applying different vector calculations using python
@date 04/01/22
@author Imran and Joel Grus
"""
from typing import List
from typing import Tuple
from typing import Callable
# A matrix is a two-dimensional collection of numbers.


#We will represent matrices as a list of lists
Matrix = List[List[float]]
Vector = List[float]
A = [[1,2,3], # 2 rows, 3 columns
    [4,5,6]]

B = [[1,2], # 3 rows, 2 columns
    [3,4],
    [5,6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of B)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 #number of elements in first row
    return num_rows, num_cols

assert shape(A) == (2, 3)

def get_row(A: Matrix, i: int)-> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]



def get_column(A: Matrix, j:int) -> Vector:
    """Returns the j-th column of A (as a vector)"""
    return [A_i[j] for A_i in A] # For each row in A, return j-th element.


def make_matrix(num_rows: int, 
                num_cols: int,
                entry_fn : Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rowx x num_cols matrix whose (i, j)-th entry is the entry_fin(i,j)
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns t he nxn identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i==j else 0)

assert identity_matrix(2) == [[1,0],
                              [0,1]]

