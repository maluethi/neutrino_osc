import numpy as np
import matplotlib.pyplot as plt

steril = True

mixing = np.array([[2./3., 1./6., 1./6.],
                   [1./3., 1./3., 1./3.],
                   [1./9., 4./9., 4./9.]])


m_1 = 1
m_2 = 3
m_3 = 10

m_steril = 24
steril_angle = 0.05

y_max = 25
fontsize = 30

mass = [m_1, m_2, m_3]
color = ['r', 'b', 'g']

if steril:
    mass.append(m_steril)
    color.append("m")

    steril_fill = 1 + steril_angle - 3*steril_angle

    mixing = np.array([[2. / 3., 1. / 6., 1. / 6., steril_angle],
                       [1. / 3., 1. / 3., 1. / 3., steril_angle],
                       [1. / 9., 4. / 9., 4. / 9., steril_angle],
                       [ steril_angle,     steril_angle,     steril_angle, steril_fill]])

stacked = np.cumsum(mixing, axis=1)

fig = plt.figure(figsize=(8, 6), dpi=100)

plt.rc('text', usetex=True)
plt.rc('font', family='Fira Sans')

for row in reversed(range(len(stacked))):
    ax = plt.barh(mass, stacked[:, row], color=color[row], align='center', height=0.4)


ax = plt.gca()
ax.get_xaxis().set_visible(False)

ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.yaxis.set_ticks_position('left')



plt.arrow(0, 0, 0, y_max, width=0.002, color='k', clip_on=False, head_width=0.02, head_length=0.2)
plt.xlim([0, 1.2])
plt.ylim([0, y_max])

if steril:
    plt.yticks(mass, ["$v_1$", "$v_2$", "$v_3$", "$v_4$"], fontsize=fontsize)
else:
    plt.yticks(mass, ["$v_1$", "$v_2$", "$v_3$"], fontsize=fontsize)

plt.ylabel("mass", fontsize=fontsize)


params_arrow = {'xycoords': 'data', "textcoords": 'data', 'arrowprops': {'arrowstyle': '<->'}}
parmas_text = {'xycoords': 'data', "textcoords": 'data', 'verticalalignment': 'center', 'fontsize': fontsize}

offset_flavour = -0.3


plt.annotate(r"$\nu_e$", xytext=(1./3, offset_flavour), xy=(0,1), color='r', horizontalalignment='center', **parmas_text)
plt.annotate(r"$\nu_{\mu}$", xytext=(0.75, offset_flavour), xy=(0,1), color='b', horizontalalignment='center', **parmas_text)
plt.annotate(r"$\nu_{\tau}$", xytext=(0.91, offset_flavour), xy=(0,1), color='g', horizontalalignment='center',**parmas_text)

# Mass splittings
# Arrows

offset_arrow = 1.1
offset_text = offset_arrow + 0.04

plt.annotate(
    '', xy=(offset_arrow, m_1),
    xytext=(offset_arrow, m_2),
    **params_arrow
    )
plt.annotate(
    '', xy=(offset_arrow, m_2),
    xytext=(offset_arrow, m_3),
    **params_arrow)

# Text
plt.annotate(
    '$\Delta m_{12}^2$',
    xy=(offset_text, m_2-m_1),
    xytext=(offset_text, m_2-m_1),
    **parmas_text)

plt.annotate(
    '$\Delta m_{23}^2$',
    xy=(offset_text, m_3-m_2),
    xytext=(offset_text, m_3-m_2),
    **parmas_text
)

if steril:

    plt.annotate(r"$\nu_{s}$", xytext=(1.02, offset_flavour), xy=(0, 1), color=color[3], horizontalalignment='center',
                 **parmas_text)
    plt.annotate(
        '$\Delta m_{34}^2$',
        xy=(offset_text, m_3 - m_2),
        xytext=(offset_text, (mass[3] - mass[2])/2 + mass[2]),
        **parmas_text
    )

    plt.annotate(
        '', xy=(offset_arrow, mass[3]),
        xytext=(offset_arrow, mass[2]),
        **params_arrow
    )




if steril:
    plt.savefig("mass_steril.pdf", transparent=True)
else:
    plt.savefig("mass_classic.pdf", transparent=True)

plt.show()