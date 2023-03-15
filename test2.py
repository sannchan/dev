from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 背景画像を表示するためのラベルを作成
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 453, 244)

        # ファイル選択ボタンを作成
        self.select_file_button = QPushButton("ファイルを選択", self)
        self.select_file_button.setGeometry(10, 10, 100, 30)
        self.select_file_button.clicked.connect(self.select_file)

    def select_file(self):
        # ファイル選択ダイアログを表示
        file_path, _ = QFileDialog.getOpenFileName(
            self, "ファイルを選択", "", "画像ファイル (*.png *.jpg *.jpeg)")

        if file_path:
            # 画像を読み込み、背景に設定
            pixmap = QPixmap(file_path)
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
            
    def analogclock(self):
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
