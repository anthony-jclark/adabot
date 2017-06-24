
Before running any commands, the ROS environment needs to be setup. You should run the following command the first time that you need to use ROS:

- General version: `source /opt/ros/{version}/setup.{bash|zsh}`
- What I use: `source /opt/ros/kinetic/setup.zsh`

To have this command run whenever you start your shell, you can run the following command (you only need to do this once):

- General version: `echo "source /opt/ros/kinetic/setup.{bash|zsh}" >> ~/.{bash|zsh}rc`
- What I use: `echo "source /opt/ros/kinetic/setup.zsh" >> ~/.zshrc`

If you are using `bash` or `zsh` it will also be useful to take advantage of the catkin-tools extended verbs:

`source $(catkin locate --shell-verbs)`

### Initial Workspace Setup from the adabot Repository

In general it is a good idea to keep your workspace separate from your git repository (based on "ROS Best Practices"). The main reason to do this is if you'd like to use a cloned package in multiple workspaces. Thus, a good series of commands for getting started on adabot are:


To checkout a specific branch of the repository you can use the following in place of the second command above:

`git clone https://github.com/anthony-jclark/adabot.git -b branch_name`

Once you have your workspace in this configuration, you need to update the ROS environmental variables with your package information. To do this you can source the new configuration file:

- General version: `source <path-to-workspace>/devel/setup.{bash|zsh}`
- What I use: `source devel/setup.zsh`

If adabot is the only ROS package that you will be working on, then you can add this to your shell configuration file as well.

`echo "source ~/ros_workspaces/adabot_ws/devel/setup.zsh" >> ~/.zshrc`

<!-- source $(catkin locate --shell-verbs) -->

### Checking and Cleaning the Workspace

You can check your catkin workspace setup with the following command (see the [catkin-tools documentation](http://catkin-tools.readthedocs.io/en/latest/verbs/catkin_config.html) for more information):

`catkin config`

You can list information about the packages in the current workspace with:

`catkin list`

For a more detailed check of package configurations (analyzes package.xml and CMakeLists.txt files) use:

`catkin lint`

If you run into trouble or something gets mixed up you can clean the directory with `clean`. This will delete the *devel* and *build* folder, but it will not touch the *src* folder.

`catkin clean`

### Building the Workspace

To build all packages in the workspace you can run the following command:

`catkin build`

To build a specific package (and its dependencies) use the following:

`catkin build <package-name>`

After you build it is generally a good idea to rerun the source command for the workspace:

`source devel/setup.zsh`

To build packages in release mode you need to change profiles before building:

```
catkin profile set release
catkin build
```

Or you can do this with one line:

`catkin build --profile release`

### Running Tests

To run all tests for the workspace use the following:

`catkin run_tests`

- Unit testing
- ROStest
- ROSlaunch Check
- build.ros.org?
- roslint


### Creating a New adabot Package

To create a new package, use the following command in the `~/ros_workspaces/adabot_ws/src/adabot/` directory:

`catkin create pkg PKG_NAME -l "MIT" -a "YOUR_NAME" "YOUR_EMAIL" -d "DESCRIPTION" --catkin-deps DEPENDENCIES`

for which you will need to supply the name of the package, your name and email address, as well as a brief description of the package. Here is an example:

`catkin create pkg adabot_control -l "MIT" -a "Anthony J. Clark" "anthonyjclark@gmail.com" -d "Controllers for the adabot's wheel motors and linear servo motors." --catkin-deps ros_control ros_controllers`

### Other Commands

- rosinstall_generator
- wstool
- vcstool
- rosdep update






## Creating Robot Model

1. Write Xacro/URDF
    + `rosrun xacro xacro --inorder model.xacro > model.urdf`
    + `check_urdf model.urdf`
    + `urdf_to_graphiz model.urdf`
    + `evince test_robot.pdf`
5. Viewing with RViz
    + create launch file
    + create rviz config file
    + `roslaunch <package> <launch-script>`

