# Pre-course Python and GitHub Setup
Welcome to Oxford and the Energy Systems MSc Course.

This pre-course activity is intended as an introduction to Python, Git, and GitHub, to ensure you have the required software installed before the *Introduction to Python for Energy Systems Analysis* Skills Week course in week 3. This is for students with no prior experience in programming or GitHub. 

For those familiar with python, you may still find this a useful refresher - please at least check you have a working python environment before the course begins.

## Pre-Course Contents
- [Course Intro](#introduction-to-python-for-energy-systems-analysis)
- [Git and GitHub](#git-and-github)
- [Software Installation](#part-1---install-software)
- [GitHub Flow](#part-2---learn-the-github-flow)
- [GitHub Activity](#part-3---github-activity)


## Introduction to Python for Energy Systems Analysis
Python is a high-level, interpreted programming language that has become one of the most popular programming languages worldwide. Its clean, readable syntax and extensive ecosystem of libraries have made it the preferred choice across diverse fields including data science, artificial intelligence, web development, scientific research, finance, automation, and many others. Python's versatility, combined with its beginner-friendly nature and powerful capabilities, explains why it's used by everyone from students learning their first programming language to engineers at major tech companies.

### Why Python for Energy Systems?

Python excels for energy systems analysis for several key reasons:

- **Data Analysis**: powerful libraries such as Pandas and NumPy make it easy to import, clean, and analyze many and large datasets related to energy.
- **Visualization**: Create compelling graphs and interactive dashboards with matplotlib, seaborn, and plotly to communicate your findings
- **Scientific Computing**: Libraries like SciPy provide advanced mathematical functions for optimization and modeling
- **Machine Learning**: Use scikit-learn, PyTorch and TensorFlow for predictive modeling and AI applications in energy.
- **Open Source**: Free to use with a vast community contributing packages and resources


Python's versatility means the skills you learn will be applicable not just during your time at Oxford, but across the entire energy sector, from renewable energy research to grid optimization and policy analysis.


## Git and GitHub
Git is a **distributed Version Control System (VCS)**, which means it is a useful tool for easily tracking changes to your code, collaborating, and sharing. With Git you can track the changes you make to your project so you always have a record of what you’ve worked on and can easily revert back to an older version if need be. It also makes working with others easier—groups of people can work together on the same project and merge their changes into one final source!

GitHub is a way to use the same power of Git all online with an easy-to-use interface. It’s used across the software world and beyond to collaborate and maintain the history of projects.

GitHub is home to some of the most advanced technologies in the world. Whether you're visualizing data or building a new game, there's a whole community and set of tools on GitHub that can get you to the next step. The majority of python libraries we'll use later in the course are hosted on GitHub.

## Part 1 - Install Software

To make the most efficient use of our short time during skills week, it will be helpful for you to install the software we intend to use before the course. Follow the instructions below for your operating system.

### Miniforge
Python is typically installed through a package manager or distribution. Anaconda is a well-known Python distribution for data science. In this course, we will use Miniforge instead.

Miniforge is a minimal Python distribution that includes the Conda package manager. By default, it uses the conda-forge channel to access open-source Python packages.

Follow the instructions to install Miniforge for your operating system here:
- Windows: [Miniforge Windows Installation](https://github.com/conda-forge/miniforge?tab=readme-ov-file#windows)
- macOS: [Miniforge macOS installation](https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos-linux--wsl)

Note, for installation on MacOS, make sure the filename referred to in the curl or wget command matches the correct file in [this table](https://github.com/conda-forge/miniforge?tab=readme-ov-file#requirements-and-installers).
For example, the command to use to download the installer for MacOS with arm64 Apple Silicon is

```curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"```

You then run:

```bash Miniforge3-MacOSX-arm64.sh``` to install.

#### Verify installation
Open a new terminal on macOS, or the Miniforge Prompt on Windows (this should appear in the Start menu).

In the prompt window, type:
```
conda --version
python --version
```

You should see version numbers for both commands.

### Visual Studio Code

Visual Studio Code (VS Code) is a free, lightweight code editor with excellent Python support, debugging capabilities, and extensions.

**Installation Steps:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Download VS Code for your operating system
3. Install using the downloaded file:
   - **Windows**: Run the `.exe` installer
   - **macOS**: Drag VS Code to your Applications folder
4. Launch VS Code after installation

**Extensions:**
Once VS Code is installed, install these extensions to help with your python programming:
1. Open VS Code
2. Click the Extensions icon in the sidebar (or press `Ctrl+Shift+X`)
3. Search for and install:
   - **Python** (by Microsoft) - Python language support
   - **Jupyter** (by Microsoft) - Jupyter notebook support
   - **Ruff** (by Astral Software) - a python linter and formatter


### GitHub Desktop

GitHub Desktop provides a visual interface for Git and GitHub, making it easier to manage version control without command-line tools.

**Installation Steps:**
1. Visit [desktop.github.com](https://desktop.github.com/)
2. Download GitHub Desktop for your operating system
3. Install the application:
   - **Windows**: Run the installer
   - **macOS**: Drag to Applications folder
4. Launch GitHub Desktop and sign in with your GitHub account
   - If you don't have a GitHub account, create one at [github.com](https://github.com)

**Setup:**
1. Open GitHub Desktop
2. Go to File → Options (Windows) or GitHub Desktop → Preferences (macOS)
3. In the "Git" tab, enter your name and email address
4. These should match your GitHub account details


## Part 2 - Learn the GitHub flow 

To get you familiar with Git and GitHub, during the course, we will ask you to commit and push your completed activities to GitHub. The activity below provides an introduction to the GitHub flow to get you started. This tutorial is based on GitHub's own [Git and GitHub tutorial](https://github.com/classroom-resources/github-starter-course).

The GitHub flow is a lightweight workflow that allows you to experiment and collaborate on your projects easily, without the risk of losing your previous work.

#### Repositories

A repository is where your project work happens--think of it as your project folder. It contains all of your project’s files and revision history.  You can work within a repository alone or invite others to collaborate with you on those files.

#### Cloning 

When a repository is created with GitHub, it’s stored remotely in the ☁️. You can clone a repository to create a local copy on your computer and then use Git to sync the two. This makes it easier to fix issues, add or remove files, and push larger commits. You can also use the editing tool of your choice as opposed to the GitHub UI. Cloning a repository also pulls down all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project! This can be helpful if you experiment with your project and then realize you liked a previous version more. 
To learn more about cloning, read ["Cloning a Repository"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

#### Committing and pushing
**Committing** and **pushing** are how you can add the changes you made on your local machine to the remote repository in GitHub. That way your instructor and/or teammates can see your latest work when you’re ready to share it. You can make a commit when you have made changes to your project that you want to “checkpoint.” You can also add a helpful **commit message** to remind yourself or your teammates what work you did (e.g. “Added a README with information about our project”).

Once you have a commit or multiple commits that you’re ready to add to your repository, you can use the push command to add those changes to your remote repository. Committing and pushing may feel new at first, but we promise you’ll get used to it.

### 💻 GitHub terms to know 

#### Repositories 
We mentioned repositories already, they are where your project work happens, but let’s talk a bit more about the details of them! As you work more on GitHub you will have many repositories which may feel confusing at first. Fortunately, your ["GitHub dashboard"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard) helps to easily navigate to your repositories and see useful information about them. Make sure you’re logged in to see it!

Repositories also contain **READMEs**. You can add a README file to tell other people why your project is useful, what they can do with it, and how to use it. We are using this README to communicate how to learn Git and GitHub. 
To learn more about repositories read ["Creating, Cloning, and Archiving Repositories](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) and ["About README's"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes). 

#### Branches
You can use branches on GitHub to isolate work that you do not want merged into your final project just yet. Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. Typically, you might create a new branch from the default branch of your repository—main. This makes a new working copy of your repository for you to experiment with. Once your new changes have been reviewed by a teammate, or you are satisfied with them, you can merge your changes into the default branch of your repository.
To learn more about branching, read ["About Branches"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

#### Forks
A fork is another way to copy a repository, but is usually used when you want to contribute to someone else’s project. Forking a repository allows you to freely experiment with changes without affecting the original project and is very popular when contributing to open source software projects!
To learn more about forking, read ["Fork a repo"](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

#### Pull requests
When working with branches, you can use a pull request to tell others about the changes you want to make and ask for their feedback. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. You can add specific people as reviewers of your pull request which shows you want their feedback on your changes! Once a pull request is ready-to-go, it can be merged into your main branch.
To learn more about pull requests, read ["About Pull Requests"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). 


#### Issues
Issues are a way to track enhancements, tasks, or bugs for your work on GitHub. Issues are a great way to keep track of all the tasks you want to work on for your project and let others know what you plan to work on. You can also use issues to tell a favorite open source project about a bug you found or a feature you think would be great to add!

For larger projects, you can keep track of many issues on a project board. GitHub Projects help you organize and prioritize your work; see [About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). You likely won’t need a project board for your assignments, but they can be useful for organizing team work.
You can also link together pull requests and issues to show that a fix is in progress and to automatically close the issue when someone merges the pull request.
To learn more about issues and linking them to your pull requests, read ["About Issues"](https://docs.github.com/en/github/managing-your-work-on-github/about-issues). 

#### Your user profile

Your profile page tells people the story of your work through the repositories you're interested in, the contributions you've made, and the conversations you've had. You can also give the world a unique view into who you are with your profile README. You can use your profile to let future employers know all about you! 
To learn more about your user profile and adding and updating your profile README, read ["Managing Your Profile README"](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme). 

#### Using Markdown on GitHub

You might have noticed already, but you can add styling to your issues, pull requests, and files. [Markdown](https://guides.github.com/features/mastering-markdown/) is an easy way to style them using simple syntax. This can help organize information and make it easier for others to read. You can also add GIFs and images to help convey a point!
To learn more about using GitHub’s flavor of markdown, read ["Basic Writing and Formatting Syntax"](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax). 



## Part 3 - GitHub Activity

In this activity, you'll get hands-on experience with GitHub, GitHub Desktop, and Python. You'll learn how to clone a repository, create and edit files, commit changes, and run your first Python script. These are essential skills for collaborating and sharing code in any programming or data science project and will ensure you are well prepared for the Introduction to Python for Energy Analysis Course during skills week.

### Step-by-Step Instructions

1. **Create a repository from this template**
   - Click the "Use this template" button at the top right of this page. This will create a new repository in your GitHub account with the same contents as this one, without copying its commit history.
2. **Clone the repository to your computer**
   - Ensure you are viewing the version of this repository that is in your GitHub account (not the original template).
   - Click the green `<> Code` button near the top right.
   - Select `Open with GitHub Desktop`. This will launch the GitHub Desktop app.
   - Choose a location on your computer to save the repository (e.g., `Documents/GitHub/{repo name}`) and click `Clone`.

3. **Create a new Python file on GitHub**
   - In your web browser, on the GitHub website for this repository, click `Add file` > `Create new file`.
   - Name the file `hello.py` (case-sensitive).
   - In the file editor, type the following code:
     ```python
     print("Hello World")
     ```
   - Scroll down and click `Commit new file` to save your changes to the main branch.

4. **Sync your local repository with GitHub**
   - Open GitHub Desktop. You may notice that `hello.py` does not appear in your local folder yet.
   - Click the `Pull origin` button in GitHub Desktop. This downloads the latest changes from GitHub to your computer.
   - Check your local repository folder (using Finder or File Explorer). You should now see `hello.py`.

5. **Edit the Python file locally in Visual Studio Code**
   - Open Visual Studio Code.
   - Go to `File > Open Folder` and select your local repository folder.
   - In the VS Code file explorer, click on `hello.py` to open it.
   - Change the code to:
     ```python
     print("Hello Oxford")
     ```
   - Save the file (`File > Save` or `Ctrl+S`/`Cmd+S`).

6. **Run your Python script in VS Code**
   - With `hello.py` open, click the `Run` button at the top (the play symbol ▶️).
   - If prompted, select your Python interpreter (it should be labelled something like: `Python 3.12.X (base) ~/miniforge3/bin/python`).
   - Look at the terminal at the bottom of the screen. You should see:
     ```
     Hello Oxford
     ```

7. **Commit and push your changes back to GitHub**
   - Go to GitHub Desktop. You should see a change detected in `hello.py`.
   - In the bottom left, write a short summary for your commit (e.g., `Update hello.py to print 'Hello Oxford'`).
   - Click `Commit to main`.
   - Click `Push origin` to upload your changes to GitHub.

8. **Check your changes on GitHub**
   - Go back to the GitHub website for your repository.
   - Click on `hello.py` and confirm it now prints `Hello Oxford`.

---

**Congratulations!**

You have:
- Cloned a repository from GitHub
- Created and edited a Python file both online and locally
- Synced changes between your computer and GitHub
- Run your first Python script in VS Code
- Committed and pushed changes using GitHub Desktop


## GitHub Resources
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)


## Author
Copyright 2026 University of Oxford. All Rights Reserved.
The authors, being Dr Scot Wheeler, have asserted their moral rights.
This work is openly licensed via CC BY 4.0. 
