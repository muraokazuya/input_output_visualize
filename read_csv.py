import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("filename", delimiter=",", encoding="sjis") #encoding must be your file encoding
plt.plot(a)
plt.show()
