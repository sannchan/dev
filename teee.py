import sys
from PyQt6.QtCore import Qt, QPoint, QTimer, QRect
from PyQt6.QtGui import QPixmap, QPainter, QTransform
from PyQt6.QtWidgets import QApplication, QWidget


class AnalogClock(QWidget):
   def __init__(self):
       super().__init__()

       # ウィンドウ設定
       self.setWindowTitle('Analog Clock')
       self.setGeometry(570, 570, 570, 570)

       # 画像ファイルを設定します
       self.bg_image = QPixmap('background.png')
       self.hour_hand_image = QPixmap('h.png')
       self.minute_hand_image = QPixmap('m.png')
       self.second_hand_image = QPixmap('s.png')

       # タイマーを設定して現在の時刻を更新
       timer = QTimer(self)
       timer.timeout.connect(self.update)
       timer.start(1000)

   def paintEvent(self, event):
       painter = QPainter(self)
       painter.setRenderHint(QPainter.RenderHint.Antialiasing)

       # 背景画像を描画
       painter.drawPixmap(QRect(0, 0, self.width(), self.height()), self.bg_image)

       # 時計の中心点を計算
       center = QPoint(self.width() // 2, self.height() // 2)

       # 時計の針の角度を計算
       from datetime import datetime
       now = datetime.now()
       hour_angle = -(30.0 * (now.hour % 12 + now.minute / 60))
       minute_angle = -(6.0 * (now.minute + now.second / 60))
       second_angle = -(6.0 * now.second)

       # 時針を描画
       self.draw_rotated_pixmap(painter, center, self.hour_hand_image, hour_angle, 65)

       # 分針を描画
       self.draw_rotated_pixmap(painter, center, self.minute_hand_image, minute_angle, 65)

       # 秒針を描画
       self.draw_rotated_pixmap(painter, center, self.second_hand_image, second_angle, 65)

   def draw_rotated_pixmap(self, painter, center, pixmap, angle, scale_percentage):
    painter.save()
    painter.translate(center)
    painter.rotate(-angle)
    
    new_width = int(pixmap.width() * (scale_percentage / 100))
    new_height = int(pixmap.height() * (scale_percentage / 100))
    scaled_pixmap = pixmap.scaled(new_width, new_height, Qt.AspectRatioMode.KeepAspectRatio)
    
    # 垂直反転の変換を適用
    transform = QTransform()
    transform.scale(1, -1)
    flipped_pixmap = scaled_pixmap.transformed(transform)
    
    painter.drawPixmap(-flipped_pixmap.width() // 2, -flipped_pixmap.height(), flipped_pixmap)
    painter.restore()

if __name__ == '__main__':
   app = QApplication(sys.argv)

   clock = AnalogClock()
   clock.show()

   sys.exit(app.exec())