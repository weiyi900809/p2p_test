import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from P2PNode import P2PNode


ID = "recv1"
node = P2PNode("123.240.196.78", 10001, ID)


# Do not forget to start it, it spins off a new thread!
node.start()

print('waiting 10 sec for connecting')


time.sleep(10)
print('Time to send message')
node.send_to_nodes('{"message": "hi from node recv"}') 
time.sleep(5)
# Gracefully stop the node.
node.stop()
