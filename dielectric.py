import numpy as np


"""Function to obtain the Dielectric Function of relevant material"""
def dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied):
    N_k = velocity.shape[0]
    constant = 4/np.pi
    z = w + (1j*damp)
    sum = 0
    for k in range(N_k):
        for n in range(numberOccupied):
            for nprime in range(numberOccupied +1, N_b):
                frac1 = velocity[k, n, nprime]*np.conjugate(velocity[k, n, nprime])/(ek[k, nprime] - ek[k, n])**2
                frac2 =  1 / (z - (ek[k, nprime] - ek[k, n]))
                sum += frac1*frac2
    return 1 - constant*sum




