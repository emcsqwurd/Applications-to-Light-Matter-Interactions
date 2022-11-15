import numpy as np
from quantum.qobj import Qobj
from quantum.velocityOp import standardVelocity, interpolatedVelocity
from quantum.interpolate import calculatek1, interpolateHamiltonianEE
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum.table import differenceInVelocity
from quantum import potential as pt
from quantum.utils import kvec, timerFloat, timerPrint



qobj = Qobj()




"""Function to be run that obtains the Velocity Opertor with respect to the Standard
Basis implementation"""
def testStandardVelocity():
    potential = qobj.getPotential()
    ck = qobj.getCk()
    result = standardVelocity(potential, ck)
    print("---------Standard Velocity------")
    return result
#print(testStandardVelocity())




"""Function to be run that obtains the Velocity Operator with respect to the Optimal
Basis implementation"""
def testInterpolatedVelocity():
    k1 = qobj.getk1()
    OBck = qobj.getOBck()
    potential = qobj.getPotential()
    result = interpolatedVelocity(potential, OBck, k1)
    print("---------Interpolated Velocity------")
    return result
#print(testInterpolatedVelocity())







def testStanVelQ():
    result = qobj.getStandardVelocityOperator()
    print("--STANDARD Velocity--")
    return result
print(testStanVelQ())


@timerPrint
def testInterVelQ():
    result = qobj.getInterpolatedVelocityOperator()
    print("--INTERPOALTED Velocity--")
    return result
#print(testInterVelQ())



