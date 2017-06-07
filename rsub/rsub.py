import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from subprocess import check_output

def rsub(path):
    """ str path: path to open """
    _ = check_output('rsub %s' % path, shell=True)

def show_plot(outpath='./tmp.png', *args, **kwargs):
    """ str outpath: path to write figure """
    plt.savefig(outpath, *args, **kwargs)
    plt.close()
    rsub(outpath)
