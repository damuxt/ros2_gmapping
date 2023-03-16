# ros2_gmapping
适配ROS2的gmapping实现。

本项目参考了https://github.com/Project-MANAS/slam_gmapping

特此感谢！原型项目基于ROS1的slam_mapping做了ROS2适配，可以在ROS2下实现机器人建图，其基本功能运行正常，但是在使用过程中也发现一些小问题，比如：参数并未动态化处理、地图更新频率设置存在BUG。当前项目便针对上述问题做了优化处理。

### 使用流程如下：

#### 1.编译

资源下载后，在工作空间下调用如下指令进行编译：

```
colcon build --packages-select openslam_gmapping slam_gmapping
```

#### 2.修改配置文件

配置文件为ros2_gmapping/slam_gmapping/params/slam_gmapping.yaml，该文件中参数众多，对于初学或只是想快速上手gmapping的同学，建议结合自己的机器人，主要修改如下参数：

* base_frame：机器人的基坐标系；
* map_frame：地图坐标系；
* odom_frame：里程计坐标系；
* use_sim_time：是否使用模拟时钟，仿真环境下设置为true，否则设置为false。

配置文件修改完毕后，重新构建。

#### 3.执行

执行步骤如下：

* 启动机器人，需要保证可以发布odom与scan数据；

* 执行launch文件，指令如下：

  ```
  ros2 launch slam_gmapping slam_gmapping.launch.py
  ```

* 启动rviz2，并在rviz2中添加TF、map等插件；

* 启动键盘控制节点，控制机器人运动，如无异常，便可实现slam建图了。



