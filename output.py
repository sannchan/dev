from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 407)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 541, 341))
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 画像の読み込み
        pixmap = QtGui.QPixmap("Image.png")

        # QGraphicsSceneオブジェクトの作成
        scene = QtWidgets.QGraphicsScene()

        # QGraphicsPixmapItemオブジェクトの作成
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)

        # QGraphicsSceneにQGraphicsPixmapItemを追加
        scene.addItem(pixmap_item)

        # QGraphicsViewオブジェクトの作成
        self.graphicsView.setScene(scene)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

do = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
do.exec()
