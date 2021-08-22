## Matrix in NumPy
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

### Create Matrix
Ones, Zeros, Identify
```python
np.ones([3,4])
np.zeros([3,4])
np.eye(4)  # creates 4x4 identity matrix
```

Matrix using 2D array
```python
np.array([[10, 20, 30], [40, 50, 60]])

# Note - using matrix type in numpy is discouraged. This feature will be removed at some point
```

### Common Operations

Matrix Multiply / Dot Product
```python
np.matmul(a, b)
# or
np.dot(a, b)
```

Determinant value
```python
np.linalg.det(a, b)
```

Transpose
```python
a.T
```


Inverse
```python
np.linalg.inv(a)

# check using: np.dot(a, np.linalg.inv(a))
```

Upper/Lower Triangle of Matrix
```python
np.triu(x)
np.tril(x)
```

Diagonal of Matrix
```python
np.diag(x)
```

