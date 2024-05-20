import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
# import random

plt.switch_backend('Agg')

def get(KepadatanInput, WaktuInput):
    #Definisi Semesta
    kepadatan = ctrl.Antecedent(np.arange(0, 13, 1), "Kepadatan")
    waktu = ctrl.Antecedent(np.arange(0, 26, 1), "Waktu")
    durasi = ctrl.Consequent(np.arange(0, 21, 1), "Durasi")

    #Membership Function
    kepadatan["low"] = fuzz.trimf(kepadatan.universe, [0, 0, 4])
    kepadatan["medium"] = fuzz.trimf(kepadatan.universe, [2, 5, 8])
    kepadatan["high"] = fuzz.trapmf(kepadatan.universe, [6, 10, 12, 12])

    waktu["w1"] = fuzz.trimf(waktu.universe, [0, 0, 6])
    waktu["w2"] = fuzz.trimf(waktu.universe, [0, 6, 9])
    waktu["w3"] = fuzz.trimf(waktu.universe, [6, 9, 12])
    waktu["w4"] = fuzz.trimf(waktu.universe, [9, 12, 16])
    waktu["w5"] = fuzz.trimf(waktu.universe, [12, 16, 20])
    waktu["w6"] = fuzz.trimf(waktu.universe, [16, 20, 25])
    waktu["w7"] = fuzz.trimf(waktu.universe, [20, 25, 25])

    durasi["sangat cepat"] = fuzz.trapmf(durasi.universe,[0, 0, 5, 10])
    durasi["cepat"] = fuzz.trimf(durasi.universe,[5, 10, 15])
    durasi["lama"] = fuzz.trimf(durasi.universe,[10, 15, 20])
    durasi["sangat lama"] = fuzz.trimf(durasi.universe,[15, 20, 20])


    #Rule 
    rule1 = ctrl.Rule(kepadatan["low"] & waktu["w1"], durasi["sangat cepat"])
    rule2 = ctrl.Rule(kepadatan["low"] & waktu["w2"], durasi["cepat"])
    rule3 = ctrl.Rule(kepadatan["low"] & waktu["w3"], durasi["sangat cepat"])
    rule4 = ctrl.Rule(kepadatan["low"] & waktu["w4"], durasi["cepat"])
    rule5 = ctrl.Rule(kepadatan["low"] & waktu["w5"], durasi["cepat"])
    rule6 = ctrl.Rule(kepadatan["low"] & waktu["w6"], durasi["sangat cepat"])
    rule7 = ctrl.Rule(kepadatan["low"] & waktu["w7"], durasi["sangat cepat"])

    rule8 = ctrl.Rule(kepadatan["medium"] & waktu["w1"], durasi["sangat cepat"])
    rule9 = ctrl.Rule(kepadatan["medium"] & waktu["w2"], durasi["lama"])
    rule10 = ctrl.Rule(kepadatan["medium"] & waktu["w3"], durasi["cepat"])
    rule11 = ctrl.Rule(kepadatan["medium"] & waktu["w4"], durasi["lama"])
    rule12 = ctrl.Rule(kepadatan["medium"] & waktu["w5"], durasi["lama"])
    rule13 = ctrl.Rule(kepadatan["medium"] & waktu["w6"], durasi["cepat"])
    rule14 = ctrl.Rule(kepadatan["medium"] & waktu["w7"], durasi["sangat cepat"])

    rule15 = ctrl.Rule(kepadatan["high"] & waktu["w1"], durasi["cepat"])
    rule16 = ctrl.Rule(kepadatan["high"] & waktu["w2"], durasi["sangat lama"])
    rule17 = ctrl.Rule(kepadatan["high"] & waktu["w3"], durasi["lama"])
    rule18 = ctrl.Rule(kepadatan["high"] & waktu["w4"], durasi["sangat lama"])
    rule19 = ctrl.Rule(kepadatan["high"] & waktu["w5"], durasi["sangat lama"])
    rule20 = ctrl.Rule(kepadatan["high"] & waktu["w6"], durasi["lama"])
    rule21 = ctrl.Rule(kepadatan["high"] & waktu["w7"], durasi["cepat"])

    lampu_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21])
    durasi_lampu = ctrl.ControlSystemSimulation(lampu_ctrl)

    #input
    durasi_lampu.input["Kepadatan"] = KepadatanInput
    durasi_lampu.input["Waktu"] = WaktuInput
    durasi_lampu.compute()

    # #Output
    durasi.view(sim=durasi_lampu)
    plt.savefig('./static/durasi_hasil.png')
    kepadatan.view(sim=durasi_lampu)
    plt.savefig('./static/kepadatan_hasil.png')
    waktu.view(sim=durasi_lampu)
    plt.savefig('./static/waktu_hasil.png')
    return durasi_lampu.output['Durasi']

# plt.show()

# for x in range(10):
#     y = random.randint(1, 12)
#     z = hasil
#     hasil = get(KepadatanInput= y, WaktuInput=z)
#     print(f"waktu jalur {'2' if x % 2 == 0 else '1'} adalah {hasil} dengan kepdatan {y} dan waktu {z}")