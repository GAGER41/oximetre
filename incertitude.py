import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# On utilise l'essais 4 pour calculer l'incertitude sur le taux

# ir_max = 0.7
# ir_min = 0.6
# r_max = 4.057854067180774
# m_min = 3.751720181004501

position = r'C:\Users\gabrielle\Desktop\Université\Session 4\Optique (lab)\oximetre\F0004CH1.CSV'
data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()

f = plt.figure()

plt.plot(data[0], data[1])
plt.xlabel("temps (s)")
plt.ylabel("intensité du signal")
plt.show()
f.savefig("ex_data.png", bbox_inches='tight',dpi=600)

# r_max

r_max_max = 4.1
r_max_min = 4.08
r_max_rel = 0.02/4.09

# r_min

r_min_max = 3.86
r_min_min = 3.84
r_min_rel = 0.02/3.85

# ir_max

ir_max_max = 0.68
ir_max_min = 0.66
ir_max_rel = 0.02/0.67

# ir_min

ir_min_max = 0.64
ir_min_min = 0.62
ir_min_rel = 0.02/0.63

#print(ir_max_rel, ir_min_rel, r_max_rel, r_min_rel)

ratio = np.log(r_min_rel+r_max_rel)/np.log(ir_min_rel+ir_max_rel)
taux_ox_incert = 0.81 - 0.18*ratio/(0.81 - 0.08 + (0.29 - 0.18) * ratio)

#print(taux_ox_incert*69)