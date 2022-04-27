import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from P2PNode import P2PNode



node = P2PNode("10.0.2.15", 8001, 1)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.
if not node.connect_with_node('123.240.196.78', 8002) :
	print('connect failure')
	node.stop()

else :
	print('connect successfull')

# Send some message to the other nodes
node.send_to_nodes('{"message": "hi from node 1"}') 



# Gracefully stop the node.
node.stop()