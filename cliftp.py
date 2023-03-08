import ftplib
from ftplib import FTP
import os
import sys
import configparser
import datetime as dt

dt_now = dt.datetime.now()
logt = dt_now.strftime('%Y:%H:%M:%S')
config = configparser.ConfigParser()
config.read('ftp_user.ini')
ftpname = config.get('useraccount', 'name')
ftppass = config.get('useraccount', 'password')



# ダウンロード先のディレクトリを作成する
if not os.path.exists('./ftp'):
    os.makedirs('./ftp')
    with open('./ftp/log/log.txt', 'a') as fp:
        fp.write(f'{logt}:Directory is Notfound Makedir:ftp\n')
if not os.path.exists('./ftp/log'):
    os.makedirs('./ftp/log')
    with open('./ftp/log/log.txt', 'a') as fp:
        fp.write(f'{logt}:Directory is Notfound Makedir:log\n')
if not os.path.exists('./ftp/temp'):
    os.makedirs('./ftp/temp')
    with open('./ftp/log/log.txt', 'a') as fp:
        fp.write(f'{logt}:Directory is Notfound Makedir:temp\n')


    
with FTP('hidakk.sakura.ne.jp') as ftp:
    ftp.login(ftpname, ftppass)
    print("Connect")
    ftp.cwd('www')
    ftp.cwd('parking')
    print("chdir")
    ftp.retrlines('LIST')
    with open('./ftp/log/log.txt', 'a') as fp:
        fp.write('Get Remote Dir\n')
        ftp.retrlines('LIST', lambda line: fp.write(f'{logt}:{line}\n')) 
    with open("./ftp/temp/index.php", "wb") as f:
        ftp.retrbinary("RETR ./index.php", f.write)    
    ftp.quit()

file_path = "./ftp/temp/index.php"
line_number = 71
price1 = input()
# 変更後の内容
new_content = f"\t\t\t<p class=\"line3\">{price1}円</p>"
# PHPファイルを読み込む80
with open(file_path, "r") as f:
    lines = f.readlines()
# 指定された行を変更する
lines[line_number - 1] = new_content + "\n"
# PHPファイルを書き込む
with open(file_path, "w") as f:
    f.writelines(lines)