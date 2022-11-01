# 🔬 Project1: Inverse Kinematics


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

Use Python to create an instance of the robotic arm. You need to use your DH table to create a `DHRobot` object.  Since XArm is a subclass of `DHRobot`, you can use all the methods and properties defined in `DHRobot`, such as `fkine`.   

**Note:** Frame {5} is attached at the tooltip because of a bug in robotics-toolbox.  It cannot plot the last link correctly if we use `robot.tool = SE3([0, 0, L4])`

Use the following values for B0, L1, L2, L3, and L4. 

```Python
def __init__(self, simulation_only=False):

    self.B0 = 0.090
    self.L1 = 0.010
    self.L2 = 0.105
    self.L3 = 0.088
    self.L4 = 0.174

    super().__init__(
        [rbt.RevoluteMDH(d=self.B0),
         """
         write your code here
         """
         ],
        name="xArm"
    )
    
    # Do not use 
    # self.tool = SE3([...]) 
    # The built-in plot method won't be able to plot Link 4.
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

Add the following lines in your constructor
```
        self.gripper_close_pos = 2200   # close position
        self.gripper_open_pos = 1700  # open position
        self.plot_axes_limits = [-0.38, 0.38, -0.38, 0.38, 0, 0.47]
        
```

Add the following methods inside `class XArm(rbt.DHRobot)`.  You can use them as needed.  

```
    def moveto(self, duration_ms, pose, wait=True, plot=False):
        """ Moves the tooltip to the specified pose.
        :param duration_ms: time in milliseconds to travel from the current
        position to the desired position.
        :param pose: 1x5 array of the pose of the tooltip.
        The first three elements are the position of the tooltip,
        and the last two elements are the wrist angles.
        :param wait: If true, sleep for duration_ms until the move is complete.
        :param plot: If true, plot the robot.
        :return: None
        """

        joint_angles = self.invkine(pose)

        if joint_angles is None:
            print("No solution to inverse kinematics for ", pose)
        else:
            self.move_joints(duration_ms, joint_angles[0, :], wait=wait)
            if plot:
                self.plot(joint_angles, limits=self.plot_axes_limits, block=True)

    def open_gripper(self, duration_ms, wait=True):
        self.move_gripper(duration_ms, self.gripper_open_pos, wait)

    def close_gripper(self, duration_ms, wait=True):
        self.move_gripper(duration_ms, self.gripper_close_pos, wait)

    def move_gripper(self, duration_ms, position, wait=True):

        packet = bytearray(XArm.HEADER)
        num_bytes = 5 + 3  # byte length + CMD + num_servos + time duration (2) + servo positions
        packet.append(num_bytes)
        packet.append(XArm.COMMAND)
        packet.append(1)    # only one servo
        packet.append(duration_ms & 0xff)
        packet.append((duration_ms >> 8) & 0xff)
        packet.append(6)  # servo 6: gripper
        packet.append(position & 0xff)
        packet.append((position >> 8) & 0xff)

        self.send_command(packet)
        if wait:
            sleep(duration_ms/1000)
```

### Deliverable 3 (50 points)

Write a Python script that moves a stack of five cubes located at (23, -15, 0) to (23, 15, 0) and demo your robot moving the cubes.  You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles.  You may be asked to move the cube from a difference location. 