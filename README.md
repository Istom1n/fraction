## Splits a fraction jff

Using the [continued fraction](https://en.wikipedia.org/wiki/Continued_fraction) method for splitting. All information [here](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#termdecs).  
Yeah, static typing is cool. ([PEP 484](https://www.python.org/dev/peps/pep-0484/) & [PEP 526](https://www.python.org/dev/peps/pep-0526/))

> I didn't use `typing.cast`, because in doc says `This returns the value unchanged`, i.e. pure `bla-bla-bla` function.

### Installing

**Python 3.6**

```bash
~# pip install pipenv (if you doesn't have it)
~# pipenv install  
~# python shell
~# pytest

Output:
==================== test session starts ====================
platform darwin -- Python 3.6.5, pytest-3.6.0, py-1.5.3, pluggy-0.6.0
rootdir: /bla-bla-bla/fraction, inifile:
collected 1 item

test_fraction.py .                                          [100%]

==================== 1 passed in 0.14 seconds ====================
```
