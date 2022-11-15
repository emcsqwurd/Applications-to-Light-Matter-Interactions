from numpy import ndarray
import quantum.potential as pt
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis
import quantum.interpolate as interpolateHamiltonian
import quantum.utils as utils 
import quantum.velocityOp as velocityoperator
import quantum.gettime as getTime
import quantum.table as Table
import quantum.plot as plot
import quantum.dielectric as dielectric
import quantum.dielectricplot as dielectricplot


class Qobj:

    # PRIVATE ATRRIBUTEs

    __defaultPtParms = { "lattice" :1, "depth" : 10, "width" :0.1}   #lattice and potential paramaters
    __defaultN_G = 10   #Number of plane waves in basis (fixed for given precision)
    __defaultN_K = 500   #Number of k-points
    __defaultN_KPrime = 200   #Number of k-points interpolated OB
    __defaultN_B = 6   #Number of Bands to run over
    __defaultSb =0.5   #Threshold Parameter
    __defaultPtType = "sech"   #Potential function
    

    __defaultDamp = 0.1   #relevant damping of such frequency regarding incident beam (relevant for Dielectric Plot)
    __defaultW = 10   #relevant frequency being considered for incident beam (relevant for Dielectric Plot)
    __defaultNumberOccupied = 1   #Fermi Distribution (relevant for Dielectric Plot)
    __defaultBottomEnergy = 0   #EnergyRangeParameter - bottom energy of Band Structure (relevant for Dielectric Plot)
    __defaultEnergyOfTopBand = 175   #EnergyRangeParamater - Energy of Top Band being run over (relevant for Dielectric Plot)
    __defaultNumSample = 200   #EnergyRangeParameter - Number of points to be discretized in sample (relevant for Dielectric Plot)
    


    # CONSTRUCTOR
    def __init__(self):
        self.__parms = {}
        self.setParms(
            ptParms = self.get__defaultPtParms(),
            N_G = self.get__defaultN_G(),
            N_K = self.get__defaultN_K(),
            N_KPrime = self.get__defaultN_KPrime(),
            N_B = self.get__defaultN_B(),
            sb = self.get__defaultSb(),
            ptType = self.get__defaultPtType(),
            Damp = self.get__defaultDamp(),
            W = self.get__defaultW(),
            NumOcc = self.get__defaultNumberOccupied(),
            BottomEnergy = self.get__defaultBottomEnergy(),
            EnergyOfTopBand = self.get__defaultEnergyOfTopBand(),
            NumSample = self.get__defaultNumSample()

        )
    



    # GETTERS
    def get__defaultPtParms(self):
        return self.__defaultPtParms
    def get__defaultN_G(self):
        return self.__defaultN_G
    def get__defaultN_K(self):
        return self.__defaultN_K
    def get__defaultN_KPrime(self):
        return self.__defaultN_KPrime
    def get__defaultN_B(self):
        return self.__defaultN_B
    def get__defaultSb(self):
        return self.__defaultSb
    def get__defaultPtType(self):
        return self.__defaultPtType
    def get__defaultLatticeConstant(self):
        return self.__defaultPtParms["lattice"]
    def get__defaultPotentialDepth(self):
        return self.__defaultPtParms["depth"]
    def get__defaultPotentialWidth(self):
        return self.__defaultPtParms["width"] 
    def get__defaultDamp(self):
        return self.__defaultDamp   
    def get__defaultW(self):
        return self.__defaultW   
    def get__defaultNumberOccupied(self):
        return self.__defaultNumberOccupied    
    def get__defaultBottomEnergy(self):
        return self.__defaultBottomEnergy
    def get__defaultEnergyOfTopBand(self):
        return self.__defaultEnergyOfTopBand
    def get__defaultNumSample(self):
        return self.__defaultNumSample    


    def getPtParms(self):
        return self.__parms["ptParms"]
    def getN_G(self):
        return self.__parms["N_G"]
    def getN_K(self):
        return self.__parms["N_K"]
    def getN_KPrime(self):
        return self.__parms["N_KPrime"]    
    def getN_B(self):
        return self.__parms["N_B"]
    def getSb(self):
        return self.__parms["sb"]
    def getPtType(self):
        return self.__parms["ptType"]
    def getLatticeConstant(self):
        return self.getPtParms()["lattice"]
    def getPotentialDepth(self):
        return self.getPtParms()["depth"] 
    def getPotentialWidth(self):
        return self.getPtParms()["width"] 
    def getDamp(self):
        return self.__parms["Damp"]
    def getW(self):
        return self.__parms["W"]  
    def getNumberOccupied(self):
        return self.__parms["NumOcc"]        
    def getBottomEnergy(self):
        return self.__parms["BottomEnergy"]
    def getEnergyOfTopBand(self):
        return self.__parms["EnergyOfTopBand"]  
    def getNumSample(self):
        return self.__parms["NumSample"]    


    def getPotential(self):
        return self.__potential
    def getEk(self):
        return self.__ek
    def getCk(self):
        return self.__ck
    def getOptimalBasis(self):
        return self.__OB
    def getk0(self):
        return self.__k0   
    def getk1(self):
        return self.__k1
    def getVLoc(self):
        return self.__vLoc         
    def getKList(self):
        return self.__klist
    def getKListNEW(self):
        return self.__klistNEW
    def getInterpolateHamiltonian(self):
        return self.interpolateHamiltonian()    
    def getInterpolateHamiltonianEE(self):
        return self.interpolateHamiltonianEC()
    def getOBek(self):
        return self.__OBek
    def getOBck(self):
        return self.__OBck     
    def getDifferenceInEkTable(self):
        return self.differenceEigenvalues()
    def getEkTimeSolveSchrodinger(self):
        return self.ekTimeSolveSchrodinger()
    def getEkTimeInterpolateHamiltonian(self):
        return self.ekTimeInterpolateHamiltonian() 
    def getDifferenceTimeForEk(self):
        return self.differenceTimeForGettingEk()   
    def getStandardVelocityOperator(self):
        return self.__standardVel
    def getInterpolatedVelocityOperator(self):
        return self.__interpolatedVel
    def getParms(self):
        return self.__parms

    def getStandardDielectric(self):
        return self.standardDielectricFunction() 
    def getOptimalDielectric(self):
        return self.optimalDielectricFunction()
    def getEnergyRangeFunc(self):
        return self.__energyRangeFunc

    def getStandardImaginaryDielectricPlot(self):
        return self.standardImaginaryDielectricPlot()
    def getStandardRealDielectricPlot(self):
        return self.standardRealDielectricPlot()
    def getOptimalImaginaryDielectricPlot(self):
        return self.optimalImaginaryDielectricPlot()
    def getOptimalRealDielectricPlot(self):
        return self.optimalRealDielectricPlot()

    def getStandardImaginaryDielectricPlotArray(self):
        return self.standardImaginaryDielectricPlotArray()
    def getStandardRealDielectricPlotArray(self):
        return self.standardRealDielectricPlotArray()
    def getOptimalImaginaryDielectricPlotArray(self):
        return self.optimalImaginaryDielectricPlotArray()
    def getOptimalRealDielectricPlotArray(self):
        return self.optimalRealDielectricPlotArray()






    # SETTERS
    def __setPtParms(self, ptParms):
        self.__parms["ptParms"] = ptParms 
    def __setN_G(self, N_G):
        self.__parms["N_G"] = N_G
    def __setN_K(self, N_K):
        self.__parms["N_K"] = N_K
    def __setN_KPrime(self, N_KPrime):
        self.__parms["N_KPrime"] = N_KPrime  
    def __setN_B(self, N_B):
        self.__parms["N_B"] = N_B
    def __setSb(self, sb):
        self.__parms["sb"] = sb
    def __setDamp(self, Damp):
        self.__parms["Damp"] = Damp  
    def __setW(self, W):
        self.__parms["W"] = W
    def __setNumOcc(self, NumOcc):
        self.__parms["NumOcc"] = NumOcc
    def __setBottomEnergy(self, BottomEnergy):
        self.__parms["BottomEnergy"] = BottomEnergy
    def __setEnergyOfTopBand(self, EnergyOfTopBand):
        self.__parms["EnergyOfTopBand"] = EnergyOfTopBand  
    def __setNumSample(self, NumSample):
        self.__parms["NumSample"] = NumSample      


    def __setPtType(self, ptType):
        typeList = ["sech"]
        if ptType not in typeList:
            raise TypeError("type not in typeList")
        else:
            self.__parms["ptType"] = ptType
    

    def __setOptimalBasis(self):
        self.__OB = self.optimalBasis()
    def __setKList(self):
        self.__klist = self.kList()
    def __setKListNEW(self):
        self.__klistNEW= self.kListNEW()
    def __setEnergyRangeFunc(self):
        self.__energyRangeFunc = self.energyRangeFunc()    
    def __setPotential(self):
        self.__potential = self.generatePotential(self.getPtType())
    def __setK0(self):
        self.__k0 = self.calculatek0()
    def __setK1(self):
        self.__k1 = self.calculatek1()
    def __setVLoc(self):
        self.__vLoc = self.calculateVLoc()
    def __setEkAndCk(self):
        ek, ck = self.solveSchrodinger()
        self.__ek = ek
        self.__ck = ck
    def __setOBekAndOBck(self):
        OBek, OBck = self.interpolateHamiltonianEC()
        self.__OBek = OBek
        self.__OBck = OBck
    def __setStandardVelocity(self):
        self.__standardVel = self.standardVelocityOperator()
    def __setInterpolatedVelocity(self):
        self.__interpolatedVel = self.interpolatedVelocityOperator()
    def setParms(self, **kwargs):
        for arg in kwargs:
            if arg == "ptParms":
                ptParms = kwargs.get("ptParms")
                self.__setPtParms(ptParms)
            if arg == "N_G":
                N_G = kwargs.get("N_G")
                self.__setN_G(N_G)
            if arg == "N_K":    
                N_K = kwargs.get("N_K")
                self.__setN_K(N_K)
            if arg == "N_KPrime":
                N_KPrime = kwargs.get("N_KPrime")
                self.__setN_KPrime(N_KPrime) 
            if arg == "N_B":
                N_B = kwargs.get("N_B")
                self.__setN_B(N_B)
            if arg == "sb":
                sb = kwargs.get("sb")
                self.__setSb(sb)
            if arg == "Damp":
                Damp = kwargs.get("Damp")
                self.__setDamp(Damp) 
            if arg == "W":
                W = kwargs.get("W")
                self.__setW(W)   
            if arg == "NumOcc":
                NumOcc = kwargs.get("NumOcc")
                self.__setNumOcc(NumOcc)  
            if arg == "BottomEnergy":
                BottomEnergy = kwargs.get("BottomEnergy")
                self.__setBottomEnergy(BottomEnergy)      
            if arg == "EnergyOfTopBand":
                EnergyOfTopBand = kwargs.get("EnergyOfTopBand")
                self.__setEnergyOfTopBand(EnergyOfTopBand)
            if arg == "NumSample":
                NumSample = kwargs.get("NumSample")
                self.__setNumSample(NumSample)    
            if arg == "ptType":
                ptType = kwargs.get("ptType")
                self.__setPtType(ptType)    


        self.__setPotential()
        self.__setEkAndCk()
        self.__setOptimalBasis()
        self.__setKList()
        self.__setKListNEW()
        self.__setK0()
        self.__setK1()
        self.__setVLoc()
        self.__setOBekAndOBck()
        self.__setStandardVelocity()
        self.__setInterpolatedVelocity()
        self.__setEnergyRangeFunc()
        
        







    # METHODS


    def restoreDefaults(self):
        self.__init__()

    def generatePotential(self, type):
        typeList = ["sech"]
        if type not in typeList:
            raise TypeError("type not in typeList")
        elif type == "sech":
            return pt.generateSechPotential(self.getPtParms())

    def solveSchrodinger(self):
        ss =  schrodinger.solveSchrodinger(
            N_G=self.getN_G(),
            N_k=self.getN_K(),
            N_b=self.getN_B(),
            potential=self.getPotential()
            )
        return ss   

    def optimalBasis(self):
        ob = optimalbasis.optimalBasis(
            sb=self.getSb(),
            N_b=self.getN_B(),
            N_k=self.getN_K(),
            ck=self.getCk()
        )
        return ob

    def calculatek0(self):
        k0 = interpolateHamiltonian.calculatek0(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return k0    

    def calculatek1(self):
        k1 = interpolateHamiltonian.calculatek1(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return k1  

    def calculateVLoc(self):
        VLoc = interpolateHamiltonian.calculateVLoc(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return VLoc    

    def kList(self):
        klist = utils.kList(
            N_k = self.getN_K(),
            potential = self.getPotential()
        )
        return klist

    def kListNEW(self):
        klistNEW = utils.kListNEW(
            N_kPrime = self.getN_KPrime(),
            potential = self.getPotential()
        )
        return klistNEW   

    def energyRangeFunc(self):
        energyRange = utils.energyRangeFunc(
            bottomEnergy = self.getBottomEnergy(),
            energyOfTopBand = self.getEnergyOfTopBand(),
            numSample = self.getNumSample()
        )  
        return energyRange

    def interpolateHamiltonian(self):
        interHamil = interpolateHamiltonian.interpolateHamiltonian(
            OB_bi = self.getOptimalBasis(),
            kList = self.getKListNEW(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return interHamil   

    def interpolateHamiltonianEC(self):
        interHamilE, interHamilC = interpolateHamiltonian.interpolateHamiltonianEE(
            OB_bi = self.getOptimalBasis(),
            kList = self.getKListNEW(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return interHamilE, interHamilC

    def differenceEigenvalues(self):
        differenceEk = Table.differenceInEigenvalues(
            sb  = self.getSb(),
            N_G = self.getN_G(),
            N_k = self.getN_K(),
            N_b = self.getN_B(),
            potential = self.getPotential(),
            N = self.getN_B()
        )
        return differenceEk

    def ekTimeSolveSchrodinger(self):
        ekTimeSS = getTime.standardTimeForEk(
            N_G= self.getN_G(),
            N_k= self.getN_K(),
            N_b= self.getN_B(),
            potential= self.getPotential()
        )
        return ekTimeSS

    def ekTimeInterpolateHamiltonian(self):
        ekTimeIH = getTime.optimisedTimeForEk(
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return ekTimeIH    

    def differenceTimeForGettingEk(self):
        differenceTime = getTime.differenceInTimeForObtainingEk(
            N_G= self.getN_G(),
            N_k= self.getN_K(),
            N_b= self.getN_B(),
            potential= self.getPotential(),
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return differenceTime

    def standardVelocityOperator(self):   #CHECK
        standardVel = velocityoperator.standardVelocity(
            potential = self.getPotential(),
            ck = self.getCk()
        )
        return standardVel

    def interpolatedVelocityOperator(self):   #CHECK
        interpolatedVel = velocityoperator.interpolatedVelocity(
            potential = self.getPotential(),
            OBck = self.getOBck(),
            k1 = self.getk1()
        )
        return interpolatedVel

    """Function that returns array of bands structure with ek calculated from 
    solveSchrodinger()"""
    def schrodingerBandStructure(self)->ndarray:
        bands = plot.bandStructure(
            ek=self.getEk(),
            potential=self.getPotential()
        )
        return bands

    """"Function thatreturns array of bands structure with ek calculated from
    interpolatehamiltonian()"""
    def interpolatedBandStructure(self)->ndarray:
        bands = plot.bandStructure(
            ek=self.getInterpolateHamiltonian(),
            potential=self.getPotential()
        )
        return bands


    def standardDielectricFunction(self):
        dielectricFun = dielectric.dielectricFunc(
            N_b = self.getN_B(),
            ek = self.getEk(),
            damp = self.getDamp(),
            w = self.getW(),
            velocity = self.getStandardVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )    
        return dielectricFun


    def optimalDielectricFunction(self):
        dielectricFun = dielectric.dielectricFunc(
            N_b = self.getN_B(),
            ek = self.getOBek(),
            damp = self.getDamp(),
            w = self.getW(),
            velocity = self.getInterpolatedVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )    
        return dielectricFun


    def standardImaginaryDielectricPlot(self):
        dielectricP = dielectricplot.dielectricPlotImaginary(
            N_b = self.getN_B(),
            ek = self.getEk(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getStandardVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP


    def optimalImaginaryDielectricPlot(self):
        dielectricP = dielectricplot.dielectricPlotImaginary(
            N_b = self.getN_B(),
            ek = self.getOBek(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getInterpolatedVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP


    def standardRealDielectricPlot(self):
        dielectricP = dielectricplot.dielectricPlotReal(
            N_b = self.getN_B(),
            ek = self.getEk(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getStandardVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP


    def optimalRealDielectricPlot(self):
        dielectricP = dielectricplot.dielectricPlotReal(
            N_b = self.getN_B(),
            ek = self.getOBek(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getInterpolatedVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP



    def standardImaginaryDielectricPlotArray(self):
        dielectricP = dielectricplot.dielectricPlotImaginaryArray(
            N_b = self.getN_B(),
            ek = self.getEk(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getStandardVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP


    def optimalImaginaryDielectricPlotArray(self):
        dielectricP = dielectricplot.dielectricPlotImaginaryArray(
            N_b = self.getN_B(),
            ek = self.getOBek(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getInterpolatedVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP    


    def standardRealDielectricPlotArray(self):
        dielectricP = dielectricplot.dielectricPlotRealArray(
            N_b = self.getN_B(),
            ek = self.getEk(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getStandardVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP   


    def optimalRealDielectricPlotArray(self):
        dielectricP = dielectricplot.dielectricPlotRealArray(
            N_b = self.getN_B(),
            ek = self.getOBek(),
            damp = self.getDamp(),
            energyRange = self.getEnergyRangeFunc(),
            velocity = self.getInterpolatedVelocityOperator(),
            numberOccupied = self.getNumberOccupied()
        )
        return dielectricP     

















