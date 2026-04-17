import os
f = os.environ.get("HIST_FILE")
def start_module(args, pipe=False):
	if os.path.exists(f):
		with open(f, "r") as ort:
			print(ort.read())
	else:
		print("history file is not found!")
