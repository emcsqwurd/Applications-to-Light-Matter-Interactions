from quantum.qobj import Qobj
from quantum.table import differenceInEigenvalues, differenceInVelocity
from quantum.table import differenceInDielectricPlotImaginary, differenceInDielectricPlotReal



qobj = Qobj()



"""Function to be run to obtain maximum difference in Eigenvalues with respect to both
approaches of obtaining such solutions, that is, difference in Eigenvalues obtained
from solveSchrodinger() and interpolateHamiltonian() respectively"""
def testTableEigenvalues():
    sb = qobj.getSb()
    N_G = qobj.getN_G()
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    N = N_b
    result = differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N)
    print("--Max difference in eigenvalues between respective methods---")
    return result
#print(testTableEigenvalues())    




"""Function to obtain difference in Velocity operator determined with respect to the
Standard Basis implementation and the Optimal Basis implementation"""
def testDifferenceVelocity():
    ck = qobj.getCk()
    potential = qobj.getPotential()
    OBck = qobj.getOBck()
    k1 = qobj.getk1()
    result = differenceInVelocity(ck, potential, OBck, k1)
    return result
#print(testDifferenceVelocity()) 





def testDifferenceInDielectricPlotImaginary():
    N_b = qobj.getN_B()
    ek = qobj.getEk()
    OBek = qobj.getOBek()
    damp = qobj.getDamp()
    energyRange = qobj.getEnergyRangeFunc()
    stanV = qobj.getStandardVelocityOperator()
    opV = qobj.getInterpolatedVelocityOperator()
    numO = qobj.getNumberOccupied()
    res = differenceInDielectricPlotImaginary(N_b, ek, OBek, damp, energyRange, stanV, opV, numO)
    return res
print(testDifferenceInDielectricPlotImaginary())





def testDifferenceInDielectricPlotReal():
    N_b = qobj.getN_B()
    ek = qobj.getEk()
    OBek = qobj.getOBek()
    damp = qobj.getDamp()
    energyRange = qobj.getEnergyRangeFunc()
    stanV = qobj.getStandardVelocityOperator()
    opV = qobj.getInterpolatedVelocityOperator()
    numO = qobj.getNumberOccupied()
    res = differenceInDielectricPlotReal(N_b, ek, OBek, damp, energyRange, stanV, opV, numO)
    return res
#print(testDifferenceInDielectricPlotReal())







