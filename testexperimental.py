from quantum import potential
from quantum.experimentalplots import EnergyVsN_G, repeatedPlotIHEE, averagePlotIHEELineOfBestFit, optimalBasisVsCk, sbEffectOnPrecision 
from quantum.experimentalplots import sbEffectOnSize, ekVsE, timePlotVaryingSb, sbEffectOnEigenvalues
from quantum.experimentalplots import kpointsVsTimeSS, kpointsVsTimeIHEE, repeatedPlotSS, averagePlotSSLineOfBestFit
from quantum.experimentalplots import respectiveLOBF, comparingInterpolates, thresholdVsMaxDiffEigenvalue, respectiveLOBFDifference
from quantum.experimentalplots import differenceInCompVaryingKPoints, averagePlotStandardDielectricLineOfBestFit
from quantum.experimentalplots import averagePlotOptimalDielectricLineOfBestFit, comparingDielectrics
from quantum.plot import plotFun
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.qobj import Qobj
import matplotlib.pyplot as plt
import os

#os._exit(00)




qobj = Qobj()




"""Function to be run to test the Relationship between the Threshold and the resulting
size of the Optimal Basis"""
def testSbEffectOnSize():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    res = sbEffectOnSize(N_b, N_k, ck)
    return res
#print(testSbEffectOnSize())    




"""Function to be run testing the plot of the Wavefunctions with respect to 
the Optimal Basis implementation"""
def testOBPlotFun():
    ik = 2
    NCell = 3
    NPoints = 10
    shift = 2
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    kList = qobj.getKList()
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    plotfun = plotFun(ik, E, OB_bi, NCell, NPoints, potential, 'b', shift )
    return plotfun
#print(testOBPlotFun())




#IMPROVED ELSEWHERE
"""Function to be run that demonstrates the relationship between the Threshold
and the computation time for obtaining the solutions of the schrodinger Equation,
that is, solutions obtained from relevant interpolateHamiltonian() function"""
def testTimePlotVaryingSb():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    potential = qobj.getPotential()
    kList = qobj.getKList()
    res = timePlotVaryingSb(N_b, N_k, ck, potential, kList)
    return res
#print(testTimePlotVaryingSb())    




"""Function to be run that plots the relationship between the Threshold and the precision
of the results obtained, that is, the maximum difference in Eigenvalues with respect
of each respective approach to obtain such solutions"""
def testSbEffectOnPrecision():
    N_G = qobj.getN_G()
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    N = N_b
    res = sbEffectOnPrecision( N_G, N_k, N_b, potential, N)
    return res
#print(testSbEffectOnPrecision())



"""Function to be run that plots the relationship of the number of k-points
to be run over and the the computation time to obtain solutions with respect
to the Standard Basis approach, that is, with respect to the solveSchrodinger()
function to obtain solutions"""
def testkpointsVsTimeSS():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    result = kpointsVsTimeSS(N_G, N_b, potential)
    return result
#print(testkpointsVsTimeSS())    



"""Function to be run that plots the above function 100 times, as the above function
result will vary each time it is ran, to achieve accurate results such a test is 
required"""
def testRepeatedPlotSS():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    result = repeatedPlotSS(N_G, N_b, potential)
    return result 
#print(testAveragePlotSS())




"""Function to be run to obtain the line of Best Fit of the plot demonstrating
the relationship between the number of k-points being considered and the 
computation time of obtaining results with respect to the Standard Basis 
implementation that has been ran 100 times"""
def testAveragePlotSSLineOfBestFit():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    result = averagePlotSSLineOfBestFit(N_G, N_b, potential)
    return result
#print(testAveragePlotSSLineOfBestFit())    




"""Function to be run to obtain the plot demonstrating the relationship of the
number of k-points to be interated over and the computation time of obtaining 
solutions with respect to the Optimal Basis implementation"""
def testkpointsVsTimeIHEE():
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    potential = qobj.getPotential()
    result = kpointsVsTimeIHEE(OB_bi, k0, k1, VLoc, N, potential)
    return result
#print(testkpointsVsTimeIHEE())    




"""Function to be run that obtains the line of best fit of the plot that 
runs 100 times demonstrating the relationship between the number of k-points
to be iterated over and the computation time of obtaining such solutions
with respect to the Optimal Basis approach"""
def testRepeatedPlotIHEE():
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    potential = qobj.getPotential()
    result = repeatedPlotIHEE(OB_bi, k0, k1, VLoc, N, potential)
    return result 
#print(testAveragePlotIHEE())





"""Function to be run to obtain the line of best fit from plotting the relationship
between the number of k-points being considered and the computational cost of 
obtaining solutions with respect to the Optimal Basis implementation"""
def testAveragePlotIHEELineOfBestFit():
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    potential = qobj.getPotential()
    result = averagePlotIHEELineOfBestFit(OB_bi, k0, k1, VLoc, N, potential)
    return result
#print(testAveragePlotIHEELineOfBestFit())    



"""Function to be run to obtain line of Best Fit for relationship between
k-points and computation time for Standard Basis, and line of Best Fit for 
relationship between k-points and computation time for Optimal Basis"""
def testRespectiveLOBF():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    result = respectiveLOBF(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N)
    return result 
#print(testRespectiveLOBF())




""""""
def testRespectiveLOBFDifference():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    result = respectiveLOBFDifference(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N)
    return result 
#print(testRespectiveLOBFDifference())







"""Function to be run that compares the computational cost with respect to the number
of k-points being interpolated over for interpolateHamiltonin() and 
interpolateHamiltonianEE() respectively"""
def testComparingInterpolates():
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    result = comparingInterpolates(OB_bi, k0, k1, VLoc, N, potential)
    return result 
#print(testComparingInterpolates())






"""NEW"""
def testThresholdVsMaxDiffEigenvalue():
    N_G = qobj.getN_G()
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    N = N_b
    result = thresholdVsMaxDiffEigenvalue(N_G, N_k, N_b, potential, N)
    return result 
#print(testThresholdVsMaxDiffEigenvalue())





"""Function to be run to"""
def testDifferenceInCompVaryingKPoints():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N = N_b
    result = differenceInCompVaryingKPoints(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N)
    return result 
#print(testDifferenceInCompVaryingKPoints())





""""""
def testStandardDielectricTimeNKRelationship():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    damp = qobj.getDamp()
    w = qobj.getW()
    numOcc = qobj.getNumberOccupied()
    res = averagePlotStandardDielectricLineOfBestFit(N_G, N_b, potential, damp, w, numOcc)
    return res
#print(testStandardDielectricTimeNKRelationship())    




""""""
def testOptimalDielectricTimeNKRelationship():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    sb = qobj.getSb()
    kList = qobj.kList()
    N = qobj.getN_B()
    damp = qobj.getDamp()
    w = qobj.getW()
    numOcc = qobj.getNumberOccupied()
    res = averagePlotOptimalDielectricLineOfBestFit(N_G, N_b, potential, sb, kList, N, damp, w, numOcc)
    return res
#print(testOptimalDielectricTimeNKRelationship())




""""""
def testCompareDielectrics():
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    damp = qobj.getDamp()
    w = qobj.getW()
    numOcc = qobj.getNumberOccupied()
    sb = qobj.getSb()
    N = qobj.getN_B()
    res = comparingDielectrics(N_G, N_b, potential, damp, w, numOcc, sb, N)
    return res
print(testCompareDielectrics())







