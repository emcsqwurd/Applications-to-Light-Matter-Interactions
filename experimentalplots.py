"""File designated for experimental plots to obtain."""




import numpy as np
from quantum.optimalbasis import optimalBasis
import matplotlib.pyplot as plt
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc, interpolateHamiltonianEE
from quantum.schrodinger import solveSchrodinger
from quantum.gettime import differenceInTimeForObtainingEk, standardTimeForEk, optimisedTimeForEk, optimisedTimeForEkEE, optimisedTimeForEkEENEW
from quantum.gettime import optimisedTimeForEkNEW, timeOptimalDielectric, timeStandardDielectric
from quantum.velocityOp import standardVelocity, interpolatedVelocity
import time
from quantum.table import differenceInEigenvalues
from quantum.utils import kvec



"""Function to investigate the size of Optimal Basis as Threshold sb varies"""
def sbEffectOnSize(N_b, N_k, ck):
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    #sbValues = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001 ]
    for s_b in (sbValues):
        getOptimalBasis = optimalBasis(s_b, N_b, N_k, ck) 
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)
    #print(myListOb)    
    myresultOb = np.array(myListOb)
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(myresultOb, myresultSb, 'g')
    plt.show()




"""Plot to show how the Number of Bands is directly dictated by the threshold sb"""
def varyingNbOBPlot(N_k, ck):
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    for N_B in range(3, 7):
        sbEffectOnSize(N_B, N_k, ck)
        symbolList[i]
        i += 1
    return 




"""Function to show size of Optimal basis against Standard Basis"""
def optimalBasisVsCk(N_b, N_k, ck):
    myListOb = []
    myListCk = []
    sbValues = np.linspace(0,1,250)
    for s_b in sbValues:
        OB_bi = optimalBasis(s_b, N_b, N_k, ck)
        sizeOB_bi = OB_bi.size
        myListOb.append(sizeOB_bi)
        sizeCk = ck.size
        myListCk.append(sizeCk)
    myresultOb = np.array(myListOb)
    myresultCk = np.array(myListCk)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Size of Ck")
    plt.plot(myresultOb, myresultCk, 'r')
    plt.show()




"""Function to show relationship between eigenvalues obtained from implementing standard
Basis against Eigenvalues obtained from implementing Optimal Basis"""
def ekVsE(OB_bi, kList, k0, k1, VLoc, N_b, N_G, N_k, potential):
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    ek, ck = solveSchrodinger(N_G, N_k, N_b, potential )
    del ck
    plt.xlabel("ek")
    plt.ylabel("E")
    plt.plot(ek, E , 'b')
    plt.show()    



"""Function demonstrating the effect of the Eigenenergies obtained agaisnt 
the number of plane-waves included in the approximation of the periodic state"""
def EnergyVsN_G(N_k, N_b, potential):
    N_GValues = np.linspace(0,100,1)
    for Ng in(N_GValues):
        ek, ck = solveSchrodinger(Ng, N_k, N_b, potential)
    del ck
    plt.plot(ek, Ng)
    plt.show()    
    return 



"""Function demonstrating the effect the Threshold sb has on the Eigenvalues obtained"""
def sbEffectOnEigenvalues(N_b, N_k, ck, OB_bi, kList, k0, k1, VLoc, N):
    myListSb = []
    sbValues = np.linspace(0,1,250)
    for s_b in sbValues:
        OB_bi = optimalBasis(s_b, N_b, N_k, ck) 
        myListSb.append(s_b)
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N )
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(E, myresultSb, 'g')
    plt.show()
    
    



#IMPROVED BELOW
"""Function demonstrating the relationship between the time taken to obtain 
solutions with respect to the optimal Basis implementation and the Threshold sb"""
def timePlotVaryingSb(N_b, N_k, ck, potential, kList):
    N = N_b
    sbValues = np.linspace(0.5,0,100)
    sbList = []
    timeList = []
    for sb in sbValues:
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
    print(arrayTime)
    plt.xlabel("InterpolateHamiltonian() Computation Time")
    plt.ylabel("sb Value")
    plt.plot(arrayTime, arraySb, 'b')
    plt.show()




"""Function demonstrating the relationship between the Threshold value sb and the 
difference in Eigenvalues obtained regarding the respective approaches implemented """
def sbEffectOnPrecision(N_G, N_k, N_b, potential, N):
    sbList = []
    maxEigList = []
    sbValues = [0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    sb = 0
    for sb in sbValues:
        difference = differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N)
        sbList.append(sb)
        maxEigList.append(difference)
        sb += 1
    sbArray = np.array(sbList)
    eigArray = np.array(maxEigList)
    plt.xlabel("Maximum difference between eigenvalues obtained comparing SS & IH")
    plt.ylabel("sb Value")
    plt.plot(eigArray, sbArray, 'b')
    plt.show()
    



"""Function demonstrating the relationship between the the number of k-points 
being considered and the computational cost of obtaining solutions to the 
Schrodinger Equation with respect to the standard approach, that is, 
with respect to the standard Basis"""
def kpointsVsTimeSS(N_G, N_b, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = standardTimeForEk(N_G, NK, N_b, potential)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    plt.ylabel("Computation time to obtain solutions for SS")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.plot(NKArray, timeArray, 'r')
    plt.show()






"""Function that obtains two arrays equivalent to the plot demonstrating the
relationship between the number of k-points being considered and the computational
cost of obtaining solutions to the Schrodinger Equation with respect to the 
Standard Basis implementation"""
def kpointsVsTimeSSArray(N_G, N_b, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = standardTimeForEk(N_G, NK, N_b, potential)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    return NKArray, timeArray




"""Function that takes the plot demonstrating the relationship between the number of 
k-points being considered and the computational cost of obtaining solutions
with respect to the standard Basis implementation, and repeats this plot 100
times to obtain an repeated for such a relationship, as the underlying plot
will vary slightly each time it is ran"""
def repeatedPlotSS(N_G, N_b, potential):
    i = 0
    for i in range(0, 100):
        repeated = kpointsVsTimeSS(N_G, N_b, potential)
        i += 1
    plt.show()    
    return repeated




"""Function that plots the relationship between the number of k-points being 
considered and the computational cost of obtaining such solutions with respect
to the Standard Basis implementation.  The function outputs the line of best fit 
from the plot obtained"""
def averagePlotSSLineOfBestFit(N_G, N_b, potential):
    i = 0
    for i in range(0, 100):
        NKArray, timeArray = kpointsVsTimeSSArray(N_G, N_b, potential)
        plt.plot(NKArray, timeArray, 'r')
        if i == 99:
            a, b = np.polyfit(NKArray, timeArray, 1)
            plt.plot(NKArray, a*NKArray+b, 'y')
            i += 1  
    plt.ylabel("Computation time to obtain solutions for SS")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.show()    
    return 







"""Function that demonstrates the relationship between the number of k-points being 
considered and the computational cost of obtaining solutions to the Schrodinger 
Equation with respect to the Optimal Basis implementation.  Function will obtain a 
plot of such a relationship"""
def kpointsVsTimeIHEE(OB_bi, k0, k1, VLoc, N, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = optimisedTimeForEkEENEW(OB_bi, k0, k1, VLoc, N, potential, NK)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    plt.ylabel("Computation time to obtain solutions for IH")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.plot(NKArray, timeArray, 'b')
    #plt.show()





"""Function that returns two Arrays equivalent to the plot that demonstrates 
the relationship between the computational cost of obtaining solutions to the 
Schrodinger Equation with respect to the Optimal Basis implementation for 
interpolateHamiltonianEE().  Outputs Array of N_K points and Array for computation time.  
This function is utilized to obtain a line of best fit when the underlying relationship 
is obtained several times"""
def kpointsVsTimeIHEEArray(OB_bi, k0, k1, VLoc, N, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = optimisedTimeForEkEENEW(OB_bi, k0, k1, VLoc, N, potential, NK)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    return NKArray, timeArray





"""Function that takes the plot demonstrating the relationship between the number
of k-points being considered and the computational cost of obtaining solutions 
with respect to the Optimal Basis implementation, and repeats the plot 100 times
to achieve an average of such a relationsip, as the underlying plot will vary
each time it is ran"""
def repeatedPlotIHEE(OB_bi, k0, k1, VLoc, N, potential):
    i = 0
    for i in range(0, 100):
        repeated = kpointsVsTimeIHEE(OB_bi, k0, k1, VLoc, N, potential)
        i += 1
    plt.show()    
    return repeated



"""Function that performs the same task as the function described above, but also 
plots the line of best fit (average) of all the plots, to give a more accurate 
representation of the relationship between k-points and the computational 
cost of achieving the results"""
def averagePlotIHEELineOfBestFit(OB_bi, k0, k1, VLoc, N, potential):
    i = 0
    for i in range(0, 100):
        NKArray, timeArray = kpointsVsTimeIHEEArray(OB_bi, k0, k1, VLoc, N, potential)
        plt.plot(NKArray, timeArray, 'b')
        if i == 99:
            a, b = np.polyfit(NKArray, timeArray, 1)
            plt.plot(NKArray, a*NKArray+b, 'y')
            i += 1  
    plt.ylabel("Computation time to obtain solutions for IH")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.show()    
    return 




"""Function to obtain plot giving the Line of Best Fit of relationship between 
computation time to obtain results and the number of k-points being considered
with respect to the Standard Basis implementation, and the line of Best fit of
the relationship between computation time to obtain results and the number of
k-points being considered with respect to the Optimal Basis implementation"""
def respectiveLOBF(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N):
    i = 0
    for i in range(0, 100):
        NKArraySS, timeArraySS = kpointsVsTimeSSArray(N_G, N_b, potential)
        NKArrayIH, timeArrayIH = kpointsVsTimeIHEEArray(OB_bi, k0, k1, VLoc, N, potential)
        if i == 99:
            a1, b1 = np.polyfit(NKArraySS, timeArraySS, 1)
            a2, b2 = np.polyfit(NKArrayIH, timeArrayIH, 1)
            plt.plot(NKArraySS, a1*NKArraySS+b1, 'r')
            plt.plot(NKArrayIH, a2*NKArrayIH+b2, 'b')
            differenceX = NKArraySS
            differenceY = a1*NKArraySS+b1 - a2*NKArrayIH+b2
            plt.plot(differenceX, differenceY, 'g')
            i += 1  
    plt.ylabel("Computation time to obtain solutions")
    plt.xlabel("Number of k-points (N_k) being considered")
    plt.legend(['Standard Basis', 'Optimal Basis'])   
    plt.show()







""""""
def respectiveLOBFDifference(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N):
    i = 0
    for i in range(0, 100):
        NKArraySS, timeArraySS = kpointsVsTimeSSArray(N_G, N_b, potential)
        NKArrayIH, timeArrayIH = kpointsVsTimeIHEEArray(OB_bi, k0, k1, VLoc, N, potential)
        if i == 99:
            a1, b1 = np.polyfit(NKArraySS, timeArraySS, 1)
            a2, b2 = np.polyfit(NKArrayIH, timeArrayIH, 1)
            differenceX = NKArraySS
            differenceY = a1*NKArraySS+b1 - a2*NKArrayIH+b2
            differencePercent = (differenceY/a1*NKArraySS+b1)/100
            plt.plot(differenceX, differencePercent, 'y')
            i += 1  
    plt.ylabel("Percentage difference ( between Green and red)")
    plt.xlabel("Number of k-points (N_k) being considered")
    #plt.legend()   
    plt.show()







"""Function that returns two Arrays equivalent to the plot that demonstrates 
the relationship between the computational cost of obtaining solutions to the 
Schrodinger Equation with respect to the Optimal Basis implementation for 
interpolateHamiltonian().  Outputs Array of N_K points and Array for computation time.  
This function is utilized to obtain a line of best fit when the underlying relationship 
is obtained several times"""
def kpointsVsTimeIHArray(OB_bi, k0, k1, VLoc, N, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = optimisedTimeForEkNEW(OB_bi, k0, k1, VLoc, N, potential, NK)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList)
    return NKArray, timeArray





"""Function to obtain the plot demonstrating the line of Best Fit with respect 
to the relationship between the number of k-points and the computation time for 
obtaining solutions for interpolateHamiltonian(), and the line of Best Fit with 
respect to the relationship between the number of k-points and the computation time
for obtaining solutions for interpolateHamiltonianEE()"""
def comparingInterpolates(OB_bi, k0, k1, VLoc, N, potential):
    i = 0
    for i in range(0, 100):
        NKArrayIH, timeArrayIH = kpointsVsTimeIHArray(OB_bi, k0, k1, VLoc, N, potential)
        NKArrayIHEE, timeArrayIHEE = kpointsVsTimeIHEEArray(OB_bi, k0, k1, VLoc, N, potential)
        if i == 99:
            a1, b1 = np.polyfit(NKArrayIH, timeArrayIH, 1)
            a2, b2 = np.polyfit(NKArrayIHEE, timeArrayIHEE, 1)
            plt.plot(NKArrayIH, a1*NKArrayIH+b1, 'darkorange')
            plt.plot(NKArrayIHEE, a2*NKArrayIHEE+b2, 'darkviolet')
            i += 1  
    plt.ylabel("Computation time to obtain solutions")
    plt.xlabel("Number of k-points (N_k) being considered")
    plt.legend(['interpolateHamiltonian()', 'interpolateHamiltonianEE()'])   
    plt.show()




"""Function to perform convergence test on the effect the Threshold has on the 
maximum difference in Eigenvalues obtained"""
def thresholdVsMaxDiffEigenvalue(N_G, N_k, N_b, potential, N):
    sbList = []
    differenceList = []
    #sbValues = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    sbValues = np.linspace(0.0001, 0.2, 100)
    for sb in sbValues:
        differenceEig = differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N)
        differenceList.append(differenceEig)
        sbList.append(sb)
    sbArray = np.array(sbList)
    differenceArray = np.array(differenceList)
    plt.xlabel("Threshold value")
    plt.ylabel("Maximum difference in Eigenvalues obtained from respective Approaches")
    plt.plot(sbArray, differenceArray, 'b')
    plt.show()        
    #return 




"""Function to compare computational cost of obtaining solutions for the standard basis
implementation for large k-values with computational cost of obtaining solutions for the
optimal basis implementation"""
def differenceInCompVaryingKPoints(N_G, N_b, potential, OB_bi, k0, k1, VLoc, N):
    NKValuesStandard = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    NKValuesOptimal = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200]
    standardTimeList = []
    standardNKList = []
    optimalTimeList = []
    optimalNKList = []
    i = 0
    for i in range(0,100):
        for NKS in NKValuesStandard:
            timeResultStandard = standardTimeForEk(N_G, NKS, N_b, potential)
            standardTimeList.append(timeResultStandard)
            standardNKList.append(NKS)
        standardTimeArray = np.array(standardTimeList)
        standardNKArray = np.array(standardNKList)
        #plt.plot(standardNKArray, standardTimeArray, 'r')
        for NKO in NKValuesOptimal:
            timeResultOptimal = optimisedTimeForEkEENEW(OB_bi, k0, k1, VLoc, N, potential, NKO)
            optimalTimeList.append(timeResultOptimal)
            optimalNKList.append(NKO)
        optimalTimeArray = np.array(optimalTimeList) 
        optimalNKArray = np.array(optimalNKList)
        #plt.plot(optimalNKArray, optimalTimeArray, 'b')
        if i == 99:
            fig, ax1 = plt.subplots()
            del fig
            ax2 = ax1.twinx()
            aS, bS = np.polyfit(standardTimeArray,standardNKArray , 1)
            aO, bO = np.polyfit(optimalTimeArray, optimalNKArray, 1)
            ax1.plot(standardTimeArray, aS*standardTimeArray+bS, 'r')
            ax2.plot(optimalTimeArray, aO*optimalTimeArray+bO, 'b')
        i += 1
    ax1.set_xlabel('Computation time to obtain solutions (seconds)')
    ax1.set_ylabel('k-points considered in Standard Basis implementation')
    ax2.set_ylabel('k-points considered in Optimal Basis implementation')
    plt.show()   
   




"""Function to obtain the relationship between the computation time to obtain the dielectric function
with regards to the standard basis implementation against the number of k-points being
considerd.  Function outputs arrays for both computation time and number of k-points
being considered"""
def standardDielectricTimeNKRelationship(N_G, N_b, potential, damp, w, numberOccupied):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    NKList = []
    timeList = []
    for NK in NKValues:
        ek, ck = solveSchrodinger(N_G,NK,N_b,potential)
        stanVel = standardVelocity(potential, ck)
        timeD = timeStandardDielectric(N_b, ek, damp, w, stanVel, numberOccupied)
        NKList.append(NK)
        timeList.append(timeD)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList)
    return NKArray, timeArray




"""Function to obtain the relationship between the computation time to obtain the dielectric
function with regards to the optimal basis implementation against the number of k-points
being considerd.  Function outputs arrays for both the computation time and the number
of k-points being considered"""
def optimalDielectricTimeNKRelationship(N_G, N_b, potential, sb, N, damp, w, numberOccupied):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    NKList = []
    timeList = []
    for NK in NKValues:
        ek, ck = solveSchrodinger(N_G,NK,N_b,potential)
        del ek
        OB_bi = optimalBasis(sb, N_b, NK, ck)
        k0 = calculatek0(OB_bi, potential)
        k1 = calculatek1(OB_bi, potential)
        VLoc = calculateVLoc(OB_bi, potential)
        a = potential.parms["lattice"]
        kList = []
        for i in range(NK):
            kList.append(kvec(i,a,NK))
        OBek, OBck = interpolateHamiltonianEE(OB_bi, kList, k0, k1, VLoc, N)
        interVel = interpolatedVelocity(potential, OBck, k1)
        timeD = timeOptimalDielectric(N_b, OBek, damp, w, interVel, numberOccupied)
        NKList.append(NK)
        timeList.append(timeD)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList)
    return NKArray, timeArray    

        


"""Function that plots the relationship between the computation time to obtain the 
dielectric function with regards to the standard basis implementation against the number of
k-points being considered.  This plot is then repeated 100 times, and an average line of
best fit of all plots is obtained"""
def averagePlotStandardDielectricLineOfBestFit(N_G, N_b, potential, damp, w, numberOccupied):
    i = 0
    for i in range(0, 100):
        NKArray, timeArray = standardDielectricTimeNKRelationship(N_G, N_b, potential, damp, w, numberOccupied)
        plt.plot(NKArray, timeArray, 'b')
        if i == 99:
            a, b = np.polyfit(NKArray, timeArray, 1)
            plt.plot(NKArray, a*NKArray+b, 'y')
            i += 1  
    plt.ylabel("Computation time to obtain Dielectric Standard Basis")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.show()    
    return 





"""Function that plots the relationship between the computation time to obtain the 
dielectric function with regards to the optimal basis implementation against the number of
k-points being considered.  This plot is then repeated 100 times, and an average line of
best fit of all plots is obtained"""
def averagePlotOptimalDielectricLineOfBestFit(N_G, N_b, potential, sb, N, damp, w, numberOccupied):
    i = 0
    for i in range(0, 100):
        NKArray, timeArray = optimalDielectricTimeNKRelationship(N_G, N_b, potential, sb, N, damp, w, numberOccupied)
        plt.plot(NKArray, timeArray, 'b')
        if i == 99:
            a, b = np.polyfit(NKArray, timeArray, 1)
            plt.plot(NKArray, a*NKArray+b, 'y')
            i += 1  
    plt.ylabel("Computation time to obtain Dielectric Optimal Basis")
    plt.xlabel("Number of k-points (N_k) being considered")   
    plt.show()    
    return 





"""Function that plots the average line of best fit regarding the standard basis for the
relationship between the computation time to obtain the dielectric function against
the number of k-points being considered, with the average line of best fit regarding
the optimal basis for the relationship between the computation time to obtain the dielectric
function against the number of k-points being considered, so a direct comparison can be made"""
def comparingDielectrics(N_G, N_b, potential, damp, w, numberOccupied, sb, N):
    i = 0
    for i in range(0, 100):
        NKArrayS, timeArrayS = standardDielectricTimeNKRelationship(N_G, N_b, potential, damp, w, numberOccupied)
        NKArrayO, timeArrayO = optimalDielectricTimeNKRelationship(N_G, N_b, potential, sb, N, damp, w, numberOccupied)
        if i == 99:
            a1, b1 = np.polyfit(NKArrayS, timeArrayS, 1)
            a2, b2 = np.polyfit(NKArrayO, timeArrayO, 1)
            plt.plot(NKArrayS, a1*NKArrayS+b1, 'purple')
            plt.plot(NKArrayO, a2*NKArrayO+b2, 'green')
            plt.ylim(0,0.0025)
            i += 1  
    plt.ylabel("Computation time to obtain Dielectric Function")
    plt.xlabel("Number of k-points (N_k) being considered")
    plt.legend(['Standard Basis Dielectric', 'Optimal Basis Dielectric'])   
    plt.show()







