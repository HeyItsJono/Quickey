import os

args = raw_input("Paste NFSHost clipboard data here (Right-click to paste).\n")

os.system("FunKeyCIA.py -titleid {0} -key {1}".format(args.split()[0], args.split()[1]))