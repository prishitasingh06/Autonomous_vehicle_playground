# Phase4: Model Predictive Control

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


Phase 4.1 — MPC Optimization Problem
What are we trying to solve?

At every time step, MPC solves:

"What acceleration and steering commands will make the vehicle follow the path while driving smoothly?"

# MPC Optimization

## Components

### Prediction Model

Uses vehicle equations to predict future states.

### Optimization Variables

The controller chooses future:

- acceleration
- steering


### Cost Function

Minimize:

- distance from reference path
- steering effort
- acceleration effort


### Constraints

Vehicle limitations:

- steering angle limits
- acceleration limits