# ✏️ HW 1 Setting up Bitbucket

## 📜 Agenda
- Create a Bitbucket repository.
- Configure git repository.

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

- Go to Teams > General > Files > Class Materials. Download the `PycharmProjects_XXXX` folder and copy everything into the `PycharmProject` folder in your home directory. Do not copy the `PycharmProjects_XXXX` folder itself into the `PycharmProject` folder.  The figure below shows an example of a local `workspace` folder on your computer.


```{image} ./figures/git6.PNG
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



### Install Code Composer Studio (CCS).

- Go to https://www.ti.com/tool/download/CCSTUDIO/11.2.0.00007 to download `Windows on-demand installer for CCS IDE`. For Mac users, download `macOS on-demand installer for CCS IDE`.  Do not download version 12 since it was recently released and there will be multiple patches next few months.   
- Run the installer by double clicking the `ccs_setup_11.X.X.X.exe` executable.
- Begin the installation process, by default it will ask you to install under a `ti` folder, which is recommended.
- Select `Custom Installation` (Recommended)
- Select the processor support for `SimpleLink MSP432 MCUs`.
- Ensure the default Install debug probe is selected and leave the rest unselected.
- Click Next until installation begins.
- Click Finish and your installation should proceed to completion.

```{image} ./figures/CCS_Setup.gif
:scale: 50%
:align: center
```
<br>

### Import Project Files.

- Open CCS.
- When asked to `Select a directory as workspace`, select `Browse` and browse to your `workspace` folder. Select the `Use this as the default and do not ask again` check box. Click `Launch`   
- Import all the projects into CSS. **File > Import...**  Choose **Code Composer Studio > CCS Projects** and click `Next`.
- Select `Search Directory` and click the `Browse...` option. Browse to the `workspace` folder.
- CCS should discover many projects inside the `workspace`.  Click `Select All` (**DO NOT** check `Automatically import...` or `Copy projects...` options). This will have CCS reference the project from the original location and preserve the original directory structure required to build. Click `Finish`.
- In Project Explorer, expand `HW01_Git` and double click test.txt to open. Edit the file and save.
- Commit and push to Bitbucket. Enter your password if prompted.
- Refresh your Bitbucket repository to observe the changes. 


```{image} ./figures/CCS_Config.gif
:scale: 50%
:align: center
```

<br>

```{Attention} 
It is your responsibility to check your files have been successfully pushed to your Bitbucket repository. Always visit your Bitbucket repository after you push your assignments to the repository.
```

## 🚚 Deliverables

Take screenshots of the following and submit them via Gradescope.  Use `Snip & Sketch` (Win+Shift+S) in Windows 10 or Shift+CMD+4 in Mac to take a screenshot. Save it in `png` or `jpg`.  

```{Warning}
Do NOT take a picture of a computer screen with your phone because it will introduce sampling aliasing (more details in ECE215/ECE315). 
```

- **[25 Points]** Provide a screenshot of your Bitbucket repository as shown below

```{image} ./figures/install11.PNG
:scale: 75%
:align: center
```

<br>

- **[25 Points]** Go to Windows Settings > Apps.  Click on Code Composer Studio and take a screenshot as shown below.  For Mac users, it is in the Applications folder.

```{image} ./figures/install12.PNG
:scale: 50%
:align: center
```

<br>

- **[-30 Points]** Take a picture of your screen with a mobile device or digital camera and submit it in Gradescope. Yes, I am serious...

```{Warning}
You will lose 30 points every time you submit a picture of a computer screen taken by your phone or mobile device. 
```




