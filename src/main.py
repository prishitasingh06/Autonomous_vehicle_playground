import matplotlib.pyplot as plt

from vehicle import Vehicle
from simulation import Simulation



def main():

    # Create vehicle
    car = Vehicle()


    # Create simulator
    sim = Simulation(
        vehicle=car,
        dt=0.05,
        duration=20
    )


    # Run simulation
    sim.run(
        acceleration=0.5,
        steering=0.15
    )


    # Get data
    results = sim.get_results()


    # Plot trajectory
    plt.figure(figsize=(8,6))

    plt.plot(
        results["x"],
        results["y"],
        linewidth=3
    )

    plt.xlabel("X position (m)")
    plt.ylabel("Y position (m)")
    plt.title("Kinematic Bicycle Vehicle Trajectory")

    plt.axis("equal")
    plt.grid()

    plt.show()



if __name__ == "__main__":
    main()