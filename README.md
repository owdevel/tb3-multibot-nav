# tb3-multibot-nav

A rudimentary naive solution to running multiple navigation stacks within ROS for the TurtleBot3. There are probably better ways to do this, if you know a better way to implement, please let me know.

The implementation copies the files from the turtlebot3 packages when they needed to be edited. Files changes were kept as minimal as possible except for when needing to pass parameters down through the multiple include chains.

## Installation
Requires
- All packages required to run the [Turtlebot3 Simulation by ROBOTIS](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)
- Clone into catkin workspace src directory

## Usage
1. Ensure the workspace is made with `catkin_make` and `source ./devel/setup.bash`
2. Launch Gazebo simulation with `roslaunch tb3-multibot-nav gazebo.launch`
3. Launch the Multiple Navigation Nodes with `roslaunch tb3-multibot-nav multinav.launch`
4. Send goal poses to individual bots with `rosrun tb3-multibot-nav SendGoal.py <Bot Index> <X> <Y> <Angle>`