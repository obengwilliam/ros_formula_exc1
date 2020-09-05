import rospy
from std_msgs.msg import String

TOPIC_NAME = 'obeng'
NODE_NAME = 'package1'
DENO = 0.5 

def callback(data):
    pub = rospy.Publisher(TOPIC_NAME, String, queue_size=10)
    k = data.data 
    result = k/DENO
    pub.publish(result)

def subscriber():

    rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(20)

    rospy.Subscriber(TOPIC_NAME, String, callback)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
