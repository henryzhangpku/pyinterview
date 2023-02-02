import sys
i = sys.maxsize
f = sys.float_info.max

import threading


class Sempahore():
    def __init__(self, max_available):
        self.cv = threading.Condition() #sempahore
        self.MAX_AVALABLE = max_available
        self.taken = 0

    def acquire(self):
        self.cv.acquire()#p
        while (self.taken == self.MAX_AVALABLE):
            self.cv.wait() #w

        self.taken += 1
        self.cv.release()#v

    def release(self):

    	self.cv.acquire()
    	self.taken-=1
    	self.cv.notify() #n
    	self.cv.release()

class LockObject():
	lock=threading.lock()
	@staticmethod
	def service(req,resp):
		while LockObject.lock:
			####
def f():
	###
t1=threading.Thread(target=f)
t1.start()
t1.join()

executor=concurrent.futures.ThreadPoolExecutor(max_workders=NTHREADS)
executor.submit(f, *args)

from multiprocessing import Pool
with Pool() as pool:
	all_h = pool.starmap(self._run, args)
