from PyQt5 import QtCore, QtGui, QtWidgets
import functools

repertory = ""

class PosWorkSpace(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #0C2444;")
        self.closeWindow = Form.close
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(280, 35, 500, 30))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500;\n"
"font-size:20px")
        self.labelTitle.setText("POS Tagging")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('Mo3ini-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour

        self.label_3 = QtWidgets.QLineEdit(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 450, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFrame(False)
        self.label_3.setStyleSheet("background-color: #fff;border: 1px solid #0C2444;border-left:0px")
        self.label_3.setPlaceholderText('Exemple: Python ou Linux et ( Libre ou Puissant ) ')
        self.label_3.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(Form) 
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 50, 30))
        self.pushButton_2.setStyleSheet("background-color: #0C2444;\n"
"color:#fff;font-size:14px;border-top-right-radius: 15px;border-bottom-right-radius: 15px;")
        self.pushButton_2.clicked.connect(self.getDir)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mo3ini."))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "..."))
        

    def retour(self, event):
        self.closeWindow()

    def getDir(self):
        global repertory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        repertory = directory
        print(repertory)

        
    def openFile(self, item):
        import os
        file = repertory+"/"+item.text()
        os.system("subl "+file)


