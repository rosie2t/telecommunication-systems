#Ylopoihsh ths antistrofhs synarthshs Q**(-1)(z) 
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
# Eisagwgh ths Q synarthshs apo to partA ths ergasias
from ergasia_partA import Q

def Q_inv(z, tol=1e-10, max_iter=100):
    # Ypologismos ths antistrofhs synarthshs me thn methodo Newton-Raphson
    func = lambda y: Q(y) - z
    return newton(func, x0=0.0)

# Paradeigma xrhshs
z = np.linspace(0.001, 0.999, 100)
Q_inv_result = [Q_inv(z) for z in z]

# Sxediasmos ths antistrofhs synarthshs Q_inv(z)
plt.plot(z, Q_inv_result, label='$Q^{-1}(z)$')
plt.xlabel('z')
plt.ylabel('$Q^{-1}(z)$')
plt.title('Inverse Q-function')
plt.legend()
plt.grid(True)
plt.show()

