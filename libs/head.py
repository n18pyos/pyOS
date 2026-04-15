info = "head - показывает начало файла\nhead (file) (flags)\n"

def start_module(args):
	col = int(args[0])
	file = args[1]
	char = False
	for i in args:
		if i == "-c":
			char = True
	filed = open(file, "r")
	schet = 0
	result = ""
	for i in filed:
		if schet == col:
			break
		if not char:
			result = result + f"{i}"
			schet += 1
		else:
			for g in i:
				result = result + g
				schet += 1
				if schet == col:
					break
	filed.close()
	print(result)
