### <img src="./godel.png" />
### A Library for working with finite valued Gödel's G(k) Logic

## Example Usage
> Obtaining n Truth Values inside the range of [0,1]  
```python
from Godel import *
tv = G(4)
print(tv)
```
### Output
```python
[0, Fraction(1, 3), Fraction(2, 3), 1]
```

> Negating the first value of the n Truth Values
```python
from Godel import *
tv = G(4)
n = NOT(tv[0])
print(n)
```
### Output
```python
1
```
