from multiprocessing import Pool
import os
import time
import random

def long_time_task(name):
	print("Run task {}({})".format(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print("Task {} runs {:.2f} seconds".format(name,(end-start)))

if __name__ == '__main__':
	print("Parent process {}.".format(os.getpid()))
	p = Pool(9)
	for i in range(5):
		p.apply_async(long_time_task,args = (i,))
	print("Waiting for all subprocess done...")
	p.close()
	p.join()

	print("All subprocess done")
