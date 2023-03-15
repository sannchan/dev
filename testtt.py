import sys
import math
from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush

class AnalogClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 400)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
    #painter.setRenderHint(QPainter.)
        painter.translate(self.width() / 2, self.height() / 2)
        side = min(self.width(), self.height())
        painter.scale(side / 200, side / 200)

        self.draw_face(painter)
        now = QDateTime.currentDateTime()
        hour = now.time().hour() % 12
        minute = now.time().minute()
        second = now.time().second()
        self.draw_hands(painter, hour, minute, second)

    def draw_face(self, painter):
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawEllipse(-95, -95, 190, 190)

        pen.setWidth(1)
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)

        for i in range(12):
            hour_angle = i * 30
            hour_x = 80 * math.sin(math.radians(hour_angle))
            hour_y = -80 * math.cos(math.radians(hour_angle))
            painter.drawText(hour_x - 5, hour_y + 3, str(i+1))

    def draw_hands(self, painter, hour, minute, second):
        hour_angle = (hour + minute / 60) * 30
        minute_angle = minute * 6
        second_angle = second * 6

        painter.save()

        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(5)
        painter.setPen(pen)
        painter.rotate(hour_angle)
        painter.drawLine(0, 0, 0, -60)

        pen.setWidth(3)
        painter.setPen(pen)
        painter.rotate(minute_angle - hour_angle)
        painter.drawLine(0, 0, 0, -80)

        pen.setWidth(1)
        painter.setPen(pen)
        painter.rotate(second_angle - minute_angle)
        painter.drawLine(0, 0, 0, -80)

        painter.restore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec())