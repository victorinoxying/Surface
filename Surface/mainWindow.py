import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal
from UI.mainWindow import Ui_MainWindow
from Surface.predictWindow import PredictWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    law_signal = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.button_submit.clicked.connect(self.click_submit)
        self.predictWindow = PredictWindow()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def click_submit(self):
        content = self.text_content.toPlainText()
        self.predictWindow.law_content = content
        self.hide()
        self.predictWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
