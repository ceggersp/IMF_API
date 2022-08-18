import sys
import os
wpath = sys.path[0]
ppath = sys.path[5]+'\\PyIMF'
os.system('mkdir '+ppath)
os.system('del '+ppath+'\\functions.py')
os.system('del '+ppath+'\\__init__.py')
os.system('copy '+'"'+wpath+'\\functions.py" '+ppath)
os.system('copy '+'"'+wpath+'\\__init__.py" '+ppath)