import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("filename", delimiter=",", encoding="sjis") #encoding must be your file encoding
plt.subplot(2,3,1)
plt.plot(a)
plt.subplot(2,3,2)
plt.plot(a)
plt.show()
