import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from P2PNode import P2PNode
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

ID = "connecter_1"
node = P2PNode("10.0.2.15", 8001, ID)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.
node.connect_with_node('123.240.196.78', 10001) 


# Send some message to the other nodes
node.send_to_nodes('{"message": "hi from node connecter_1"}') 


time.sleep(10)
# Gracefully stop the node.
node.stop()