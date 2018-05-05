@echo on

set HPEESOF_DIR=C:\Program Files\Keysight\ADS2017
set COMPL_DIR=%HPEESOF_DIR%
set SIMARCH=win32_64
set SVECLIENT_DIR=%HPEESOF_DIR%/SystemVue/2016.08/%SIMARCH%

path %HPEESOF_DIR%\bin\%SIMARCH%;%HPEESOF_DIR%\bin;%HPEESOF_DIR%\lib\%SIMARCH%;%HPEESOF_DIR%\circuit\lib.%SIMARCH%;%HPEESOF_DIR%\adsptolemy\lib.%SIMARCH%;%PATH%;.
path %SVECLIENT_DIR%/bin/MATLABScript/runtime/win64;%SVECLIENT_DIR%/sveclient;%PATH%


hpeesofsim %1%
@echo on