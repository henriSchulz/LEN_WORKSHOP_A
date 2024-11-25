import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

R_VALUES = [10, 100, 440, 680, 900, 1000, 1220, 1440, 1660, 2000, 3300, 4980]

data_path = "data"


# reads the data from the csv file and calculates the current and voltage values
def process_measurements(src, resistance):
    file_path = os.path.join(data_path, f"{src}_{resistance}.csv")
    R_T = 10 ** 5
    try:
        data = pd.read_csv(file_path, sep=";")
        voltage = data.iloc[:, 2].mean()
        current = I = (voltage * (2 * R_T + resistance)) / (resistance * R_T)

        return current, voltage
    except Exception as e:
        print(f"Failed to open file {file_path}. Error: {e}")


# Daten verarbeiten

currents = []
voltages = []

for resistance in R_VALUES:
    src = "informatikom"
    current, voltage = process_measurements(src, resistance)
    currents.append(current)
    voltages.append(voltage)

# Daten plotten U-I-Kennlinie mit verbundenen Punkten

plt.plot(currents, voltages, marker="o")
plt.xlabel("Spannung [V]")
plt.ylabel("Strom [A]")
plt.title("U-I-Kennlinie")
plt.grid()
plt.show()