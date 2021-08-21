Prerequisite
```python
import numpy as np 
```

## 1. Arithmetic

Lowest Common Multiple
```python
np.lcm(10,15)
```
Greatest Common Divisor
```python
np.gcd(10,15)
```

Remainder / Mod
```python
np.mod(22,5)
```


## 2. Trignometry
```python
a = np.array([0,30,45,60,90,135,180,270,360])
```

Degree to Radian
```python
np.deg2rad(a)
```

Radian to Degree
```python
r = np.deg2rad(a)
np.rad2deg(r)
```

Sin / Cos / Tan 
```python
r = np.deg2rad(a)
np.sin(r)
np.cos(r)
bp.tan(r)
np.arcsin(0.5)  # 30 degree
np.arcsin(0.5)  # 60 degree
np.arctan(1)  # 45 degree
```

## 3. Power, Log, Exponent
```python
x = np.array([1,3,4,6,9,15,18,27])
```

Power
```python
np.power(x, 2)  # power of 2
```

Square Root
```python
np.sqrt(x)
```

Exponential
```python
np.exp(x)  # e^x
```

Log
```python
np.log(x)  # ln(x)
np.log10(x)  # log(x) with base 10

```

## 4. Regression
```python
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([10,21,32,39,48,61,72,78,91,98])
```

Linear Regression
```python
beta, intercept = np.polyfit(x,y,1)  # equation of best fit line: y = x * beta + intercept
```

Regression - Curve fitting 
```python
dof = 3  # degree of freedom. Highest power of best-fit polynomial in y = x^dof * b1 + x^(dof-1) * b2 + ... + bn
np.polyfit(x,y,dof)  # returns b1, b2, ... bn (dof+1 elements)
```


## 5. Solving Equations

Roots of single variable equation (like quadratic equation)

```python
np.roots([1, -3, 2])  # solution for x^2 - 3*x^2 + 2

np.roots([1, -6, 11, -6])  # solution for x^3 - 6x^3 + 11x - 6

```


Simultaneous Equations
```python
# Two Variables x, y
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])

# x + 2y = 1
# 5x + 7y = 2

np.linalg.solve(a, b)


# Three Variables x, y, z
a = np.array([[1, 1, 1], [2, 1, 2], [1, -1, -1]])
b = np.array([2, 6, 0])

# x + y + z = 2
# 2x + y + 2z = 6
# x - y - z = 0

np.linalg.solve(a, b)
```


