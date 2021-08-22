## Matrix in NumPy
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

### Create Matrix
Ones, Zeros, Identify
```python
np.ones([3,4])
np.zeros([3,4])
np.eye(4)  # creates 4x4 identity matrix
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


Inverse
```python
np.linalg.inv(a)

# check using: np.dot(a, np.linalg.inv(a))
```

