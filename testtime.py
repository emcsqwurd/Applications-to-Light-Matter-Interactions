from quantum.gettime import differenceInTimeVaryingSb
from quantum.gettime import standardTimeForEk, optimisedTimeForEk, differenceInTimeForObtainingEkSPECIFIC, differenceInTimeForObtainingEk
from quantum.gettime import timeOptimalDielectric, timeStandardDielectric
from quantum.qobj import Qobj
import numpy as np



qobj = Qobj()


"""Obtaining input paramters by utilizing Quantum Object Class"""
N_G = qobj.getN_G()
N_k = qobj.getN_K()
N_b = qobj.getN_B()
potential = qobj.getPotential()
OB_bi = qobj.getOptimalBasis()
kList = qobj.getKList()
k0 = qobj.getk0()
k1 = qobj.getk1()
VLoc = qobj.getVLoc()
N = qobj.getN_B()
ck = qobj.getCk()




"""Function to be run that obtains difference in Computationan time for obtaining
Eigenvalues with respect to the Standard Basis implementation and the Optimal
Basis implementation respectively.  Function denoted SPECIFIC as gives time for
each respective method, can be utilized to determine result when running individual 
tests"""
def testTimesForEigenvaluesSPECIFIC():
    resultDifference = differenceInTimeForObtainingEkSPECIFIC(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N)
    return resultDifference
#print(testTimesForEigenvaluesSPECIFIC())    




"""Function to be run to obtain Array demonstrating the relationship for Sb value
and the difference in Computation time regarding both respective methods"""
def varyingSbEk():
    differenceList = []
    sbValues = np.linspace(0,1,100)
    for sb in (sbValues):
        qobj.__setSb(sb)
        resultDifference = differenceInTimeForObtainingEk(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N)
        differenceList.append(resultDifference)
    differenceArray = np.array(differenceList)    
    return differenceArray
#print(varyingSbEk())





#QUANTUM OBJECT IMPLEMENTATION TESTING




"""Function to be run to test computation time for obtaining Eigenvalues with respect
to the standard Basis implementation, i.e, time for solveSchrodinger() function"""
def testTimeEkSS():
    res = qobj.getEkTimeSolveSchrodinger()
    print("----Time Elapsed using solveSchrodinger()----")
    print("solveSchrodinger: " + str(res))
    return
#print(testTimeEkSS())    




"""Function to be run to test computation time for obtaining Eigenvalues with respect
to the Optimal Basis implementation, i.e, time for interpolateHamiltonian() function"""
def testTimeEkIH():
    res = qobj.getEkTimeInterpolateHamiltonian()
    print("----Time Elapsed using interpolateHamiltonian()----")
    print("interpolateHamiltonian: " + str(res))
    return
#print(testTimeEkIH())





"""Function to be run to test difference in computation time for obtaining 
Eigenvalues regarding both respective approaches"""
def testDifferenceInTimeEk():
    res = qobj.getDifferenceTimeForEk()
    print("----Time difference in obtaining EigenValues----")
    print("Difference: " + str(res))
    return 
#print(testDifferenceInTimeEk())





"""Function that obtains difference in computation time regarding both respective
approaches as the Threshold value varies"""
def testDifferenceInTimeVaryingSb():
    res = differenceInTimeVaryingSb(N_b, N_k, ck, potential, kList)
    return res
#print(testDifferenceInTimeVaryingSb())



def testTimeStandardDielectric():
    N_b = qobj.getN_B()
    ek = qobj.getEk()
    damp = qobj.getDamp()
    w = qobj.getW()
    stanV = qobj.getStandardVelocityOperator()
    numOcc = qobj.getNumberOccupied()
    res = timeStandardDielectric(N_b, ek, damp, w, stanV, numOcc)
    return res
print(testTimeStandardDielectric())    





#N_b, OBek, damp, w, OBvelocity, numberOccupied
def testTimeOptimalDielectric():
    N_b = qobj.getN_B()
    OBek = qobj.getOBek()
    damp = qobj.getDamp()
    w = qobj.getW()
    OBV = qobj.getInterpolatedVelocityOperator()
    numOcc = qobj.getNumberOccupied()
    res = timeOptimalDielectric(N_b, OBek, damp, w, OBV, numOcc)
    return res
print(testTimeOptimalDielectric())    








