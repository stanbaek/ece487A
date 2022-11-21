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


## 💻 Procedure

### OpenMV Cam

Go to https://openmv.io/pages/download to download the latest OpenMV IDE.  Install the software on your computer.

- Connect the camera to your computer and run the software. 
- Download `find_apriltags_3d_pose_4.py` from Teams.
- In OpenMV IDE, go to File > Open File and select `find_apriltags_3d_pose_4.py` to load.
- Click the Connect button on the bottom left of the IDE.  
- Click the Start button (green arrow).
- Click the `Serial Terminal` tab at the bottom of the window.
- Bring in blocks under the camera to detect them.


```{image} ./figures/DetectingBlock.png
:width: 350
:align: center
```

On Serial Terminal, you will find numbers similar to

`2,3,4.041906,-1.517668,-9.712036,181.984062,358.371687,224.128056,4,5.561428,1.540591,-9.330090,160.538206,354.057860,201.279116`

The descriptions of the data fields are as follows.
- Field 1: Number of AprilTags detected.
- Field 2: AprilTag ID
- Field 3: x value
- Field 4: y value
- Field 5: z value
- Field 6: Rx value
- Field 7: Ry value
- Field 8: Rz value
- Field 9: AprilTag ID
- Field 10: x value
- Field 11: y value
- Field 12: z value
- Field 13: Rx value
- Field 14: Ry value
- Field 15: Rz value
-    :
-    :

The values are based on large-sized AprilTags. So, the distances returned by the program must be scaled. For example, $z = -9.712$ m is incorrect, and it shoud probably be 11 cm. So, we need to find the scale factor and offset.  


### Least Sqaures Regression

We need to solve a least squares regression problem to find a linear equation that best fits the measured data. 
Let the measured data is given by 

$$ y = [-10, 4, 7, 21]$$

and the corresponding values are given by

$$ x = [0, 1, 2, 3]$$

The goal is to find $m$ and $c$ such that 

$$ y = mx + c $$ best approximates the linear relationship between $x$ and $y$.

Let's first plot the data

```Python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-10, 4, 7, 21])

plt.plot(x, y, 'o', markersize=10)
plt.grid('on')
plt.show()

```


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
