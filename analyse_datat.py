import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal, interpolate


for i in range(10):
    position = r'C:\Users\gabrielle\Desktop\Université\Session 4\Optique (lab)\oximetre\F000{}CH1.CSV'.format(i)
    data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
    temps = data[0][600:2000]
    _signal = data[1][600:2000]
    data = np.array([temps, _signal])
    #print(data)
    if i == 7:
        continue
    
    #plt.plot(data[0], data[1])
    #plt.title('essai {}'.format(i))
    #plt.show()

    freq_card = []
    ir_min = []
    ir_max = []
    r_min = []
    r_max = []
    j = 0
    while j < ((data.size) - 1):
        try:
            # ROUGE
            if data[1][j+10] - data[1][j] > 2:                  # Pour séparer rouge et infrarouge
                try:
                    s_temps = np.array(data[0][j:j+500])        # Crée des sous-arrays
                    s_signal = np.array(data[1][j:j+500])       # 2 secondes = 500 éléments

                    s_temps = s_temps[20:]                      # coupe les débuts louches
                    s_signal = s_signal[20:]

                    # frequence cardiaque
                    spl = interpolate.UnivariateSpline(s_temps, s_signal)       # "filtre"
                    spl.set_smoothing_factor(0.2)

                    peaks, _ = signal.find_peaks(spl(s_temps), distance=50)     # trouve les max
                    p_temps = s_temps[peaks]                                    # matrice avec seulement les max, donc écart entre deux max = un pouls

                    periode = []
                    for k in range(1, p_temps.size):
                        intervalle = p_temps[k] - p_temps[k-1]
                        periode.append(intervalle)

                    periode = np.array(periode)         # périodes, un array
                    freqs_card = 60 / periode           # array des fréquences calulées dans ce sous-array
                    freq_card.append(np.mean(freqs_card))       #fait une moyenne pour ce sous-array (fréquence en bpm)

                    # max et min 
                    max_loc = np.amax(spl(s_temps))                 # Trouve des max et les min de chaque sous-array
                    r_max.append(max_loc)

                    min_loc = np.amin(spl(s_temps))
                    r_min.append(min_loc)

                except IndexError:
                    #j += 2
                    continue
                else:
                    """plt.plot(s_temps, s_signal)
                    plt.plot(s_temps, spl(s_temps))
                    #plt.plot(s_temps[peaks], s_signal[peaks], 'rx')
                    plt.title('essai {}, rouge'.format(i))
                    plt.show()"""

                j += 10

            # INFRAROUGE
            elif data[1][j+10] - data[1][j] < -2:
                try:
                    s_temps = np.array(data[0][j:j+500])
                    s_signal = np.array(data[1][j:j+500])

                    s_temps = s_temps[20:]
                    s_signal = s_signal[20:]

                    # max et min
                    max_loc = np.amax(s_signal)
                    ir_max.append(max_loc)

                    min_loc = np.amin(s_signal)
                    ir_min.append(min_loc)

                except IndexError:
                    #j += 2
                    continue
                else:
                    """plt.plot(s_temps, s_signal)
                    plt.title('essai {}, infrarouge'.format(i))
                    plt.show()"""

                j += 10
            
            j += 2

        except IndexError:
            break

    frq_moy = np.nanmean(np.array(freq_card))
    #print(frq_moy)
    ir_max = np.nanmean(np.array(ir_max))
    ir_min = np.nanmean(np.array(ir_min))
    r_max = np.nanmean(np.array(r_max))
    r_min = np.nanmean(np.array(r_min))

    if i == 4:
        print(ir_max, ir_min, r_max, r_min)

    ratio = np.log(r_min/r_max)/np.log(ir_min/ir_max)
    taux_ox = 0.81 - 0.18*ratio/(0.81 - 0.08 + (0.29 - 0.18) * ratio)

    print('    Essai {}'.format(i))
    print("Taux d'oxygénation: {}%".format(taux_ox*100))
    print("Fréquence cardiaque: {} bpm".format(frq_moy))