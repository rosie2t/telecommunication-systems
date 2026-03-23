# Ypologismos ths fasmatikhs apodoshs tou kathe systhmatos apo to D erwthma
import numpy as np
import matplotlib.pyplot as plt
from ergasia_partA import Q
from ergasia_partC import required_SNR
from ergasia_partD import M_values
from ergasia_partD import Pb
from ergasia_partD import SNR_b_values

def spectral_efficiency(M, SNR_b):
    return np.log2(M) * (1 - 2 * (M - 1) / (M * np.log2(M)) * Q(np.sqrt(3 * np.log2(M) * SNR_b / (M**2 - 1))))

# Ypologismos ths fasmatikhs apodoshs gia kathe M
efficiencies = [spectral_efficiency(M, SNR_b) for M, SNR_b in zip(M_values, SNR_b_values)]

# Sxediash ths fasmatikhs apodoshs se sxesh me to M
plt.plot(M_values, efficiencies, marker='o')
plt.xlabel('M')
plt.ylabel('Spectral Efficiency (bits/s/Hz)')
plt.title('Spectral Efficiency vs M')
plt.xscale('log')
plt.grid(True)
plt.show()
