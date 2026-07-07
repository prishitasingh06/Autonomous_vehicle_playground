import matplotlib.pyplot as plt

from vehicle import Vehicle
from simulation import Simulation
from visualization import Visualizer

from path import Path
from controller import PurePursuitController



def main():

    car = Vehicle(
        x=0,
        y=0,
        velocity=2
    )


    path = Path()


    controller = PurePursuitController()


    sim = Simulation(
        car,
        dt=0.05,
        duration=25
    )


    steps = int(sim.duration/sim.dt)


    for i in range(steps):

        steering = controller.compute_steering(
            car,
            path
        )


        car.update(
            acceleration=0,
            steering=steering,
            dt=sim.dt
        )


        sim.x_history.append(car.x)
        sim.y_history.append(car.y)
        sim.yaw_history.append(car.yaw)
        sim.velocity_history.append(car.velocity)



    visualizer = Visualizer()


    # Desired path

    px, py = path.get_points()

    visualizer.ax.plot(
        px,
        py,
        "--",
        label="Reference Path"
    )


    # Vehicle trajectory

    visualizer.ax.plot(
        sim.x_history,
        sim.y_history,
        color="blue",
        label="Vehicle Path"
    )


    visualizer.ax.legend()

    plt.show()



if __name__ == "__main__":
    main()