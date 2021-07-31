# IterTypes Private Library

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

This library has some useful types and functions used to get types of iterables.
Whilst iterable types were purposely avoided by the types library, iterables offer
unique types which could sometimes be useful to obtain.

### Getting started

Start by importing the module:

```py
import itertypes
```

There are various functions which follow the naming convention `is[type]iterator`.

```py
itertypes.isstringiterator(iter("string"))
>>> True

dictionary = {1: 2, 3: 4}
iteration = iter(dictionary.items())
itertypes.isdictitemiterator(iteration)
>>> True
```

There's also the `itertypes.isiterator` function where it checks if the given
object is iterable or not.

```py
my_variable = 5
itertypes.isiterable(my_variable)
>>> False

my_variable = ['a', 'b', 'c', 'd']
all([itertypes.isiterable(my_variable), itertypes.islistiterator(iter(my_variable))])
>>> True
```

Finally, there's various types which resolve to iterable types.
These types can be used with isinstance, or with the equality operator
and the type function.

```py
byte = bytearray()
isinstance(iter(byte), itertypes.BytearrayIteratorType)
>>> True

iterable = iter({1: 2, 3: 4}.values())
isinstance(iterable, itertypes.DictValueIteratorType)
>>> True
```

### Notes about the package

This package is small-scale, I created it simply for experience points.

### Installation

Install through pip as if it's a regular github repository.

```sh
python -m pip install git+https://github.com/Kreusada/itertypes.git
```