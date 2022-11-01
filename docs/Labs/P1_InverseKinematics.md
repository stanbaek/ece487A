# 🔬 Project1: Inverse Kinematics


## Project1 is not ready

## Objectives
The purpose of this project is to compare the theoretical solution to the inverse kinematics with a physical implementation on the 5 DoF robotic arm shown below.  

```{image} ./figures/xArm.jpg
:width: 300
:align: center
```

## 💻 Procedure

### Inverse kinematics of 5 DoF robotic arm

Use the schematic diagram shown in the figure below to find the forward kinematics of the robotic manipulator. 

```{image} ./figures/xArm2.png
:width: 450
:align: center
```


Add the following methods at the end of `class XArm(rbt.DHRobot)` right before "End of Class Xarm"


```Python
        self.gripper_close_pos = 2200   # close position
        self.gripper_open_pos = 1700  # open position
        self.plot_axes_limits = [-0.38, 0.38, -0.38, 0.38, 0, 0.47]
        
```


Use Python to create an instance of the robotic arm. You need to use your DH table to create a `DHRobot` object.  Since XArm is a subclass of `DHRobot`, you can use all the methods and properties defined in `DHRobot`, such as `fkine`.   

**Note:** Frame {5} is attached at the tooltip because of a bug in robotics-toolbox.  It cannot plot the last link correctly if we use `robot.tool = SE3([0, 0, L4])`

Use the following values for B0, L1, L2, L3, and L4. 

```Python
def __init__(self, simulation_only=False):

    self.B0 = 0.090
    self.L1 = 0.010  # <-- Ensure L1 is 0.01.
    self.L2 = 0.105
    self.L3 = 0.088
    self.L4 = 0.174

```



### Deliverable 1 (25 points)

Demo `test_inverse_kinematics( )` with `simulation_only=False`

In your `invkine()`, you must check the operating ranges of joint angles and should not return solutions that violate the oerating ranges. You can add the following two lines inside your constructor (`def __init__(...)`) and create a function that checks the ranges before returning from `invkine()`.

``` 
self.max_joint_angle = (pi/2, pi, pi/4, pi/2, pi/2)
self.min_joint_angle = (-pi/2, 0, -3*pi/4, -pi/2, -pi/2)
```


### Deliverable 2 (25 points)

Write a Python script that moves a cube located at (25, 0, 0) to (20, 16, 0) and demo your robot moving the cube.  You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles.  You may be asked to move the cube from a difference location. 






### Deliverable 3 (50 points)

Write a Python script that moves a stack of five cubes located at (23, -15, 0) to (23, 15, 0) and demo your robot moving the cubes.  You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles.  You may be asked to move the cube from a difference location. 