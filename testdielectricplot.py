import numpy as np
from quantum.dielectricplot import dielectricPlotImaginary, dielectricPlotImaginaryArray, dielectricPlotRealArray
from quantum.dielectricplot import dielectricPlotReal
from quantum.utils import timerPrint
from quantum.velocityOp import standardVelocity, interpolatedVelocity
from quantum.dielectric import dielectricFunc
import matplotlib.pyplot as plt
from quantum.qobj import Qobj


qobj = Qobj()





#STANDARD DIELECTRIC FUNCTION PLOT USING STANDARD BASIS IMPLEMENTATION

@timerPrint
def testStandardDielectricPlotImaginary():
    numberOccupied = qobj.getNumberOccupied()
    N_b = qobj.getN_B()
    energyRange = qobj.getEnergyRangeFunc()
    ek = qobj.getEk()
    damp = qobj.getDamp()
    stanvel = qobj.getStandardVelocityOperator()
    wlist = dielectricPlotImaginaryArray(N_b, ek, damp, energyRange, stanvel, numberOccupied)
    plt.xlabel("Energy")
    plt.ylabel("Imaginary part of Dielectric Function")
    plt.title("Complex Dielectric Function with Standard Basis")
    plt.plot(energyRange, wlist, 'b')
    plt.show()  
    return 
print(testStandardDielectricPlotImaginary())

@timerPrint
def testStandardDielectricPlotReal():
    numberOccupied = qobj.getNumberOccupied()
    N_b = qobj.getN_B()
    energyRange = qobj.getEnergyRangeFunc()
    ek = qobj.getEk()
    damp = qobj.getDamp()
    stanvel = qobj.getStandardVelocityOperator()
    wlist = dielectricPlotRealArray(N_b, ek, damp, energyRange, stanvel, numberOccupied)
    plt.xlabel("Energy")
    plt.ylabel("Real part of Dielectric Function")
    plt.title("Real Dielectric Function with Standard Basis")
    plt.plot(energyRange, wlist, 'r')
    plt.show() 
    return
print(testStandardDielectricPlotReal())








#OPTIMAL DIELECTRIC FUNCTION USING OPTIMAL BASIS IMPLEMENTATION

@timerPrint
def testOptimalDielectricPlotImaginary():
    numberOccupied = qobj.getNumberOccupied()
    N_b = qobj.getN_B()
    energyRange = qobj.getEnergyRangeFunc()
    OBek = qobj.getOBek()
    E, OBck = qobj.getInterpolateHamiltonianEE()
    del OBck
    damp = qobj.getDamp()
    velocity = qobj.getInterpolatedVelocityOperator()
    wlist = dielectricPlotImaginaryArray(N_b, OBek, damp, energyRange, velocity, numberOccupied)
    plt.xlabel("Energy")
    plt.ylabel("Imaginary part of Dielectric Function")
    plt.title("Complex Dielectric Function with Optimal Basis")
    plt.plot(energyRange, wlist, 'b')
    plt.show() 
    return 
print(testOptimalDielectricPlotImaginary())  


@timerPrint
def testOptimalDielectricPlotReal():
    numberOccupied = qobj.getNumberOccupied()
    N_b = qobj.getN_B()
    energyRange = qobj.getEnergyRangeFunc()
    OBek = qobj.getOBek()
    E, OBck = qobj.getInterpolateHamiltonianEE()
    del OBck
    damp = qobj.getDamp()
    velocity = qobj.getInterpolatedVelocityOperator()
    wlist = dielectricPlotRealArray(N_b, OBek, damp, energyRange, velocity, numberOccupied)
    plt.xlabel("Energy")
    plt.ylabel("Real part of Dielectric Function")
    plt.title("Real Dielectric Function with Optimal Basis")
    plt.plot(energyRange, wlist, 'r')
    plt.show() 
    return 
print(testOptimalDielectricPlotReal())








