import os
import shutil
import subprocess
import toml

info = "n18pm - пакетный менеджер для псевдо ос pyOS\n"
trace = True

oldir = os.getcwd()
path = os.environ.get("U_LIBS_PATH")
of = open(os.environ.get("SYS_INFO_PATH"), "r")
g = toml.load(of)

def start_module(args):
	burl = "https://github.com/"
	try:
		if not args:
			return
		if args[0] == "help":
			print("n18pm help - выводит это окно\nn18pm install (packet) - устанавливает пакет на вашу псевдо ос\nn18pm remove (packet) - удаляет пакет\nn18pm list - показывает все бибилотеки из менеджера пакетов")
			return
		elif args[0] == "list":
			listpm = subprocess.run(["curl", "https://raw.githubusercontent.com/n18pyos/list-packages/refs/heads/main/list"], capture_output=True, text=True)
			print(listpm.stdout.replace("\\n", "\n"))
			return
		if len(args) < 3:
			burl = burl + "n18pyos/"
		else:
			burl = burl + args[2] + "/"
		if len(args) < 2:
			print("введите пакет для установки!")
			return
		elif args[0] == "install":
			os.chdir(path)
			furl = burl + args[1]
			print("downloading . . .")
			subprocess.run(["git", "clone", furl])
			if os.path.exists(args[1]):
				lst = []
				lbst = []
				vrst = None
				aut = None
				contact = None
				desc = None
				if os.path.exists(f"{args[1]}.toml"):
					os.remove(f"{args[1]}.toml")
				os.chdir(args[1])
				if os.path.exists("pymodule.toml"):
					try:
						ip = open("pymodule.toml", "r")
						ipp = toml.load(ip)
						ip.close()
						if ipp.get("libs", False):
							if not os.path.exists(os.path.join(path, "libs")):
								os.mkdir(os.path.join(path, "libs"))
								with open(os.environ.get("SETTING_PATH"), "a") as ftemp:
									ftemp.write(f"\nmodlib = '{os.path.join(path, 'libs')}'")
							for _u in ipp.get("libs"):
								if not os.path.exists(os.path.join(path, "libs", _u)):
									shutil.move(_u, os.path.join(path, "libs", _u))
									lbst.append(os.path.abspath(os.path.join(path, "libs", _u)))
									print("libs: ", _u, " is finished")
								else:
									if input(f"библиотека  {_u} уже существует, перезаписать ее? y/n  ").lower() == "y":
										os.remove(os.path.join(path, "libs", _u))
										shutil.move(_u, os.path.join(path, "libs", _u))
										lbst.append(os.path.abspath(_u))
										print("libs: ", _u, " is finished")
									else:
										pass
						else:
							print("libs: not libs to install")
						if ipp.get("version", False):
							print("version: ", ipp.get("version"))
							vrst = ipp.get("version")
						if ipp.get("author", False):
							aut = ipp.get("author")
						if ipp.get("contact", False):
							contact = ipp.get("contact")
						if ipp.get("desc", False):
							desc = ipp.get("desc")
					except Exception as evx:
						print("ошибка! ", evx)
						return
				else:
					print("Warning! module pymodule.toml is not found")
				for i in os.listdir():
					if i.endswith(".py"):
						if os.path.exists(f"{path}/{i}"):
							inn = input(f"в бибилотеках уже имеется файл {i} перезаписать его? y/n  ")
							if inn.lower() == "y":
								shutil.move(i, os.path.join(path, i))
								lst.append(i)
								print(i, " обработан")
							else:
								pass
						else:
							shutil.move(i, os.path.join(path, i))
							lst.append(i)
							print(i, " обработан")
			else:
				print("ошибка папка пакета не обнаружена")
				return
			if not os.path.exists("requirements.txt"):
				print("Warning! requirements.txt is not found")
			else:
				h = g["system"]["python_version"].rfind(".")
				new = g["system"]["python_version"][:h]
				print("python version ", new)
				if float(new) < 3.13:
					os.system("pip3 install -r requirements.txt")
				else:
					os.system("pip3 install -r requirements.txt --break-system-packages")
				os.remove("requirements.txt")
			if os.path.exists("pymodule.toml"):
				os.remove("pymodule.toml")
			progs = {
			"files": lst,
			"libs": lbst,
			"version": vrst,
			"author": aut,
			"contact": contact,
			"desc": desc
			}
			os.chdir(path)
			shutil.rmtree(args[1])
			op = open(f"{args[1]}.toml", "w")
			toml.dump(progs, op)
			op.close()
			os.chdir(oldir)
		elif args[0] == "remove":
			os.chdir(path)
			if os.path.exists(f"{args[1]}.toml"):
				inn = input(f"вы хотите удалить библиотеку {args[1]}? y/n  ")
				if inn.lower() == "y":
					op = open(f"{args[1]}.toml", "r")
					toml_td = toml.load(op)
					if toml_td.get("version", False) and toml_td.get("version", False) is not None:
						print("removing ", args[1], " ", toml_td.get("version"))
					else:
						print("removing ", args[1])
					for e in toml_td["files"]:
						os.remove(f"{e}")
					if toml_td.get("libs", False) and len(toml_td.get("libs", False)) > 0:
						for e in toml_td["libs"]:
							os.remove(e)
					op.close()
					os.remove(f"{args[1]}.toml")
			else:
				print("пакет не найден!")
				return
	except Exception as exc:
		print("ошибка при выполнении n18pm! ", exc)
	finally:
		os.chdir(oldir)
