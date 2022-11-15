"""File to calculate the time differences in determining the time taken to obtain
the eigenvalues from each respective aprroach (SS and IH).  The difference in such
time is also calculated."""


from quantum.schrodinger import solveSchrodinger
from quantum.interpolate import interpolateHamiltonian, interpolateHamiltonianEE
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import calculatek0, calculatek1, calculateVLoc
from quantum.utils import kvec
from quantum.dielectric import dielectricFunc
import numpy as np
import time



"""Function to obtain the time taken to calculate solutions of the
Schrodinger Equation using solveSchrodinger(), that is, using the standard
Basis approach"""
def standardTimeForEk(N_G, N_k, N_b, potential):
    startTimeStandard = time.time()
    solveSchrodinger(N_G, N_k, N_b, potential)
    endTimeStandard = time.time()
    timeElapsed = endTimeStandard - startTimeStandard
    return timeElapsed




"""Function to obtain the time taken to calculate eigenvalues using 
interpolateHamiltonain(), that is, to determine the eigenvalues when solving 
the Schrodinger Equation with respect to the Optimal Basis implementation"""
def optimisedTimeForEk(OB_bi, kList, k0, k1, VLoc, N):
    startTimeOptimised = time.time()
    interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
    endTimeOptimised = time.time() 
    timeElapsed = endTimeOptimised - startTimeOptimised
    return timeElapsed
    


"""Function to perform the same task as the function above, however is altered such
that kList is now not included as a paramter, which gives rise to greater
Flexability when plotting such time against other parameters """
def optimisedTimeForEkNEW(OB_bi, k0, k1, VLoc, N, potential, N_k):
    a = potential.parms["lattice"]
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    startTimeOptimised = time.time()
    interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
    endTimeOptimised = time.time() 
    timeElapsed = endTimeOptimised - startTimeOptimised
    return timeElapsed




"""Function to obtain the time taken to obtain the solutions of the Schrodinger 
Equation (this time both Eigenvalues and Eigenvectors) with respect to the 
Optimal Basis implementation"""
def optimisedTimeForEkEE(OB_bi, kList, k0, k1, VLoc, N):
    startTimeOptimised = time.time()
    interpolateHamiltonianEE(OB_bi, kList, k0, k1, VLoc, N)
    endTimeOptimised = time.time() 
    timeElapsed = endTimeOptimised - startTimeOptimised
    return timeElapsed




"""Function to perform the same task as the function above, however is altered such
that kList is now not included as a paramter, which gives rise to greater
Flexability when plotting such time against other parameters"""
def optimisedTimeForEkEENEW(OB_bi, k0, k1, VLoc, N, potential, N_k):
    a = potential.parms["lattice"]
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    startTimeOptimised = time.time()
    interpolateHamiltonianEE(OB_bi, kList, k0, k1, VLoc, N)
    endTimeOptimised = time.time() 
    timeElapsed = endTimeOptimised - startTimeOptimised
    return timeElapsed





"""Function that obtains the difference in the time taken to calculate the solutions
to the Schrodinger Equation between both respective methods.  Labelled SPECIFIC as 
running this function allows for individual tests to be conducted"""
def differenceInTimeForObtainingEkSPECIFIC(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N):
    SSTimeForEk = standardTimeForEk(N_G, N_k, N_b, potential)
    IHTimeForEk = optimisedTimeForEk(OB_bi, kList, k0, k1, VLoc, N)
    difference = SSTimeForEk - IHTimeForEk
    print("----solveSchrodinger() Time for obtaining ek----")
    print(SSTimeForEk)
    print("----interpolateHamiltonian() Time for obtaining ek----")
    print(IHTimeForEk)
    print("----Difference in Time between SS and IH for ek----")
    print(difference)
    return




"""Function that performs the same task as the function above, which is introduced
such that it can be utilized elsewhere as appose to running specific, individual
tests"""
def differenceInTimeForObtainingEk(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N):
    SSTimeForEk = standardTimeForEk(N_G, N_k, N_b, potential)
    IHTimeForEk = optimisedTimeForEk(OB_bi, kList, k0, k1, VLoc, N)
    difference = SSTimeForEk - IHTimeForEk
    return difference



#CHECK IF NEEDED
"""Function to obtain the difference in time for varying sb"""
def differenceInTimeVaryingSb(N_b, N_k, ck, potential, kList):
    N = N_b
    sbValues = np.linspace(0.5,0,100)
    sbList = []
    timeList = []
    for sb in (sbValues):
        OB_bi = optimalBasis(sb, N_b, N_k, ck)
        k0 = calculatek0(OB_bi, potential)
        k1 = calculatek1(OB_bi, potential)
        VLoc = calculateVLoc(OB_bi, potential)
        startTime = time.time()
        interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
        endTime = time.time()
        elapsedTime = endTime - startTime
        sbList.append(sb)
        timeList.append(elapsedTime)
    sbList = sbList[:-1]
    timeList = timeList[:-1]  
    arraySb = np.array(sbList)
    arrayTime = np.array(timeList) 
    print("---------arraySb values--------")
    print(arraySb)
    print("---------arrayTime values-------")
    print(arrayTime)
    return 






def timeStandardDielectric(N_b, ek, damp, w, velocity, numberOccupied):
    starttime = time.time()
    dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
    endtime = time.time()
    timeElapsed = endtime - starttime
    return timeElapsed




def timeOptimalDielectric(N_b, OBek, damp, w, OBvelocity, numberOccupied):
    starttime = time.time()
    dielectricFunc(N_b, OBek, damp, w, OBvelocity, numberOccupied)
    endtime = time.time()
    timeElapsed = endtime - starttime
    return timeElapsed




def differenceTimeDielectric(N_b, ek, OBek, damp, w, velocity, OBvelocity, numberOccupied):
    timeStandard = timeStandardDielectric(N_b, ek, damp, w, velocity, numberOccupied)
    timeOptimal = timeOptimalDielectric(N_b, OBek, damp, w, OBvelocity, numberOccupied)
    timeDifference = timeStandard - timeOptimal
    return timeDifference



    



