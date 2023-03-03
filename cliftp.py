import ftplib
from ftplib import FTP
import os
import sys
import glob
import tkinter as tk
import configparser

config = configparser.ConfigParser()
config.read('ftp_user.ini')
ftpname = config.get('useraccount', 'name')
ftppass = config.get('useraccount', 'password')

# ダウンロード先のディレクトリを作成する
if not os.path.exists('./onions'):
    os.makedirs('./onions')

with FTP('hidakk.sakura.ne.jp') as ftp:
    ftp.login(ftpname, ftppass)
    print("Connect")
    ftp.cwd('www')
    ftp.cwd('img')
    
    print("chdir")
    ftp.retrlines('LIST')
    with open('./onions/onions.txt', 'w') as fp:
        ftp.retrlines('LIST', lambda line: fp.write(line + '\n'))
    print("listwrite OK")
    
    wget = ftp.nlst()
    print(wget)
    ftp.retrlines('LIST')
    
    ftp.quit()