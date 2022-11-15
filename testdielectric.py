import numpy as np
from quantum.dielectric import dielectricFunc
from quantum.velocityOp import standardVelocity, interpolatedVelocity
from quantum.qobj import Qobj

qobj = Qobj()




def testDielectricFunc():
    result = qobj.getStandardDielectric()
    print("-------Standard Dielectric Function----------")
    return result
print(testDielectricFunc())




def testOptimalDielectricFunc():
    result = qobj.getOptimalDielectric()
    print("-------Optimal Dielectric Function------")
    return result
print(testOptimalDielectricFunc())







