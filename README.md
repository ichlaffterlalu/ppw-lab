# Tutorials and Assignment Repository

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Table of Contents

Welcome to the code repository.
This repository hosts weekly tutorial codes and other, such as course-related
code snippets.

1. Weekly Exercises
    1. [Lab 1](lab_1/README.md) - Introduction to Git (on GitLab) & TDD (Test-Driven Development) with Django
    2. [Lab 2](lab_2/README.md) - Introduction to Django Framework
    3. [Lab 3](lab_instruction/lab_3/README.md) - Introduction to _Models_ Django and Heroku Database with TDD Discipline
    4. [Lab 4](#) - TBA
    5. [Lab 5](#) - TBA
    6. [Lab 6](#) - TBA
    7. [Lab 7](#) - TBA
    8. [Lab 8](#) - TBA
    9. [Lab 9](#) - TBA
    10. [Lab 10](#) - TBA
2. [Quickstart Guide](#tldr)
3. [Initial Setup](#initial-setup)
4. [Doing the Tutorial](#doing-the-tutorial)
5. [Pulling Updates From Upstream](#pulling-updates-from-upstream)
6. [Show Code Coverage in Gitlab](#show-code-coverage-in-gitlab)
7. [Grading Scheme & Demonstration](#grading-scheme-demonstration)


## TL;DR

After you work at [Lab 1](lab_1/README.md), make sure to link this repository to your Lab 1 Repository :

1. Add this repository link to your remote list as `upstream` (`git remote add upstream https://gitlab.com/PPW-2017/ppw-lab`)
2. Pull the latest update to check whether new tutorials have been updated (`git pull upstream master`)
3. Fix any merge conflict(s) that might arise (hopefully none)
    - Always choose latest commit from `upstream` when fixing merge
    conflict(s)
3. Do not forget to commit your merged `master` branch and push it
to your own `master` branch at GitLab repository
    - Use Git command: `git push origin master`

Working on a tutorial problem set (This instructions applied for 3rd tutorials and so on):

1. Pull any updates from `upstream`
2. Create new apps on Django Project based on your tutorials `python manage.py startapp lab_n` where **n** is turoial number. E.g. **lab_2**
3. Do the exercises as instructed in README.md file ([click this](lab_instruction/lab_3/README.md) to see this week Tutorials README.md)
4. Commit your work frequently
5. Write good commit message(s)
6. If your work is ready for grading: `git push origin master`

If you want to know the detailed explanation about each instructions above,
please read the following sections.


## Initial Setup

If you previously haven't worked on [Lab 1](lab_1/README.md) Tutorial

1. then Create a fork of this repository to your GitLab account, which
will create a copy of this repository under your own account. 
2. Open the forked repository page at
`https://gitlab.com/<YOURNAME>/ppw-lab` where `<YOURNAME>`
is your GitLab username.
3. Set the clone URL to HTTPS and copy the URL into clipboard.
4. Clone the repository into your local machine. Use Git command:
`git clone https://gitlab.com/<YOURNAME>/ppw-lab.git <PATH>`
where `<PATH>` is a path to a directory in your local machine.
5. Go to the directory where the cloned repository is located in your
local machine.
6. Add new remote called **upstream** that points to the original
GitLab repository. Use Git command: `git remote add upstream https://gitlab.com/PPW-2017/ppw-lab`
7. Tell your TA about your GitLab username and URL to your tutorial
repository so s/he can grade it later.
8. Ensure that your repository page has visibility level set to
**Internal** or **Public**. Check it in **Edit Project** menu at
your repository page.

If you did [Lab 1](lab_1/README.md) Tutorial

1. Add new remote called **upstream** that points to the original
GitLab repository. Use Git command: `git remote add upstream git remote add upstream https://gitlab.com/PPW-2017/ppw-lab`
3. Tell your TA about your GitLab username and URL to your tutorial
repository so s/he can grade it later.
4. Ensure that your repository page has visibility level set to
**Internal** or **Public**. Check it in **Edit Project** menu at
your repository page.

## Doing the Tutorial

1. Suppose that you want to work on Lab 2 problem set. Go to the
directory that containing Lab 2 README.md.
2. To ensure your work regarding Lab 2 problem is isolated from
your other attempts on other problems, create a new apps
specifically for working on Lab 2 problem. Use Python command:
`python manage.py startapp lab_2`
3. Read the README file carefully because It contains set of tasks and instructions that you can work on.
4. Do the tutorial.
5. Use `git add` or `git rm` to stage/unstage files that you want to
save into Git later.
6. Once you want to save your progress, commit your work to Git. Use
Git command: `git commit` A text editor will appear where you should
write a commit message. Please try to follow the guidelines written
in [this guide](http://chris.beams.io/posts/git-commit/) on how to
write a good commit message.
7. Repeat steps 4 - 6 until you finish the tutorial.
8. Once you are ready to submit your work or you want to save it to
your repository on GitLab, do a Git **push**. The Git command: 
`git push origin master`

## Pulling Updates From Upstream

If there are any updates from upstream, you can get the latest commits
and integrate it into your fork by using the following Git command:
`git pull upstream master`

Merge conflicts may arise since the repository is updated weekly and
may have overlapping changes with the `master` branch in your own
forked repository. If merge conflict happens, please always use latest
commit from `upstream`. Once you have resolved any merge conflicts and all commits from
upstream are merged succesfully to your own `master` branch, do not
forget to push it back to your own GitLab repository. Use Git command:
`git push origin master`

## Show Code Coverage in Gitlab

1. Go to Pipeline Settings (`Settings -> Pipelines`)
2. Go to section Coverage Settings (`Pipelines -> Test coverage parsing`)
3. Write this Regex (Regular Expression) in textbox `Test Coverage Parsing` 

    > TOTAL\s+\d+\s+\d+\s+(\d+)%

4. Now your pipelines page will show your Code Coverage

## Grading Scheme & Demonstration

Weekly tutorials contribute **20%** to the final grade of this course.
For each exercises, student can obtain grade ranging from **A (4)** to
**E (0)**. The grading scheme is as follows:

1. **A** if student completed **all checklists**
2. **B** if student completed **80% of checklist**
3. **C** if student completed **at least half of the checklist**
4. **D** if student completed **30% of checklist**
5. **E** if student skipped the tutorial by doing nothing, e.g.
    no signs of work to the tutorial in the repository

All students required to demonstrate their work to teaching assistant.
This demonstration mechanism applies for both students in Regular and
International classes:

1. Demonstrations should be done no later than the end of the
    lab session week. The time allocation for the demonstration can be
    adjusted to the availability of the Teaching Assistants. As long as
    the demonstration is still done before **your lab session**, students have the chance
    to achieve maximum score for the tutorial.
2. If the demonstration is done after **your lab session**, you have to demonstrate
 your work to your **lecturer** and your score won't reach maximum point eventhough you 
 **do all checklists**

### Happy Coding :)
