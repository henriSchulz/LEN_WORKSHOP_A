import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

R_VALUES = [10, 100, 440, 680, 900, 1000, 1220, 1440, 1680, 2000, 3300, 4980]

data_path = "data"


def read_csv(file_path):
    data = pd.read_csv(file_path, sep=";")
    if data.empty:
        raise ValueError(f"File {file_path} is empty")

    return data


# reads the data from the csv file and calculates the current and voltage values
def process_measurements(src, resistance):
    file_path = os.path.join(data_path, f"{src}_{resistance}.csv")
    R_T = 10 ** 5
    data = read_csv(file_path)
    voltage = data.iloc[:, 2].mean() * 2

    # check if voltage is a number

    if np.isnan(voltage):
        raise ValueError("Voltage is not a number for ", file_path)

    current = (voltage * (2 * R_T + resistance)) / (resistance * R_T)
    power = voltage * current

    return current, voltage, power


sources = ["schreibtischlampe75"]

for src in sources:
    currents = []
    voltages = []
    powers = []
    for resistance in R_VALUES:
        current, voltage, power = process_measurements(src, resistance)
        currents.append(current)
        voltages.append(voltage)
        powers.append(power)
    plt.plot(voltages, currents, marker="o")

    plt.xlabel("Spannung [V]")
    plt.ylabel("Strom [A]")

    # add second y-axis for power

    ax2 = plt.twinx()

    ax2.plot(voltages, powers, marker="o", color="red")

    ax2.set_ylabel("Leistung [W]")

    plt.title("U-I-Kennlinie")
    plt.grid()
    plt.savefig(f"plots/{src}.png")
