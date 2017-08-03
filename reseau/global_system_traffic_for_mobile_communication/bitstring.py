#!/usr/bin/python3

frame = [
0x00, 0x00, 0x03, 0x34, 0x00, 0x01, 0xa0,
0x00, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x00, 0xf5, 0xa0, 0x00, 0x01, 0x00, 0x69,
0x00, 0x00, 0x67, 0x00, 0xff, 0x9c, 0x04,
0x02, 0x03, 0x02, 0x01, 0xff, 0xff, 0x0b,
0x5a, 0x07, 0x91, 0x23, 0x30, 0x10, 0x21,
0x00, 0x68, 0x04, 0x0b, 0x91, 0x71, 0x20,
0x33, 0x66, 0x03, 0xf8, 0x00, 0x00, 0x21,
0x40, 0x20, 0x61, 0x65, 0x02, 0x80, 0x47,
0xc7, 0xf7, 0x9b, 0x0c, 0x52, 0xbf, 0xc5,
0x2c, 0x10, 0x1d, 0x5d, 0x06, 0x99, 0xd9,
0xe1, 0x33, 0x28, 0x3d, 0x07, 0x85, 0xe7,
0x64, 0xf8, 0x7b, 0x6d, 0xa7, 0x95, 0x6b,
0xb7, 0xf8, 0x2d, 0x2c, 0x8b
]

framebin = [
'00000000', '00000000', '00000011', '00110100', '00000000', '00000001', '10100000',
'00000000', '00100000', '00100000', '00100000', '00100000', '00100000', '00100000',
'00000000', '11110101', '10100000', '00000000', '00000001', '00000000', '01101001',
'00000000', '00000000', '01100111', '00000000', '11111111', '10011100', '00000100',
'00000010', '00000011', '00000010', '00000001', '11111111', '11111111', '00001011',
'01011010', '00000111', '10010001', '00100011', '00110000', '00010000', '00100001',
'00000000', '01101000', '00000100', '00001011', '10010001', '01110001', '00100000',
'00110011', '01100110', '00000011', '11111000', '00000000', '00000000', '00100001',
'01000000', '00100000', '01100001', '01100101', '00000010', '10000000', '01000111',
'11000111', '11110111', '10011011', '00001100', '01010010', '10111111', '11000101',
'00101100', '00010000', '00011101', '01011101', '00000110', '10011001', '11011001',
'11100001', '00110011', '00101000', '00111101', '00000111', '10000101', '11100111',
'01100100', '11111000', '01111011', '01101101', '10100111', '10010101', '01101011',
'10110111', '11111000', '00101101', '00101100', '10001011'
]

gsm7bin_to_ascii = {
	'0000000':'@', '0010000':u'Δ', '0100000':' ', '0110000':'0', '1000000':u'¡', '1010000':'P', '1100000':u'¿', '1110000':'p',
	'0000001':u'£', '0010001':'_', '0100001':'!', '0110001':'1', '1000001':'A', '1010001':'Q', '1100001':'a', '1110001':'q',
	'0000010':'$', '0010010':u'Φ', '0100010':'"', '0110010':'2', '1000010':'B', '1010010':'R', '1100010':'b', '1110010':'r',
	'0000011':u'¥', '0010011':u'Γ', '0100011':'#', '0110011':'3', '1000011':'C', '1010011':'S', '1100011':'c', '1110011':'s',
	'0000100':u'è', '0010100':u'Λ', '0100100':'¤', '0110100':'4', '1000100':'D', '1010100':'T', '1100100':'d', '1110100':'t',
	'0000101':u'é', '0010101':u'Ω', '0100101':'%', '0110101':'5', '1000101':'E', '1010101':'U', '1100101':'e', '1110101':'u',
	'0000110':u'ù', '0010110':u'Π', '0100110':'&', '0110110':'6', '1000110':'F', '1010110':'V', '1100110':'f', '1110110':'v',
	'0000111':u'ì', '0010111':u'Ψ', '0100111':"'", '0110111':'7', '1000111':'G', '1010111':'W', '1100111':'g', '1110111':'w',
	'0001000':u'ò', '0011000':u'Σ', '0101000':'(', '0111000':'8', '1001000':'H', '1011000':'X', '1101000':'h', '1111000':'x',
	'0001001':u'Ç', '0011001':u'Θ', '0101001':')', '0111001':'9', '1001001':'I', '1011001':'Y', '1101001':'i', '1111001':'y',
	'0001010':'\n', '0011010':u'Ξ', '0101010':'*', '0111010':':', '1001010':'J', '1011010':'Z', '1101010':'j', '1111010':'z',
	'0001011':u'Ø', '0011011':'ESC', '0101011':'+', '0111011':';', '1001011':'K', '1011011':'Ä', '1101011':'k', '1111011':'ä',
	'0001100':u'ø', '0011100':u'Æ', '0101100':',', '0111100':'<', '1001100':'L', '1011100':'Ö', '1101100':'l', '1111100':'ö',
	'0001101':'\n', '0011101':u'æ', '0101101':'-', '0111101':'=', '1001101':'M', '1011101':'Ñ', '1101101':'m', '1111101':'ñ',
	'0001110':u'Å', '0011110':u'ß', '0101110':'.', '0111110':'>', '1001110':'N', '1011110':'Ü', '1101110':'n', '1111110':'ü',
	'0001111':u'å', '0011111':u'É', '0101111':'/', '0111111':'?', '1001111':'O', '1011111':'§', '1101111':'o', '1111111':'à'
}

framebinstr = ''.join(framebin)
start = 0
while start < len(framebinstr):
	section = framebinstr[start:]
	remainder = len(section) % 7

	i = 0
	j = 7
	print(str(start) + ': ', end='')
	while j < len(section):
		#print(framebinstr[i:j])
		print(gsm7bin_to_ascii[section[i:j]], end='')
		i += 7
		j += 7
	if remainder > 0:
		print(gsm7bin_to_ascii['0'*(7-remainder) + section[i:j]])
	else:
		print('\n\n\n')
	start += 1

i = 0
while i < len(frame):
	try:
		b = bytes(frame[i:])
		s = b.decode('utf-16')
		print(s)
	except UnicodeDecodeError:
		i += 1
		continue
	i += 1

#______________________________________ISI message formatFieldDescription	Notes______________________________________
#H	media	Defines the media to be	used. e.g. PN-- MEDIA-- MBUS,	PN-- MEDIA-- FBUS
#H	receiver device	Device address of the	receiver.	1st part of sender's address
#H	sender device	Device address of the	sender.	1st part of sender's address
#H	Resource	ISI Resource group, as	defined in the ISI	specification.	This is known as `function`	in PhoNet terms.
#H	length	Number of subsequent bytes	in the message, starting	with and including the	receiver object.	This field always follows a	processors LSB/MSB	conventions for handling	word data. The media	drivers in PhoNet handle the	conversion to and from the	PhoNet fixed MSB, LSB order	during interprocessor	communication.
#H	Receiver object	Internal address of the	receiver object.	2nd part of receiver's	address.
#H	Sender object	Internal address of the	sender object.	2nd part of sender's	address.
#D	Unique	Transaction ID	Used to identifier which	transaction a message	belongs to.
#D	Message ID	ISI message ID.
#D	Msg data 1	Message data as indicated in	the ISIS specification for	this message.
#D	Msg data 2	Message data . . .
#D	Msg data n	Message data . . .______________________________________
#
#The ISI message specification need not include the complete ISI message description for each message, as many of the fields in the message header are handled in the same way for all messages. The ISI message specifications use the following format to describe ISI messages.
