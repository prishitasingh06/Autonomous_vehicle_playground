"""
Main program for running the MPC path-tracking simulation.
"""

from vehicle import Vehicle
from path import Path
from mpc_controller import MPCController
from mpc_simulation import MPCSimulation
from visualization import Visualizer
from metrics import Metrics
import config


def main():

    # Create vehicle
    vehicle = Vehicle(
        x=config.INITIAL_X,
        y=config.INITIAL_Y,
        yaw=config.INITIAL_YAW,
        velocity=config.INITIAL_SPEED
    )

    # Create path, controller, and simulation
    path = Path()
    controller = MPCController()
    simulation = MPCSimulation(vehicle=vehicle, controller=controller, path=path)

    # Run simulation
    simulation.run(steps=config.SIMULATION_STEPS)

    # Display performance metrics
    performance = Metrics(simulation)
    performance.summary()

    # Plot simulation results
    visualizer = Visualizer(simulation, path)
    visualizer.plot_path_tracking()
    visualizer.plot_velocity()
    visualizer.plot_steering()
    visualizer.plot_acceleration()
    visualizer.plot_tracking_error()
    visualizer.show()


if __name__ == "__main__":
    main()