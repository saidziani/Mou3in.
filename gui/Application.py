from PyQt5 import QtCore, QtGui, QtWidgets
import SumWorkSpace

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1100, 650)
        Form.setGeometry(140, 80, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #fff;color: #1ead8a;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hideWindow = Form.hide

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 400, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(640, 400, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 400, 21, 51))

        self.label_3.setObjectName("label_3")

        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        pixmap = QtGui.QPixmap('mou3in-logo.png').scaledToWidth(200)
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(450, 100, 220, 200))

        self.label.mousePressEvent = self.openSum
        # self.label_2.mousePressEvent = self.openSum

        self.label_3.setStyleSheet("font-weight:100")
        self.label_2.setStyleSheet("font-weight:600")
        self.label.setStyleSheet("font-weight:600")


        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_5.setObjectName("label_5")

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label_5.setPixmap(pixmap1)
        self.label_5.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label_5.mousePressEvent = self.retour


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mou3ini."))
        self.label.setText(_translate("Form", "Summarization"))
        self.label_2.setText(_translate("Form", "POS Tagging"))
        self.label_3.setText(_translate("Form", " |"))
        self.label_5.setText(_translate("Form", ""))


    def openSum(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = SumWorkSpace.SumWorkSpace()
        self.ui.setupUi(self.window)
        self.window.show()


    # def openSum(self, event):
    #     self.window = QtWidgets.QWidget()
    #     self.ui = SearchSpaceVec.SearchSpaceVec()
    #     self.ui.setupUi(self.window)
    #     self.window.show()


    def retour(self, event):
        Form.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
