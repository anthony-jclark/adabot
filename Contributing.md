
<!-- https://github.com/Microsoft/vscode/wiki -->

TODO:

- Typical Github workflow (clone, fork, push, pull, pull-requests)
- Using issues and projects
- Contributing to the wiki
---
# **Typical Github Workflow**
[Github] is a code repository, where a team can collaborate on a body of code easily and efficiently. The following are good steps to follow when working on a Github repository.
## How to set up the repository on your computer.
- Once you have created your Github account navigate to the repository you wish to work on. In this case [adabot].

- On the top right of the main page, click the "Fork" button. This will give you your own separate copy of the repository you can do whatever you want to without worrying about messing up the original code base.

- To get your repository on your computer so you can start working on it click on the "Clone or download" button on the repository main page. This will give you a link you need to download the repository. Then in your command line enter `git clone <link you got above>`.

Now you have the repository on your local machine!

[Github]: https://github.com/
[adabot]: https://github.com/anthony-jclark/adabot
## Basic workflow
The basic idea of Github is that you make some changes to the code, `git add` the file to stage it for a `git commit`, then finally `git push` it to the online version of the code base. Then finally you will request a "Merge" to the original [adabot] repository and your changes become official! Here are the steps to do this.
#### Get the latest before you start working
- The first thing you do is set up a `branch`, this is a local copy of the code that you can change freely without changing the default `master` branch. From your repository folder use `git branch develop`. Then `git checkout develop`. You are now in your local develop branch! Use `git branch` to see all your branches and where you are now.

- You should always update your local repository before each time you start working so you get the latest changes form the original [adabot] repository.
1. Run `git remote add upstream <adabot Github link>`.
2. Run `git fetch upstream` then `git pull upstream master` while you are in your master branch.

- Now you have the latest version of the [adabot] repository in your master branch.
---

# **Contributing to the Wiki**
Keeping the wiki as up-to-date as possible is probably one of the most important tasks of anyone on this project. Documentation here will allow the future generations of students to more quickly get up to speed and make this research successful.
## Tools for contributing
- Atom - Githubs code editor. It is very handy as it supports the markdown syntax and even has a Preview feature activated with the shortcut *Ctrl+Shift+M* that gives you a live preview of your changes as you edit the .md files of the wiki. It also connects to the Github you're working in automatically and shows your branch and commit status on the bottom bar.


Add some notes about formatting:
- parameter names with two letter into
- element names are full names