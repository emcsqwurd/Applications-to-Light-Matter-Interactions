from math import pi
import numpy as np
from time import time



"""Function representing the reciprocal lattice vector"""
def Gvec(m, a):
        return 2*pi*m/a
   


"""Function that allows for formualation of the interpolation k-grid"""   
def kgrid(a,N,Nk):
    k = np.zeros(N)
    for ik in range(N):
        k[ik]=kvec(ik,a,Nk)
    return k



"""Function defining the relevant wave vector k"""
def kvec(i,a,N):
        return -pi/a + i*2*pi/a/(N-1)




"""Function defining the relevant kinetic energy of the particle in reciprocal space"""
def kinetic(i,m,a,N):
        return 0.5*(kvec(i,a,N) - Gvec(m,a))**2 





"""Function that defines the releant k-list to be interpolated over"""
def kList(N_k, potential):
        a = potential.parms["lattice"]
        kList = []
        for i in range(N_k):
            kList.append(kvec(i,a,N_k))
        return kList



"""Updated function, same as above, required to be independent"""
def kListNEW(N_kPrime, potential):
    a = potential.parms["lattice"]
    kList = []
    for i in range(N_kPrime):
        kList.append(kvec(i,a,N_kPrime))
    return kList




"""Function that obtains the periodic part of the Bloch Wavefunctions as a linear 
combination of planewaves up to some cutoff """
def OB_bix(OB_bi, a, potential, Ncell, Npoints):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    x, U = potential.v(Ncell, Npoints)
    del U
    OB_bix = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for m in range(0, Ng):
            OB_bix[i, m] = OB_bi[:,i]*np.exp(1j * Gvec(m- int((Ng-1)/2), a)*x)
    return OB_bix




""""""
def phi(N_b, OB_bi, a, potential, Ncell, Npoints):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    OB_biXDep = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    Unk = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    OB_biXDep = OB_bix(OB_bi, a, potential, Ncell, Npoints)
    for i in range(N_b):
        Unk = Unk + OB_bi[:, i] * OB_biXDep[:, i]
    return Unk


"""Function that prints formatted string showing execution time of 
the function object that is passed through"""
def timerPrint(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.10f}s') # displays execution time to 10 d.p
        return result
    return wrap_func


"""Function that returns float - the execution time of the function object
that is passed through"""
def timerFloat(func):
    def wrap_func(*args, **kwargs)->float:
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        return (t2-t1)
    return wrap_func



"""Function to obtain the energy range being considered for the relevant implementation
of the dielectric plot being investigated"""
def energyRangeFunc(bottomEnergy, energyOfTopBand, numSample):
    result = np.linspace(bottomEnergy, energyOfTopBand, numSample)
    return result




    

