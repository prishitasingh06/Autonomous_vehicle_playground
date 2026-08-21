# Vehicle Dynamics Simulator

A Python-based vehicle dynamics simulator developed as part of a personal autonomous driving and robotics project.

Hi!

Dear reader, thanks for being here! Whether you are browsing out of curiosity or digging into the project, I appreciate the visit.

## A little bit about how this project started 
This project grew out of two experiences that came together for me: studying
control systems at the University of Waterloo and working in the automotive
industry during my co-ops at Ford.
I started building this as a way to explore autonomous vehicles beyond just reading about them. During my co-ops at Ford, I got the opportunity to see firsthand how much engineering goes into modern vehicles and became increasingly interested in autonomous driving, vehicle dynamics, and the software and
controls behind these systems.

This Spring 2026, I took ECE 380 at the University of Waterloo, where I learned about control systems, including feedback, system dynamics, stability, and controller design. I wanted to take those concepts beyond the classroom and actually see them come to life in a vehicle simulation.




Working around automotive engineering gave me a much better appreciation for
the gap between a theoretical model and a system that has to operate reliably
in the real world. Vehicle behavior is affected by sensor noise, latency,
uncertainty, actuator limitations, changing environments, and many other
factors that are easy to overlook when working with an ideal simulation.

At the same time, ECE 380 at Waterloo gave me the control-system foundation to
understand these problems mathematically. Concepts such as feedback,
stability, system dynamics, and controller design made me want to build my
own environment where I could experiment with these ideas.

This project is where those interests came together.

I started with a simple kinematic bicycle model and gradually built toward a
more complete autonomous-vehicle simulation environment with trajectory
tracking, PID control, MPC, visualization, metrics, and ROS 2 integration.

My goal is not to recreate a production autonomous-driving stack. Instead, I
want this project to be a space where I can understand the underlying
engineering, experiment with different approaches, and explore what happens
when autonomous systems move beyond ideal conditions.

The next direction I'm exploring is sensor noise, failures, system telemetry,
and AI/ML-based anomaly detection, essentially asking:

> **Can an autonomous system recognize that something is going wrong before
> it actually fails?**

This project is a work in progress, and I'm using it as a space to learn,
experiment, break things, and hopefully build some interesting ideas along the
way.

Thanks for stopping by! 🚗

## Features

- Kinematic bicycle model
- Modular project architecture
- Vehicle state simulation
- Trajectory visualization

## Technologies

- Python
- NumPy
- Matplotlib
- Git

## Roadmap

- [x] Vehicle dynamics model
- [x] Simulation loop
- [x] Trajectory visualization
- [x] Vehicle animation
- [x] PID controller
- [x] Path following
- [x] Model Predictive Control (MPC)
- [x] ROS 2 integration