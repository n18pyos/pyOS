info = "grep - программа для поиска совпадений в файле\ngrep (file) (to find)\n"

def start_module(args, pipeline=False):
	schet = 0
	if not pipeline:
		file = args[0]
		find = args[1]
		f = open(file, "r")
	else:
		find = args[0]
		f = pipeline.split("\n")
	for i in f:
		schet += 1
		if i.count(find) > 0:
			print(schet, " ", i)
