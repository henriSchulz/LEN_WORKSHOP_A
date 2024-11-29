import pandas as pd
import numpy as np

def calc_energy(voltages):
    currents = np.diff(voltages * 2) * C
    powers = voltages[1:len(voltages)] * currents

    return np.trapezoid(powers)

file_path = "data/schreibtischlampe5_500_mk.csv"
C = 0.22  # F
data = pd.read_csv(file_path, sep=";")
voltages = data.iloc[:, 2]
discharge_index = voltages.idxmax()
charge_voltages = voltages[:discharge_index]
discharge_voltages = voltages[discharge_index:]
charge_energie = calc_energy(charge_voltages)
discharge_energie = calc_energy(discharge_voltages)
efficiency = discharge_energie/charge_energie
print(f"Wirkungsgrad: {abs(round(efficiency, 5)) * 100}%")







