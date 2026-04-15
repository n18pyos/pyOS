info = "wc - программа для подсчета линий/символов\nwc (argument) (file)\n"

def start_module(args):
	lines = False
	char = False
	bytess = False
	file = False
	schet = 0
	for i in args:
		if i == "-l":
			lines = True
		elif i == "-c":
			char = True
		elif i == "-b":
			bytess = True
		else:
			file = i
	fo = open(file, "r")
	for i in fo:
		if lines:
			schet += 1
		elif char:
			for _ in repr(i):
				schet += 1
		elif bytess:
			schet += len(i.encode())
	print(file, " ", schet)
