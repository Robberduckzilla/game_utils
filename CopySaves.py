import datetime
import os
import shutil
import time

delay_in_minutes = 0.1
source = ""
dest =  ""

print(f'Backing up stuff every {delay_in_minutes} minutes.')
i=0

while(True):
    timestamp = datetime.datetime.now().strftime(r'%Y-%m-%d_%H-%M')
    src_files = os.listdir(source)
    directory = dest + timestamp + "/"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    for file_name in src_files:
        full_file_name = os.path.join(source, file_name)
        if os.path.isfile(full_file_name):
            shutil.copytree(full_file_name, directory + file_name) 
    i+=1
    print(f'Backups so far: {i}')
    
    time.sleep(60 * delay_in_minutes)
