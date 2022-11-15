from cProfile import label
import numpy as np
from quantum.qobj import Qobj
import os
import matplotlib.pyplot as plt



script_dir = os.path.dirname(__file__)
plots_dir = os.path.join(script_dir, "plots/")
if not os.path.isdir(plots_dir):
    os.makedirs(plots_dir)



""""""
def plotSbAgainstOptimalBasisSize(qobjList: list[Qobj])->None:
    sb = np.zeros(len(qobjList))
    size = np.zeros(len(qobjList))
    index = 0
    for qobj in qobjList:
        tempSb = qobj.getSb()
        tempSize = qobj.getOptimalBasis().size
        sb[index] = tempSb
        size[index] = tempSize
        index+=1
    plt.plot(sb, size, "r-", label="sb against optimal basis size")
    plt.xlabel("sb")
    plt.ylabel("optimal basis size")
    plt.savefig(plots_dir + "sbAgainstOptimalbasis.png")
    plt.show()
    
        