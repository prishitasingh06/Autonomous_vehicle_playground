Phase 5.2 — Controller Node Communication Test

Objective:

Verify that the ROS 2 controller node receives the planned trajectory and publishes vehicle commands.

Verification:

Command:

ros2 topic list

Output:

/reference_path
/control_command

Command:

ros2 topic echo /control_command

Output:

data:
- 1.0
- 0.0

Interpretation:

The controller successfully publishes a control message:

First value → acceleration command
Second value → steering command

Current controller uses placeholder commands. Later this will be replaced with the MPC optimization output.