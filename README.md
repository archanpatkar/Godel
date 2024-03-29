### <img src="./godel.png" />
### A Library for working with Gödel's finite and infinite valued G(k) and G(∞) Logics in Python

## Example Usage

### `Truth Values`
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

### `Not Operator`
> Negating the first truth value (0)
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

### `And Operator`
```python
from Godel import *
tv = G(4)
n = AND(tv[1],tv[2])
print(n)
```
### Output
```python
1/3
```

### `OR Operator`
```python
from Godel import *
tv = G(4)
n = OR(tv[1],tv[2])
print(n)
```
### Output
```python
2/3
```

### `IMPLICATION Operator`
```python
from Godel import *
tv = G(4)
n = IMP(tv[2],tv[3])
print(n)
```
### Output
```python
1
```
