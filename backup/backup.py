#encoding: utf-8
#Filename : backup.py

import os
import time

source = ['/home/lintian/Code/']
target_dir = '/home/lintian/Desktop/'

target = target_dir + time.strftime('%Y%m%d%H%M%S')+ '.zip'

zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup'
else:
    print 'Backup Failed'

