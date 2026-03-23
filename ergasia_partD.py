# Sxediasmos grafikhs parastashs me xrhsh teleutaiou pshfioy AM
import numpy as np
import matplotlib.pyplot as plt
from ergasia_partC import required_SNR

# Orismos tou M
M_values = [2**m for m in range(1, 10)]

# Xrhsh tou teleutaiou pshfiou tou AM gia ton upologismo tou Pb
# Proswpikos AM - 2021056
x = 6
Pb = 10**(-x-2)

# Ypologismos tou apaitoumenou SNR_b gia kathe M
SNR_b_values = [required_SNR(Pb, M) for M in M_values]

# Metatrpoh tou SNR_b apo grammikh klimaka se dB
SNR_b_dB_values = 10 * np.log10(SNR_b_values)

# Sxediash tou SNR_b (se dB) se sxesh me to M
plt.plot(M_values, SNR_b_dB_values, marker='*')
plt.xlabel('M (Order of PAM)')
plt.ylabel('SNR_b (dB)')
plt.title(f'Required SNR_b vs M for Pb = {Pb}')
plt.xscale('log')
plt.grid(True)
plt.show()
