# Configuration File

A dedicated configuration file stores all controller and simulation parameters.

Advantages:

- Easy tuning
- Cleaner code
- Centralized constants
- Better reproducibility

Typical parameters include:

- Prediction horizon
- Vehicle wheelbase
- Simulation time
- Tracking weights (Q)
- Control weights (R)
- Terminal weight (Qf)

## MPC Cost Function

The controller minimizes three objectives:

1. Tracking error (Q)
2. Control effort (R)
3. Terminal error (Qf)

Additional steering smoothing reduces rapid steering changes and produces more realistic vehicle behavior.

Moving tuning parameters into `config.py` makes experiments repeatable and keeps the controller implementation clean.

## Performance Metrics

The simulator evaluates controller performance using objective metrics instead of only visual inspection.

Implemented metrics:

- RMS tracking error
- Mean tracking error
- Maximum tracking error
- Final tracking error
- Average vehicle speed
- Maximum vehicle speed

Separating performance evaluation from the controller improves modularity and makes it easier to compare different control algorithms.


## Visualization Module

A dedicated visualization module separates plotting from simulation logic.

Advantages:

- Cleaner code
- Easier debugging
- Reusable plotting functions
- Simpler main program

Generated plots:

- Path tracking
- Vehicle velocity
- Steering command
- Acceleration command
- Tracking error