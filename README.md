# Pattern Letters
## Geting started

This library has been tested with Python 3.6-3.10 and Pypy 3.
+ Installation using pip<br>
`$ pip install patlet`

## Use PatLet
#### printing
  ```python
  from patlet import PatLet
  
  # output the entered text to the console
  PL = PatLet("PatLet")
  PL.printer(char='*')
  ```
#### writing .txt file
  ```python
  from patlet import PatLet
  
  # write the entered text to a .txt file
  PL = PatLet("i am reading a book")
  PL.writer(char="*", filename="book")
  ```
## Use PrettyLetter
#### printing
```python
from patlet import PrettyLetter

# output the entered text to the console
PL = PrettyLetter("PrettyLetter")

#the number of styles for the letters is 12
PL.printer(number=8)
```
```shell
『P』『R』『E』『T』『T』『Y』『L』『E』『T』『T』『E』『R』
```

#### writing .txt file
```python
from patlet import PrettyLetter

PL = PrettyLetter("PrettyLetter")
PL.writer(number=8)
```
