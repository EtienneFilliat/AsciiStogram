# AsciiStogram

## Installation
### install from source
```
$ git clone git@github.com:EtienneFilliat/AsciiStogram.git
$ cd AsciiStogram
$ python setup.py install
```

### Example

```Python
#!/usr/bin/env python3
from AsciiStogram.Histogram import Histogram

marks = [0,1,1,1,1,1,1,9,9,10,11,12,15,15,15,18,18,19,19,19,20,23,23,24,24,
            24,25,26,27,27,28,28,30,30,30,31,31,33,33,33,34,34,35,37,37,38,
            39,39,42,42,43,45,46]

hist = Histogram(marks, title="CPP - R-Type",
                    x_axis_step=5, xlab="Marks",
                    pch="█", showSummary=True)
hist.show()
```

Output :

![example](https://user-images.githubusercontent.com/26181710/50698490-5c5e9100-1045-11e9-90df-f76e704f845a.png)
