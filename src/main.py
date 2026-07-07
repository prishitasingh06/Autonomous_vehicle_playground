import matplotlib.pyplot as plt

from vehicle import Vehicle
from path import Path
from mpc_controller import MPCController
from mpc_simulation import MPCSimulation



def main():


    car = Vehicle(
        x=0,
        y=0,
        yaw=0,
        velocity=2
    )


    path = Path()


    controller = MPCController()


    simulation = MPCSimulation(
        car,
        controller,
        path
    )


    simulation.run(
        steps=100
    )


    plt.figure(figsize=(8,6))


    plt.plot(
        path.x,
        path.y,
        "--",
        label="Reference Path"
    )


    plt.plot(
        simulation.x_history,
        simulation.y_history,
        label="MPC Vehicle Path"
    )


    plt.xlabel("X position")
    plt.ylabel("Y position")

    plt.axis("equal")

    plt.grid()

    plt.legend()

    plt.show()



if __name__ == "__main__":
    main()