import os

info = "cd - программа созданная для того чтобы менять директории\ncd (dir)\n"

def start_module(dir):
	dir = "".join(dir)
	os.chdir(dir)
