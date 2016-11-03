import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# data from here: https://www-boone.fnal.gov/for_physicists/data_release/nue_nuebar_2012/combined.html#fit200 (90%CL)
data_1s = np.genfromtxt("miniboone_90CL.txt")
data_3s = np.genfromtxt("cont_3s.txt")

#super kamiokande data from here and here http://hitoshi.berkeley.edu/neutrino/alltan2014.top (95%CL)
#https://arxiv.org/pdf/0803.4312v1.pdf
data_sk = np.genfromtxt("sk-combined.txt")

# from here: https://arxiv.org/pdf/1403.1532v3.pdf (fig 3. / 90%CL)
data_t2k = np.genfromtxt("t2k_1.csv", delimiter=',')

data_daya = np.genfromtxt("daya-bay.csv", delimiter=',')

plt.figure(figsize=(8, 6), dpi=100)

plt.rc('text', usetex=True)
plt.rc('font', family='Fira Sans')

markersize = 3


#CS = plt.loglog(data_3s[:, 0], data_3s[:, 1], '*')
CS = plt.loglog(data_sk[:, 2], 1E-4*np.sin(np.arctan(np.sqrt(data_sk[:, 3])))**2,
                '.',
                label="KamLand (95\% CL)",
                markersize=markersize
                )
CS = plt.loglog(data_t2k[:, 0], data_t2k[:, 1]*1E-3,
                '.',
                label="T2K (90\% CL)",
                markersize=markersize
                )

CS = plt.loglog(data_daya[:, 0], data_daya[:, 1]*1E-3,
                '.',
                label="Daya Bay (90\% CL)",
                markersize=markersize
                )

CS = plt.loglog(data_1s[:, 0], data_1s[:, 1],
                '.',
                label="Miniboone (90\% CL)",
                markersize=markersize,
                )

label_fontsize = 20
plt.xlim([1E-3, 1E0])
plt.ylim([1E-5, 1E0])

plt.xlabel(r"$sin^2 2 \theta_{ij}$", fontsize=label_fontsize)
plt.ylabel(r"$\Delta m_{ij}^2 \ [eV^2]$", fontsize=label_fontsize)

plt.tick_params(axis='both', which='major', labelsize=15)
plt.legend(loc=3)
plt.grid(which='both')

plt.savefig("contours_all.pdf", transparent=True)

plt.show()