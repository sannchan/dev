from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

app = QApplication([])
window = QWidget()

# 画像の読み込み
pixmap = QPixmap("Image.png")

# 幅453、高さ244のQPixmapオブジェクトを作成
pixmap = pixmap.scaled(453, 244)

# 背景画像を表示するためのラベルを作成
background_label = QLabel(parent=window)
background_label.setPixmap(pixmap)
background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

window.show()
app.exec()