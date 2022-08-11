# ✏️ Software Configuration

## 📜 Agenda
- Create a Bitbucket repository.
- Configure git repository.
- Install and Configure PyCharm

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
:scale: 60%
:align: center
```
<br>

- Go to Teams > General > Files > Class Materials. Download the `PycharmProjects_XXXX` folder and copy everything into the `PycharmProject` folder in your home directory. Do not copy the `PycharmProjects_XXXX` folder itself into the `PycharmProject` folder.  The figure below shows an example of a local `PycharmProject` folder on your computer.


```{image} ./figures/PycharmProjectsFolder.png
:scale: 80%
:align: center
```

<br>

- Go back to Git Bash. If you have already closed it, right click on an empty space inside the `workspace` folder and select `Git Bash Here`.
- Type `git add -A` or `git add -all` and hit `Enter`.
- Type `git commit -m "Initial commit."` and hit `Enter`.
- Type `git push` as shown below
- Enter your username and password if prompted.

```{image} ./figures/GitPush.gif
:scale: 60%
:align: center
```

<br>

- In the future you will repeat these three steps when committing your changes:
    - git add -A
    - git commit -m "Comment"
    - git push

- Refresh your Bitbucket repository to observe the new files as shown below

```{image} ./figures/git10.PNG
:scale: 60%
:align: center
```
<br>

```{Attention}
After you push your assignments to Git, it is your responsibility to check your code has been successfully pushed to Bitbucket.
```



### Install PyCharm

- Download the latest version of [PyCharm Edu](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu) and install it on your computer.
- Ensure you have the installation optioned checked as shown below. 

```{image} ./figures/PyCharmInstallationOptions.png
:width: 460
:align: center
```
<br>

### PyCharm Configuration


```{Attention} 
It is your responsibility to check your files have been successfully pushed to your Bitbucket repository. Always visit your Bitbucket repository after you push your assignments to the repository.
```

## 🚚 Deliverables

Take screenshots of the following and submit them via Gradescope.  Use `Snip & Sketch` (Win+Shift+S) in Windows 10 or Shift+CMD+4 in Mac to take a screenshot. Save it in `png` or `jpg`.  

```{Warning}
Do NOT take a picture of a computer screen with your phone because it will introduce sampling aliasing (more details in ECE215/ECE315). 
```

- **[25 Points]** Provide a screenshot of your Bitbucket repository as shown below

<br>

- **[25 Points]** Go to Windows Settings > Apps.  Click on Code Composer Studio and take a screenshot as shown below.  For Mac users, it is in the Applications folder.


<br>

- **[-30 Points]** Take a picture of your screen with a mobile device or digital camera and submit it in Gradescope. Yes, I am serious...

```{Warning}
You will lose 30 points every time you submit a picture of a computer screen taken by your phone or mobile device. 
```





