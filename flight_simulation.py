# Flight Simulation

class FlightSimulation:
    def __init__(self, aircraft, environment):
        self.aircraft = aircraft
        self.environment = environment

    def start_simulation(self):
        print(f"Starting simulation for {self.aircraft} in {self.environment}.")

# Example Usage
if __name__ == '__main__':
    sim = FlightSimulation('Boeing 747', 'Tropical Weather')
    sim.start_simulation()