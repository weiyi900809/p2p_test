#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.2 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# MyOwnPeer2PeerNode is an example how to use the p2pnet.Node to implement your own peer-to-peer network node.        #
# 28/06/2021: Added the new developments on id and max_connections
#######################################################################################################################
from p2pnetwork.node import Node
import time
import socket 
class P2PNode (Node):

    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(P2PNode, self).__init__(host, port, id, callback, max_connections)
        print("P2PNode: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id+ " ip: " + node.host + " port: " + str(node.port))
        
    def inbound_node_connected(self, node):
        
        #self.connect_with_node(node.host, node.port) #如果有node連接我,我會返回去連接對方
      
        print("inbound_node_connected: (" + self.id + "): " + node.id+ " ip: " + node.host + " port: " + str(node.port))

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id+ " ip: " + node.host + " port: " + str(node.port))

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id + " ip: " + node.host + " port: " + str(node.port))

    def node_message(self, node, data):
        print("node_message (" + self.id + ") from " + node.id + " ip: " + node.host + " port: " + str(node.port) + " : " + str(data))
        
    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")
        
    def run(self):
        """The main loop of the thread that deals with connections from other nodes on the network. When a
           node is connected it will exchange the node id's. First we receive the id of the connected node
           and secondly we will send our node id to the connected node. When connected the method
           inbound_node_connected is invoked."""
        while not self.terminate_flag.is_set():  # Check whether the thread needs to be closed
            try:
                self.debug_print("Node: Wait for incoming connection")
                connection, client_address = self.sock.accept()

                self.debug_print("Total inbound connections:" + str(len(self.nodes_inbound)))
                # When the maximum connections is reached, it disconnects the connection 
                if self.max_connections == 0 or len(self.nodes_inbound) < self.max_connections:
                    
                    # Basic information exchange (not secure) of the id's of the nodes!
                    connected_node_port = client_address[1] # backward compatibilty
                    connected_node_id   = connection.recv(4096).decode('utf-8')
                    if ":" in connected_node_id:
                        (connected_node_id, connected_node_port) = connected_node_id.split(':') # When a node is connected, it sends it id!
                    connection.send(self.id.encode('utf-8')) # Send my id to the connected node!

                    thread_client = self.create_new_connection(connection, connected_node_id, client_address[0], connected_node_port)
                    thread_client.start()
                    self.connect_with_node(thread_client.host,thread_client.port)
                    self.nodes_inbound.append(thread_client)
                    self.inbound_node_connected(thread_client)

                else:
                    self.debug_print("New connection is closed. You have reached the maximum connection limit!")
                    connection.close()
            
            except socket.timeout:
                self.debug_print('Node: Connection timeout!')

            except Exception as e:
                raise e

            self.reconnect_nodes()

            time.sleep(0.01)

        print("Node stopping...")
        for t in self.nodes_inbound:
            t.stop()

        for t in self.nodes_outbound:
            t.stop()

        time.sleep(1)

        for t in self.nodes_inbound:
            t.join()

        for t in self.nodes_outbound:
            t.join()

        self.sock.settimeout(None)   
        self.sock.close()
        print("Node stopped")
