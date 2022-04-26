import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from p2pnetwork.node import Node

class MyOwnPeer2PeerNode (Node):

    # Python class constructor
	def __init__(self, host, port, id=None, callback=None, max_connections=0):
		super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)
		print("MyPeer2PeerNode: Started")
	def node_message(self, node, data):
        	print("node_message (" + self.id + ") from " + node.id + ": " + str(data))    	
    

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.
'''
	def outbound_node_connected(self, node):
		print("outbound_node_connected (" + self.id + "): " + node.id)
		
	def inbound_node_connected(self, node):
		print("inbound_node_connected: (" + self.id + "): " + node.id)

	def inbound_node_disconnected(self, node):
		print("inbound_node_disconnected: (" + self.id + "): " + node.id)

	def outbound_node_disconnected(self, node):
		print("outbound_node_disconnected: (" + self.id + "): " + node.id)
	
	    
   
	def node_disconnect_with_outbound_node(self, node):
		print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)
		
	def node_request_to_stop(self):
		print("node is requested to stop (" + self.id + "): ")
		'''


# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
node = MyOwnPeer2PeerNode("10.0.2.15", 8002, 2)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.

print('waiting 10 sec for connection...')

'''if not node.connect_with_node('127.0.0.1', 10001) :
	print('connect failure')

# Send some message to the other nodes
if not node.send_to_nodes('{"message": "hi from node 2"}') : 
	print('send failure')

'''

time.sleep(10) # Replace this sleep with your main loop!

# Gracefully stop the node.
node.stop()