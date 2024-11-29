import pandas as pd
import matplotlib.pyplot as plt


file_path_without_capacitor = "data/schreibtischlampe5_1000.csv"
file_path_with_capacitor = "data/schreibtischlampe5_1000_mk.csv"


def get_plot_data(file_path):
    data = pd.read_csv(file_path, sep=";")
    y_axis = voltages = data.iloc[:, 2]
    x_axis = range(len(voltages))

    return x_axis, y_axis




def plot_with_and_without_capacitor():
    fig, axs = plt.subplots(2)
    fig.tight_layout(pad=3)
    fig.set_size_inches(8, 6)
    x_axis, y_axis = get_plot_data(file_path_without_capacitor)

    axs[0].plot(x_axis, y_axis, label="ohne Kondensator")

    x_axis, y_axis = get_plot_data(file_path_with_capacitor)

    axs[1].plot(x_axis, y_axis, label="mit Kondensator", color="green")


    # label x and y axis
    axs[0].set(xlabel="Zeit in Sekunden", ylabel="Spannung in Volt")
    axs[1].set(xlabel="Zeit in Sekunden", ylabel="Spannung in Volt")
    plt.savefig("plots/capacitor-2.png")

def plot_outside_measurement():
    plt.clf()
    file_path_outside = "data/outside_1000.csv"
    x_axis, y_axis = get_plot_data(file_path_outside)
    plt.plot(x_axis, y_axis)


    plt.xlabel("Zeit in Sekunden")
    plt.ylabel("Spannung in Volt")
    plt.savefig("plots/outside_measurement.png")




def plot_capacitor():
    plt.clf()
    file_path_capacitor = "data/schreibtischlampe5_500_mk.csv"
    x_axis, y_axis = get_plot_data(file_path_capacitor)
    plt.plot(x_axis, y_axis)
    plt.xlabel("Zeit in Sekunden")
    plt.ylabel("Spannung in Volt")
    plt.savefig("plots/capacitor.png")




plot_capacitor()
plot_outside_measurement()
plot_with_and_without_capacitor()
