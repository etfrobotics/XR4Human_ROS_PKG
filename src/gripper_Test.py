import panda_api_ETF 
import rospy

if __name__ == '__main__':
    try:
        pandica = panda_api_ETF.robot_dealerNODE()
        
        
        
        pandica.grasp_client_variable(0.05,0.05)
        pandica.grasp_client(0.00,0.005,0.005,0.25,10)
    except rospy.ROSInterruptException:
        print("program interrupted before completion")
