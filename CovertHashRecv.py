import hashlib
import time
import sys

if __name__=="__main__":
	
	numbits=sys.argv[1]
	

	timenow=time.time()

	duration=timenow + (numbits*5)
	fileloc=['samplevid.mp4','samplevid2.mp4']

	while(duration-timenow>0):
		for i in range (0,2)
			t1=time.time()
			hashcalc = hashlib.sha512()
			filevar = open('samplevid2.mp4', 'rb')
			buf=filevar.read()
			hashcalc.update(buf)
			#print (hashcalc.hexdigest())
			t2=time.time()
			latency=t2-t1
			print latency
			timenow=time.time()
			os.system('sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'')
		
