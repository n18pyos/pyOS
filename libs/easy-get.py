import requests as req
import certifi as certi
import shlex

cavc = True
info = "easy-get - программа для минимального взаимодействия с интернетом\n easy-get post/get (url)\n"

def start_module(args):
	args = shlex.split(args)[1:]
	if len(args) < 1:
		print("введите корректные аргументы")
		return
	if args[0] == "help":
		print(info)
		return
	if len(args) < 2:
		print("введите корректные аргументы")
		return
	if args[0] == "get":
		get = req.get(args[1], verify=certi.where())
		print(get.text)
	if args[0] == "post":
		if len(args) < 3:
			print("введите параметры запроса")
			return
		dat_dic = {}
		for o in args[2:]:
			if "=" in o:
				k, v = o.split("=", 1)
				dat_dic[k] = v
		get = req.post(args[1], verify=certi.where(), data=dat_dic)
		print(get.text)