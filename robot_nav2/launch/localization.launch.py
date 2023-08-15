import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    robot_config = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_amcl.yaml')
    

    map_file = os.path.join(get_package_share_directory('sim_worlds2'),
            'maps',
            'akskR3.yaml')

    return LaunchDescription([

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'velodyne', 'cloud']
        ),


        Node(
            package='pointcloud_to_laserscan',
            namespace='',
            executable='pointcloud_to_laserscan_node',
            name='pointcloud_to_laserscan',
            remappings=[('cloud_in', '/lio_sam/mapping/cloud_registered'),
                         ('scan', '/scan')],
            parameters=[{
                'target_frame': 'cloud',
                'transform_tolerance': 0.01,
                'min_height': 0.0,
                'max_height': 6.0,
                'angle_min': -1.5708,  # -M_PI/2
                'angle_max': 1.5708,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 20.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            output='screen'
        ),

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
            namespace='',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[robot_config]
        ),

        # Node(
        #     package='nav2_lifecycle_manager',
        #     executable='lifecycle_manager',
        #     name='lifecycle_manager_localization',
        #     output='screen',
        #     parameters=[{'use_sim_time': True},
        #                 {'autostart': True},
        #                 {'bond_timeout': 0.0},
        #                 {'node_names': ['map_server', 'amcl', 'pointcloud_to_laserscan']}]
        # ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': ['map_server', 'amcl']}]
        ),

    ])