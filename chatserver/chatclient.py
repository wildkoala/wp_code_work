import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receiving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print(str(data.decode())) #added decoding.. no effect, think i need to do this on the server.
				 # + "[" + time.strftime('%l:%M%p') + "]")

		except:
			time.sleep(0.1)

		finally:
			tLock.release()


host = '127.0.0.1'
port = 0


server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

s.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

alias = input("Name: ")
message = input(alias + "--> ")

while message != "q":
	if message != '':
		s.sendto(alias.encode() + ": ".encode() + message.encode(), server) #added encoding, now it works, but it's giving back bytes, need to decode.
	tLock.acquire()
	message = input(alias + "--> ")
	tLock.release()
	time.sleep(0.1)

shutdown = True

rT.join()
s.close()




