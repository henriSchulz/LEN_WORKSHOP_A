import numpy as np
import pandas as pd
import os

cwd = os.getcwd()


def calc_power(t, voltages):
    R = 1000
    R_T = 10 ** 5
    U = 2 * voltages[t]
    R_GES = (2 * R_T * R) / (2 * R_T + R)

    return (U ** 2) / R_GES


def calc_total_energie(voltages):
    time_array = range(len(voltages))
    powers = [calc_power(i, voltages) for i in range(0, len(voltages))]
    total_energie = np.trapezoid(powers, time_array)
    return total_energie


if __name__ == "__main__":
    file_path = cwd + "/data/outside_1000.csv"
    data = pd.read_csv(file_path, sep=";")
    voltages = data.iloc[:, 2][0:7200]
    times = range(0, len(voltages))

    total_energie = calc_total_energie(voltages)
    print(f"Total energy: {total_energie} J")
