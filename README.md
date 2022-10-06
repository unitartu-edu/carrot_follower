# carrot_follower
A package that makes the robot consecutively visit detected blobs.

Created for course "ROSi algkursus" (ROS for Beginners) <https://sisu.ut.ee/rosak>.

Completed with the support by IT Acadamy Programme of Education and Youth Board of Estonia.

## To use the package:

Add it into your catkin_ws/src directory along with the following package:

<https://github.com/ut-ims-robotics/opencv_apps/>

## To run the code:

Build and source the catkin workspace.

Then run the `carrot_follower.py` file using ROS.

## To visualize what the robot can see:

In your catkin workspace:

`rviz -d src/carrot_follower/config/watch_carrots.rviz`
