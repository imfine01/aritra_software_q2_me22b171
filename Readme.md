# Aritra Question 2 by ME22B171
There are 3 parts in the repo - URDF_models, Vessel_ctrl_setup, media

# For Integration with RVIZ2:
1. With the requirements installed and urdf files downloaded, 
2. execute "ros2 launch urdf_tutorial display.launch.py model:=/pathtofile/kcs_model.urdf" to visualize in KCS dummy model in Rviz2
3. execute "ros2 launch urdf_tutorial display.launch.py model:=/pathtofile/otter_katamaran_model.urdf" to visualize in otter catamaran dummy model in Rviz2

# For ROS2 Control Setup:
1. With the requirements installed and vessel_ctrl_setup folder downloaded,
2. there are 2 nodes which can be called by "kcs_ctrl", "otter_ctrl"
3. watch the demo video of KCS control in /media
4. execute "ros2 run week_2 kcs" in terminal1
5. execute "ros2 run teleop_twist_keyboard teleop_twist_keyboard" terminal2
6. execute "ros2 run vessel_ctrl_setup kcs_ctrl" in terminal3
7. to see changes occuring, execute "ros2 topic echo /kcs/odom"*

* "ros2 topic list" showed /kcs/odom & not /kcs/kcs/odom so same will reflect in node file "/kcs/commands"
