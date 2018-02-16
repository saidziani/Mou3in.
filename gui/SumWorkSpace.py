from PyQt5 import QtCore, QtGui, QtWidgets
import functools, os
import PreProcess
from bs4 import BeautifulSoup

files, repertory = "", ""
index = 0

class SumWorkSpace(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1100, 650)
        Form.setGeometry(140, 80, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;color: #1ead8a;")
        self.closeWindow = Form.close
        self.newSent, self.itemIndex, self.method = [], -1, 1

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(340, 35, 420, 50))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500;font-size:30px")
        self.labelTitle.setText("Summarization pre-processing")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('mou3in-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(975, 15, 150, 80))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(650, 120, 200, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:#1c1c1c")

        self.pushButton_2 = QtWidgets.QPushButton(Form) 
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(850, 125, 60, 25))
        self.pushButton_2.setStyleSheet("background-color: #1c1c1c;color:#fff;font-size:14px;")
        self.pushButton_2.clicked.connect(self.getFiles)
        self.pushButton_2.setDisabled(True)

        self.labelList = QtWidgets.QLabel(Form)
        self.labelList.setGeometry(QtCore.QRect(760, 220, 250, 30))
        self.labelList.setObjectName("labelList")
        self.labelList.setStyleSheet("color: #1c1c1c;font-size:25px;")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(760, 260, 280, 300))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#f7f7f7;font-size:17px;font-weight:500;color:1c1c1c")
        self.listWidget.itemClicked.connect(self.chooseFile)

        self.pushButton_choose = QtWidgets.QPushButton(Form) 
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.pushButton_choose.setGeometry(QtCore.QRect(760, 575, 100, 30))
        self.pushButton_choose.setStyleSheet("background-color: #1c1c1c;color:#fff;font-size:14px;")
        self.pushButton_choose.mousePressEvent = functools.partial(self.processing, source_object=self.pushButton_choose)

        self.labelTextEdit = QtWidgets.QLabel(Form)
        self.labelTextEdit.setGeometry(QtCore.QRect(50, 220, 200, 30))
        self.labelTextEdit.setObjectName("labelTextEdit")
        self.labelTextEdit.setStyleSheet("color: #1c1c1c;font-size:25px;")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 260, 650, 230))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("color: #1c1c1c;font-size:16px;")

        self.pushButton_keep = QtWidgets.QPushButton(Form) 
        self.pushButton_keep.setObjectName("pushButton_keep")
        self.pushButton_keep.setGeometry(QtCore.QRect(600, 530, 100, 30))
        self.pushButton_keep.setStyleSheet("background-color: green;color:#fff;font-size:14px;")
        self.pushButton_keep.mousePressEvent = functools.partial(self.processing, source_object=self.pushButton_keep)

        self.pushButton_remove = QtWidgets.QPushButton(Form) 
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_remove.setGeometry(QtCore.QRect(480, 530, 100, 30))
        self.pushButton_remove.setStyleSheet("background-color: red;color:#fff;font-size:14px;")
        self.pushButton_remove.mousePressEvent = functools.partial(self.processing, source_object=self.pushButton_remove)

        self.labelRest = QtWidgets.QLabel(Form)
        self.labelRest.setGeometry(QtCore.QRect(50, 495, 50, 30))
        self.labelRest.setObjectName("labelRest")
        self.labelRest.setStyleSheet("color: #1c1c1c;font-size:14px;")

        self.pushButton_save = QtWidgets.QPushButton(Form) 
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setGeometry(QtCore.QRect(50, 530, 100, 30))
        self.pushButton_save.setStyleSheet("background-color: #1c1c1c;color:#fff;font-size:14px;")
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_save.setDisabled(True)

        self.pushButton_skip = QtWidgets.QPushButton(Form) 
        self.pushButton_skip.setObjectName("pushButton_skip")
        self.pushButton_skip.setGeometry(QtCore.QRect(600, 530, 100, 30))
        self.pushButton_skip.setStyleSheet("background-color: blue;color:#fff;font-size:14px;")
        self.pushButton_skip.mousePressEvent = functools.partial(self.processing, source_object=self.pushButton_skip)
        self.pushButton_skip.setVisible(False)


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 150, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:#1c1c1c")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(300, 120, 100, 30))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText('Classic')
        self.radioButton.clicked.connect(self.enable)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 120, 100, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText('XML')
        self.radioButton_2.clicked.connect(self.enable)

        self.pushButton_save.setDisabled(True)
        self.pushButton_choose.setDisabled(True)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mo3in."))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Choose files or directory."))
        self.label_4.setText(_translate("Form", "Choose file format."))
        self.labelRest.setText(_translate("Form", "0/0"))
        self.labelTextEdit.setText(_translate("Form", "Sentence"))
        self.labelList.setText(_translate("Form", "Files"))
        self.pushButton_2.setText(_translate("Form", "..."))
        self.pushButton_keep.setText(_translate("Form", "Keep"))
        self.pushButton_remove.setText(_translate("Form", "Remove"))
        self.pushButton_skip.setText(_translate("Form", "Skip"))
        self.pushButton_save.setText(_translate("Form", "Save"))
        self.pushButton_choose.setText(_translate("Form", "Select"))


    def retour(self, event):
        self.closeWindow()


    def enable(self):
        self.pushButton_2.setDisabled(False)

    def getFiles(self):
        global files
        global repertory

        self.pushButton_choose.setDisabled(False)

        filter = ""
        if self.radioButton.isChecked():
            filter = ""
            self.method = 1
        if self.radioButton_2.isChecked():
            filter = "XML (*.xml)"
            self.method = 2

        files = QtWidgets.QFileDialog.getOpenFileNames(None, "Choose your files", "", filter)

        if len(files[0]) > 0:
            repertory = "/".join(str(files[0][0]).split('/')[:-1])
            self.files = files[0]
            for file in self.files:
                file = str(file).split('/')[-1]
                self.listWidget.addItem(file)


    def chooseFile(self, item):
        for index in range(self.listWidget.count()):
            if self.listWidget.item(index).text() == item.text():
                self.itemIndex = index
        preProcess = PreProcess.PreProcess()
        content = preProcess.getArticleContent(repertory+"/"+item.text())
        if self.method == 1:
            self.sents = preProcess.getSents(content)
            size = len(self.sents)
        else:
            size, self.sents = preProcess.getXMLsents(content)

        self.labelRest.setText('0/'+str(size))
        self.file = item.text()
        self.newSent = []
        self.pushButton_save.setDisabled(True) 
        

    def processing(self, event, source_object=None):
        self.pushButton_choose.setDisabled(True)
        self.pushButton_keep.setVisible(True) 
        self.pushButton_remove.setVisible(True)
        self.listWidget.setDisabled(True)
        global index
        preProcess = PreProcess.PreProcess()
        if source_object.objectName() == "pushButton_choose":
            index = 0
            self.textEdit.clear()
            if self.method == 1:
                sent = self.sents[index]
            else:
                sent = preProcess.getXMLtext(self.sents[index][0])
                if self.sents[index][1] == 0:
                    self.pushButton_skip.setVisible(True)
                    self.pushButton_keep.setVisible(False) 
                    self.pushButton_remove.setVisible(False)
                else:
                    self.pushButton_skip.setVisible(False)
                    self.pushButton_keep.setVisible(True) 
                    self.pushButton_remove.setVisible(True)
            self.textEdit.setText(sent)
        else:
            sent = ""
            if self.method == 1:
                sent = self.sents[index]
            else:
                sent = preProcess.getXMLtext(self.sents[index][0])
                if self.sents[index][1] == 0:
                    self.pushButton_skip.setVisible(True)
                    self.pushButton_keep.setVisible(False) 
                    self.pushButton_remove.setVisible(False)
                else:
                    self.pushButton_skip.setVisible(False)
                    self.pushButton_keep.setVisible(True) 
                    self.pushButton_remove.setVisible(True)
            self.textEdit.setText(sent)
            self.labelRest.setText(str(index+1)+'/'+str(len(self.sents))) 
            if source_object.objectName() == "pushButton_keep":
                self.newSent.append("<source id='"+str(index+1)+"' operation='S'>﻿\n"+sent+"\n</source>")
            elif source_object.objectName() == "pushButton_remove":
                self.newSent.append("<source id='"+str(index+1)+"' operation='R'>\n﻿"+sent+"\n</source>")
            elif source_object.objectName() == "pushButton_skip":
                self.newSent.append(str(self.sents[index][0]))
            index += 1
            if index < len(self.sents):
                if self.method == 1:
                    sent = self.sents[index]
                else:
                    sent = preProcess.getXMLtext(self.sents[index][0])
                    if self.sents[index][1] == 0:
                        self.pushButton_skip.setVisible(True)
                        self.pushButton_keep.setVisible(False) 
                        self.pushButton_remove.setVisible(False)
                    else:
                        self.pushButton_skip.setVisible(False)
                        self.pushButton_keep.setVisible(True) 
                        self.pushButton_remove.setVisible(True)
                self.textEdit.setText(sent)
            if index >= len(self.sents):
                self.pushButton_save.setDisabled(False)    
                self.pushButton_keep.setVisible(False) 
                self.pushButton_remove.setVisible(False) 
                self.pushButton_skip.setVisible(False)

            

    def save(self):
        withoutExt = ".".join(self.file.split('.')[:-1])
        fileName = repertory+"/_preprop/prep_"+withoutExt+".xml"
        if not os.path.exists(repertory+"/_preprop"):
            os.makedirs(repertory+"/_preprop")
        output = open(fileName, 'w')
        head = "<?xml version='1.0' encoding='UTF-8'?>\n<file>\n"
        foot = "\n</file>"
        toWrite = "\n".join(self.newSent)
        output.write(head); output.write(toWrite); output.write(foot)
        self.textEdit.setText('')
        self.listWidget.takeItem(self.itemIndex)
        self.pushButton_choose.setDisabled(False)
        self.listWidget.setDisabled(False)
        self.labelRest.setText("0/0") 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SumWorkSpace()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())