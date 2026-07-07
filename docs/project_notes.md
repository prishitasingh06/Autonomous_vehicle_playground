Autonomous Vehicle Simulator
1. Project Objective

Develop a simplified autonomous vehicle simulation environment that can later be used to test:

Vehicle controllers
Path planning algorithms
Model Predictive Control (MPC)
Autonomous driving algorithms

The simulator will act as a virtual vehicle before deploying algorithms on real hardware.

2. Why Do We Need a Vehicle Simulator?

In autonomous driving, we need to test algorithms safely.
Real vehicle testing is:expensive, dangerous and time-consuming
A simulator allows us to test:

steering controllers
speed controllers
navigation algorithms

before using a real car.

Example:

Controller
     |
     ↓
Vehicle Simulator
     |
     ↓
Vehicle Response

3. Vehicle Modeling

A real vehicle is complicated:

A real car contains:

engine/motor
transmission
tires
suspension
steering system
sensors

For our first model, we simplify the vehicle.

We use:

Kinematic Bicycle Model

A four-wheel vehicle is represented as:

        Front wheel

            |
            |
            ●


            ●

        Rear wheel

Instead of modeling four wheels, we model:

one front wheel
one rear wheel

This captures steering behavior while keeping the math simple.

4. Vehicle State

A vehicle needs a way to describe its current condition.

We define the state:

X=
	x
    y
    θ
    v
	​
	​


Where:

Variable	Meaning	Unit
x	position in x direction	meters
y	position in y direction	meters
θ	vehicle heading angle	radians
v	vehicle velocity	m/s

Example:

x = 10 m
y = 5 m
θ = 30°
v = 15 m/s

means:

"The vehicle is located at (10,5), facing 30 degrees, moving at 15 m/s."

5. Control Inputs

The vehicle receives commands:

U=[
a
δ
	​

]

where:

Input	Meaning
a	acceleration
δ	steering angle

Example:

Acceleration = 1 m/s²

Steering = 10 degrees

The simulator calculates how the car moves.

6. Vehicle Update Loop

The simulator runs repeatedly:

Start

 ↓

Read vehicle state

 ↓

Apply control input

 ↓

Calculate new position

 ↓

Update vehicle state

 ↓

Repeat

This happens every timestep.

Example:

dt = 0.05 seconds

means:

"We update the vehicle 20 times per second."

7. Code Architecture

Our software is separated into modules:

src/

vehicle.py
    |
    |-- Vehicle physics model


simulation.py
    |
    |-- Runs time loop


main.py
    |
    |-- Starts simulation
    |-- Creates plots

cmd: python3 main.py  