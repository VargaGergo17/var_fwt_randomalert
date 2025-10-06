from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='var_fwt_randomalert',
            executable='publisher',
            name='publisher_node'
        ),
        Node(
            package='var_fwt_randomalert',
            executable='processor',
            name='processor_node'
        )
    ])
