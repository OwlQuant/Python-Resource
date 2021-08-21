## Pivot Table with flattened string

Name | Class
------------
John | Physics
John | Chemistry
Mary | Math
Mary | English

expected answer

Name | Classes
--------------
John | Physics, Chemistry
Mary | Math, English

```python
df.groupby("Name").apply(["Clases"].join(", "))


