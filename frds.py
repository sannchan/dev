import sys
from PyQt6.QtWidgets import QApplication, QMessageBox


def show_message_box():
    # メッセージボックスを作成する
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_message_box()
    sys.exit(app.exec())