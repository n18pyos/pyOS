import os

info = "touch - программа для создания файлов\ntouch (file)\n"

def start_module(args):
	on = os.open(args[0], os.O_CREAT)
	os.close(on)
	os.utime(args[0], None)
