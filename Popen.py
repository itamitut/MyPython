import subprocess, time

opentext = subprocess.Popen(['C:\Windows\\notepad.exe', 'C:\Windows\IE11_main.log'])
print('Закройте редактор!')
opentext.wait()
print('Спасибо!')

