import os,sys
from datetime import date

today = date.today()
today = str(today)

os.chdir(r'C:\Users\jerome\Desktop\please fix this for me folder')


with open('daysave.txt' , 'r') as save_file:
    savedate = save_file.read()
    if savedate == today:
        sys.exit()
    
with open('daysave.txt' , 'w') as save_file:
    save_file.write(today)
    
os.system(r'cmd /k "cd C:\Users\jerome\Desktop\please fix this for me folder && t_t_d.txt && exit"')
