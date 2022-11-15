"""File given in model to fill the matrix with the hamiltonian which can then be
diagonalised to obtain the eigenvalues and corresponding eigenvectors.  This is
done with respect to the Standard Basis implementation"""


import numpy as np
from quantum.utils import kinetic



"""Function that builds the relevant Matrix and fills it with the Hamiltonian
with respect to the standard Basis implementation that is set to be diagonalized"""
def fillmatrix(ik, N_G, N_k, potential): #Matrix we want to fill with Hamiltonian
    a = potential.parms["lattice"]
    M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_) #Matrix to fill
    for ig1 in range(-N_G, N_G+1):
        for ig2 in range(-N_G, N_G+1):
            if (ig1 == ig2):
                M[ig1+N_G, ig2+N_G] = kinetic(ik, ig1, a, N_k)
                #kinetic - Diagonal
            else:
                M[ig1+N_G, ig2+N_G] = potential.ft(ig2-ig1)
                #potential - Outside
    return M
#No potential component for KE






