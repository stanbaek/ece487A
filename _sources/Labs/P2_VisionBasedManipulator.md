# 🔬 Project2: Vision-Based Control

## 📌 Objectives

The purpose of this project is to control the robotic arm using computer vision.

In this project, you will  
- Use the OpenMV camera to detect, identify, and localize multiple AprilTags.
- Write a Python script to search for blocks and find the locations of the blocks using the AprilTags attached on them.
- Write a Python script for the robotic arm to move the blocks.

```{image} ./figures/AprilTagBlocks.jpg
:width: 500
:align: center
```

## 💻 Procedure


### Apriltag Localization

In this section, we need to find the location of an AprilTag using the OpenMV camera. Let $^C\mathbf{p}_{A}$ be the position of the AprilTag with repsect to the camera frame and $^B\mathbf{p}_{A}$ be the position of the AprilTag with repsect to the base frame. Note that the camera frame is attached to the camera lens.  Given the joint angles, $(\theta_1, \theta_2, \theta_3, \theta_4, \theta_5)$, we can find the tooltip pose with repect to the base frame, $^BT_{T}$, using the forward kinematics. Using the same method, we can also find the camera pose with respect to the base frame, $^BT_{C}$. 


```{image} ./figures/xArm_Cam.png
:width: 500
:align: center
```

Given the position of an AprilTag, $^C\mathbf{p}_{A} = \left({}^Cx_A, {}^Cy_A, {}^Cz_A\right)$, the joint angles of the robotic arm, $(\theta_1, \theta_2, \theta_3, \theta_4, \theta_5)$, the link lengths defined in [Project 1](P1:Procedure:InvKine), and the  camera offset distance ($d_s$ in the above figure), find  
$^B\mathbf{p}_{A} = \left({}^Bx_A, {}^By_A, {}^Bz_A \right)$. Include your mathematical derivation in the final report.  You can use ${}^1T_2$, ${}^2T_3$, etc., but it should be descriptive enough to seamlessly write in Python. 

### Search for Blocks

We need to search for blocks with AprilTags using the OpenMV cammera attached to the robotic arm. Use the following code snippet in the constructor (`def --init__(...)`) 

```Python
self.camera_dist_offset = 0.037  # L4 - camera_distance

self.mvcam = None
self.curr_joint_angles = None
        
# dictionary for block locations
# for short tutorial for Python dictionary, visit https://www.w3schools.com/python/python_dictionaries.asp
self.block_locations = dict()
```

The `Tag` class in `xarm.py` can be used to store AprilTag data.

```Python
class Tag(NamedTuple):
```

Use the following function to connect to your OpenMV camera.

```Python
def connect_mvcam(self):
```
            

```Python
    def search_for_blocks(self, duration_ms, pose, steps):
        """ Search for blocks with AprilTags.
        The robotic arm will be moved from the current pose to pose (argument) for duration_ms.
        During the transition from the current pose to the desired pose, the robot will stop moving to search
        for blocks. The number of stops during the transition is given by the steps argument.
        Once it finds a block, it will calculate the pose of the block wrt Frame 0 using the
        current joint angles and the position of the block wrt to the camera frame. Then, it will update
        self.block_locations with the pose of the block wrt Frame 0.
        If a block is detected multiple times, self.block_locations will be updated with the latest location.
        :param duration_ms: time in milliseconds to travel from the current
        position to the desired position.
        :param pose: 1x5 array of the pose of the tooltip.
        The first three elements are the position of the tooltip in meters,
        and the last two elements are the wrist angles in radians.
        :param steps: the number of stops during the transition
        :return: None

        Example:
        robot = XArm(simulation_only=False)
        robot.connect_mvcam()
        robot.connect()

        duration_ms = 2000
        steps = 20

        robot.move_to_initial_pose(duration_ms)
        pose = (0.12, -0.15, 0.12, -pi/4, 0)
        robot.search_for_blocks(duration_ms, pose, steps)
        """
        
        joint_angles = self.invkine(pose)

        if joint_angles is None:
            print("No solution to inverse kinematics for ", pose)
            return

        angle_step = (joint_angles[0, :] - self.curr_joint_angles)/steps
        dtime_ms = duration_ms//steps

        for i in range(steps):
            self.curr_joint_angles += angle_step
            self.move_joints(dtime_ms, self.curr_joint_angles, wait=True)

            # print(np.rad2deg(self.curr_joint_angles))
            data = self.mvcam.readline().decode('ascii').strip().split(',')

            if len(data) < 2:
                continue

            num_tags = int(data.pop(0))
            tags = list()
            for i in range(num_tags):
                tagid = int(data[4*i])
                x, y, z = map(float, data[4*i+1:4+4*i])

                """ Write your code to find the location of the block wrt the 
                inertial reference frame, Frame {0}
                """
                # Find the transformation matrix of Tool Frame wrt Frame 0
                # Hint: You need only one line of code here
                
                
                # Find the transformation matrix of the block wrt Frame 0
                # Hint: you need only one line of code (Look at Lab1)
                
                
                # Add the location (translation, or the x-,y-,z-coordinates) of the block.
                self.block_locations[tagid] = 0  # replace 0 with the location of the block.  
                
            # comment out the following line if you don't want to print    
            [print(key, ', ', self.block_locations[key]) for key in self.block_locations.keys()]

```


Complete the search_for_blocks function. Use the following code to test the function.

```Python
def test_search_for_blocks():

    # Set simulation_only=True to test the OpenMV cam.
    # Set it False to test the camera while the robot is moving.    
    robot = XArm(simulation_only=True)
    robot.connect_mvcam()
    robot.connect()

    duration_ms = 2000
    steps = 0  # pick a number for steps.

    robot.move_to_initial_pose(duration_ms)
    
    pose = (0, 0, 0, 0, 0)  # pick the start pose for searching 
    robot.moveto(duration_ms, pose, wait=True)

    pose = (0, 0, 0, 0, 0)  # pick the destination pose for searching
    robot.search_for_blocks(duration_ms, pose, steps)
    
    pose = (0, 0, 0, 0, 0) # pick the next destination pose for searching
    robot.search_for_blocks(duration_ms, pose, steps)
```

## 🚚 Deliverables

###  Deliverable 1 (20 points)

Your code should be able to find and identify the blocks placed at,
- (22, 0, 0)
- (30, 0, 0)
- (19, -10, 0)
- (26, -11, 0)
- (25, 18, 0)

**Report the console output printed by the following code inside `search_for_blocks`.**

`[print(key, ', ', self.block_locations[key]) for key in self.block_locations.keys()]`


### Deliverable 2 (40 points)
As you can find, the localization accuracy is sometimes very poor depending highly on where the block is located in the image frame. If the block is at the center of the image frame, it is usually pretty accurate. If the block is located at the corner or side of the image frame, it has a large error. How would you improve the accuracy? 

A few ideas that you may want to consider (not necessarily good ideas)
- Average out all the measurements
- Based on the locations you initially have, move the arm where a block can be located at the center of the image frame, and retake a measurement.

**Report the following in your final report**
- Implementation of your idea in xArm.py.  You can modify the `search_for_blocks` method or create your own method.
- Justification of the idea.
- Measurements.
- Analysis of your data.

In the real engineering world, there are always multiple solutions available. There is no right or wrong solution, but there are better solutions. I would like to see your ideas, implementation, justification, and analysis. 

### Deliverable 3 (20+ points)

**Demo (30 pts):** Search for a block with AprilTag ID 0 (let's call it Block 0) and Block 1, and place Block 0 on top of Block 1.

The blocks are placed anywhere near the five locations ($\pm 5$ cm) in Deliverable 1. 

**Demo (3 - 7 bonus pts):** Move multiple blocks (Blocks 0 - 3) on top of Block 4.
- 2 blocks: + 3 points
- 3 blocks: + 5 points
- 3 blocks: + 7 points



**You must use the inverse kinematics, not the forward kinematics with pre-calculated joint angles except the intial pose.** 

### Deliverable 4 (20 points)

**Submit final report.**

Your report should include the following sections or similar:

- Objective
- Methods
- Analysis and Results
- Conclusion 

There are no requirements for font size, page margins, number of pages, etc. Write a professional, senior-level report. 
Do not use _you_ in your report.  
Hint: I love figures and tables as long as they are legible.
