Széchenyi Istvány Egyetem -Autonóm járművek és robotok programozása (GKNB_AUTM078)- beadandó munka


Telepítés és build

Navigálj a ROS 2 workspace-be: cd ~/ros2_ws

Buildeld a csomagot: colcon build --packages-select var_fwt_randomalert

Forrásold a buildet: source install/setup.bash

Futtatás

A csomag launch fájljával egyszerre indíthatók a node-ok:

ros2 launch var_fwt_randomalert var_fwt_randomalert_launch.py


Alternatívaként külön terminálokban:

# Terminál 1
source install/setup.bash
ros2 run var_fwt_randomalert publisher

# Terminál 2
source install/setup.bash
ros2 run var_fwt_randomalert processor

Kimenet

A node-ok logja így néz ki:

[publisher-1] Publishing: "Hello ROS2 0"
[processor-2] Received: "Hello ROS2 0" | Processed: "HELLO ROS2 0"
[publisher-1] Publishing: "Hello ROS2 1"
[processor-2] Received: "Hello ROS2 1" | Processed: "HELLO ROS2 1"
...
