import casadi as ca


class MPCController:

    def __init__(self):

        # MPC parameters
        self.N = 15
        self.dt = 0.1
        self.L = 2.5

        # Target speed
        self.target_speed = 5.0


    def solve(self, state, reference):

        opti = ca.Opti()

        # States: x, y, yaw, velocity
        X = opti.variable(4, self.N + 1)

        x = X[0, :]
        y = X[1, :]
        yaw = X[2, :]
        v = X[3, :]


        # Controls: steering, acceleration
        U = opti.variable(2, self.N)

        steering = U[0, :]
        acceleration = U[1, :]


        # Initial condition
        opti.subject_to(
            X[:, 0] == state
        )


        # Vehicle model
        for k in range(self.N):

            x_next = (
                x[k]
                + v[k] * ca.cos(yaw[k]) * self.dt
            )

            y_next = (
                y[k]
                + v[k] * ca.sin(yaw[k]) * self.dt
            )

            yaw_next = (
                yaw[k]
                + (v[k] / self.L)
                * ca.tan(steering[k])
                * self.dt
            )

            v_next = (
                v[k]
                + acceleration[k] * self.dt
            )

            opti.subject_to(
                X[:, k + 1]
                ==
                ca.vertcat(
                    x_next,
                    y_next,
                    yaw_next,
                    v_next
                )
            )


        # Cost function
        cost = 0

        target_x = reference[0]
        target_y = reference[1]


        for k in range(self.N):

            # Position tracking
            position_error = (
                (x[k] - target_x)**2
                +
                (y[k] - target_y)**2
            )

            # Maintain target speed
            speed_error = (
                v[k] - self.target_speed
            )**2

            # Smooth controls
            control_cost = (
                0.05 * steering[k]**2
                +
                0.05 * acceleration[k]**2
            )

            cost += (
                position_error
                + 0.2 * speed_error
                + control_cost
            )


        opti.minimize(cost)


        # Steering limits (radians)
        opti.subject_to(
            steering <= 0.5
        )

        opti.subject_to(
            steering >= -0.5
        )


        # Acceleration limits
        opti.subject_to(
            acceleration <= 2.0
        )

        opti.subject_to(
            acceleration >= -2.0
        )


        # Velocity limits
        opti.subject_to(
            v >= 0
        )

        opti.subject_to(
            v <= 10
        )


        # Solver
        opti.solver(
            "ipopt",
            {
                "ipopt.max_iter": 50,
                "ipopt.print_level": 0,
                "print_time": False
            }
        )


        try:
            solution = opti.solve()

            # Return [steering, acceleration]
            control = solution.value(U[:, 0])

        except Exception:
            control = [
                0.0,
                0.0
            ]


        return control
