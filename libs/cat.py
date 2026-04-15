info = "cat - программа для просмотра текста файлов\ncat (file)\n"

def start_module(file):
	file = "".join(file)
	with open(file, "r") as md:
		print(md.read())
