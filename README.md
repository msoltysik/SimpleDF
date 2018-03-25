# SimpleDataFrame Workshop
The goal of this project is to learn python internals by creating a clone of well-known `pandas.DataFrame`.

## Project Scope
### As a User I'm able to:

#### Iteration 1
- Initialize empty SimpleDF: `df = SimpleDF()`
- Initialize SimpleDF using dict: `df = SimpleDF({'A': 1})`
- Check length of DF: `len(df)`

#### Iteration 2
- Get value using getters: `df.A`
- Get value using brackets: `df['A']`

#### Iteration 3
- Compare SimpleDF to each other: `df1.equals(df2)`
- Check SimpleDF truthness of any boolean condition: `df.A > 0`
- Filter SimpleDF by single column values: `df[df.A > 0]`

#### Iteration 4
- Concat two SimpleDFs: `df1.append(df2)`
- Slice SimpleDF by ranges: `df.iloc[1:2]`
- Get SimpleDF values by arrays of indexes: `df.iloc[[1, 2, 3], [0, 2]]`



## Resources
- https://pandas.pydata.org/pandas-docs/stable/10min.html
- https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py
