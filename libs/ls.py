import os

info = "ls - программа для вывода файлов и папок в текущей директории\n"

def start_module(args):
	if len(args) > 0:
		oldir = os.getcwd()
		os.chdir(args[0])
	for i in os.listdir():
		print(i)
	if len(args) > 0:
		os.chdir(oldir)
