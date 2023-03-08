import sys
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ウィンドウの作成
    w = QWidget()
    w.setWindowTitle('Hello PyQt6')
    w.setGeometry(100, 100, 300, 200)  # ウィンドウの位置とサイズを指定

    # ウィンドウを表示
    w.show()

    # アプリケーションを実行
    sys.exit(app.exec())
