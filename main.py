import sys
import threading
import os
import atexit
import time
import toml
import io

vuryb = True
oldir = os.getcwd()
def go_to_old_dir():
	os.chdir(oldir)
def bt_boot():
	while vuryb:
		sobiratel = "booting"
		for _ in range(5):
			sobiratel = sobiratel + " ."
			if vuryb:
				print(f"\r{sobiratel}", end="")
				time.sleep(0.8)
		if vuryb:
			print("\r" + " " * 20, end="")
atexit.register(go_to_old_dir)

oj = False
def pipe(symbol=False, stm="open", app=False):
	global oj
	print(symbol, stm, app)
	if stm == "open":
		if app:
			pos = symbol.rfind(">>") + 2
		else:
			pos = symbol.rfind(">") + 1
		file_pipe = symbol[pos:].strip()
		if app == False:
			oj = open(file_pipe, "w")
		else:
			oj = open(file_pipe, "a")
	else:
		oj.close()

def pipeline(pipelines):
	pipe_temp = pipelines.split("|")
	pipe_very_temp = []
	for i in pipe_temp:
		pipe_very_temp.append(i.strip())
	pipe_temp = pipe_very_temp
	return pipe_temp

outio = False
ostdderr = False
ostddout = False
def openline(option="open"):
	global outio, ostdderr, ostddout
	if option == "open":
		outio = io.StringIO()
		ostddout = sys.stdout
		ostdderr = sys.stderr
		sys.stdout = outio
		sys.stderr = outio
	else:
		sys.stdout = ostddout
		sys.stderr = ostdderr
		return outio

def kill(excepti):
	global vuryb
	print("\r" + " " * 50, end="")
	print(f"\r{str(excepti).upper()}", end="")
	print(f"\n\r{str(excepti).lower()}", end="")
	print("\n")
	if vuryb:
		vuryb = False
	sys.exit(1)
thr_boot = threading.Thread(target=bt_boot).start()
try:
	to_read = open("sys.toml")
	toml_read = toml.load(to_read)
	sys_libs = toml_read["sys_path"]
	u_libs = toml_read["module_path"]
	sys_info = toml_read["sys_info_path"]
	to_read.close()
	if os.path.exists(sys_libs) and os.path.exists(u_libs) and os.path.exists(sys_info):
		pass
	else:
		kill("system libs is not finded")
except Exception as exc:
	kill(exc)
os.environ["U_LIBS_PATH"] = u_libs
os.environ["SYS_LIBS_PATH"] = sys_libs
os.environ["SYS_INFO_PATH"] = sys_info
os.environ["MAIN_FILE_PATH"] = __file__

vuryb = False
time.sleep(0.9)
print("\r" + " " * 50, end="")
print("system start".upper())
while True:
	try:
		inp = input(":  ")
		if inp == "help":
			print("this is pyOS its is not a real OS")
		elif inp == "exit":
			kill("User Exit")
		elif inp.startswith("info"):
			try:
				if len(inp.split()) == 2:
					moduls = inp.split()[1]
					man_to_print = __import__(f"libs.{moduls}", fromlist=["*"])
					if hasattr(man_to_print, "info"):
						print("\n")
						print(man_to_print.info)
					else:
						print("program has not info")
				elif len(inp.split()) == 1:
					print("write program to see info")
				else:
					print("do not write arguments for program in info")
			except Exception as ecx:
				print(ecx)
		elif inp == "":
			pass
		elif inp == "libs":
			for t in os.listdir(u_libs):
				if not t.startswith("__") and t.count(".") > 0 and not t.startswith(".") and t.endswith(".py"):
					f = t.rfind(".")
					print(t[:f])
		else:
			mkvn = False
			try:
				argus = ""
				mod = False
				def module_start(use_pipeline=False):
					global mod
					pipeline_dat = ""
					if not use_pipeline:
						mod = __import__(f"libs.{moduls}", fromlist=["*"])
						if getattr(mod, "cavc", False) == True:
							mod.start_module(inp)
						else:
							mod.start_module(argus)
					elif use_pipeline == True:
						longoflist = len(pipeline(inp)) - 1
						schtt = 0
						for _i in pipeline(inp):
							schtt += 1
							lib = _i.split(" ")
							mod = __import__(f"libs.{lib[0]}", fromlist=["*"])
							if True:
								if getattr(mod, "cavc", False) == True:
									pass
								else:
									if len(_i.split(" ")) > 1:
										_i = _i.split(" ")[1:]
									else:
										_i = []
								if schtt == 1:
									openline()
									mod.start_module(_i)
									res = openline(option="close")
									pipeline_dat = res.getvalue()
								elif schtt == longoflist + 1:
									mod.start_module(_i,  pipeline_dat)
								else:
									openline()
									mod.start_module(_i,  pipeline_dat)
									res = openline(option="close")
									pipeline_dat = res.getvalue()
									
					else:
						mod.start_module(argus)
				if inp.count(">") > 0:
					if inp.count(">>") > 0:
						pipe(inp, app=True)
						pos_inp = inp.rfind(">>")
					else:
						pipe(inp)
						pos_inp = inp.rfind(">")
					inp = inp[:pos_inp]
					ostdout = sys.stdout
					ostderr = sys.stderr
					sys.stdout = oj
					sys.stderr = oj
					mkvn = True
				if inp.count(" ") > 0:
					ninp = inp.split()
					moduls = ninp[0]
					argus = ninp[1:]
				else:
					moduls = inp
					argus = []
				if inp.count("|") < 1:
					module_start()
				else:
					module_start(use_pipeline=True)
			except Exception as excx:
				print(excx)
			finally:
				if mkvn:
					pipe(stm="close")
					sys.stdout = ostdout
					sys.stderr = ostderr
	except Exception as exc:
		kill(exc)
