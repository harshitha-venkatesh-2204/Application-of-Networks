import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_simulation_results(file_path):
    data = {
        'Simulation Step': [],
        'Queue Length': [],
        'Dropped Packets': []
    }

    with open(file_path, 'r') as file:
        for line in file:
            step, queue_length, dropped_packets = map(int, line.split())
            data['Simulation Step'].append(step)
            data['Queue Length'].append(queue_length)
            data['Dropped Packets'].append(dropped_packets)

    df = pd.DataFrame(data)

    sns.set(style='darkgrid')
    plt.figure(figsize=(10, 6))

    sns.lineplot(x='Simulation Step', y='Queue Length', data=df, label='Queue Length')
    sns.lineplot(x='Simulation Step', y='Dropped Packets', data=df, label='Dropped Packets')

    plt.title('Simulation Results with Variable Arrival Rate')
    plt.xlabel('Simulation Step')
    plt.ylabel('Count')
    plt.legend()
    plt.savefig(f"{file_path[:-4]}_seaborn.png")
    plt.show()

if __name__ == "__main__":
    simulation_file_path = "variable_simulation_results_alternate.txt"
    plot_simulation_results(simulation_file_path)
