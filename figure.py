import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


position = r'C:\Users\gabrielle\Desktop\Université\Session 4\Optique (lab)\oximetre\figure.xlsx'
data = np.array(pd.read_excel(position)).transpose()

essais = data[0]
taux_c = data[1]
pouls_c = data[2]
taux_e = data[3]
pouls_e = data[4]

f = plt.figure()
plt.plot(essais, taux_c, "bo", label="oximètre commercial")
plt.plot(essais, taux_e, "rx", label="résultats expérimentaux")
plt.legend()
plt.xlabel("Essais")
plt.ylabel("Taux d'oxygénation (%)")
plt.show()
f.savefig("taux.png", bbox_inches='tight',dpi=600)

g = plt.figure()
plt.plot(essais, pouls_c, "bo", label="oximètre commercial")
plt.plot(essais, pouls_e, "rx", label="résultats expérimentaux")
plt.legend()
plt.xlabel("Essais")
plt.ylabel("Pouls (bpm)")
plt.show()
g.savefig("pouls.png", bbox_inches='tight',dpi=600)
