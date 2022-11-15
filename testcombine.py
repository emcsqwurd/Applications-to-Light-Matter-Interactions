from quantum.qobj import Qobj
import matplotlib.pyplot as plt


qobj = Qobj()

def varyingLatticeConstantStandardImaginaryDielectricPlot():
    energy = qobj.getEnergyRangeFunc()
    for i in energy:
        qobj.setParms(lattice = 1)
        res1 = qobj.getStandardImaginaryDielectricPlotArray()
        plt.plot(energy, res1, 'r' )
        qobj.setParms(depth = 80)
        res2 = qobj.getStandardImaginaryDielectricPlotArray()
        plt.plot(energy, res2, 'b--')
        i+1
    plt.show()
    return 
print(varyingLatticeConstantStandardImaginaryDielectricPlot()) 







