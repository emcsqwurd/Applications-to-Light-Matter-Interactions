from quantum.qobj import Qobj
import numpy as np

def effectVaryingSbOnOptimalBasis():
    qobj = Qobj()
    print("---ck info---")
    ckv = qobj.getCk()
    print(ckv.size)
    print(np.shape(ckv))
    
    print("---Default sb---")
    test1 = qobj.optimalBasis()
    print(test1.size)
    print(np.shape(test1))
    
    print("---varied sb---")
    qobj.setSb(0.11) #weirdness occurring between sb= 0.21 - 0.22.  Check default parameters
    test2 = qobj.optimalBasis()
    print(test2.size)
    print(np.shape(test2))






print(effectVaryingSbOnOptimalBasis())


