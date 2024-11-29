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

    if np.isnan(voltage):
        raise ValueError("Voltage is not a number for ", file_path)

    current = (voltage * (2 * R_T + resistance)) / (resistance * R_T)
    power = voltage * current

    return current, voltage, power


def save_latex_table(src, resistances, voltages, currents, powers):
    if not os.path.isdir("latex"):
        os.mkdir("latex")

    with open(f"latex/{src}.tex", "w") as f:
        latex_string = pd.DataFrame(
            {"R": resistances, "V": voltages, "I": currents, "P": powers}
        ).to_latex(index=False)
        f.write(latex_string)


def plot_sources(sources):
    for src in sources:
        currents = []
        voltages = []
        powers = []

        for resistance in R_VALUES:
            current, voltage, power = process_measurements(src, resistance)
            currents.append(current)
            voltages.append(voltage)
            powers.append(power)

        save_latex_table(src, R_VALUES, voltages, currents, powers)


        plt.plot(voltages, currents, marker="o")

        max_power = max(powers)
        max_power_index = powers.index(max_power)
        max_power_voltage = voltages[max_power_index]
        max_power_current = currents[max_power_index]

        plt.xlabel("Spannung [V]")
        plt.ylabel("Strom [A]")

        plt.axvline(x=max_power_voltage, color="green", linestyle="--")
        plt.axhline(y=max_power_current, color="green", linestyle="--")

        fig = plt.gcf()

        fig.set_size_inches(8, 6)

        plt.plot(max_power_voltage, max_power_current, marker="o", color="green")

        plt.legend(["U-I-Kennlinie", "max. Leistung"], loc="upper left")

        ax2 = plt.twinx()

        ax2.plot(voltages, powers, marker="o", color="red")

        ax2.set_ylabel("Leistung [W]")

        plt.title("U-I-Kennlinie")
        plt.grid(True)



        if not os.path.isdir("plots"):
            os.mkdir("plots")
        plt.savefig(f"plots/{src}.png")
        plt.clf()


if __name__ == "__main__":
    plot_sources(["schreibtischlampe75", "lampe1", "lampe2"])
