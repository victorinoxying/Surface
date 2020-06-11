import sys
import threading
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from UI.predictWindow import Ui_formResult
from Surface.lawWindow import LawWindow


class PredictWindow(QWidget, Ui_formResult):
    def __init__(self):
        super(PredictWindow, self).__init__()
        self.setupUi(self)
        self.loading_process = 0
        self.law_content = ''
        self.lawWindow = LawWindow()
        self.timer = QTimer(self.progress_predict)

        self.timer.timeout.connect(self.move_process)
        self.button_law1.clicked.connect(lambda: self.law_click(self.button_law1))
        self.button_law2.clicked.connect(lambda: self.law_click(self.button_law2))
        self.button_law3.clicked.connect(lambda: self.law_click(self.button_law3))

        self.timer.start(50)

    def law_click(self, label):
        # if self.is_loading < 100:
        #     return
        self.lawWindow.label_law_name.setText('刑法第'+label.text()+'条')
        self.lawWindow.show()

    def move_process(self):
        if self.progress_predict.value() == self.progress_predict.maximum():
            self.timer.stop()
        self.loading_process += 1
        self.progress_predict.setValue(self.loading_process)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    predictWindow = PredictWindow()
    predictWindow.show()
    sys.exit(app.exec_())
