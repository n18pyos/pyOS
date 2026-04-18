import readline
import os
frd = False
pust = False
trace = True
info = "edit - легкая программа для редактирования текста\n"
def hook():
	tet = frd
	readline.insert_text(tet)
	readline.redisplay()
	
def start_module(args, pipe=False):
	global frd, pust
	if not pipe:
		file = args[0]
	else:
		file = "".join(pipe)
	if not os.path.exists(file):
		pust = True
		j = open(file, "w", encoding="utf-8")
		j.close()
	fread = open(file, "r+", encoding="utf-8")
	frd = fread.read()
	try:
		readline.set_pre_input_hook(hook)
		k = input("")
		readline.set_pre_input_hook(None)
		inp = input("сохранить изменения? y/n  ")
		if inp.lower() == "y":
			fread.seek(0)
			fread.truncate(0)
			fread.write(k)
			fread.close()
		else:
			if pust:
				os.remove(file)
	except:
		return
