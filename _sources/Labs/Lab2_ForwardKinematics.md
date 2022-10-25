# 🔬 Lab2: Forward Kinematics


## Objectives
The purpose of this lab is to compare the theoretical solutions to the forward kinematics problem with a physical implementation on the 5 Dof robotic arm shown below.  

```{image} ./figures/xArm.jpg
:width: 350
:align: center
```

In this lab, you will  
- Parameterize the robotic arm following the Denavit-Hartenberg (DH) convention.
- Use Python to compute the forward kinematic equations for the robot.
- Write a Python script that moves the robot to the configurations specified by the user.



:::{note}
First, solve the problem. Then, write the code. – John Johnson
:::


## 💻 Procedure

## Danavit-Hartenberg of 5 DoF robotic arm

This is part of ICE5. Use the schematic diagram shown below to find the DH table of the robotic manipulator. 

```{image} ./figures/xArm.png
:width: 450
:align: center
```

```{attention}
Before starting this lab, check the solution to the DH table posted in Gradescope to ensure you have the correct answer. If the solution is not published in Gradescope, go through your table with the instructor.
```

### USB to Serial Connection

- Connect the provided USB cable to your computer.
- Connect the UART port to the robot controller board shown in the figure below.
- Note that the red wire (5 Vcc) is not connected to the board.

```{image} ./figures/USB-UART_connection.jpg
:width: 400
:align: center
```


### Python simulation for rothe botic arm

Download xArm.py from Teams and complete the constructor of XArm, which is a subclass of [DHRobot](https://petercorke.github.io/robotics-toolbox-python/intro.html#denavit-hartenberg-parameters).  You need to use your DH table to create a `DHRobot` object.  Since XArm is a subclass of `DHRobot`, you can use all the methods and properties defined in `DHRobot`, such as the `fkine` method. 



```Python
def __init__(self, simulation_only=False):

    self.B0 = 0.090
    self.L1 = 0.000     # self.L1 = 0.010 for inverse kinematics
    self.L2 = 0.105
    self.L3 = 0.088
    self.L4 = 0.170

    self.ordered_joints = ('base', 'shoulder', 'elbow', 'wpitch', 'wroll')

    super().__init__(
        [rbt.RevoluteMDH(d=self.B0),
         """
         write your code here
         """
         ],
        name="xArm"
    )
```

Find the forward kinematics and generate plots for the following configurations in xArm.py

```Python
def test_forward_kinematics():
    robot = XArm(simulation_only=True)

    q = list()
    q.append([0, pi/2, 0, 0, 0])  # rest position
    q.append([0, 0, 0, 0, 0])     # zero position
    q.append([0, pi/2, -pi/2, 0, 0])
    q.append([0, pi/2, pi/2, 0, 0])
    q.append([0, pi/2, 0, -pi/2, 0])
    q.append([0, pi/2, 0, pi/2, 0])
    q.append([0, pi/2, 0, 0, -pi/2])
    q.append([0, pi/2, 0, 0, pi/2])
    q.append([-pi/2, pi/2, -pi/2, 0, -pi/2])
    q.append([pi/2, pi/2, pi/2, 0, pi/2])
    
    for angles in q:
        """
        Write your code to find the forward kinematics and generate plots.
        Hints:
        - robot is an instance of XArm, which is a subclass of DHRobot. So you can use fkine.
        - use printline to print pose and angle. In Python Console, try
             from spatialmath import SE3
             help(SE3.printline)
          to get help on the printline function.
          
        Angles must be reported in degrees, not radians.
        """

```

**Deliverable 1**: Submit the pose (position and orientation) of the tooltip for each configuration. You don't have to submit the figures, but they will help verify your results. The angles must be in degrees.



```{caution}
Always set the robot to the upright position as shown below before you send the first command to the robot. 
```

```{image} ./figures/xArm_Upright.png
:width: 400
:align: center
```




### Physical Implementation of Forward Kinematics for Robotic Arm

- Carefully read the following functions inside xArm.py.
- You don't have to know how the following functions work, but you need to know what they do.
    - `get_servo_command()`: 
    - `servo_angles_to_positions()`: 
    - `send_command()`
- You should know how the following functions work and what they do.
    - `joint_to_servo_angles()`: 
    - `move_joints()`
    - `move_to_initial_pose()`

Comment out `test_forward_kinematics() ` inside `if __name__ == '__main__':`, which is located at the end of the code, and 
uncomment the next line.  

```Python
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)
        
    # test_forward_kinematics()     <--  COMMENT OUT
    test_servo_position_command()   <--  UNCOMMENT
    # test_servo_angle_command()
    # test_move_joints()
```

Carefully look at the joint angles for the corresponding servo positions.  

Comment out the first two test functions and uncomment the third line.  

```Python
    # test_forward_kinematics()       <--  COMMENT OUT
    # test_servo_position_command()   <--  COMMENT OUT
    test_servo_angle_command()        <--  UNCOMMENT
    # test_move_joints()
```

- Read `def test_servo_angle_command():` and complete the rest of the function.  Run the Python script to find the mathematical relationship between the servo angles ($\alpha_i$) and the joint angles ($\theta_i$). For example, $\alpha_2 = -\theta_2 + \pi/2$ because when $\theta_2 = 0$, $\alpha_2 = 90^\circ$ and when $\theta_2 = 90$, $\alpha_2 = 0^\circ$, 

```{hint}
You may want to put breakpoints in the code and execute one line at a time to observe the joint angles of the robot.
```

**Deliverable 2**: For each joint, report the mathematical equation for $\alpha_i$ in terms of $\theta_i$, where $i\in \{1,2,3,4,5\}$ is the joint index. Write the five equations on paper and submit it in Gradescope. You don't have to impletement the equations in Python.  

Comment out the first three test functions and uncomment the last line.  

```Python
if __name__ == '__main__':
    # test_forward_kinematics()         <--  COMMENT OUT
    # test_servo_position_command()   <--  COMMENT OUT
    # test_servo_angle_command()      <--  COMMENT OUT
    test_move_joints()                <--  UNCOMMENT
```

Use the results from Deliverable 2 to update the following two lines of code inside the constructor, ` def __init__(self, simulation_only=False):`

```Python
    # alpha = direction * theta + offset
    # where alpha is the servo angle and theta is the joint angle.
    self.joint_servo_offset = (0, 0, 0, 0, 0)
    self.joint_servo_direction = (1, 1, 1, 1, 1)
```

Read `def test_move_joints():` and complete the rest of the function.

**Deliverable 3**: Demo your robot moving the joints as described in the function.

Go to `def test_forward_kinematics():` and replace `True` with `False` in the following line.

```Python
   robot = XArm(simulation_only=True)  <-- change it to False
```    
    
Uncomment the first test function inside __name__ == '__main__': and comment out the rest.

```Python
if __name__ == '__main__':
    test_forward_kinematics()         <--  UNCOMMENT
    # test_servo_position_command()   <--  COMMENT OUT
    # test_servo_angle_command()      <--  COMMENT OUT
    # test_move_joints()              <--  COMMENT OUT
```

You need to add the `move_joints` function inside `test_forward_kinematics`.  Execute the code and use a ruler to measure the position of the tooltip. Compare the measured values with the calculated values.

**Deliverable 4**: Demo your robot moving the tooltip to the calculated position.
