import os

info = "sys - позволяет оперировать любыми командами системы\nsys (command)\n"

def start_module(args):
	os.system(" ".join(args))
