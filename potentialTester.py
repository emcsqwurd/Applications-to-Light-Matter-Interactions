from quantum import potential as pt

class PotentialTester:
    ## CONSTRUCTOR
    def __init__(self, ptparms):
        self.ptparms = self.setPtparms(ptparms)
        self.pf = pt.PotentialFactory()

    ## GETTERS
    def getPtparms(self):
        return self.ptparms

    ## SETTERS
    def setPtparms(self, ptparms):
        self.ptparms = ptparms
    def addSechType(self):
        self.pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)

    ## GENERATORS
    def generateSechPotential(self):
        self.addSechType
        return self.pf.createPotential("sech", self.ptparms)



ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
potentialTester = PotentialTester(ptparms)
sechPotential = potentialTester.generateSechPotential()
print(sechPotential)


