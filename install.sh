sudo apt update &&
sudo apt install snapd python3-colcon-common-extensions ros-foxy-ros2-control \
ros-foxy-ros2-controllers && \
##the below one is for ubuntu 20.04 
sudo add-apt-repository ppa:borglab/gtsam-release-4.0 &&
sudo apt update &&
sudo apt install libgtsam-dev libgtsam-unstable-dev &&
sudo snap install cloudcompare 
