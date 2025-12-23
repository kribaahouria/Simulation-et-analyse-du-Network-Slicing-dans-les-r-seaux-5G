from traffic import generate_traffic
import simpy

def run_simulation(env, slices, arrival_rates, duration=100):
    """
    Lancer la simulation pour chaque slice.
    env : environnement SimPy
    slices : liste d'objets Slice5G
    arrival_rates : dict {slice_name: arrival_rate}
    duration : temps total de simulation
    """
    for s in slices:
        env.process(generate_traffic(env, s, arrival_rate=arrival_rates[s.name]))

    env.run(until=duration)
