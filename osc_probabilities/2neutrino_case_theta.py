import numpy as np
import matplotlib.pyplot as plt


def P_alpha_beta(sin2_theta, delta_m2, LE):
    return sin2_theta * (np.sin(1.27 * delta_m2 * LE))**2


def theta_string(value):
    return r"$sin^2 2 \theta_{ij} = " + str(value) + "$"


sin2_theta = [0.8, 0.7, 0.6]
delta_m2 = 8E-5

LE = np.linspace(0, 40000, 100)

plt.figure(figsize=(10, 8), dpi=100)

plt.rc('text', usetex=True)
plt.rc('font', family='Fira Sans')

for value in sin2_theta:
    CS = plt.plot(LE, P_alpha_beta(value, 8E-5, LE),
                    '-',
                    label=theta_string(value),
                    linewidth = 2.0
                  )


label_fontsize = 30
plt.text(1000,0.9, r"$\Delta m_{ij}^2 = 8 \times 10^{-5} eV^2 $",
         fontsize=label_fontsize)

plt.xlabel(r"$L / E \ [km/GeV]$", fontsize=label_fontsize)
plt.ylabel(r"$P_{\alpha \rightarrow \beta }$", fontsize=label_fontsize)



plt.ylim([0,1])
plt.legend(loc=3, fontsize=label_fontsize)
plt.tick_params(axis='both', which='major', labelsize=20)


plt.grid(which='both')

plt.legend(fontsize=20)
plt.savefig("2neutrino_sin.pdf", transparent=True)
plt.show()

