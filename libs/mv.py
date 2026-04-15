import shutil

info = "mv - программа для перемещения файлов\nmv (file_to_move) (place_to_move)\n"

def start_module(args):
	file = args[0]
	place = args[1]
	shutil.move(file, place)
