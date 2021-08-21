## Pivot Table with flattened string

Name | Class
-----|------
John | Physics
John | Chemistry
Mary | Math
Mary | English
Mary | Physics

expected answer

Name | Class
-----|--------
John | Physics, Chemistry
Mary | Math, English, Physics

```python
pd.DataFrame([["John", "Physics"],["John", "Chemistry"], ["Mary", "Math"],["Mary", "English"], ["Mary", "Physics"]], columns=["Name", "Class"])
df.groupby("Name")["Class"].apply(", ".join)

