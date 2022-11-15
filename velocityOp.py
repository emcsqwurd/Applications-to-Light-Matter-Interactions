import numpy as np
from quantum.utils import Gvec, kvec




"""Function that obtains the velocity of the particle with respect to
the Standard Basis implementation"""
def standardVelocity(potential, ck):
    [N_G, N_k, N_b] = np.shape(ck)
    a = potential.parms["lattice"]
    velocity = np.zeros((N_k, N_b, N_b), dtype = np.complex_)
    for k in range(N_k):
        for ib1 in range(N_b):
            for ib2 in range(N_b):
                if (ib1 == ib2):
                    velocity[k, ib1 , ib2] = kvec(k, a, N_k)
                for m in range(N_G):
                    velocity[k, ib1, ib2] += np.conjugate(ck[m, k, ib1])*ck[m, k, ib2]*Gvec(m- int((N_G-1)/2), a)   
    return velocity



"""Function that obtains the velocity of the particle with respect to
the Optimal Basis implementation"""
def interpolatedVelocity(potential, OBck, k1):
    [N_k, N_b, Nbasis] = np.shape(OBck)
    a = potential.parms["lattice"]
    velocity = np.zeros((N_k, N_b, N_b), dtype = np.complex_)
    for k in range(N_k):
        for ib1 in range(N_b):
            for ib2 in range(N_b):
                if (ib1 == ib2):
                    velocity[k, ib1, ib2] = kvec(k, a, N_k)
                for m in range(Nbasis):
                    for n in range(Nbasis):
                        velocity[k, ib1, ib2] += 0.5*np.conjugate(OBck[k, ib1, m])*OBck[k, ib2, n]*k1[m, n] 
    return velocity



