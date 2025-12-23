class Slice5G:
    def __init__(self, name, bandwidth, latency_target):
        self.name = name
        self.bandwidth = bandwidth
        self.latency_target = latency_target
        self.packets = 0
        self.total_delay = 0
        self.delays = []

    def record_packet(self, delay):
        self.packets += 1
        self.total_delay += delay
        self.delays.append(delay)

    def average_delay(self):
        if self.packets == 0:
            return 0
        return self.total_delay / self.packets
