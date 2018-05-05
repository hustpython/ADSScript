# CODING:UTF-8
import os
import time


os.environ['HPEESOF_DIR']=r'C:\Program Files\Keysight\ADS2017'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\bin'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\circuit\lib.win32_64'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\adsptolemy\lib.win32_64'
os.environ['SIMARCH']='win32_64'



os.chdir('E:\ADSdata\MyWorkspace_wrk')

#os.system('hpeesofsim netlist.log')


os.system('hpeesofsim -help')

 



