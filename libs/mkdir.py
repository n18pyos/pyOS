import os

info = "mkdir - программа для создания директорий\nmkdir (dir)\n"

def start_module(args):
	os.mkdir(args[0])
