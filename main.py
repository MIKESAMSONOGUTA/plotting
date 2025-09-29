import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pip

pip.main(['install', 'matplotlib'])
pip.main(['install', 'numpy'])
pip.main(['install', 'pandas'])

def process_cocoa_data():
    file_path = "/mnt/data/FAOSTAT_data_en_9-29-2025 (1).csv"
    df = pd.read_csv(file_path)
    df = df[df['Country'].isin(['Ghana', "Côte d'Ivoire"])]
    df = df[df['Element'].isin(['Area harvested', 'Yield', 'Production'])]

    table = df.pivot_table(
        index=['Area', 'Year'],
        columns='Element',
        values='Value',
        aggfunc='first'
    ).reset_index()

    ghana_table = table[table['Area'] == 'Ghana'].drop(columns='Area').reset_index(drop=True)
    ivory_table = table[table['Area'] == "Côte d'Ivoire"].drop(columns='Area').reset_index(drop=True)

    table = table[['Area', 'Year', 'Area harvested', 'Yield', 'Production']]
    return ghana_table, ivory_table


def plot_cocoa_production(ghana, ivory):
    plt.figure(figsize=(10, 6))
    plt.plot(ghana['Year'], ghana['Production'], marker='o', label='Ghana')
    plt.plot(ivory['Year'], ivory['Production'], marker='s', label="Côte d'Ivoire")

    plt.title("Cocoa Production Trends")
    plt.xlabel("Year")
    plt.ylabel("Production (tonnes)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def main():
    file_path = "/mnt/data/FAOSTAT_data_en_9-29-2025 (1).csv"
    ghana_table, ivory_table = process_cocoa_data(file_path)

    ghana_table.to_csv("/mnt/data/ghana_cocoa.csv", index=False)
    ivory_table.to_csv("/mnt/data/ivory_coast_cocoa.csv", index=False)

    print("Ghana and Côte d'Ivoire tables saved as CSV.")
    print("Displaying production plot...")
    plot_cocoa_production(ghana_table, ivory_table)

    ax.scatter(x, y)= plot_scatter()

    def plot_scatter():
        import matplotlib.pyplot as plt
        import random
        x = [random.random() for _ in range(30)]
        y = [random.random() for _ in range(30)]
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        plt.show()

    if __name__ == "__main__":
      main()