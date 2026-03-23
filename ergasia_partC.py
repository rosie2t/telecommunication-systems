# Ypologismos tou apaitoumenou SNRb
import numpy as np
from scipy.optimize import newton
from ergasia_partA import Q

def required_SNR(Pb, M):
    def equation(SNR_b):
        # H ejiswsh pou prepei na luthei gia ton upologismo tou SNR_b
        return Pb - 2 * (M - 1) / (M * np.log2(M)) * Q(np.sqrt(3 * np.log2(M) * SNR_b / (M**2 - 1)))
    
    # Xrhsh ths methodou Newton-Raphson gia thn epilush ths ejiswshs
    SNR_b = newton(equation, x0=10)
    return SNR_b

# Paradeigma xrhshs
M = 4
Pb = 1e-3
SNR_b = required_SNR(Pb, M)
print(f"Required SNR_b for M={M}, Pb={Pb}: {SNR_b} dB")

