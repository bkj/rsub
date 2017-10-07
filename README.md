### rsub

[rsub](http://log.liminastudio.com/writing/tutorials/sublime-tunnel-of-love-how-to-edit-remote-files-with-sublime-text-via-an-ssh-tunnel) is a nice tool for using Sublime Text over ssh.  This is a (very) simple module for using `rsub` from within python.

#### Usage

```
from rsub import *
from matplotlib import pyplot as plt

_ = plt.scatter(range(10), range(10))
show_plot()
```
