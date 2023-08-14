import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    robot_config = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_amcl.yaml')
    

    map_file = os.path.join(get_package_share_directory('sim_worlds2'),
            'maps',
            'sh.yaml')

    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'topic_name': "map"},
                        {'frame_id': "map"},
                        {'yaml_filename': map_file}]
        ),

        Node(
            namespace='robot',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[robot_config]
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': ['map_server', 'robot/amcl']}]
        ),

    ])