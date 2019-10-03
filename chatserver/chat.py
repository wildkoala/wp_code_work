import socket
import threading
import sys

class Server:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []

	def __init__(self):
		self.s.bind(('0.0.0.0', 10001))
		self.s.listen(1)
		print("Server is starting...")		

	def handler(c, a):
		while True:
			data = c.recv(1024)
			for connection in self.connections:
				connection.send(data)
				if not data:
					break

	def run(self):
		while True:
			c,a = self.s.accept()
			cThread = threading.Thread(target=self.handler, args=(c, a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(self.connections)



class Client:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
                
        def send_msg(self):
                while True:
                        self.s.send(bytes(input("-->"), 'utf-8'))

                
        def __init__(self, address):
                self.s.connect((address, 10001))

                iThread = threading.Thread(target=self.send_msg)
                iThread.daemon = True
                iThread.start()
                
                
                while True:
                        data = self.s.recv(1024)
                        if not data:
                                break
                        print(data)
                

                
                





if (len(sys.argv) > 1):
        client = Client(sys.argv[1])

server = Server()
server.run()



