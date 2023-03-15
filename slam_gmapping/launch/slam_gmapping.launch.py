from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
import launch.actions
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    return LaunchDescription([
        launch_ros.actions.Node(
            package='slam_gmapping', 
            executable='slam_gmapping', 
            output='screen', 
            parameters=[os.path.join(get_package_share_directory("slam_gmapping"), "params", "slam_gmapping.yaml")]),
    ])
