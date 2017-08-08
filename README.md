#### rsub

`rsub` is a nice tool for using Sublime Text over ssh:

    http://log.liminastudio.com/writing/tutorials/sublime-tunnel-of-love-how-to-edit-remote-files-with-sublime-text-via-an-ssh-tunnel

This is a very simple module for using `rsub` from within Python.

#### Usage

```
    from rsub import rsub, show_plot
    from matplotlib import pyplot as plt

    _ = plt.scatter(range(10), range(10))
    show_plot()
```
