# Pattern Letters
## Geting started

This library has been tested with Python 3.6-3.10 and Pypy 3.
+ Installation using pip<br>
`$ pip install patlet`

## Use
#### horizontal printing
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
