"""
Project configuration.
Stores simulation, vehicle, and MPC parameters.
"""


# Simulation
TIME_STEP = 0.1          # s
SIMULATION_STEPS = 150


# Vehicle
WHEELBASE = 2.8          # m

INITIAL_X = 0.0
INITIAL_Y = 0.0
INITIAL_YAW = 0.0
INITIAL_SPEED = 5.0


# MPC
PREDICTION_HORIZON = 15

# Tracking weights (Q)
Q_X = 10.0
Q_Y = 10.0
Q_YAW = 2.0
Q_SPEED = 1.0

# Control weights (R)
R_STEERING = 0.5
R_ACCELERATION = 0.2

# Terminal weight
Q_TERMINAL = 20.0

# Desired speed
TARGET_SPEED = 5.0

# Constraints
MAX_STEERING = 0.5
MAX_ACCELERATION = 2.0
MIN_ACCELERATION = -2.0

# Steering smoothness penalty
STEERING_SMOOTHNESS = 5.0