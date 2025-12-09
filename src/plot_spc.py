from pyspectra.readers.read_spc import read_spc,read_spc_dir
import matplotlib.pyplot as plt
import pandas as pd

#code qui permet de visualiser un spectre raman en python
spc1=read_spc('data_j1_2024\\240604_EI_Bioreacteur_J1_20240604-153306.spc')
spc1.plot()
plt.xlabel("nombre d'onde (en cm^-1)")
plt.ylabel("intensité ")
plt.title("Spectre Raman de la mesure du jour 1 à 15h33 (Données 2024)")
plt.show()


