@SET dest="C:\svn\trunk\K1_20_MasterPlant\02_Library\Python\004.Release\100\VCM\AutomationGUI"
copy /Y "AutomationGUI.py" %dest%
copy /Y "AutomationGUI_ui.py" %dest%
copy /Y "AutomationGUI_rc.py" %dest%
copy /y "strings.py" %dest%
copy /y "__init__.py" %dest%
tortoiseproc /command:commit /path:%dest%