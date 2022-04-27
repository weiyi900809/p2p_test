from re import A
import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode


from P2PNode import P2PNode



# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
ID_path1 = "path1"
ID_path2 = "path2"
node_path1 = P2PNode("123.240.196.78", 10002, ID_path1)
node_path2 = P2PNode("123.240.196.78", 10003, ID_path2)
# Do not forget to start it, it spins off a new thread!
node_path1.start()
node_path2.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.

print('waiting 30 sec for connection...')

'''if not node.connect_with_node('127.0.0.1', 10001) :
	print('connect failure')

# Send some message to the other nodes
if not node.send_to_nodes('{"message": "hi from node 2"}') : 
	print('send failure')

'''

time.sleep(30) # Replace this sleep with your main loop!

# Gracefully stop the node.
node_path1.stop()
node_path2.stop()