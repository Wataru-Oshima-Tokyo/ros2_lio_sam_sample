sudo apt update &&
sudo apt install python3-colcon-common-extensions ros-humble-ros2-control \
ros-humble-ros2-controllers &&
cd gtsam && mkdir build && cd build && cmake .. && make && sudo make install
##the below one is for ubuntu 20.04 
#sudo add-apt-repository ppa:borglab/gtsam-release-4.0 &&
#sudo apt update &&
#sudo apt install libgtsam-dev libgtsam-unstable-dev &&
sudo snap install cloudcompare 
