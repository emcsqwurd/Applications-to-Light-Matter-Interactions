from quantum.plot import bandStructure
from quantum.qobj import Qobj

qobj1 = Qobj()
ek = qobj1.getEk()
potential = qobj1.getPotential()
res = bandStructure(ek, potential)
print(res)

