import ftplib

with FTP('192.168.0.210') as ftp:
    ftp.login(user='Lus',passwd='9j5%2sRG')
    ftp.cwd('onion')
    ftp.retrlines('LIST')
    
