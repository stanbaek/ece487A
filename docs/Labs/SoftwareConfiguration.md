# ✔️ Preflight: Software Setup

## 📜 Agenda
- Create a Bitbucket repository.
- Configure git repository.
- Install and Configure PyCharm

:::{note}
Don’t worry if it doesn’t work right. If everything did, you’d be out of a job.
:::

## 💻 Procedure

### Create a Bitbucket Repository

- Create a <a href="https://bitbucket.org/" target="_blank">Bitbucket</a> account if you do not already have one.
- Create a new repository in Bitbucket as shown below.
- Name it ECE487\_LastName\_FirstName.
- Give your instructor read access: Click `Invite` on the top of the right-hand navigation and then click `Add members`. Provide your instructor **read access**. 
    - Dr. Baek: stanley.baek@afacademy.af.edu

```{image} ./figures/BitBucketConfig.gif
:scale: 60%
:align: center
```

```{Note}
Your repository name must be ECE487\_LastName\_FirstName. Otherwise, the instructor may not be able to find your repository.
```

- You may need to create a Bitbucket `app password` as shown below.
- Click `Your Profile` on the top of the right-hand navigation and then click `Personal Settings`. 
- Click `App Passwords` and then click `Create app password`. 
- Write your preferred label and select permissions as shown below.
- Click `Create`.
- Save the password as you cannot view it after you create it.

```{image} ./figures/BitBucketAppPassword.gif
:scale: 60%
:align: center
```

### Install Git

- Go to https://git-scm.com/download/win to download `64-bit Git for Windows setup`
- Install Git with the default settings. Git is already installed on Mac. 
- Create a folder named `PycharmProjects` under your home folder, e.g., C:\Users\stanley.baek\PycharmProjects. 
- Right-click the `PycharmProjects` folder and select `Git Bash Here` as shown below.   
- From your repository in Bitbucket, click Clone and copy the command that begins with _git clone_ by clicking on the copy button as shown below.  
- Paste it within the Bash terminal (middle-click, right-click > Paste, or `Shift+Ins` to paste) and add a space followed by a _period_ as shown below. The _period_ at the end means that the destination is the _current folder_. Hit Enter.
- If it asks for a password, enter the app password you saved in the previous step.
- Notice that you have `(master)` at the end of the folder name. If you type `ls`, it should return nothing.

```{image} ./figures/GitClone.gif
:width: 680
:align: center
```
<br>

- Go to Teams > General > Files > Class Materials. Download the `PycharmProjects_XXXX` folder and copy everything into the `PycharmProject` folder in your home directory. Do not copy the `PycharmProjects_XXXX` folder itself into the `PycharmProjects` folder.  The figure below shows an example of a local `PycharmProjects` folder on your computer.


```{image} ./figures/PycharmProjectsFolder.png
:width: 580
:align: center
```
<br>


### Install and Configure PyCharm

- Download the latest version of [PyCharm Edu](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu) and install it on your computer.
- Ensure you have the installation options checked as shown below. 

```{image} ./figures/PyCharmInstallationOptions.png
:width: 440
:align: center
```
<br>

- Start PyCharm and create a new project.
- Ensure the project location is `PycharmProjects` under your home folder, e.g., C:\Users\stanley.baek\PycharmProjects.
- The location of virtual environment should be `env` under `PycharmProjects`, e.g., C:\Users\stanley.baek\PycharmProjects\env.

```{image} ./figures/PycharmNewProject.gif
:width: 720
:align: center
```
<br>

- Open `Settings` under the `File` menu and browse to `Project: PycharmProjects` > `Python Interpreter`.
- Click `+` 
- Search for `numpy` and click `Install Package`.
- Install the following packages
    - `matplotlib`
    - `spatialmath-python`
    - `sympy`
    - `roboticstoolbox-python`
    - `opencv-python`
    - `serial`
    

```{image} ./figures/InstallNumpy.gif
:width: 720
:align: center
```
<br>

- Go back to Git Bash. If you have already closed it, right click on an empty space inside the `PycharmProjects` folder and select `Git Bash Here`.
- Type `git add -A` or `git add -all` and hit `Enter`.
- Type `git commit -m "Initial commit."` and hit `Enter`.
- Type `git push` as shown below
- Enter your username and password if prompted.


- In the future you will repeat these three steps when committing your changes:
    - git add -A
    - git commit -m "Comment"
    - git push

- Refresh your Bitbucket repository to observe the new files as shown below


```{image} ./figures/BitBucketPushed.png
:width: 640
:align: center
```
<br>

```{Attention} 
It is your responsibility to check your files have been successfully pushed to your Bitbucket repository. Always visit your Bitbucket repository after you push your assignments to the repository.
```

## 🚚 Deliverables

Take screenshots of the following and submit them via Gradescope.  Use `Snip & Sketch` (Win+Shift+S) in Windows 10 or Shift+CMD+4 in Mac to take a screenshot. Save it in `png` or `jpg`.  

```{Warning}
Take a picture of your screen with a mobile device or digital camera and upload it in
Gradescope to show that you have no idea what sampling aliasing (you learned it in ECE215) is and
you are not qualified for bachelor's degree in ECE. You will lose 30 points every time you submit a picture of a computer screen taken by your phone or mobile device. Yes, I am serious..., and it takes more time if you do.
```

### Deliverable 1
- Provide a screenshot of your Bitbucket repository as shown below 

```{image} ./figures/BitBucketPushed.png
:width: 640
:align: center
```
<br>

### Deliverable 2

- Take a screenshot of your PyCharm settings as shown below

```{image} ./figures/PyCharmSettings.png
:width: 640
:align: center
```
<br>







