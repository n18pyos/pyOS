import os

info = "tail - показывает конец файла\ntail (file) (int) (flags)"

def start_module(args):
	file = args[0]
	search = int(args[1])
	char = False
	for i in args:
		if i == "-c":
			char = True
	jk = open(file, "r")
	schet = 0
	minus = 0
	chars = ""
	gk = jk.readlines()
	for m in range(len(gk)):
		minus += 1
		i = gk[-minus]
		if char == False:
			if schet > search:
				break
			schet += 1
			chars = chars + i
		else:
			for _i in i:
				if schet > search:
					break
				schet += 1
				chars = chars + _i
	print(chars)
	jk.close()
