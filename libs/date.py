from datetime import datetime
import time

info = "date - программа для просмотра времени\n"
def print_time():
	dat = datetime.now()
	print(f"\r{dat.year}/{dat.month:02d}/{dat.day:02d}   {dat.hour:2d}:{dat.minute:02d}:{dat.second:02d}", end="")

def start_module(args):
	if len(args) < 1:
		print_time()
	if len(args) > 0:
		for i in range(int(args[0])):
			print_time()
			time.sleep(1)
	print("\n")
