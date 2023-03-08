import ftplib
from ftplib import FTP 
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication
import os
import sys
import configparser
import datetime as dt
import shutil
class Ui_mainWindow(object):
    
    def __init__(self):        
        dt_now = dt.datetime.now()
        logt = dt_now.strftime('%Y:%H:%M:%S')
        config = configparser.ConfigParser()
        config.read('ftp_config.ini')
        ftpname = config.get('useraccount', 'name')
        ftppass = config.get('useraccount', 'password')
        ftpurl = config.get('Remoteurl','url')
        ftpdir1 = config.get('RemoteDir','dir1')
        ftpdir2 = config.get('RemoteDir','dir2')
        self.var1 = 0
        self.var2 = 0
        if not os.path.exists('./ftp'):
            os.makedirs('./ftp')
        if not os.path.exists('./ftp/log'):
            os.makedirs('./ftp/log')
        if not os.path.exists('./ftp/temp'):
            os.makedirs('./ftp/temp')
        if not os.path.exists('./ftp/temp/upload'):
            os.makedirs('./ftp/temp/upload')
        with FTP(ftpurl) as ftp:
            ftp.login(ftpname, ftppass)
            print("Connect")
            ftp.cwd(ftpdir1)
            ftp.cwd(ftpdir2)
            print("chdir")
            ftp.retrlines('LIST')
            with open('./ftp/log/log.txt', 'a') as fp:
                fp.write('Get Remote Dir\n')
                ftp.retrlines('LIST', lambda line: fp.write(f'{logt}:{line}\n')) 
            with open("./ftp/temp/index.php", "wb") as f:
                ftp.retrbinary("RETR ./index.php", f.write)    
            ftp.quit()
        
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(578, 399)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 290, 361, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 340, 361, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(372, 300, 201, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.write_php)
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 170, 101, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox.setSingleStep(1)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(470, 170, 101, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_2.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_2.setSingleStep(1)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(360, 210, 101, 21))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_3.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_3.setSingleStep(1)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(470, 210, 101, 21))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_4.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_4.setSingleStep(1)
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(360, 250, 101, 21))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_5.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_5.setSingleStep(1)
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(470, 250, 101, 21))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setMaximum(9999)  # 入力できる最大値を指定
        self.spinBox_6.setMinimum(0)     # 入力できる最小値を指定
        self.spinBox_6.setSingleStep(1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 150, 60, 16))
        self.label_2.setObjectName("label_2")
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
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 170, 281, 111))
        self.textBrowser_3.setObjectName("textBrowser_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "駐車場料金変更"))
        self.pushButton.setText(_translate("mainWindow", "設定"))
        self.label.setText(_translate("mainWindow", "平日料金"))
        self.label_2.setText(_translate("mainWindow", "休日料金"))
        self.label_3.setText(_translate("mainWindow", "設定予定料金"))
        self.label_4.setText(_translate("mainWindow", "パーク１"))
        self.label_5.setText(_translate("mainWindow", "パーク２"))
        self.label_6.setText(_translate("mainWindow", "パーク４"))
        self.label_7.setText(_translate("mainWindow", "現在料金"))
    
    def get_now_index_php_disp(self):
        file_path = "./ftp/temp/index.php"
        p1_line_numbers = [22, 23, 24, 29, 30, 31] # 表示する行番号をリストで指定する
        p2_line_numbers = [69, 70, 71, 76, 77, 78] # 表示する行番号をリストで指定する
        p4_line_numbers = [123, 124, 125, 130, 131, 132] # 表示する行番号をリストで指定する
# PHPファイルを読み込む
        with open(file_path, "r") as f:
            lines = f.readlines()
        html ="西口パーク１"
        html += "<table>"
        html += "<tr>"
        for p1_line_number in p1_line_numbers:
            html += f"<td>{lines[p1_line_number - 1]}</td>"
        html += "</tr>"
        html += "</table>"
        self.textBrowser_4.setHtml(html)

        with open(file_path, "r") as f:
            lines = f.readlines()
        html +="西口パーク2"
        html += "<table>"
        html += "<tr>"
        for p2_line_number in p2_line_numbers:
            html += f"<td>{lines[p2_line_number - 1]}</td>"
        html += "</tr>"
        html += "</table>"
        self.textBrowser_4.setHtml(html)
        
        with open(file_path, "r") as f:
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
        shutil.copy('./ftp/temp/index.php', './ftp/temp/upload/index.php')
        file_path = "./ftp/temp/upload/index.php"
        print(self.spinBox.value())
        line_number = 24
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)
        
        line_number = 31
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_2.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)
            
        line_number = 71
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_3.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)
    
        line_number = 78
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_4.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)
            
        line_number = 125
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_5.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)
        
        line_number = 132
        new_content = f"\t\t\t<p class=\"line3\">{self.spinBox_6.value()}円</p>"
        with open(file_path, "r") as f:
            lines = f.readlines()
            lines[line_number - 1] = new_content + "\n"
        with open(file_path, "w") as f:
            f.writelines(lines)

        self.finished()
    
    def finished(self):
        msgBox = QMessageBox()
        msgBox.setText("Are you sure you want to quit?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.setDefaultButton(QMessageBox.StandardButton.No)

    # メッセージボックスを表示し、ユーザーからの応答を取得する
        response = msgBox.exec()

    # ユーザーが「Yes」を選択した場合、アプリケーションを終了する
        if response == QMessageBox.StandardButton.Yes:
            sys.exit()

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.get_now_index_php_disp()
    mainWindow.show()
    sys.exit(app.exec())