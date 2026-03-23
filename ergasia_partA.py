#Ylopoihsh ths synarthshs Q(y)
import numpy as np 
from scipy.integrate import quad
import matplotlib.pyplot as plt

def Q(y):
    # Orizw thn synarthsh pou tha oloklhrwsw
    result, _ = quad(lambda z: np.exp(-z**2 / 2), y, np.inf)
    return result / np.sqrt(2 * np.pi)

# Paradeigma xrshhs
y = np.linspace(0, 5, 100)
Q_result = [Q(y) for y in y]

# Sxediasmos ths synarthshs Q(y)
plt.plot(y, Q_result, label='Q(y)')
plt.xlabel('y')
plt.ylabel('Q(y)')
plt.title('Q-function')
plt.legend()
plt.grid(True)
plt.show()
