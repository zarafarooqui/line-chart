import matplotlib.pyplot as plt
import numpy as np
x=np.arange(2,13,2)
y1=(2*x)+2
y2=(x*x)+3
plt.plot(x,y1,'g',linewidth=3,label="2x+2")
plt.plot(x,y2,'r',linewidth=3,label="x^2+3")
plt.legend()
plt.show()