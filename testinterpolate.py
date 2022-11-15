from quantum.interpolate import interpolateHamiltonian, interpolateHamiltonianEE
from quantum.interpolate import calculatek0,calculatek1,calculateVLoc
from quantum.qobj import Qobj
from quantum.utils import kvec, timerPrint


qobj = Qobj()



"""Function to be run when k0 is wished to be determined.  This function calculates
k0 with a standard approach, that is, without the use of the Quantum Object Class"""
def testCalculateK0():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculatek0(OB_bi, potential)
    print("------------K0-------------")
    return result
#print(testCalculateK0())    




"""Function to be run when k0 is wished to be determied.  This function calculates
k0 with respect to the implementation of the Quantum Object Class"""
def testQuantumCalculatek0():
    result = qobj.getk0()
    print("-------------k0-----------")
    return result
#print(testQuantumCalculatek0())





"""Function to be run when k1 is wished to be determined"""
def testCalculateK1():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculatek1(OB_bi, potential)
    print("------------K1-------------")
    return result
#print(testCalculateK1())




"""Function to be run when the Local Potential of the particle, denoted VLoc,
is wished to be determined"""
def testCalculateVLoc():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculateVLoc(OB_bi, potential)
    print("------------VLoc-----------")
    return result 
#print(testCalculateVLoc())




"""Function to be run when the Eigenvalues are wished to be dtermined from 
solving the 1P Schrodinger Equation with periodic potential (Before Quantum
Object implementation is introduced).  Function also gives resulting time taken 
for such solutions to be determined"""
@timerPrint
def testInterpolateHamiltonian():
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    kList = qobj.getKListNEW()
    eigenEnergies = interpolateHamiltonian(OB_bi, kList,k0, k1, VLoc, N_b)
    print("-----Interpolate Hamiltonian NEWkList--------") 
    return eigenEnergies   
#print(testInterpolateHamiltonian())    





"""Function to be run when Eigenvalues are wished to be obtained when solving
the 1P Schrodinger Equation, with respect to the Optimal Basis approach.  This 
function makes use of the Quantum Object Class implementation to immediatley obtain 
Eigenvalue Array with respect to the default parameters outlined in the Private 
Attributes located in the Quantum Object Class.  Function also prints the time taken 
to obtain such results, which can be compared to standard approach of obtaining solutions, 
to demonstrate effectiveness of Quantum Object Class regarding computational efficiency"""
@timerPrint
def testInterpolateHamiltonian():
    eigenEnergies = qobj.getInterpolateHamiltonian()
    print("-----Interpolate Hamiltonian--------")
    return eigenEnergies  
print(testInterpolateHamiltonian())  





"""Function to be run when complete set of solutions is wished to be obtained
from the relevant solving of the 1P Schrodinger Equation with respect to the 
Optimal Basis implementation, that is, to obtain both Eigenvalues and Eigenvectors.  
Function also prints the time taken to calculate, obtaining input parameters
by utilizing the Quantum Object Class.  Computation time can be compared to 
obtaining such solutions directly from the Quantum Object Class"""
@timerPrint
def testInterpolateHamiltonianEE():
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = qobj.getKListNEW()
    ek1, ck1 = interpolateHamiltonianEE(OB_bi, kList,k0, k1, VLoc, N_b)
    return ek1, ck1 
#print(testInterpolateHamiltonianEE())




"""Function to be run when complete set of solutions of the 1P Schrodinger Equation 
is wished to be obtained with respect to the Optimal Basis implementation, that is,
to obtain both EigenValues and Eigenvectors, by directly utilizing the Quantum Object
Class implementation.  Relevant function also outputs computation time to obtain
such solutions, where such a time can be compared to the above approach of 
obtaining solutions to demonstrate computational efficiency of Quantum Object Class"""
@timerPrint
def testT():
    ek, ck = qobj.getInterpolateHamiltonianEE()
    print("----interpolatedEE Quantum Object Implementation---")
    return ek, ck
print(testT())




