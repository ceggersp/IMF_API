import sys
import os
import platform

if platform.system() == 'Linux':

    wpath = sys.path[0]
    ppath = sys.path[4]+'/PyIMF'
    os.system('mkdir '+ppath)
    os.system('rm '+ppath+'/functions.py')
    os.system('rm '+ppath+'/__init__.py')
    os.system('cp '+'"'+wpath+'/src/functions.py" '+ppath)
    os.system('cp '+'"'+wpath+'/src/__init__.py" '+ppath)

else:

    wpath = sys.path[0]
    ppath = sys.path[5]+'\\PyIMF'
    os.system('mkdir '+ppath)
    os.system('del '+ppath+'\\functions.py')
    os.system('del '+ppath+'\\__init__.py')
    os.system('copy '+'"'+wpath+'\\src\\functions.py" '+ppath)
    os.system('copy '+'"'+wpath+'\\src\\__init__.py" '+ppath)

print('Package succesfully installed in '+ppath)