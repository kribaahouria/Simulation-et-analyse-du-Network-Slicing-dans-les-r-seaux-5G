import random
import simpy

def generate_traffic(env, slice_obj, arrival_rate):
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        delay = random.uniform(0.5, slice_obj.latency_target * 2)
        slice_obj.record_packet(delay)
