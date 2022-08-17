# Spatial Math for Python

## Purpose
This lab assignment will introduce the spatialmath package that will be used throughout the semester to control robotic arms.

## Documentation
This lab has been adapted from the Spatial Math for Python Documentation https://petercorke.github.io/spatialmath-python/.  Refer to the follwing links for more details.

https://github.com/petercorke/spatialmath-python
https://petercorke.github.io/spatialmath-python/

## Deliverables
Create a folder named Lab1 in which you add exercise1.py, exercise2.py, and so on for the following exercises. 

**Submit your code to Bitbucket and provide the outputs in Gradescope.**

### Exercise 1
Using the ZYX Euler angles, find the rotation matrix $R_{ZYX}(\psi,\theta,\phi)$ for $\psi=45^\circ, \theta=60^\circ, \phi=45^\circ$.

(i) Use low-level spatial math functions to find $R_{ZYX}$ and the Euler angles from $R_{ZYX}$.

(ii) Use high-level spatial math functions to find $R_{ZYX}$ and the Euler angles from $R_{ZYX}$.

Did you get the same Euler angels, $\psi$, $\theta$, and $\phi$?  If not, explain why.  

### Exercise 2
Using the ZYX Euler angles, find the rotation matrix $R_{ZYX}(\psi,\theta,\phi)$ for $\psi=45^\circ, \theta=90^\circ, \phi=45^\circ$. 

(i) Use low-level spatial math functions to find $R_{ZYX}$ and the Euler angles from $R_{ZYX}$.

(ii) Use high-level spatial math functions to find $R_{ZYX}$ and the Euler angles from $R_{ZYX}$.

Did you get the same Euler angels, $\psi$, $\theta$, and $\phi$?  If not, explain why.  


### Exercise 3
Find $\phi$, $\theta$, and $\psi$ for YZY Euler angles, $R=R_Y(\phi)R_Z(\theta)R_Y(\psi)$, that generate the blue frame shown in figure below.  The blue frame has been rotated with respect to the blakc frame.  Use SE3.Rx, SE3.Ry and SE3.Rz.

```{image} ./figures/SpatialMath_Ex3.png
:width: 450
:align: center
```
<br>

Use the following code snippet.


```Python
from spatialmath.base import *
from spatialmath import *
import matplotlib.pyplot as plt

# add your code here.





print(T)
T.plot()
plotvol3([-2, 2, -2, 2, -2, 2], grid=True)
plt.show()

```