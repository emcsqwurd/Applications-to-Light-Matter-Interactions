import unittest

from numpy import shape
from quantum.interpolate import interpolateHamiltonian
from quantum.plot import bandStructure
from quantum.potential import generateSechPotential
from quantum.qobj import Qobj
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis


""" Testing Qobj Class"""



class QobjTester(unittest.TestCase):
    qobj = Qobj()
    
    def test_00_get_defaultPtParms(self):
        print("Start get_defaultPtParms test \n")
        self.assertEqual({ "lattice" : 1, "depth" : 10, "width" :0.1 }, self.qobj.get__defaultPtParms())

    def test_01_get_ptParms(self):
        print("Start get_ptParms test \n")
        self.assertEqual(self.qobj.get__defaultPtParms(), self.qobj.getPtParms()) #checks ptParms equal to default value

    def test_02_set_ptParms(self):
        print("Start set_ptParms test \n")
        newPtParms = { "lattice" : 3, "depth" : 2, "width" :2 }
        self.qobj.setParms(ptParms=newPtParms)
        self.assertEqual(newPtParms, self.qobj.getPtParms()) # check ptParms is equal to newPtParms
    
    def test_03_get_potential(self):
        print("Start set_potential test \n")
        ptParms = self.qobj.getPtParms()
        expected = generateSechPotential(ptParms)
        result = self.qobj.getPotential()
        self.assertEqual(expected.name, result.name)
        self.assertEqual(expected.parms, result.parms)

    def test_04_getN_G(self):
        print("Start getN_G test  \n")
        self.assertEqual(10, self.qobj.getN_G())
    
    def test_05_getN_K(self):
        print("Start getN_K test \n")
        self.assertEqual(25, self.qobj.getN_K())

    def test_06_getN_B(self):
        print("Start getN_B test \n")
        self.assertEqual(5, self.qobj.getN_B())

    def test_07_setN_G(self):
        print("Start setN_G test \n")
        newN_G = self.qobj.getN_G() + 1
        self.qobj.setParms(N_G=newN_G)
        self.assertEqual(newN_G, self.qobj.getN_G())

    def test_08_setN_K(self):
        print("Start setN_K test \n")
        newN_K = self.qobj.getN_K() + 1
        self.qobj.setParms(N_K=newN_K)
        self.assertEqual(newN_K, self.qobj.getN_K())

    def test_09_setN_B(self):
        print("Start setN_B test \n")
        newN_B = self.qobj.getN_B() + 1
        self.qobj.setParms(N_B=newN_B)
        self.assertEqual(newN_B, self.qobj.getN_B())

    def test_10_getCk(self):
        print("Start getCk test \n")
        ck = self.qobj.getCk()
        ek, expected = schrodinger.solveSchrodinger(
            N_G=self.qobj.getN_G(),
            N_k=self.qobj.getN_K(),
            N_b=self.qobj.getN_B(),
            potential=self.qobj.getPotential()
        )
        del ek
        self.assertEqual(ck.all(), expected.all())

    def test_11_getSb(self):
        print("Start getSb test \n")
        sb = self.qobj.getSb()
        expected = self.qobj.get__defaultSb()
        self.assertEqual(sb, expected)

    def test_11_setSb(self):
        print("Start setSb test \n")
        newSb = 0.01
        self.qobj.setParms(sb=newSb)
        self.assertEqual(newSb, self.qobj.getSb())

    def test_12_restoreDefaults(self):
        print("Start restoreDefaults test \n")
        self.qobj.restoreDefaults()
        self.assertEqual(self.qobj.getPtParms(), self.qobj.get__defaultPtParms())
        self.assertEqual(self.qobj.getN_G(), self.qobj.get__defaultN_G())
        self.assertEqual(self.qobj.getN_K(), self.qobj.get__defaultN_K())
        self.assertEqual(self.qobj.getN_B(), self.qobj.get__defaultN_B())
        self.assertEqual(self.qobj.getSb(), self.qobj.get__defaultSb()) 

    def test_13_solveSchrodinger(self):
        print("Start solveSchrodinger test \n")
        ek, ck =  self.qobj.solveSchrodinger()
        ekExp, ckExp = schrodinger.solveSchrodinger(
            N_G=self.qobj.getN_G(),
            N_k=self.qobj.getN_K(),
            N_b=self.qobj.getN_B(),
            potential=self.qobj.getPotential()
        )
        self.assertEqual(ek.all(), ekExp.all())
        self.assertEqual(ck.all(), ckExp.all())

    def test_14_optimalBasis(self):
        print("Start optimalBasis test \n")
        ob = self.qobj.optimalBasis()
        obExp = optimalbasis.optimalBasis(
            sb=self.qobj.getSb(),
            N_b=self.qobj.getN_B(),
            N_k=self.qobj.getN_K(),
            ck=self.qobj.getCk()
        )
        self.assertEqual(ob.all(), obExp.all())

    def test_15_getPtType(self):
        print("Start getPtType test \n")
        expected = self.qobj.get__defaultPtType()
        result = self.qobj.getPtType()
        self.assertEqual(expected, result)


    def test_15_setPtType(self):
        print("Start setPtType test \n")
        expected = "sech"
        self.qobj.setParms(ptType=expected)
        result = self.qobj.getPtType()
        self.assertEqual(expected, result)
    
    def test_16_getLatticeConstant(self):
        print("Start getLatticeConstant test \n")
        expected = 1
        res = self.qobj.getLatticeConstant()
        self.assertEqual(expected, res)

    def test_17_getPotentialDepth(self):
        print("Start getPotentialDepth test \n")
        expected = 10
        res = self.qobj.getPotentialDepth()
        self.assertEqual(expected, res)

    def test_18_getPotentialWidth(self):
        print("Start getPotentialWidth test \n")
        expected = 0.1
        res = self.qobj.getPotentialWidth()
        self.assertEqual(expected, res)
    
    """"ensures methods returs correct array"""
    def test_19_schrodingerBandStructure(self):
        print("Start schrodingerBandStructure test \n")
        qobj1 = Qobj()
        res = qobj1.schrodingerBandStructure()
        ek = qobj1.getEk(),
        exp = bandStructure(ek[0], qobj1.getPotential())
        self.assertEqual(res.all(), exp.all())

    def test_20_interpolatedBandStructure(self):
        print("Start interpolatedBandStructure test \n")
        qobj1 = Qobj()
        res = qobj1.interpolatedBandStructure()
        ih = interpolateHamiltonian(
            OB_bi=qobj1.getOptimalBasis(),
            kList=qobj1.getKList(),
            k0=qobj1.getk0(),
            k1=qobj1.getk1(),
            VLoc=qobj1.getVLoc(),
            N=qobj1.getN_B()
        )
        exp = bandStructure(ih, potential=qobj1.getPotential())
        self.assertEqual(res.all(), exp.all())
        


    
    