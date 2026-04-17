import os

info = "ls - программа для вывода файлов и папок в текущей директории\n"

def start_module(args):
	try:
		if len(args) > 0:
			oldir = os.getcwd()
			os.chdir(args[0])
		for i in os.listdir():
			print(i)
	finally:
		if len(args) > 0:
			os.chdir(oldir)

