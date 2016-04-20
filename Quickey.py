import os

args = raw_input("Paste NFSHost clipboard data here (Right-click to paste).\n")
tid = args.split()[0]
tkey = args.split()[1]

os.system("FunKeyCIA.py -titleid {0} -key {1}".format(tid, tkey))