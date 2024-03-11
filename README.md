# Autonomous Navigation Using Reinforcement Learning and Simulaneous Localization and Mapping (SLAM)

The primary objective is to enable the mobile rover to autonomously traverse through its surroundings, reaching a predetermined destination while adeptly avoiding obstacles, all without human intervention. 

The project adopts two key approaches to achieve this goal: Simultaneous Localization and Mapping (SLAM)-based navigation and Q-Learning algorithm which is a Reinforcement  Learning (RL) approach.

The performance of the robot on both approaches is subsequently assessed within the confines of the simulated environment (Gazebo) to gauge its effectiveness and efficiency.

View project [paper](https://drive.google.com/file/d/1_x7usDO6wIquJcFIdQVEo0Na8ZDFspDH/view)

## Highlights
- scripts
    - init_pose.py -> aligns both the static and physical map together
    - goal_pose.py -> moves robot to a specified pose
    - learning_node.py -> init node for learning process contains hyperparameters
    - Qlearning.py -> Q-Learning functions
    - Lidar.py -> process lidar message and perform discretization
    - scan_node.py -> init node for displaying lidar measurements and current state
- launch
    - turtlebot3_auto_nav -> launch robot without pre-saved map. Robot builds map as it moves through using SLAM


