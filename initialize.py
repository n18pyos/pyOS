import os
import toml
import platform
from datetime import datetime
python = platform.python_version()
vers = "0.5"
osn = "pyOS"
ydra = os.cpu_count()
archh = platform.machine()
print("\rInitializing . . .", end="")
try:
		if os.path.exists("libs/sys_libs"):
			donl = open("sys.toml", "w")
			syste = {
			"system": {
			"os_name": osn,
			"os_version": vers,
			"os_time_initialize": datetime.now(),
			"python_version": python
			},
			"hardware": {
			"arch": archh,
			"cpu_count": ydra,
			}}
			dat = {
			"sys_path": os.path.abspath("libs/sys_libs"),
			"module_path": os.path.abspath("libs"),
			"sys_info_path": os.path.abspath("libs/sys_libs/info.toml")
			}
			toml.dump(dat, donl)
			if not os.path.exists("libs/sys_libs/info.toml"):
				conl = open("libs/sys_libs/info.toml", "w")
				toml.dump(syste, conl)
			print("\n")
		else:
			print("\rsys_libs is not found!", end="")
			print("\n")
except Exception as exc:
	print(exc)
try:
	conl.close()
	try:
		donl.close()
	except:
		pass
except:
	pass
