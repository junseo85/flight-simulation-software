class FlightDynamics:
    def __init__(self):
        """Initialize flight dynamics variables."""
        self.altitude = 0.0  # In meters
        self.speed = 0.0  # In m/s
        self.roll = 0.0  # Rotation in degrees
        self.pitch = 0.0  # Rotation in degrees
        self.yaw = 0.0  # Rotation in degrees

    def update(self, control_input, delta_time):
        """Update flight state based on control inputs and time step."""
        # Control logic
        self.speed += control_input.get('throttle', 0) * delta_time
        self.pitch += control_input.get('pitch', 0) * delta_time
        self.roll += control_input.get('roll', 0) * delta_time
        self.yaw += control_input.get('yaw', 0) * delta_time

        # Example: Change altitude based on pitch and current speed
        self.altitude += self.speed * delta_time * (self.pitch / 90.0)

    def get_state(self):
        """Return the current state of the aircraft."""
        return {
            'altitude': self.altitude,
            'speed': self.speed,
            'roll': self.roll,
            'pitch': self.pitch,
            'yaw': self.yaw,
        }
