import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode


from P2PNode import P2PNode


import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from P2PNode import P2PNode


ID_path1 = "connecter2"
node = P2PNode("10.0.2.15", 8002, ID_path1)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.
if  node.connect_with_node('123.240.196.78', 10002) :
	print('connect successfull')

else :
	
	print('connect failure')
	node.stop()

# Send some message to the other nodes
node.send_to_nodes('{"message": "hi from node 1"}') 



# Gracefully stop the node.
node.stop()