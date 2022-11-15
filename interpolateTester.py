import unittest
import quantum.interpolate 
import quantum.qobj 

class InterpolateTester(unittest.TestCase):

    def test_00_calculateVLoc(self):
        print("--------------------------------------")
        print("Start calculateVLoc test \n")
        qobj = quantum.qobj.Qobj()
        result = quantum.interpolate.calculateVLoc(
            OB_bi=qobj.getOptimalBasis(),
            potential=qobj.getPotential(),
        )
        print(result) 


    def test_01_calculateK0(self):
        print("Start calculateK0 test \n")
        qobj = quantum.qobj.Qobj()
        res = quantum.interpolate.calculatek0(
            OB_bi=qobj.getOptimalBasis(),
            a = qobj.getPotential().parms["lattice"],
        )
        print(res)

    def test_02_calculateK1(self):
        print("Start calculateK1 test \n")
        qobj = quantum.qobj.Qobj()
        res = quantum.interpolate.calculatek1(
            OB_bi=qobj.getOptimalBasis(),
            a = qobj.getPotential().parms["lattice"],
        )
        print(res) 


    def test_02_interpolateHamiltonian(self):
        print("Start interpolateHamiltonian test \n")
        qobj = quantum.qobj.Qobj()
        result = quantum.interpolate.interpolateHamiltonian(
            OB_bi=qobj.getOptimalBasis(),
            N_G=qobj.getN_G(),
            m=10,
            N_GPrime=23,
            N_GPrimePrime=79,
            Ncell=3,
            Npoints=10,
            potential=qobj.getPotential(),
        )
        print(result)






