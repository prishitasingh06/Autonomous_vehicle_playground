import matplotlib.pyplot as plt

from vehicle import Vehicle
from simulation import Simulation
from visualization import Visualizer



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


    visualizer = Visualizer()


    # Plot trajectory

    visualizer.ax.plot(
        sim.x_history,
        sim.y_history,
        "--",
        color="gray"
    )


    # Draw vehicle positions
    for i in range(0, len(sim.x_history), 20):

        car.x = sim.x_history[i]
        car.y = sim.y_history[i]
        car.yaw = sim.yaw_history[i]

        visualizer.draw_vehicle(car)

    plt.show()



if __name__ == "__main__":
    main()