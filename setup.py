import sys
import os
import platform

if platform.system() == 'Linux':

    wpath = sys.path[0]
    ppath = sys.path[5]+'/PyIMF'
    os.system('mkdir '+ppath)
    os.system('rm '+ppath+'/functions.py')
    os.system('rm '+ppath+'/__init__.py')
    os.system('cp '+'"'+wpath+'/functions.py" '+ppath)
    os.system('cp '+'"'+wpath+'/__init__.py" '+ppath)

else:

    wpath = sys.path[0]
    ppath = sys.path[5]+'\\PyIMF'
    os.system('mkdir '+ppath)
    os.system('del '+ppath+'\\functions.py')
    os.system('del '+ppath+'\\explorer.py')
    os.system('del '+ppath+'\\__init__.py')
    os.system('copy '+'"'+wpath+'\\functions.py" '+ppath)
    os.system('copy '+'"'+wpath+'\\explorer.py" '+ppath)
    os.system('copy '+'"'+wpath+'\\__init__.py" '+ppath)