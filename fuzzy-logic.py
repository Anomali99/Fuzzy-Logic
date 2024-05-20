import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

plt.switch_backend('Agg')

#Definisi Semesta
suhu_udara = ctrl.Antecedent(np.arange(0, 38, 1), "Suhu Udara")
kelembaban = ctrl.Antecedent(np.arange(0, 71, 1), "Kelembaban")
durasi = ctrl.Consequent(np.arange(0, 91, 1), "Durasi Penyiraman")

#Membership Function
suhu_udara['coll'] = fuzz.trimf(suhu_udara.universe, [0, 7.5, 15])
suhu_udara['normal'] = fuzz.trimf(suhu_udara.universe, [11, 18.5, 26])
suhu_udara['hot'] = fuzz.trimf(suhu_udara.universe, [22, 29.5, 37])

kelembaban['dry'] = fuzz.trimf(kelembaban.universe, [0, 10, 20])
kelembaban['moist'] = fuzz.trimf(kelembaban.universe, [15, 32.5, 50])
kelembaban['wet'] = fuzz.trimf(kelembaban.universe, [45, 55, 70])

durasi['short'] = fuzz.trimf(durasi.universe, [0, 14, 28])
durasi['medium'] = fuzz.trimf(durasi.universe, [20, 34, 48])
durasi['long'] = fuzz.trimf(durasi.universe, [40, 65, 90])

suhu_udara.view()
plt.savefig('./chart/suhu_udara_membership_function.png')
plt.close()
kelembaban.view()
plt.savefig('./chart/kelembaban_membership_function.png')
plt.close()
durasi.view()
plt.savefig('./chart/durasi_membership_function.png')
plt.close()

#Rule
rule1 = ctrl.Rule(suhu_udara['hot'] & kelembaban['dry'], durasi['long'])
rule2 = ctrl.Rule(suhu_udara['hot'] & kelembaban['moist'], durasi['medium'])
rule3 = ctrl.Rule(suhu_udara['normal'] & kelembaban['dry'], durasi['long'])
rule4 = ctrl.Rule(suhu_udara['normal'] & kelembaban['moist'], durasi['medium'])

penyiraman_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
durasi_penyiraman = ctrl.ControlSystemSimulation(penyiraman_ctrl)

#Input
durasi_penyiraman.input["Suhu Udara"] = 13
durasi_penyiraman.input["Kelembaban"] = 20
durasi_penyiraman.compute()

#Output
print(durasi_penyiraman.output["Durasi Penyiraman"])
durasi.view(sim=durasi_penyiraman)
plt.savefig('./chart/durasi_hasil.png')
plt.close()