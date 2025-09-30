from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_pubsub_demo',
            executable='publisher',
            name='publisher_node'
        ),
        Node(
            package='ros2_pubsub_demo',
            executable='processor',
            name='processor_node'
        )
    ])
