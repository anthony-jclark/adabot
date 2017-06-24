## Useful Documentation and Tutorials

- [Programming for Robotics - ROS](http://www.rsl.ethz.ch/education-students/lectures/ros.html)
- [ROS Package Template](https://github.com/ethz-asl/ros_best_practices/tree/master/ros_package_template)
- [Example ROS Robot](https://github.com/carlosjoserg/rrbot)
- [[Overview] Getting Starting with Autonomous Robots in ROS via Simulations](http://moorerobots.com/blog/post/6)
- [ROS Documentation](http://wiki.ros.org/)
- [Gazebo Tutorials](http://gazebosim.org/tutorials)


https://github.com/qboticslabs/mastering_ros

- Working with the `rrbot_gazebo` launch file.
- Fixing the file hierarchy (workspace doesn't belong in repo)

## Other Tips

- Never edit files in */opt/ros/...*
- Always use version control
    + Don't check in binaries
    + Don't check in generated files (use .gitignore, etc.)
- Leverage 3rd party libraries
- Use ROS Overlays for managing ROS versions
    + Install `rosws`
    + `rosws init ~/fuerte /opt/ros/fuerte/`
    + `source ~/fuerte/setup.zsh`
    + [More Info Here](http://robohow.eu/_media/meetings/first-integration-workshop/ros-best-practices.pdf)
    + [ROS Official Documentation Here](http://wiki.ros.org/catkin/Tutorials/workspace_overlaying)
- You can use an IDE (e.g., Eclipse) to develop and build ROS code



- https://askubuntu.com/questions/816540/how-do-you-install-hub-git-wrapper-on-ubuntu-with-autocomplete-and-man-documen
- http://stackoverflow.com/questions/24987542/is-there-a-link-to-github-for-downloading-a-file-in-the-latest-release-of-a-repo
- http://www.growingwiththeweb.com/2016/07/enabling-pull-requests-on-github-wikis.html


- creating videos
    + add camera
    + save to jpgs
    + convert with ffmpeg