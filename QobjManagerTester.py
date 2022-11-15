from quantum.QobjManager import QobjManager
from quantum.qobj import Qobj
import numpy as np


manager = QobjManager()

qobj1 = Qobj()
qobj2 = Qobj()

def testBandsTogether():
    manager.addQobj(qobj1)
    manager.addQobj(qobj2)
    qobj1.setParms(N_B = 6)
    qobj2.setParms(N_B = 6)
    manager.plotDataBands()
    return 
print(testBandsTogether())



def testImaginaryDielectricComparison():
    manager.addQobj(qobj1)
    manager.addQobj(qobj2)
    qobj1.setParms(sb = 0.1)
    qobj2.setParms(sb = 0.001)
    manager.plotStandardOptimalDielectricFunction()
    return 
#print(testImaginaryDielectricComparison())







