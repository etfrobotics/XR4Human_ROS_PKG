
# XR4Human ROS Package

This repository provides a comprehensive ROS 1 Noetic package tailored for the XR4Human project. It integrates the Franka Emika Panda robot with MoveIt! for motion planning, facilitates Unity-ROS communication via `ros_tcp_endpoint`, and supports advanced functionalities for human-robot interaction in extended reality (XR) environments.

---

## 🚀 Prerequisites

Ensure your system meets the following requirements:

- **Operating System**: Ubuntu 20.04 LTS (Focal Fossa)
- **ROS Distribution**: ROS Noetic Ninjemys
- **Robot Hardware**: Franka Emika Panda

---

## 🛠️ Installation

### 1. Install ROS Noetic

Follow the official ROS Noetic installation guide for Ubuntu 20.04:

```bash
sudo apt update
sudo apt install curl gnupg2 lsb-release
curl -sSL http://packages.ros.org/ros.key | sudo apt-key add -
echo "deb [arch=amd64] http://packages.ros.org/ros/ubuntu $(lsb_release -c | awk '{print $2}') main" | sudo tee /etc/apt/sources.list.d/ros-latest.list
sudo apt update
sudo apt install ros-noetic-desktop-full
```

Initialize rosdep:

```bash
sudo rosdep init
rosdep update
```

Set up the ROS environment:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 2. Install Franka ROS Interface

Install the Franka ROS interface:

```bash
sudo apt install ros-noetic-franka-ros
```

For detailed setup instructions, refer to the [Franka ROS Interface documentation](https://projects.saifsidhik.page/franka_ros_interface/instructions.html).

### 3. Install MoveIt! for ROS Noetic

Install MoveIt!:

```bash
sudo apt install ros-noetic-moveit
```

For more information, visit the [MoveIt! installation guide](https://moveit.ai/install/).

### 4. Install Panda MoveIt! Configuration

Clone the `panda_moveit_config` repository:

```bash
cd ~/catkin_ws/src
git clone https://github.com/moveit/panda_moveit_config.git
cd ..
catkin_make
source devel/setup.bash
```

For setup assistance, refer to the [MoveIt! Setup Assistant tutorial](https://moveit.picknik.ai/main/doc/examples/setup_assistant/setup_assistant_tutorial.html).

### 5. Install Unity-ROS Communication via `ros_tcp_endpoint`

Clone the `ros_tcp_endpoint` repository:

```bash
cd ~/catkin_ws/src
git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git
cd ..
catkin_make
source devel/setup.bash
```

For detailed instructions, visit the [ROS-TCP-Endpoint GitHub repository](https://github.com/Unity-Technologies/ROS-TCP-Endpoint).

---

## 📦 Usage


### 1. Launch MoveIt! with Panda Configuration

In another terminal:

```bash
roslaunch panda_moveit_config franka_control.launch robot_ip:=<robot_ip> load_gripper:=true
```

### 2. Start Unity-ROS Communication

In a new terminal:

```bash
roslaunch ros_tcp_endpoint endpoint.launch tcp_ip:=<ros_host>
```

Ensure that Unity is configured to connect to the ROS endpoint.

### 3. Start xr4human_ros_pkg

In a new terminal:

```bash
rosrun XR4Humna_ROS_PKG robot_rack_picking.py
```


---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For support or inquiries, please contact [knezevic@etf.rs](mailto:knezevics@etf.rs).
