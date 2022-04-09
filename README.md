# Pattern Letters
## Geting started

+ Installation using pip<br>
`$ pip install patlet`

#### Use
+ horizontal printing
  ```python
  from patlet import PatLet

  obj = PatLet("PatLet")
  obj.printer(char='*')
  ```
+ writing .txt file
```python
from patlet import PatLet

obj = PatLet("PatLet")
obj.writer(char="*")
```