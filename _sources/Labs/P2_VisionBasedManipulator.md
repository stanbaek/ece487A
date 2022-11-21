# 🔬 P2: Vision-Based Control


## Objectives

The purpose of this project is to control the robotic arm using computer vision.

In this project, you will  
- Use OpenMV camera to detect, identify, and localize multiple AprilTags.
- Write a Python script to search for blocks and find the locations of the blocks using the AprilTags attached on them.
- Write a Python script for the robotic arm to move the blocks.

```{image} ./figures/AprilTagBlocks.jpg
:width: 500
:align: center
```



### Least Sqaures Regression

We need to solve a least squares regression problem to find a linear equation that best fits the measured data. 
Let the measured data is given by 

$$ y = [-10, 4, 7, 21]$$

and the corresponding values are given by

$$ x = [0, 1, 2, 3]$$


Let's first plot the data



### Deliverable 1 (25 points)

- Complete the code inside the `invkine` method. 
- In your `invkine()`, you must check the operating ranges of joint angles and should not return solutions that violate the operating ranges. Ensure you have the following two lines inside the constructor of XArm (`def __init__(...)`) and use the `check_joint_angle_limits` method to check the ranges before returning from `invkine()`.

``` 
self.max_joint_angle = (pi/2, pi, pi/4, pi/2, pi/2)
self.min_joint_angle = (-pi/2, 0, -3*pi/4, -pi/2, -pi/2)
```

- Demo `test_inverse_kinematics( )` with `simulation_only=False`.  Although it is not required, it is strongly recommended to run `test_inverse_kinematics( )` with `simulation_only=True` to observe the simulation outputs. 


<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/C3O-E2JJ3Qo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br>





### Deliverable 2 (25 points)

Write a Python script that moves a cube located at (25, 0, 0) to (20, 16, 0) and demo your robot moving the cube.  You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles. You must lift the block no less than 10 cm before placing it down. You may be asked to move the cube from a different location. 


### Deliverable 3 (50 points)

Write a Python script that moves a stack of five cubes located at (23, -15, 0) to (23, 15, 0) and demo your robot moving the cubes.  You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles.  You may be asked to move the cube from a different location.
