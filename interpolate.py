import numpy as np
from quantum.utils import Gvec

#eq 16, obtain ek, compare with solveschrodinger
#should be summing over m
#want NbasisxNbasis array
#OB_bi -> (2N_G+1, NBasis)
#k0 -> (Nbasis, Nbasis)
#Nbasis = OB_bi.shape[1]
#Ng = OB_bi.shape[0]
#k0 = np.zero((Nbasis, Nbasis))
#i contain [0, Nbasis)
#j contain [0, Nbasis)
#m contain [0, Ng)
#k0[i,j] += np.conj(OB_bi[m,i])*OB_bi[m,j]*Gvec(m-Ng, a)
#m -> 0,....,2N_G +1 where this is = -N_G -> N_G



"""Function to obtain relevant element representing the kinetic energy
component of the Hamiltonian with respect to the optimal basis implementation"""
def calculatek0(OB_bi, potential):
    a = potential.parms["lattice"]
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k0 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k0[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m-int((Ng-1)/2),a)**2
    return k0




"""Function to obtain relevant element representing the additional kinetic energy
component of the Hamiltonian with respect to the optimal Basis implementation"""
def calculatek1(OB_bi, potential):
    a = potential.parms["lattice"]
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k1[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)  
    return 2*k1  
   



"""Function to obtain relevant element representing the Potential energy
component of the Hamiltonian with respect to the optimal Basis implementation"""
def calculateVLoc(OB_bi, potential):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    vloc = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0, Ng):
                for n in range(0, Ng):
                    vloc[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[n, j]*potential.ft(m-n)
    return vloc




"""Function that builds the relevant Hamiltonian with respect to the optimal
Basis implementation, interpolating over all k-points.  Additionally, the function
also diagonalizes the relevant Hamiltonian when built.  This function only obtains
the relevant Eigenvalues when solved.  Function introduced to achieve more
computationally efficient results"""
def interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N):
    Nbasis = OB_bi.shape[1]
    E = np.zeros((len(kList), N))
    ik = 0
    for k in(kList):
        Hk = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
        for i in range(Nbasis):
            for j in range(Nbasis):
                Hk[i,j] = 0.5*k0[i,j] + VLoc[i,j]
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
        ek2 = np.linalg.eigvalsh(Hk)    
        E[ik,0:N] = ek2[0:N]
        ik +=1
    return E 




"""Additional function that builds and diagonalizes the relevant Hamiltonian 
when built, interpolating over all k-points.  However, this function obtains 
both the Eigenvalues and Eigenvectors when diagonalized, demonstrating 
the required set of solutions when solving the Schrodinger Equation"""
def interpolateHamiltonianEE(OB_bi, kList, k0, k1, VLoc, N):
    Nbasis = OB_bi.shape[1]
    E = np.zeros((len(kList), N))
    C = np.zeros((len(kList), N, Nbasis), dtype = np.complex_)
    ik = 0
    for k in(kList):
        Hk = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
        for i in range(Nbasis):
            for j in range(Nbasis):
                Hk[i,j] = 0.5*k0[i,j] + VLoc[i,j]
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
        ek2, ck2 = np.linalg.eigh(Hk)    
        E[ik,0:N] = ek2[0:N]
        C[ik, 0:N, 0:Nbasis] = ck2[0:N, 0:Nbasis]
        ik +=1
    return E, C




