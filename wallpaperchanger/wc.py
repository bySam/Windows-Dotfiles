import winreg
import win32gui

REG_PATH = r"SOFTWARE\Microsoft\Windows\DWM"


registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
							   winreg.KEY_READ)
value, regtype = winreg.QueryValueEx(registry_key, 'AccentColor')
winreg.CloseKey(registry_key)



winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
							   winreg.KEY_WRITE)
winreg.SetValueEx(registry_key, 'AccentColorInactive', 0, winreg.REG_DWORD, value)
winreg.CloseKey(registry_key)




