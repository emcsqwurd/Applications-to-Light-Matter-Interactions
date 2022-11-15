import matplotlib.pyplot as plt
from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisGetOBBI
from quantum import potential as pt
import numpy as np
from quantum.qobj import Qobj
from quantum.interpolate import calculateVLoc
from quantum.potential import PotentialFactory as pf
from quantum.utils import energyRangeFunc, timerPrint
from quantum.experimentalplots import standardDielectricTimeNKRelationship
from quantum.experimentalplots import averagePlotStandardDielectricLineOfBestFit


"""File to run quick tests if required"""


qobj = Qobj()



@timerPrint
def funcStandard():
    res = qobj.getStandardImaginaryDielectricPlot()
    return res
#print(funcStandard())    




@timerPrint
def funcOptimal():
    res = qobj.getOptimalImaginaryDielectricPlot()
    return res
#print(funcOptimal())    


res = qobj.getStandardVelocityOperator()
print(res)





