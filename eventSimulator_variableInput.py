from random import random

def get_arrival_rate(event, total_events):
    """Determine the arrival rate (λ) based on the current event number."""
    percentage = (event / total_events) * 100
    
    if 0 <= percentage < 10:
        return 70
    elif 10 <= percentage < 70:
        return 200
    elif 70 <= percentage < 80:
        return 130
    elif 80 <= percentage < 90:
        return 120
    else:  # 90 <= percentage <= 100
        return 70

def simulate_variable_rate_events():
    departure_rate = 120  # Departure rate (μ)
    buffer_size = 100     # Maximum queue size (n)
    num_events = 1000000  # Number of simulation steps

    packets_in_queue = 0
    packets_dropped = 0

    output_file = "variable_simulation_results_alternate.txt"
    
    with open(output_file, "w") as file:
        for event in range(num_events):
            arrival_rate = get_arrival_rate(event, num_events)
            threshold = arrival_rate / (departure_rate + arrival_rate)
            
            random_value = random()
            
            if random_value < threshold:  # Arrival event
                if packets_in_queue < buffer_size:
                    packets_in_queue += 1
                else:
                    packets_dropped += 1
            else:  # Departure event
                if packets_in_queue > 0:
                    packets_in_queue -= 1

            file.write(f"{event} {packets_in_queue} {packets_dropped}\n")

if __name__ == "__main__":
    simulate_variable_rate_events()
