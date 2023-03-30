import numpy as np

U,V,W = np.random.randint(10,size=(4,1)),np.random.randint(10,size=(4,1)),np.random.randint(10,size=(4,1))
k=np.random.randint(10)
print(np.vdot(U,V))