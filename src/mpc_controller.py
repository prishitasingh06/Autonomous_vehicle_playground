import casadi as ca
import config


class MPCController:

    def __init__(self):
        # Load MPC parameters from config
        self.N = config.PREDICTION_HORIZON
        self.dt = config.TIME_STEP
        self.L = config.WHEELBASE

        # Tracking weights
        self.Qx = config.Q_X
        self.Qy = config.Q_Y
        self.Qyaw = config.Q_YAW
        self.Qv = config.Q_SPEED

        # Control weights
        self.Rdelta = config.R_STEERING
        self.Ra = config.R_ACCELERATION

        # Terminal weight and target speed
        self.Qf = config.Q_TERMINAL
        self.target_speed = config.TARGET_SPEED


    def solve(self, state, reference):

        # Create optimization problem
        opti = ca.Opti()

        # Decision variables: states and controls
        X = opti.variable(4, self.N + 1)
        U = opti.variable(2, self.N)

        x, y, yaw, v = X[0,:], X[1,:], X[2,:], X[3,:]
        acceleration, steering = U[0,:], U[1,:]

        # Set initial vehicle state
        opti.subject_to(X[:,0] == state)

        # Predict future states using the bicycle model
        for k in range(self.N):

            x_next = x[k] + v[k] * ca.cos(yaw[k]) * self.dt
            y_next = y[k] + v[k] * ca.sin(yaw[k]) * self.dt
            yaw_next = yaw[k] + (v[k] / self.L) * ca.tan(steering[k]) * self.dt
            v_next = v[k] + acceleration[k] * self.dt

            opti.subject_to(
                X[:,k+1] == ca.vertcat(x_next, y_next, yaw_next, v_next)
            )

        # Build MPC cost function
        cost = 0

        for k in range(self.N):

            # Penalize tracking error
            cost += self.Qx * (x[k] - reference[0])**2
            cost += self.Qy * (y[k] - reference[1])**2

            # Penalize heading and speed error
            cost += self.Qyaw * yaw[k]**2
            cost += self.Qv * (v[k] - self.target_speed)**2

            # Penalize control effort
            cost += self.Rdelta * steering[k]**2
            cost += self.Ra * acceleration[k]**2

            # Penalize steering changes
            if k > 0:
                cost += config.STEERING_SMOOTHNESS * (steering[k] - steering[k-1])**2

        # Penalize final tracking error
        cost += self.Qf * ((x[self.N] - reference[0])**2 + (y[self.N] - reference[1])**2)

        opti.minimize(cost)

        # Apply steering and acceleration limits
        opti.subject_to(steering <= config.MAX_STEERING)
        opti.subject_to(steering >= -config.MAX_STEERING)
        opti.subject_to(acceleration <= config.MAX_ACCELERATION)
        opti.subject_to(acceleration >= config.MIN_ACCELERATION)

        # Solve optimization problem
        opti.solver("ipopt")
        solution = opti.solve()

        # Return first optimal control input
        return solution.value(U[:,0])