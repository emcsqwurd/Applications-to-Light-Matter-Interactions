import numpy as np
from math import pi



"""Class introduced defining  """
class Potential:
    def __init__(self, name, parms, v, ft):
        self.name = name
        self.parms = parms
        self.v = v
        self.ft = ft
    def __str__(self):
        return self.name


class PotentialFactory:
    def __init__(self):
        self.potentialList = {}
    def addType(self, name, v, ft):
        potential = {
            "V" : v,
            "FourierTransform" : ft
            }
        self.potentialList[name] = potential
    def createPotential(self, name, parms):
        return Potential(
            name,
            parms,
            self.potentialList[name]["V"](parms),
            self.potentialList[name]["FourierTransform"](parms)
            )




""" ----------------------  GENERATORS  ------------------------------ """




### SECH
def sechpotGenerator(parms):
        a = parms["lattice"]
        a0 = parms["width"]
        v0 = parms["depth"] 
        def pot(N, m):
                x = np.linspace(-N*a,N*a,N*m) 
                U = np.zeros(len(x))
                for n in range(-N,N+1):
                        U = U - 1/np.cosh((x-n*a)/a0)
                return x,v0*U
        return pot 
        

### sech fourtier transform
def sechFTGenerator(parms):
        a = parms["lattice"]
        a0 = parms["width"]
        v0 = parms["depth"] 
        def ft(m):
                Ug=-1/np.cosh(pi**2*a0*m/a)
                return Ug*v0*pi*a0/a
        return ft #returns Fourier Transform




def generateSechPotential(parms):
    pf = PotentialFactory()
    pf.addType("sech", sechpotGenerator, sechFTGenerator)
    ptl = pf.createPotential("sech", parms )
    return ptl


## saw wave
def sawpotGenerator(parms):
        a = parms["lattice"]
        v0 = parms["depth"]
        def pot(N, m):
                x = np.linspace(-N*a,N*a,2*N*m) 
                U = np.zeros(len(x))
                #define grid
                for n in range(-N,N+1):
                    l=(N+n)*m
                    u= l+m-1
                    U[l:u] = x[l:u]/a - n  
                return x,-v0*U
        return pot 

## saw wave fourier transform
def sawFTGenerator(parms):
        a = parms["lattice"]
        v0 = parms["depth"]
        def ft(m):
            if m==0:
                Ug = pi*a/2
            else:
                Ug = -2j/m    
            return -Ug*v0/pi/a
        return ft

## cos
def cospotGenerator(parms):
        a = parms["lattice"]
        v0 = parms["depth"]
        def pot(N, m):
            x = np.linspace(-N*a,N*a,N*m)
            return x,v0*(np.cos(2*pi*x/a)-1)
        return pot

## cos fourier transform
def cosFTGenerator(parms):
        a = parms["lattice"]
        v0 = parms["depth"]
        def ft(m):
            Ug = 0
            
            if abs(m) == 1:
                Ug = v0/2
            elif m == 0:
                Ug = -v0
            return Ug  
        return ft
    

## well
def wellpotGenerator(parms):
        a = parms["lattice"]
        h = parms["width"]
        v0 = parms["depth"]
        def pot(N, m):
            x = np.linspace(-N*a,N*a,2*N*m)
            U = np.zeros(len(x))
            for n in range(-N,N):
                l=(N+n)*m
                u= l+m-1
                for ix in range(l,u):
                    y = x[ix]-n*a
                    if y>0 and y<= a/h: 
                        U[ix] = v0
            return x,-v0*U
        return pot
    
    
## well fourier transform
def wellFTGenerator(parms):
        a = parms["lattice"]
        h = parms["width"]
        v0 = parms["depth"]
        def ft(m):
            if m==0:
                Ug = -pi*a/h
            else:
                Ug = -1j/m*(1-(np.exp(2j*pi*a/h))**m)  
            return Ug*v0/pi/2
        return ft

