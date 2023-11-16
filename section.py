import numpy as np
import matplotlib.pyplot as plt
m=1100

n=2

M = np.ones((m//2,))*m
N = np.ones((m//2,))*n
ONE = np.ones((m//2,))

L = np.linspace(1,m//2,m//2)
# complexity = (N/L*3)*(L+M-ONE)*(np.log2(L+M-ONE)+ONE)
complexity = (M/L*3)*(L+N-ONE)*(np.log2(L+N-ONE)+ONE)
inx = complexity.argmin()
print(f'min:{complexity.min()}')
print(f'inx:{inx}')

plt.plot(L,complexity)
plt.show()
