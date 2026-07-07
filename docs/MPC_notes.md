# Model Predictive Control

## Objective

Develop an optimization-based controller for autonomous vehicle path tracking.

## Difference from Pure Pursuit

Pure Pursuit:
- geometric controller
- reacts to current error


MPC:
- predicts future vehicle behavior
- optimizes future inputs


## MPC Loop

1. Measure vehicle state
2. Predict future states
3. Optimize control inputs
4. Apply first input
5. Repeat


## State

x = position
y = position
yaw = heading
v = velocity


## Control

a = acceleration
delta = steering angle