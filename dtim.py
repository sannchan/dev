import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer, QTime, Qt


class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ウィンドウのサイズとタイトルを設定
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle('Digital Clock')
        
        # ラベルを作成し、ウィンドウの中央に配置
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 200, 100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # タイマーを設定して、1秒ごとに時刻を更新
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        
    def update_time(self):
        # 現在時刻を取得し、時刻の文字列を作成
        current_time = QTime.currentTime()
        time_str = current_time.toString('hh:mm:ss')
        
        # ラベルに時刻の文字列を設定
        self.label.setText(time_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
