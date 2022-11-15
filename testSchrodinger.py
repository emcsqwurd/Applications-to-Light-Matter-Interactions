from quantum.qobj import Qobj
from quantum.utils import timerPrint




qobj = Qobj()




"""Function to be run when Eigenvalues and Eigenvectors are wished to be obtained from
solving the 1P Schrodinger Equation with respect to the Standard Basis implementation,
that is, the solutions obtained with respsect to the solveSchrodinger() function.
Function also outputs computation time for obtaining such solutions"""
@timerPrint
def testSS():
    ek, ck = qobj.solveSchrodinger()
    print("---solveSchrodinger() solutions---")
    return ek, ck
print(testSS())




"""Function to be run when Eigenvalues and Eignvectors are wished to be obtained from
solving the 1P Schrodinger Equation with respect to the Optimal Basis implementation,
that is, the solutions obtained with respect to the interpolateHamiltonian() function.
Function also outputs computation time for obtaining such solutions, can be directly
compared to function above to demonstrate increase in Computational Efficiency"""
@timerPrint
def testIHEE():
    ekOB, ckOB = qobj.getInterpolateHamiltonianEE()
    print("---interpolateHamiltonian() solutions---")
    return ekOB, ckOB
print(testIHEE())    











