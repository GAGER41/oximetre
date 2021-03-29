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

# figure taux

f = plt.figure()
plt.plot(essais, taux_c, "ko", label="oximètre commercial")
plt.plot(essais[0], taux_e[0], "kx", label="résultats expérimentaux")
plt.legend()
plt.errorbar(essais[:7], taux_e[:7], yerr=30, mec="black", marker="x", fmt=' ', ecolor="black")
plt.errorbar(essais[8:], taux_e[8:], yerr=30, mec="black", marker="x", fmt=' ', ecolor="black")
plt.xlabel("Essais")
plt.ylabel("Taux d'oxygénation (%)")
#plt.show()
#f.savefig("taux.png", bbox_inches='tight',dpi=600)

# figure pouls

g = plt.figure()
plt.plot(essais, pouls_c, "ko", label="oximètre commercial")
plt.plot(essais[:5], pouls_e[:5], "kx", label="résultats expérimentaux")
plt.plot(essais[8:], pouls_e[8:], "kx")
plt.legend()
plt.xlabel("Essais")
plt.ylabel("Pouls (bpm)")
#plt.show()
#g.savefig("pouls.png", bbox_inches='tight',dpi=600)
