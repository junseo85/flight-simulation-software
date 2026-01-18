# flight_simulation.py

"""
Flight Simulation Core Module

This Python module provides the core functionality for flight simulation, including 
flight dynamics, control input handling, and subsystem interactions.

Author: junseo85
"""

class FlightSimulation:
    def __init__(self):
        """
        Initialize the simulation variables such as position, speed, altitude, and inputs.
        """
        self.position = [0, 0, 0]  # [x, y, z]
        self.speed = 0  # meters per second
        self.altitude = 0  # meters above sea level
        self.inputs = {
            'throttle': 0.0,  # Throttle position (0.0 to 1.0)
            'pitch': 0.0,     # Pitch angle in degrees
            'roll': 0.0,      # Roll angle in degrees
            'yaw': 0.0        # Yaw angle in degrees
        }

    def update(self, delta_time):
        """
        Update the simulation state based on input commands and time step.

        Args:
        delta_time (float): Time step in seconds.
        """
        # Simulate altitude change based on throttle input
        self.altitude += self.inputs['throttle'] * delta_time * 10  # Example value

        # Update position (simplistic example)
        self.position[0] += self.speed * delta_time
        self.position[1] += self.inputs['roll'] * delta_time
        self.position[2] += self.inputs['pitch'] * delta_time

    def set_input(self, input_name, value):
        """
        Set control input values for the simulation.

        Args:
        input_name (str): The name of the input control.
        value (float): The value to assign to the input.
        """
        if input_name in self.inputs:
            self.inputs[input_name] = value
        else:
            raise ValueError(f"Invalid input name: {input_name}")

    def get_state(self):
        """
        Retrieve the current state of the simulation.

        Returns:
        dict: A dictionary containing position, speed, altitude, and inputs.
        """
        return {
            'position': self.position,
            'speed': self.speed,
            'altitude': self.altitude,
            'inputs': self.inputs
        }