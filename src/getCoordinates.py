import panda_api_ETF 
import rospy



if __name__ == '__main__':
    try:
        pandica = panda_api_ETF.robot_dealerNODE()
        r = rospy.Rate(1)
        while True:
            print("Joint Pos")
            print(pandica.group.get_current_joint_values())
            print("Cart Pos")
            print(pandica.group.get_current_pose().pose)
            r.sleep()

    except rospy.ROSInterruptException:
        print("program interrupted before completion")

   
