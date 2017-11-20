from multiprocessing import Process
import os

def run_proc(name):
	print("Run process {}({})".format(name,os.getpid()))

if __name__ == "__main__":
	print("parent process {} ".format(os.getpid()))
	p = Process(target=run_proc,args=("test",))
	print("child process will start")
	p.start()
	p.join()
	print("child process end")