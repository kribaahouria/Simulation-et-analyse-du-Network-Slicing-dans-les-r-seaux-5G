import simpy
from slice import Slice5G
from scheduler import run_simulation
from plots import plot_slices
from metrics import max_delay, min_delay, variance_delay

# Définir les slices
embb = Slice5G("eMBB", bandwidth=100, latency_target=20)
urllc = Slice5G("URLLC", bandwidth=50, latency_target=5)
mmtc = Slice5G("mMTC", bandwidth=30, latency_target=50)

slices = [embb, urllc, mmtc]

# Définir plusieurs scénarios de trafic
scenarios = {
    "Faible trafic": {"eMBB": 0.5, "URLLC": 1, "mMTC": 0.1},
    "Trafic normal": {"eMBB": 1, "URLLC": 5, "mMTC": 0.2},
    "Congestion": {"eMBB": 3, "URLLC": 10, "mMTC": 1}
}

# Lancer chaque scénario
for scenario_name, arrival_rates in scenarios.items():
    print(f"\n--- {scenario_name} ---")
    # Réinitialiser l'environnement
    env = simpy.Environment()
    # Réinitialiser les slices
    for s in slices:
        s.packets = 0
        s.total_delay = 0
        s.delays = []
    # Lancer simulation
    run_simulation(env, slices, arrival_rates, duration=100)
    # Afficher résultats
    for s in slices:
        print(f"{s.name}: délai moyen={s.average_delay():.2f} ms, "
              f"max={max_delay(s):.2f} ms, min={min_delay(s):.2f} ms, "
              f"variance={variance_delay(s):.2f}")
    # Graphique
    plot_slices(slices, filename=f"{scenario_name.replace(' ','_')}.png")
