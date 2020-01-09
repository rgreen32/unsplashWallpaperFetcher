
C:\path\to\python.exe C:\path\to\fetchImage.py

echo yes | reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:\path\to\image.jpg  
echo yes | reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v WallpaperStyle /t "6"


RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters
