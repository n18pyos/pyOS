import shutil

info = "cp - программа для копирования файлов\ncp (file to copy) (place to copy) (flags)\n"

def start_module(args):
	recursive = False
	for i in args:
		if i == "-r":
			recursive = True
	file = args[0]
	place = args[1]
	if recursive:
		shutil.copytree(file, place, dirs_exist_ok=True)
	else:
		shutil.copy2(file, place)
