import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from subprocess import Popen, check_output

def rsub(path):
    """ str path: path to open """
    _ = check_output('rsub %s' % path, shell=True)

def show_plot(outpath='./tmp.png'):
    """ str outpath: path to write figure """
    plt.savefig(outpath)
    plt.close()
    rsub(outpath)
