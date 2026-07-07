import matplotlib.pyplot as plt

from vehicle import Vehicle
from path import Path
from mpc_controller import MPCController
from mpc_simulation import MPCSimulation


def main():

    # ==================================
    # 1. Create Vehicle
    # ==================================

    # Initial vehicle state:
    # x position = 0 m
    # y position = 0 m
    # yaw angle = 0 rad
    # velocity = 5 m/s

    car = Vehicle(
        x=0,
        y=0,
        yaw=0,
        velocity=5
    )


    # ==================================
    # 2. Create Reference Path
    # ==================================

    path = Path()


    # ==================================
    # 3. Create MPC Controller
    # ==================================

    controller = MPCController()


    # ==================================
    # 4. Create Closed Loop Simulation
    # ==================================

    simulation = MPCSimulation(
        car,
        controller,
        path
    )


    # ==================================
    # 5. Run Simulation
    # ==================================

    # dt = 0.1 seconds
    # 300 steps = 30 seconds simulation

    simulation.run(
        steps=300
    )


    # ==================================
    # 6. Plot Path Tracking
    # ==================================

    plt.figure(figsize=(8, 6))

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


    plt.xlabel("X position (m)")
    plt.ylabel("Y position (m)")

    plt.title(
        "MPC Path Tracking"
    )

    plt.axis("equal")

    plt.grid()

    plt.legend()

    plt.show()



    # ==================================
    # 7. Plot Vehicle Velocity
    # ==================================

    plt.figure(figsize=(8,4))


    plt.plot(
        simulation.velocity_history
    )


    plt.xlabel(
        "Time Step"
    )

    plt.ylabel(
        "Velocity (m/s)"
    )


    plt.title(
        "Vehicle Velocity"
    )


    plt.grid()

    plt.show()



    # ==================================
    # 8. Plot Steering Command
    # ==================================

    plt.figure(figsize=(8,4))


    plt.plot(
        simulation.steering_history
    )


    plt.xlabel(
        "Time Step"
    )


    plt.ylabel(
        "Steering Angle (rad)"
    )


    plt.title(
        "MPC Steering Command"
    )


    plt.grid()

    plt.show()



    # ==================================
    # 9. Plot Acceleration Command
    # ==================================

    plt.figure(figsize=(8,4))


    plt.plot(
        simulation.acceleration_history
    )


    plt.xlabel(
        "Time Step"
    )


    plt.ylabel(
        "Acceleration (m/s²)"
    )


    plt.title(
        "MPC Acceleration Command"
    )


    plt.grid()

    plt.show()



    # ==================================
    # 10. Plot Tracking Error
    # ==================================

    plt.figure(figsize=(8,4))


    plt.plot(
        simulation.error_history
    )


    plt.xlabel(
        "Time Step"
    )


    plt.ylabel(
        "Tracking Error (m)"
    )


    plt.title(
        "MPC Path Tracking Error"
    )


    plt.grid()

    plt.show()



    # ==================================
    # 11. Print Performance Results
    # ==================================

    average_error = sum(
        simulation.error_history
    ) / len(
        simulation.error_history
    )


    max_error = max(
        simulation.error_history
    )


    print("==============================")
    print("MPC Performance Results")
    print("==============================")

    print(
        f"Average Tracking Error: {average_error:.3f} m"
    )

    print(
        f"Maximum Tracking Error: {max_error:.3f} m"
    )

    print("==============================")



if __name__ == "__main__":
    main()