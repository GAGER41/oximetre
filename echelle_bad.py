import numpy as np
from matplotlib import pyplot as plt
import pandas as pd



position = r'C:\Users\gabrielle\Desktop\Université\Session 4\Optique (lab)\oximetre\F0004CH1.CSV'
data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()

temps_r = data[0][760:1240]
_signal_r = data[1][760:1240]

temps_ir = data[0][1270:1740]
_signal_ir = data[1][1270:1740]


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(temps_r, _signal_r)
ax1.set_title("LED rouge allumée")
ax2.plot(temps_ir, _signal_ir)
ax2.set_title("LED infrarouge allumée")
plt.xlabel("temps (s)")
plt.ylabel("Signal")
plt.show()
fig.savefig("taux_echelle.png", bbox_inches='tight',dpi=600)