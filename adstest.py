# CODING:UTF-8
import os
import time


os.environ['HPEESOF_DIR']=r'C:\Program Files\Keysight\ADS2017'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\bin'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\circuit\lib.win32_64'
os.environ['path']+=';'+os.environ['HPEESOF_DIR']+r'\adsptolemy\lib.win32_64'
os.environ['SIMARCH']='win32_64'


N='''
Options ResourceUsage=yes UseNutmegFormat=no EnableOptim=no TopDesignName="MyLibrary19_lib:cell_1:schematic" DcopOutputNodeVoltages=yes DcopOutputPinCurrents=yes DcopOutputAllSweepPoints=no DcopOutputDcopType=0
S_Param:SP1 CalcS=yes CalcY=no CalcZ=no GroupDelayAperture=1e-4 FreqConversion=no FreqConversionPort=1 StatusLevel=2 CalcNoise=no SortNoise=0 BandwidthForNoise=1.0 Hz DevOpPtLevel=0 \
SweepVar="freq" SweepPlan="SP1_stim" OutputPlan="SP1_Output"

SweepPlan: SP1_stim Start=0 GHz Stop=10.0 GHz Step=0.01 GHz

OutputPlan:SP1_Output \
 Type="Output" \
 UseEquationNestLevel=yes \
 EquationNestLevel=2 \
 UseSavedEquationNestLevel=yes \
 SavedEquationNestLevel=2
#load "python","LinearCollapse"
Component Module="LinearCollapse" Type="ModelExtractor" NetworkRepresentation=2

Port:Term1 N__0 0 Num=1 Z=50 Ohm Noise=yes
Port:Term2 N__3 0 Num=2 Z=50 Ohm Noise=yes
L:L1 N__0 N__3 L=1.0 nH Noise=yes
C:C1 N__3 0 C=1.0 pF
'''
N = '''
Options ResourceUsage=yes UseNutmegFormat=no EnableOptim=no UseNutmegFormat=no ASCII_Rawfile=yes TopDesignName="MyLibrary_lib:cell_1:schematic" DcopOutputNodeVoltages=yes DcopOutputPinCurrents=yes DcopOutputAllSweepPoints=no DcopOutputDcopType=0
R:R1  N__1 N__3 R=75 Ohm tune{ 25 Ohm to 75 Ohm by 5 Ohm } Noise=yes 
L:L1  N__3 N__4 L=0.77 nH tune{ 0.5 nH to 1.5 nH by 0.1 nH } Noise=yes  
C:C1  N__4 0 C=1.02 pF tune{ 0.5 pF to 1.5 pF by 0.1 pF } 
S_Param:SP1 CalcS=yes CalcY=no CalcZ=no GroupDelayAperture=1e-4 FreqConversion=no FreqConversionPort=1 StatusLevel=2 CalcNoise=no SortNoise=0 BandwidthForNoise=1.0 Hz DevOpPtLevel=0 \
SweepVar="freq" SweepPlan="SP1_stim" OutputPlan="SP1_Output" 

SweepPlan: SP1_stim Start=1.0 GHz Stop=10.0 GHz Step=0.10 GHz 

OutputPlan:SP1_Output \
      Type="Output" \
      UseEquationNestLevel=yes \
      EquationNestLevel=2 \
      UseSavedEquationNestLevel=yes \
      SavedEquationNestLevel=2

#load "python","LinearCollapse"
Component Module="LinearCollapse" Type="ModelExtractor" NetworkRepresentation=2
#uselib "ckt" , "TLSC"
TLSC:TL1  N__1 0 Z=377.0 Ohm E=90 F=10 GHz 
Port:Term1  N__1 0 Num=1 Z=377 Ohm Noise=yes 

;#@# autodisplay="S_Params_Quad_dB_Smith"
'''
os.chdir('E:\ADSdata')


f=open('temp.log','w')
f.writelines(N)
f.close()


os.system('hpeesofsim temp.log')


try:
    os.stat('./data')
except:
    os.mkdir('./data')


'''try:
    os.system("TASKKILL /F /IM dds_launcher.exe")
    time.sleep(0.1)
except:
    pass'''


try:
    os.remove('./data/cell_1.ds')
except:
    pass


#os.rename('cell_1.ds','./data/cell_1.ds')


#os.system('dds cell_1.dds')



