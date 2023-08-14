import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    
    default_nav_to_pose_bt_xml_robot = os.path.join(get_package_share_directory(
    'robot_nav2'), 'config', 'robot_behavior.xml')
    controller_yaml_robot = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_controller.yaml')
    bt_navigator_yaml_robot = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_bt_navigator.yaml')
    planner_yaml_robot = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_planner_server.yaml')
    recovery_yaml_robot = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_recovery.yaml')

    waypoints_yaml_robot = os.path.join(get_package_share_directory(
        'robot_nav2'), 'config', 'robot_waypoint_follower.yaml')

    return LaunchDescription([

        # Nodes for robot

        Node(
            namespace='robot',
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_yaml_robot]),

        Node(
            namespace='robot',
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_yaml_robot]),

        Node(
            namespace='robot',
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            parameters=[recovery_yaml_robot],
            output='screen'),

        Node(
            namespace='robot',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_yaml_robot, {"default_nav_to_pose_bt_xml": default_nav_to_pose_bt_xml_robot}]),

        Node(
            namespace='robot',
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            parameters=[waypoints_yaml_robot]),        


        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='robot_lifecycle_manager_pathplanner',
            output='screen',
            parameters=[{'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': [
                            'robot/planner_server',
                            'robot/controller_server',
                            'robot/behavior_server',
                            'robot/bt_navigator',
                            'robot/waypoint_follower'
                        ]}]),

        # Node(
        #     namespace='robot',
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     arguments=['-d', robot_rviz_config_dir],
        #     parameters=[{'use_sim_time': use_sim_time}],
        #     output='screen'),
    ])