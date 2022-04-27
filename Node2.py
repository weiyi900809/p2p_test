import time
#from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode


from P2PNode import P2PNode



# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
node = P2PNode("123.240.196.78", 8002, 2)

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