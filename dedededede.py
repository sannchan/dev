from PyQt6.QtCore import QTimer, QDateTime, QPointF
from PyQt6.QtGui import QColor, QBrush, QPen, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow

class AnalogClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Analog Clock')
        self.setGeometry(100, 100, 250, 250)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
       # qp.setRenderHint(QPainter.AntialiasingFlag)
        side = min(self.width(), self.height())
        qp.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        qp.setWindow(-50, -50, 100, 100)
       # qp.setPen(QPen(QColor(0, 0, 0), 1))
        qp.setBrush(QBrush(QColor(0, 0, 0)))
        qp.drawEllipse(QPointF(0, 0), 46, 46)
      #  qp.setPen(QPen(QColor(0, 0, 0), 2))
        for i in range(12):
            qp.drawLine(QPointF(0, -42), QPointF(0, -46))
            qp.rotate(30.0)
        qp.setPen(QPen(QColor(0, 0, 0), 1))
        for i in range(60):
            if (i % 5) != 0:
                qp.drawLine(QPointF(0, -44), QPointF(0, -46))
            qp.rotate(6.0)
        current_time = QDateTime.currentDateTime()
        hour_angle = 30 * (current_time.time().hour() % 12) + 0.5 * current_time.time().minute()
        print(f"H={hour_angle}")
        minute_angle = 6 * current_time.time().minute() + 0.1 * current_time.time().second()
        print(f"M={minute_angle}")
        second_angle = 6 * current_time.time().second()
        print(f"S={second_angle}")
        
        qp.setPen(QPen(QColor(0, 0, 255), 4))
        qp.save()
        qp.rotate(hour_angle)
        qp.drawLine(QPointF(0, 0), QPointF(0, -20))
        qp.restore()
        
        qp.setPen(QPen(QColor(0, 255, 0), 2))
        qp.save()
        qp.rotate(minute_angle)
        qp.drawLine(QPointF(0, 0), QPointF(0, -30))
        qp.restore()
        
        qp.setPen(QPen(QColor(255, 0, 0), 1))
        qp.save()
        qp.rotate(second_angle)
        qp.drawLine(QPointF(0, 0), QPointF(0, -35))
        qp.restore()

app = QApplication([])
clock = AnalogClock()
app.exec()
