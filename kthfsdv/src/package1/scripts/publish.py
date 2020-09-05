import rospy
from std_msgs.msg import String

TOPIC_NAME = 'obeng'
NODE_NAME = 'package1'
INCR = 4 

def publisher():
    pub = rospy.Publisher(TOPIC_NAME, String, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(20)
    num = 0 #    num is k

    while  (num > 0 and not rospy.is_shutdown()):
        rospy.loginfo("k at %s is %d", rospy.get_time(), num)
        pub.publish(num)
        rate.sleep()
        num =  num + INCR 
        
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
