@SET dest="C:\svn\trunk\K1_20_MasterPlant\03_Tools\AutomationGUI"
copy /Y "AutomationGUI.py" %dest%
copy /Y "AutomationGUI_ui.py" %dest%
copy /Y "AutomationGUI_rc.py" %dest%
copy /y "deletepyc.bat" %dest%
copy /y "__init__.py" %dest%
tortoiseproc /command:commit /path:%dest%

@SET karmacustom="C:\SVN\trunk\K1_20_Body_HIL_dSPACE_2018B\04_Automation\K1_20_BODY\01_Library\KarmaCustom_2018B\Karma"
tortoiseproc /command:update /path:%karmacustom%
del %dest%\*.pyc