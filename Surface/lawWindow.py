import sys
from PyQt5.QtWidgets import QApplication, QWidget
from UI.lawWindow import Ui_formLawContent


class LawWindow(QWidget, Ui_formLawContent):
    def __init__(self):
        super(LawWindow, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    lawWindow = LawWindow()
    lawWindow.show()
    sys.exit(app.exec_())
