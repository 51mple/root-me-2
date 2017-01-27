#!/usr/bin/python

msg = "tm bcsv qolfp\n\
f'dmvd xuhm exl tgak\n\
hlrkiv sydg hxm\n\
qiswzzwf qrf oqdueqe\n\
dpae resd wndo\n\
liva bu vgtokx sjzk\n\
hmb rqch fqwbg\n\
fmmft seront sntsdr pmsecq\n"
shift = 1
result = ''

for letter in msg:
	if letter == ' ':
		shift += 1
		result += letter
		continue
	elif letter == '\n':
		shift += 1
		result += letter
	elif letter == '\'':
		shift += 1
		result += letter
	else:
		if ord(letter) + shift > ord('z'):
			result += chr(ord('a') + (ord(letter)+shift) - ord('z') - 1)
		else:
			result += chr(ord(letter) + shift)

print(result)


