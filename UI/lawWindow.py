# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lawWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formLawContent(object):
    def setupUi(self, formLawContent):
        formLawContent.setObjectName("formLawContent")
        formLawContent.resize(998, 618)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        formLawContent.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(formLawContent)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_law_name = QtWidgets.QLabel(formLawContent)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_law_name.setFont(font)
        self.label_law_name.setObjectName("label_law_name")
        self.verticalLayout.addWidget(self.label_law_name, 0, QtCore.Qt.AlignHCenter)
        self.text_law_content = QtWidgets.QTextEdit(formLawContent)
        self.text_law_content.setEnabled(False)
        self.text_law_content.setObjectName("text_law_content")
        self.verticalLayout.addWidget(self.text_law_content)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(formLawContent)
        QtCore.QMetaObject.connectSlotsByName(formLawContent)

    def retranslateUi(self, formLawContent):
        _translate = QtCore.QCoreApplication.translate
        formLawContent.setWindowTitle(_translate("formLawContent", "法律条文"))
        self.label_law_name.setText(_translate("formLawContent", "刑法第 条"))

