# control_gui

## Subscriber
`/detection_result/image`, `Image` (porposted) get the detection result and show in the GUI

## Update Blog
2022-3-8-22:50 rename `Pose.py` to `control_gui.py` and correct the Icon path by `rospkg`, integrate all the things into roslaunch file (commit by Hei)


## Usage guide
```
cd ~/catkin_ws/src
git clone https://github.com/Drone-FYP2021-PolyU-EIE/Control_UI.git

# Then, rename this Control_UI to control_gui manually

cd ..
catkin_make

roslaunch control_gui control_gui.launch
```

## Input of the Node
`/mavros/local_position/pose`, `PoseStamped` get the current position and quaternion of the drone

`/mavros/state`, `State` get the state of the drone


## Output of the Node
`/mavros/setpoint_position/local`, `PoseStamped` send the position

## Pose 
No.1 and 6 => Forward

No.2 and 3 => Left

No.4 and 7 => Right

N0.5 and 8 => Back

# Screenshoot  of software
![image](https://user-images.githubusercontent.com/45313904/158188202-9e412de5-2663-4d0c-8053-847f48f004c9.png)

