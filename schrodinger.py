import numpy as np 
from quantum.matrix import fillmatrix




"""Function that perfoms the relevant diagonalization of the Hamiltonian to obtain
the desired solutions to the Schrodinger Equation.  This function outputs the 
relevant Eigenvalue array and the relevant Eigenvector array.  This is all done 
in regards to the Standard Basis implementation."""
def solveSchrodinger(N_G,N_k,N_b,potential):
    #iterates k-point by k-point
    #e and c are NOT dependent on ik, however, we alter to make e,c k-dependent
    ek = np.zeros((N_k,N_b)) #energy band
    ck = np.zeros((2*N_G+1,N_k,N_b),dtype=np.complex_)#eigenstate, is a vector with dimension
    for ik in range(N_k):
        M=fillmatrix(ik,N_G,N_k,potential)
        [e,c]=np.linalg.eigh(M)
        ek[ik,0:N_b] = e[0:N_b]
        ck[:,ik,0:N_b] = c[:,0:N_b]
    return ek,ck





