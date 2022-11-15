import numpy as np
from quantum.dielectric import dielectricFunc
import matplotlib.pyplot as plt



#COMPLEX DIELECTRIC FUNCTION


"""Function to obtain the relevant plot of the Imaginary part of the Dielectric Function
vs Energy"""
def dielectricPlotImaginary(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.imag)    
    plt.xlabel("Energy")
    plt.ylabel("Imaginary part of Dielectric Function")
    plt.plot(energyRange, wlist, 'b')
    plt.show()    
    return 



"""Function to obtain the relevant array for the resulting plot of the Imaginary part
of the Dielectric Function vs Energy"""
def dielectricPlotImaginaryArray(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.imag)   
    resultImaginary = np.asarray(wlist)
    return resultImaginary







#REAL DIELECTRIC FUNCTION


"""Function to obtain the relevant plot of the Real part of the Dielectric Function
vs Energy"""
def dielectricPlotReal(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.real)  
    plt.xlabel("Energy")
    plt.ylabel("Real part of Dielectric Function")
    plt.plot(energyRange, wlist, 'r')
    plt.show()    
    return 



"""Function to obtain the relevant array for the plot of the Real part of the 
Dielectric Function vs Energy"""
def dielectricPlotRealArray(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.real)  
    resultReal = np.asarray(wlist)
    return resultReal

