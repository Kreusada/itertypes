# IterTypes Private Library

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

This library has some useful types and functions used to get types of iterables.

Start by importing the module:

```py
import itertypes
```

There are various functions which follow the naming convention `is<type>iterator`.

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
```

Finally, there's various types which resolve to iterable types.

```py
iterable = iter({1, 2, 3, 4})
isinstance(iterable, itertypes.SetIteratorType)
>>> True

iterable = iter({1: 2, 3: 4}.values())
isinstance(iterable, itertypes.DictValueIteratorType)
>>> True
```

### Notes about the package

This package is small-scale, I created it simply for experience points.

* I am not expecting or wanting further distribution of this library.
* I am not actively maintaining this project.
* I will not be publishing this library to PyPi.

This may change in the future.