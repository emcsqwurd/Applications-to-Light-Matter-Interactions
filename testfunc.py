from quantum.plot import plotFun
from quantum.potential import PotentialFactory
from quantum.schrodinger import solveSchrodinger
from quantum.interpolate import interpolateHamiltonianEE
from quantum import potential as pt
from quantum.qobj import Qobj


qobj = Qobj()




"""Function to run when testing the plot of the wave functions with respect
to the Standard Basis implementation"""
def testPlotFunOB():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    kList = qobj.getKList()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    N_b = qobj.getN_B()
    N = N_b
    [ek, ck] = interpolateHamiltonianEE(OB_bi, kList, k0, k1, VLoc, N)
    plot = plotFun(10, ek, ck, 3, 10, potential, 'b', 2 )
    return plot
print(testPlotFunOB())    





