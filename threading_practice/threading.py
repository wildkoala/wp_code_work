import threading
from queue import Queue
import time

#want to do multiple things at the same time. Shared variables are dangerous.
printLock = threading.Lock()

q = Queue()

def exampleJob(job):
	time.sleep(0.5)
	with printLock:
		print(threading.current_thread().name, worker)

def threader():
	while True:
		worker = q.get()
		exampleJob(worker)
		q.task_done()

for x in range(10):
	t = threading.Thread(target=threader)

	t.daemon = True
	t.start()

start = time.time()

for worker in range(20):
	q.put(worker)

q.join()

print('Entire job took: ' + str(time.time()-start))

































