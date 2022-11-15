import numpy as np 
from math import pi
from quantum import potential as pt 
import matplotlib.pyplot as plt

#TEST1 - sech potential

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.1 }
ptl = pf.createPotential("sech", ptparms)
x, U = ptl.v(2, 2000)
plt.plot(x,U)
plt.xlabel("Length of Lattice")
plt.ylabel("Potential Depth")



Ur=np.zeros(len(x))
a = ptl.parms["lattice"]
for m in range(-5,5): 
    Ur = Ur + ptl.ft(m) * np.exp(-1j*2*pi*m/a*x)

#plt.plot(x,Ur,'r-')
#plt.xlabel("Brillouin Zone") #FIX
#plt.ylabel("***********************************FIX**************************")
#plt.show()





pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.2 }
ptl = pf.createPotential("sech", ptparms)
x, U = ptl.v(2, 2000)
plt.plot(x, U, 'g')
plt.show()


""" plt.plot(x,U)
Ur=np.zeros(len(x))
a = ptl.parms["lattice"]
for m in range(-5,5): 
    Ur = Ur + ptl.ft(m) * np.exp(-1j*2*pi*m/a*x)
plt.plot(x,Ur,'y-') #Ur=orange, x=blue
plt.show()
 """





#reduction of basis
