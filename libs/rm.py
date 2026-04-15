import os
import shutil

info = "rm - программа для удаления директорий/файлов\nrm (file/directory)\n"
def start_module(args):
	rdir = False
	tdir = False
	local_schet = 0
	for i in args:
		if i == "-r":
			rdir = True
		else:
			tdir = local_schet
		local_schet += 1
	if rdir:
		shutil.rmtree(args[tdir])
	else:
		os.remove(args[tdir])
