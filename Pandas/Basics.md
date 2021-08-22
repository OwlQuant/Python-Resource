prerequisites
```python
import pandas as pd
```

## Create Series / DataFrame

From Clipboard (most convenient)
```python
# Copy excel table to clipboard first Ctrl-C
pd.read_clipboard()
```

From CSV
```python
filepath = "c://data.csv"
pd.read_csv(filepath)
```


From Data (for ad-hoc use)
```python
pd.DataFrame([
    ["John", "Physics", 101],
    ["John", "Chemistry", 102], 
    ["Mary", "Math", 103],
    ["Mary", "Physics", 101]], 
  columns=["Name", "Class", "Course#"])
  
pd.Series(["Physics", "Chemistry", "Math", "English"], 
  index=[101, 102, 103, 104])
```



