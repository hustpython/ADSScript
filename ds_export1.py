import os
import time


os.environ['HPEESOF_DIR']=r'C:\Program Files\Keysight\ADS2017'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\bin'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\circuit\lib.win32_64'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\adsptolemy\lib.win32_64'
os.environ['SIMARCH']='win32_64'
#os.system("hpeesofsim temp.log")
a = os.popen("dsdump cell_1.ds").read()
print(a)

from math import log             
S11=-0.847751321102689 + 1j*0.0944559443149849
        


print((20*log(abs(S11),10))) 