import numpy as np
import pandas as pd


def calc_power(t, voltages):
    R = 1000
    R_T = 10 ** 5
    U = 2 * voltages[t]
    R_GES = (2 * R_T * R) / (2 * R_T + R)

    return (U ** 2) / R_GES


def calc_total_energie():
    file_path = "data/outside_1000.csv"
    data = pd.read_csv(file_path, sep=";")
    voltages = data.iloc[:, 2]
    times = data.iloc[:, 0]
    powers = [calc_power(i, voltages) for i in range(0, len(times))]
    total_energie = np.trapezoid(powers, times)
    return total_energie


if __name__ == "__main__":
    total_energie = calc_total_energie()
    print(f"Total energy: {total_energie} J")
