import sys
import random
import matplotlib.pyplot as plt

def event_simulation(arrival_rate, departure_rate, buffer_size, total_events):
    pkt_in_q = 0
    pkt_dropped = 0
    steps = []
    pkts_in_q = []
    pkts_dropped = []
    
    for i in range(total_events):
        y = random.random()
        if y <= arrival_rate / (departure_rate + arrival_rate):  # Arrival event
            if pkt_in_q < buffer_size:
                pkt_in_q += 1
            else:
                pkt_dropped += 1
        else:  # Departure event
            if pkt_in_q > 0:
                pkt_in_q -= 1
        
        steps.append(i)
        pkts_in_q.append(pkt_in_q)
        pkts_dropped.append(pkt_dropped)
    
    return steps, pkts_in_q, pkts_dropped

def plot_simulation_results(steps, pkts_in_q, pkts_dropped, filename):
    plt.figure()
    plt.plot(steps, pkts_in_q, label='Packets in Queue')
    plt.plot(steps, pkts_dropped, label='Packets Dropped')
    plt.xlabel('Simulation Step')
    plt.ylabel('Count')
    plt.title('Simulation Results with Constant Input Rate')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def write_to_file(steps, pkts_in_q, pkts_dropped, filename):
    with open(filename.replace('.png', '.txt'), 'w') as f:
        f.write("Step, Packets in Queue, Packets Dropped\n")
        for i in range(len(steps)):
            f.write(f"{steps[i]}, {pkts_in_q[i]}, {pkts_dropped[i]}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python eventSimulation_constantInput.py <arrival_rate> <departure_rate> <buffer_size>")
        sys.exit(1)

    arrival_rate = float(sys.argv[1])
    departure_rate = float(sys.argv[2])
    buffer_size = int(sys.argv[3])
    total_events = 1000000

    steps, pkts_in_q, pkts_dropped = event_simulation(arrival_rate, departure_rate, buffer_size, total_events)
    filename = f"constant_simulation_results_lambda_{arrival_rate}_mu_{departure_rate}_n_{buffer_size}.png"
    plot_simulation_results(steps, pkts_in_q, pkts_dropped, filename)
    write_to_file(steps, pkts_in_q, pkts_dropped, filename)
