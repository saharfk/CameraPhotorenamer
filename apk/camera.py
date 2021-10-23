from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            global g
            g = path[0]


setting = False
whiteCam = False
blackCam = False
if os.path.isfile('sample.txt'):
    file = open("sample.txt")
    a = file.read().split(' ')
    whiteNumber = int(a[0])
    blackNumber = int(a[1])
else:
    whiteNumber = 7000
    blackNumber = 20000
    file = open("sample.txt", 'w')
    file.write(str(whiteNumber) + ' ' + str(blackNumber))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 239)
        Dialog.setStyleSheet("background-color: rgb(195, 204, 191)")
        self.blackCam = QtWidgets.QPushButton(Dialog)
        self.blackCam.setGeometry(QtCore.QRect(50, 20, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.blackCam.setFont(font)
        self.blackCam.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.blackCam.setObjectName("blackCam")
        self.WhiteCam = QtWidgets.QPushButton(Dialog)
        self.WhiteCam.setGeometry(QtCore.QRect(240, 20, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.WhiteCam.setFont(font)
        self.WhiteCam.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.WhiteCam.setObjectName("WhiteCam")
        self.whitesubmit = QtWidgets.QPushButton(Dialog)
        self.whitesubmit.setGeometry(QtCore.QRect(260, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.whitesubmit.setFont(font)
        self.whitesubmit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.whitesubmit.setObjectName("whitesubmit")
        self.blacksubmit = QtWidgets.QPushButton(Dialog)
        self.blacksubmit.setGeometry(QtCore.QRect(260, 180, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.blacksubmit.setFont(font)
        self.blacksubmit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.blacksubmit.setObjectName("blacksubmit")
        self.whitetext = QtWidgets.QTextEdit(Dialog)
        self.whitetext.setGeometry(QtCore.QRect(123, 140, 121, 31))
        self.whitetext.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.whitetext.setObjectName("whitetext")
        self.whitetext.setPlainText(str(whiteNumber))
        self.blacktext = QtWidgets.QPlainTextEdit(Dialog)
        self.blacktext.setGeometry(QtCore.QRect(123, 180, 121, 31))
        self.blacktext.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.blacktext.setObjectName("blacktext")
        self.blacktext.setPlainText(str(blackNumber))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 149, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.blackCam.clicked.connect(self.blackCam1)
        self.WhiteCam.clicked.connect(self.whiteCam1)
        self.whitesubmit.clicked.connect(self.CamNumber)
        self.blacksubmit.clicked.connect(self.CamNumber)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.blackCam.setText(_translate("Dialog", "blackCam"))
        self.WhiteCam.setText(_translate("Dialog", "WhiteCam"))
        self.whitesubmit.setText(_translate("Dialog", "submit white"))
        self.blacksubmit.setText(_translate("Dialog", "submit black"))
        self.label.setText(_translate("Dialog", "White camera"))
        self.label_2.setText(_translate("Dialog", "Black camera"))

    def blackCam1(self):
        blackCam = True
        whiteCam = False
        g = dest
        old_name = g
        print(g)
        # my code
        g = str(g).split('/')
        numberAndFormat = g[-1].split('_')[-1].split('.')
        exist = True
        stickyG = ''
        for i in range(len(g) - 1):
            stickyG += g[i] + '/'

        counter = 0
        while exist:
            new_name = ''

            if whiteCam:
                new_name = stickyG + 'SAM_W_' + str(int(numberAndFormat[0]) + whiteNumber + counter) + '.' + \
                           numberAndFormat[1]
            elif blackCam:
                new_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + blackNumber + counter) + '.' + \
                           numberAndFormat[
                               1]

            if os.path.isfile(new_name):
                msg = QMessageBox()
                msg.setWindowTitle("fail message")
                msg.setText(new_name, " already exists please check the files and try again :(")
                x = msg.exec_()  # this will show our messagebox
                break
            else:
                # Rename the file
                os.rename(old_name, new_name)

            # ----------
            counter += 1

            number = str(int(numberAndFormat[0]) + counter)
            if len(number) < 4:
                number = number.zfill(4)
            old_name = stickyG + 'SAM_' + number + '.JPG'
            if os.path.isfile(old_name):
                exist = True
                numberAndFormat[1] = 'JPG'
            else:
                old_name = stickyG + 'SAM_' + number + '.MP4'
                if os.path.isfile(old_name):
                    exist = True
                    numberAndFormat[1] = 'MP4'
                else:
                    old_name = stickyG + 'SAM_' + number + '.jpg'
                    if os.path.isfile(old_name):
                        exist = True
                        numberAndFormat[1] = 'jpg'
                    else:
                        old_name = stickyG + 'SAM_' + number + '.mp4'
                        if os.path.isfile(old_name):
                            exist = True
                            numberAndFormat[1] = 'mp4'
                        else:
                            exist = False

        msg = QMessageBox()
        msg.setWindowTitle("Success message")
        msg.setText("All Files are renamed :)")
        x = msg.exec_()  # this will show our messagebox
        whiteCam = False
        blackCam = False
        sys.exit()

    def whiteCam1(self):
        whiteCam = True
        blackCam = False
        g = dest
        old_name = g
        # my code
        g = str(g).split('/')
        numberAndFormat = g[-1].split('_')[-1].split('.')
        exist = True
        stickyG = ''
        for i in range(len(g) - 1):
            stickyG += g[i] + '/'

        counter = 0
        while exist:
            new_name = ''

            if whiteCam:
                new_name = stickyG + 'SAM_W_' + str(int(numberAndFormat[0]) + whiteNumber + counter) + '.' + \
                           numberAndFormat[1]
            elif blackCam:
                new_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + blackNumber + counter) + '.' + \
                           numberAndFormat[
                               1]

            if os.path.isfile(new_name):
                msg = QMessageBox()
                msg.setWindowTitle("fail message")
                msg.setText(new_name, " already exists please check the files and try again :(")
                x = msg.exec_()  # this will show our messagebox
                break
            else:
                # Rename the file
                os.rename(old_name, new_name)

            # ----------
            counter += 1

            number = str(int(numberAndFormat[0]) + counter)
            if len(number) < 4:
                number = number.zfill(4)

            old_name = stickyG + 'SAM_' + number + '.JPG'
            if os.path.isfile(old_name):
                exist = True
                numberAndFormat[1] = 'JPG'
            else:
                old_name = stickyG + 'SAM_' + number + '.MP4'
                if os.path.isfile(old_name):
                    exist = True
                    numberAndFormat[1] = 'MP4'
                else:
                    old_name = stickyG + 'SAM_' + number + '.jpg'
                    if os.path.isfile(old_name):
                        exist = True
                        numberAndFormat[1] = 'jpg'
                    else:
                        old_name = stickyG + 'SAM_' + number + '.mp4'
                        if os.path.isfile(old_name):
                            exist = True
                            numberAndFormat[1] = 'mp4'
                        else:
                            exist = False

        msg = QMessageBox()
        msg.setWindowTitle("Success message")
        msg.setText("All Files are renamed :)")
        x = msg.exec_()  # this will show our messagebox
        whiteCam = False
        blackCam = False
        sys.exit()

    def CamNumber(self):
        whiteNumber = self.whitetext.toPlainText()
        file = open("sample.txt", 'w')
        file.write(str(whiteNumber) + ' ' + str(blackNumber))
        msg = QMessageBox()
        msg.setWindowTitle("Success message")
        msg.setText("submitted successfully:)")
        x = msg.exec_()  # this will show our messagebox
        sys.exit()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
dest = str(g)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
