![stern](https://raw.githubusercontent.com/VasilSalkov/stern/main/images/stern-logo.png "0px")
![pypi](https://img.shields.io/pypi/v/stern "Орк")
![PyPI - Downloads](https://img.shields.io/pypi/dm/stern?color=green&label=pip%20downloads)
![PyPI - License](https://img.shields.io/pypi/l/stern)
![Total lines](https://img.shields.io/tokei/lines/github.com/tomschimansky/stern?color=green&label=total%20lines)
# stern
stern is a free and open-source library by developer saivan

# Installation

`pip install stern`

# Examples Programs
Computing the difference between creation Python and PyPI:
```Python
import stern
def sumAB(a,b):
    return a - b
print(sumAB(2003, 1991))
```
Written five times ***Hello beautiful world of programming!***:
```Python
import stern
def SealN():
    n=5
    string="Hello beautiful world of programming! "
    print(string * n)
SealN()
```

Flip the line to the other side:
```Python
import stern
def flip():
    a = "stern"
    print(a[::-1])
flip()
```

Moving x and y:
```Python
import stern
def IPS():
    x = 91
    y = 56
    print(x,y)
    x, y = y, x
    print(x,y)
IPS()
```

Case of Letters:
```Python
import stern
def letters():
    s = "sTeRn"
    print(s.lower())
    print(s.upper())
letters()
```

Spelling a word:
```Python
import stern
def listletters():
    s = "stern"
    print(list(s))
listletters()
```

Unique or NOT unique list:
```Python
import stern
def unique():
    x = [1,9,9,1]
    if(len(x) == len(set(x))):
        print("The list is unique")
    else:
        print("The list is NOT unique")
unique()
```

For Else construct:
```Python
import stern
def forelse():
    numbers = [2,4,6,8,1]
    for number in numbers:
        if number % 2 == 1:
            print(number)
            break
        else:
            print("No odd numbers")
forelse()
```

Difference between == u is:
```Python
import stern
def difference():
    first = [1,2,3]
    second = [1,2,3]
    print(first == second)
    print(first is second)
    third = first
    print(first is third)
difference()
```

Removing duplicates:
```Python
import stern
def duplicates():
    list_numbers = [20,22,24,26,28,28,20,30,24]
    print('Before:',list_numbers)
    list_numbers = list(set(list_numbers))
    print('After:',list_numbers)
duplicates()
```
# Help
If you are just getting started with stern, you should be able to get started fairly quickly. 

The online documentation stays up to date with the development version of stern on github. This may be a bit newer than the version of stern you are using. To upgrade to the latest full release, run pip install stern --upgrade in your terminal.

# Contribute
* Issue Tracker: https://github.com/VasilSalkov/stern/issues
* Source Code: https://github.com/VasilSalkov/stern

# Support
If you are having issues, please let us know. We have a mailing list located at: vasilsalkou@gmail.com with subject as stern.

# Building From Source
If you want to use features that are currently in development, or you want to contribute to stern, you will need to build stern locally from its source code, rather than pip installing it.

Installing from source is fairly automated. The most work will involve compiling and installing all the stern dependencies. Once that is done, run the setup.py script which will attempt to auto-configure, build, and install stern.

This is how you help the stern module learn and achieve new technologies and features of the Python programming language.

# License
This library is distributed under GNU LGPL version 3.0, which can be found in the file `LICENSE`. We reserve the right to place future versions of this library under a different license. This basically means you can use stern in any project you want, but if you make any changes or additions to stern itself, those must be released with a compatible license (preferably submitted back to the stern project).
<h1 align="middle" style="font-size: 72px;">I 💖⚙️ STERN</h1>
