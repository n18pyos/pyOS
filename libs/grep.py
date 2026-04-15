info = "grep - программа для поиска совпадений в файле\ngrep (file) (to find)\n"

def start_module(args):
	schet = 0
	file = args[0]
	find = args[1]
	f = open(file, "r")
	for i in f:
		schet += 1
		if i.count(find) > 0:
			print(schet, " ", i)
