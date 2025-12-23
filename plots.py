import matplotlib.pyplot as plt

def plot_slices(slices, filename="slices_5G_results.png"):
    names = [s.name for s in slices]
    avg_delays = [s.average_delay() for s in slices]
    max_delays = [max(s.delays) if s.delays else 0 for s in slices]
    min_delays = [min(s.delays) if s.delays else 0 for s in slices]

    plt.figure(figsize=(10,6))
    plt.bar(names, avg_delays, color=['blue', 'red', 'green'], alpha=0.7)
    plt.errorbar(names, avg_delays, yerr=[avg_delays[i]-min_delays[i] for i in range(len(slices))],
                 fmt='o', color='black', capsize=5)
    plt.ylabel("Délai moyen (ms)")
    plt.title("Simulation Network Slicing 5G")
    plt.savefig(filename)
    plt.show()
