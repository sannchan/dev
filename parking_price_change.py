##Auther s.nyuumura
##Made 2023.03.09
##2023 Hidakankou kaihatu All Rights Reserved.
##version 1.0.0

from PyQt6 import QtCore,  QtWidgets
from ftplib import FTP 
from PyQt6.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import os
import sys
import configparser
import shutil
import heapq
import webbrowser
import logging
import datetime



class Ui_mainWindow(object):
    ###APP起動時###
    def __init__(self):
        ########変数のイニシャライズ########
        ##configparserで./ftp_config.iniからコンフィグを読み込む
        config = configparser.ConfigParser()
        config.read('ftp_config.ini')
        self.weburl =config.get('webURL','url')
        self.ftpname = config.get('useraccount', 'name')
        self.ftppass = config.get('useraccount', 'password')
        self.ftpurl = config.get('Remoteurl','url')
        self.ftpdir1 = config.get('RemoteDir','dir1')
        self.ftpdir2 = config.get('RemoteDir','dir2')
        self.workdir_ftp = "./ftp"
        self.workdir_log = "./ftp/log"
        self.workdir_tmp = "./ftp/temp"
        self.workdir_upload = "./ftp/temp/upload"
        self.filename = './ftp/temp/upload/index.php'
        self.filename2 = 'index.php'
        self.pk1_wd_init_ln = 24
        self.pk1_hd_init_ln = 31
        self.pk2_wd_init_ln = 71
        self.pk2_hd_init_ln = 78
        self.pk4_wd_init_ln = 125
        self.pk4_hd_init_ln = 132
        self.init_setval = 0
        self.init_setval2 = 0
        self.init_setval3 = 0
        self.init_setval4 = 0
        self.init_setval5 = 0
        self.init_setval6 = 0
        
        

        ######変数のイニシャライズ######
        
        ######ディレクトリのイニシャライズ######
        ##./ftpをイニシャライズ
        #ディレクトリが存在しない場合は作成
        if not os.path.exists(self.workdir_ftp):
            os.makedirs(self.workdir_ftp)
        
        ##./ftp/logをイニシャライズ
        #ディレクトリがそんないしない場合は作成
        if not os.path.exists(self.workdir_log):
            os.makedirs(self.workdir_log)
            
        #存在する場合は最新のログ10件を残してログローテ
        else:
            directory = self.workdir_log
            # ディレクトリ内の全てのファイルのパスを取得
            files2 = [os.path.join(directory, filename2) for filename2 in os.listdir(directory)]
            # ファイルの最終更新日時を取得
            timestamps = [os.path.getmtime(file2) for file2 in files2]
            # 最新の10個のファイルのパスを取得
            newest_files2 = heapq.nlargest(10, zip(timestamps, files2))
            # 最新の10個以外のファイルを削除
            for file2 in files2:
                if file2 not in [f for t, f in newest_files2]:
                    os.remove(file2)
        
        #./ftp/tempをイニシャライズ  
        #ディレクトリが存在しない場合は作成    
        if not os.path.exists(self.workdir_tmp):
            os.makedirs(self.workdir_tmp)
        #ディレクトリ内の全てを削除
        else:
            for filename in os.listdir(self.workdir_tmp):
                file_path = os.path.join(self.workdir_tmp, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    
        #./ftp/uploadをイニシャライズ
        #ディレクトリが存在しない場合は作成   
        if not os.path.exists(self.workdir_upload):
            os.makedirs(self.workdir_upload)
        #ディレクトリがそんないしない場合は作成 
        else:
            for filename in os.listdir(self.workdir_upload):
                file_path = os.path.join(self.workdir_upload, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        #######=============ディレクトリのイニシャライズ===========########
        
        logfilename = f"./ftp/log/example_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(filename=logfilename, level=logging.DEBUG)
        
        #######=============リモートサーバのindex.phpを取得=======########
        #ry:
        try:
            with FTP(self.ftpurl) as ftp:
            #ftpログイン
                ftp.login(self.ftpname, self.ftppass)
                logging.info('ftp_get_php success')
            #www階層へcwd
                ftp.cwd(self.ftpdir1)
                logging.info('ftp_get_php cwd www success')
            #parking階層へcwd
                ftp.cwd(self.ftpdir2)
                logging.info('ftp_get_php cwd parking success')
            #.index.phpをバイナリ形式で取得
                with open(f"{self.workdir_tmp}/index.php", "wb") as f:
                    ftp.retrbinary("RETR ./index.php", f.write)
                    logging.info('ftp_get_php saved success')      
                ftp.quit()
        except Exception as e:
            logging.error(f'ftp_get_php saved error{e}')


       # except Exception as e:
       #     logging.error('0x01:ftp_get_php_error')
        #######=============リモートサーバのindex.phpを取得=======########
        
        #######=============spinboxの初期値設定=================########
        
        ##Spinbox
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk1_wd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if p_tag:
                        self.init_setval  = int(p_tag.text.replace("円", ""))
                    break
            
        ##spinbox2
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk1_hd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if  p_tag:
                        self.init_setval2  = int(p_tag.text.replace("円", ""))
                    break
                
        #spinbox3
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk2_wd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if p_tag:
                        self.init_setval3  = int(p_tag.text.replace("円", ""))
                    break
        #spinbox4
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk2_hd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if p_tag:
                        self.init_setval4  = int(p_tag.text.replace("円", ""))
                    break
        #spinbox5
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk4_wd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if p_tag:
                        self.init_setval5  = int(p_tag.text.replace("円", ""))
                        
                    break
        #spinbox6   
        with open(f"{self.workdir_tmp}/index.php", "r") as file:
            for i, line in enumerate(file):
                if i == self.pk4_hd_init_ln - 1:
                    soup = BeautifulSoup(line, "html.parser")
                    p_tag = soup.find("p", {"class": "line3"})
                    if p_tag:
                        self.init_setval6  = int(p_tag.text.replace("円", ""))
                    break
        
    ###APP起動時(Qtdesignerで出力したからsetupUiメソッドで呼び出してるけど別に__init__でもいい気がするね###       
    def setupUi(self, mainWindow):
        #######=============画面設計=================########
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(578, 419)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 291, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.write_php)
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 170, 101, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox.setValue(self.init_setval)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(470, 170, 101, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_2.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_2.setValue(self.init_setval2)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(360, 210, 101, 21))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_3.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_3.setValue(self.init_setval3)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(470, 210, 101, 21))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_4.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_4.setValue(self.init_setval4)
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(360, 250, 101, 21))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_5.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_5.setValue(self.init_setval5)
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(470, 250, 101, 21))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_6.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_6.setValue(self.init_setval6)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 150, 60, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 170, 271, 111))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 170, 60, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 210, 60, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 250, 60, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 30, 551, 101))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 300, 261, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.finished)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        #######=============画面設計=================########
        
    ###APP起動時###
    def retranslateUi(self, mainWindow):
        #######=============画面カスタマイズ=================########
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "駐車場料金変更プログラム"))
        self.pushButton.setText(_translate("mainWindow", "適用"))
        self.label.setText(_translate("mainWindow", "平日料金"))
        self.label_2.setText(_translate("mainWindow", "休日料金"))
        self.label_3.setText(_translate("mainWindow", "設定予定料金"))
        self.label_4.setText(_translate("mainWindow", "パーク１"))
        self.label_5.setText(_translate("mainWindow", "パーク２"))
        self.label_6.setText(_translate("mainWindow", "パーク４"))
        self.label_7.setText(_translate("mainWindow", "現在料金"))
        self.pushButton_2.setText(_translate("mainWindow", "アップロード"))
        #######=============画面カスタマイズ=================########
    
    def get_now_index_php_disp(self):
        #######=============webサーバに設定されている料金表示=================########
        file_path = "./ftp/temp/index.php"
        p1_line_numbers = [22, 23, 24, 29, 30, 31] # 表示する行番号をリストで指定する
        p2_line_numbers = [69, 70, 71, 76, 77, 78] # 表示する行番号をリストで指定する
        p4_line_numbers = [123, 124, 125, 130, 131, 132] # 表示する行番号をリストで指定する
        ###上記で読み取った文字列を抽出しhtml形式で加工を行なってtextbrowserで表示する。
        ###気にしてなかったけど<p>タグが表示されていないのはsetHtmlを使ってるから###
        
        ##パーク1現在料金
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
        html ="西口パーク１"
        html += "<table>"
        html += "<tr>"
        for p1_line_number in p1_line_numbers:
            html += f"<td>{lines[p1_line_number - 1]}</td>"
        html += "</tr>"
        html += "</table>"
        self.textBrowser_4.setHtml(html)

        ##パーク2現在料金
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
        html +="西口パーク2"
        html += "<table>"
        html += "<tr>"
        for p2_line_number in p2_line_numbers:
            html += f"<td>{lines[p2_line_number - 1]}</td>"
        html += "</tr>"
        html += "</table>"
        self.textBrowser_4.setHtml(html)
        
        ##パーク4現在料金
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
        html +="東口パーク4"
        html += "<table>"
        html += "<tr>"
        for p4_line_number in p4_line_numbers:
            html += f"<td>{lines[p4_line_number - 1]}</td>"
        html += "</tr>"
        html += "</table>"
        self.textBrowser_4.setHtml(html)
        
    def write_php(self):
        #######=============料金変更処理=================########
        ##作業ファイルの事前コピー
        shutil.copy('./ftp/temp/index.php', './ftp/temp/upload/index.php')
        
        ###書き換え処理　spinboxの値を取得して1行づつ書き込み　処理の簡素化できそうだけどめんどくさい。
        ##パーク１　平日
        file_path = "./ftp/temp/upload/index.php"
        line_number = 24
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)
        
        ##パーク１休日
        line_number = 31
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_2.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)
        
        ##パーク２平日
        line_number = 71
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_3.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)

        ##パーク２休日
        line_number = 78
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_4.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)
            
        ##パーク４平日
        line_number = 125
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_5.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)
        
        ##パーク4休日
        line_number = 132
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_6.value()}円</p>"
        with open(file_path, "r",encoding='utf-8') as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w",encoding='utf-8') as f:
            f.writelines(lines)
        park1wd = self.spinBox.value()
        park1hd = self.spinBox_2.value()
        park2wd = self.spinBox_3.value()
        park2hd = self.spinBox_4.value()
        park4wd = self.spinBox_5.value()
        park4hd = self.spinBox_6.value()
        logging.info('php_write success')
        
        ##書き込み後のphpを読み込み
        text = f"パーク１ 平日{park1wd} 休日{park1hd}\n" \
            f"パーク2 平日{park2wd} 休日{park2hd}\n" \
                f"パーク4 平日{park4wd} 休日{park4hd}"
        self.textBrowser_3.setText(text)
        logging.info(f'php_read success\n{text}')
        
    def finished(self): #メソッド名めんどくさくてそのままにしちゃってるけどftp_uploadとかがいいね
        ######=================FTPアップロード処理=================########
        ##意思確認
        msgBox = QMessageBox()
        msgBox.setText("設定を反映させてもよろしいですか？設定は即時反映されます。")
        msgBox.setWindowTitle("FTP_Upload")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
        response = msgBox.exec()

        ##ユーザがYesをおしたらwebページを開いて終了、そのまま終了
        ##ユーザがNoをおしたらreturnでmainWindowへ
        ##適用ボタンを押していなく./ftp/temp/upload/index.phpにファイルが存在しない場合はreturnでmainWindowへ
        if response == QMessageBox.StandardButton.Yes:
            
            if not os.path.exists(self.filename):
                msgBox = QMessageBox()
                msgBox.setText("適用ボタンをクリックしてから再度実行してください。")
                msgBox.setWindowTitle("ChangeNotFound")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Yes)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
                msgBox.exec()
                return
            
            else:
                try:
                    with FTP(self.ftpurl) as ftp:
                        ftp.login(self.ftpname, self.ftppass)
                        logging.info('ftp_upload_php_login success')
                        ftp.cwd(self.ftpdir1)
                        logging.info('ftp_upload_php_cwd www success')
                        ftp.cwd(self.ftpdir2)
                        logging.info('ftp_upload_php_cwd parking success')
                        with open(self.filename, 'rb') as f:
                            ftp.storlines(f'STOR {self.filename2}', f)
                            logging.info('ftp_upload_php_success')
                            ftp.quit()
                except Exception as e:
                    logging.error(f'upload_php_error{e}')
            
                msgBox = QMessageBox()
                msgBox.setText("設定が完了しました。更新後のwebページを確認して終了しますか？")
                msgBox.setWindowTitle("FTP_Upload_success")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
                if msgBox.exec() == QMessageBox.StandardButton.Yes:
                    webbrowser.open(self.weburl)
                    sys.exit()
                else:
                    sys.exit()
                
        else:
            return

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.get_now_index_php_disp()
    mainWindow.show()
    sys.exit(app.exec())