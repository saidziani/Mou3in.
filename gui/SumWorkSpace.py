from PyQt5 import QtCore, QtGui, QtWidgets
import functools

files = ""

class SumWorkSpace(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1100, 650)
        Form.setGeometry(140, 80, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #0C2444;")
        self.closeWindow = Form.close
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(320, 35, 500, 50))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500;font-size:30px")
        self.labelTitle.setText("Summarization pre-processing")

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

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 450, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: #fff;border: 1px solid #0C2444;")

        self.pushButton_2 = QtWidgets.QPushButton(Form) 
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(720, 120, 50, 30))
        self.pushButton_2.setStyleSheet("background-color: #0C2444;\n"
"color:#fff;font-size:14px;")
        self.pushButton_2.clicked.connect(self.getFiles)

        self.labelList = QtWidgets.QLabel(Form)
        self.labelList.setGeometry(QtCore.QRect(800, 200, 150, 30))
        self.labelList.setObjectName("labelList")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(800, 260, 250, 300))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#f7f7f7;font-size:22px;font-weight:500;")

        self.pushButton_open = QtWidgets.QPushButton(Form) 
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_open.setGeometry(QtCore.QRect(800, 575, 100, 30))
        self.pushButton_open.setStyleSheet("background-color: #0C2444;color:#fff;font-size:14px;")


        self.labelTextEdit = QtWidgets.QLabel(Form)
        self.labelTextEdit.setGeometry(QtCore.QRect(50, 200, 150, 30))
        self.labelTextEdit.setObjectName("labelTextEdit")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 260, 650, 200))
        self.textEdit.setObjectName("textEdit")

        self.pushButton_keep = QtWidgets.QPushButton(Form) 
        self.pushButton_keep.setObjectName("pushButton_keep")
        self.pushButton_keep.setGeometry(QtCore.QRect(600, 500, 100, 30))
        self.pushButton_keep.setStyleSheet("background-color: #0C2444;color:#fff;font-size:14px;")

        self.pushButton_remove = QtWidgets.QPushButton(Form) 
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_remove.setGeometry(QtCore.QRect(480, 500, 100, 30))
        self.pushButton_remove.setStyleSheet("background-color: #0C2444;color:#fff;font-size:14px;")

        self.labelRest = QtWidgets.QLabel(Form)
        self.labelRest.setGeometry(QtCore.QRect(50, 465, 50, 30))
        self.labelRest.setObjectName("labelRest")
 
        self.pushButton_save = QtWidgets.QPushButton(Form) 
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setGeometry(QtCore.QRect(50, 500, 100, 30))
        self.pushButton_save.setStyleSheet("background-color: #0C2444;color:#fff;font-size:14px;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mo3ini."))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Veuillez choisir un repertoire ou un fichier"))
        self.labelRest.setText(_translate("Form", "5/12"))
        self.labelTextEdit.setText(_translate("Form", "Phrase à traiter"))
        self.labelList.setText(_translate("Form", "Ensemble des fichiers"))

        self.pushButton_2.setText(_translate("Form", "..."))
        self.pushButton_keep.setText(_translate("Form", "Keep"))
        self.pushButton_remove.setText(_translate("Form", "Remove"))
        self.pushButton_save.setText(_translate("Form", "Save"))
        self.pushButton_open.setText(_translate("Form", "Select"))


        

    def retour(self, event):
        self.closeWindow()

    def getFiles(self):
        global files
        files = QtWidgets.QFileDialog.getOpenFileNames()
        self.files = files[0]
        print(self.files[0])
        for file in self.files:
            file = str(file).split('/')[-1]
            self.listWidget.addItem(file)
        # self.listWidget.itemClicked.connect(self.addSelectItem)

        
    # def openFile(self, item):
    #     import os
    #     file = files+"/"+item.text()
    #     os.system("subl "+file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SumWorkSpace()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())