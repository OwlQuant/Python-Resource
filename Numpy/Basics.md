
Prerequisite
```python
import numpy as np 
```
## 1. Arrays

One Dimension
```python
np.array([1,4,5,7,4,2,0])
```
Two Dimension
```python
np.array([[1,3,5],[2,4,6]])
```
Addressing Array

```python
x = np.array([1,4,5,7,4,2,0])

# second element
x[1]  # index starts with 0

# first five
x[:5]

# second to fifth  
x[1:5]  # index starts with 0

# Last  
x[-1]

# Last three
x[-3:]

# All but last two
x[:-2]

```

Array Manipulation

```python
x = np.array([1,3,5,7,2,4,6,8])

# Elementwise update
x * 10  # multiplies each element of array by 10
x / 2  # divides each element of array by 2
x + 100  # adds each element of array by 100
-x  # reverses sign of each element of array

# Sorting
x.sort()  # Sorted in-place
# or
np.sort(x)  # returns copy of array that is sorted

```


## 2. Generate Numbers

### Sequential Numbers

Numbers from - to
```python
np.arange(10) # 0, 1, ... 9
np.arange(5, 15) # 5, 6, 7, ... 14
np.arange(2, 20, 4) # 2, 6, 10, 14, 18
```

Split Range - start, stop, count
```python
np.arange(0, 50, 6) # 0, 10, 20, 30, 40, 50
```

### Random Numbers

Generate array of 100 random numbers
```python
np.random.rand(100)
```
Generate 2d array of 10x5 random numbers
```python
np.random.rand([10,5])
```
Generate 10 random integers between 1000 and 2000
```python
np.random.randint(1000, 2000, 10)
```

## 3. Basic Math
```python
x = np.random.rand(10)
```
Count of elements
```python
np.size(x)
# or
x.size

Length of array
len(x)  # for 1-dimension array this is the same as x.size or np.size(x)
```

Add
```python
np.sum(x)
# or
x.sum()
```

Average
```python
np.mean(x)
# or
x.mean()
```

Median
```python
np.median(x)
```

Product
```python
np.prod(x)
# or
x.prod()
```

Min / Max 
```python
np.min(x)
np.max(x)
# or
x.min()
x.max()
```

Cumulative Sum / Product
```python
np.cumsum(x)
np.cumprod(x)
# or
x.cumsum()
x.cumprod()

# multiple operations can be combined in one statement
np.cumprod(x/100 + 1) - 1
```




