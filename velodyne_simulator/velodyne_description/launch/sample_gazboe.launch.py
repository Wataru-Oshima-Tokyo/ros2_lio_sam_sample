import os
import launch
import launch_ros.actions
from launch_ros.actions import Node


def generate_launch_description():
    # Define the Gazebo environment variables
    my_env = os.environ.copy()
    my_env["QT_QPA_PLATFORM"] = "offscreen"  # Ensure that no Qt windows are created

    # The Gazebo command with the '--headless' flag
    gazebo = launch.actions.ExecuteProcess(
        cmd=['gazebo', '--headless', '-s', 'libgazebo_ros_factory.so'],
        env=my_env,
        output='both'
    )

    return launch.LaunchDescription([
        gazebo
        # Node(
        #     package='demo_nodes_cpp',
        #     executable='talker',
        #     name='talker',
        #     output='screen'
        # )
        # Add other nodes, actions, event handlers if necessary
    ])
