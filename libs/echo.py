import shlex

info = "echo - программа для быстрой записи текста в файл\n"
cavc = True
def start_module(args, pipeline=False):
	if not pipeline:
		args = shlex.split(args)
		text = args[1]
		print(text)
	else:
		text = pipeline.split("\n")
		for i in text:
			print(i)
		args = shlex.split(args)
		if len(args) > 1 and args[1] != (">" or ">>"):
			print(args[1])
