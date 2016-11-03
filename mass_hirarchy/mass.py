import numpy as np
import matplotlib.pyplot as plt

# Physics declarations
steril = True

mixing = np.array([[2. / 3., 1. / 6., 1. / 6.],
                   [1. / 3., 1. / 3., 1. / 3.],
                   [1. / 9., 4. / 9., 4. / 9.]])

m_1 = 1
m_2 = 3
m_3 = 10

m_steril = 24
steril_angle = 0.05

mass = [m_1, m_2, m_3]
color = ['r', 'b', 'g']

nus_flavour = [r"$\nu_e$", r"$\nu_{\mu}$", r"$\nu_{\tau}$"]
nus_mass = [r"$v_1$", r"$v_2$", r"$v_3$"]

# add stuff if we plot the sterile case
if steril:
    mass.append(m_steril)
    color.append("m")

    steril_fill = 1 + steril_angle - 3 * steril_angle

    mixing = np.append(mixing, [[steril_angle, steril_angle, steril_angle]], axis=0)
    mixing = np.append(mixing, [[steril_angle], [steril_angle], [steril_angle], [steril_fill]], axis=1)

    nus_flavour.append(r"$\nu_{s}$")
    nus_mass.append(r"$v_4$")

print mixing
stacked_mixing = np.cumsum(mixing, axis=1)

# actual plotting
y_max = np.ceil(1.1 * m_steril)
fontsize = 30

fig = plt.figure(figsize=(8, 6), dpi=100)

plt.rc('text', usetex=True)

for row in reversed(range(len(stacked_mixing))):
    ax = plt.barh(mass, stacked_mixing[:, row], color=color[row], align='center', height=0.5)

ax = plt.gca()
ax.get_xaxis().set_visible(False)

ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')

ax.yaxis.set_ticks_position('left')
ax.arrow(0, 0, 0, y_max, width=0.002, color='k', clip_on=False, head_width=0.02, head_length=0.2)
plt.xlim([0, 1.2])
plt.ylim([0, y_max])
plt.yticks(mass, nus_mass, fontsize=fontsize)
plt.ylabel("mass", fontsize=fontsize)

# generic settings for annotation
params_arrow = {'xycoords': 'data', "textcoords": 'data', 'arrowprops': {'arrowstyle': '<->'}}
parmas_text = {'xycoords': 'data', "textcoords": 'data', 'verticalalignment': 'center', 'fontsize': fontsize}

# Flavour eigenstate labels
for idx, nu in enumerate(nus_flavour):
    x_midpoint = stacked_mixing[0, idx] - mixing[0, idx] / 2
    offset_flavour = -0.3
    plt.annotate(nu,
                 xytext=(x_midpoint, offset_flavour),
                 xy=(0, 1), color=color[idx],
                 horizontalalignment='center',
                 **parmas_text)

# Mass splittings
offset_arrow = 1.1
offset_text = offset_arrow + 0.04

for idx, (m_low, m_high) in enumerate(zip(mass[:-1], mass[1:])):
    print m_low, m_high
    midpoint = (m_high - m_low) / 2 + m_low

    # arrows
    plt.annotate('',
                 xy=(offset_arrow, m_low),
                 xytext=(offset_arrow, m_high),
                 **params_arrow
                 )

    # labels
    plt.annotate('$\Delta m_{%(low)s%(high)s}^2$' % {'low': str(idx + 1), 'high': str(idx + 2)},
                 xy=(0, 0),
                 xytext=(offset_text, midpoint),
                 **parmas_text)

if steril:
    plt.savefig("mass_steril.pdf", transparent=True)
else:
    plt.savefig("mass_classic.pdf", transparent=True)

plt.show()
