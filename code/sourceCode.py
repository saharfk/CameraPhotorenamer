import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox


# you can copy and run this code

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            global g
            g = path[0]


app = QApplication(sys.argv)
window = MainWindow()

whiteCam = True
blackCam = False
whiteNumber = 7000
blackNumber = 20000
old_name = g

g = str(g).split('/')
numberAndFormat = g[-1].split('_')[-1].split('.')
exist = True
stickyG = ''
for i in range(len(g) - 1):
    stickyG += g[i] + '/'

counter = 1
while exist:
    new_name = ''

    if whiteCam:
        new_name = stickyG + 'SAM_W_' + str(int(numberAndFormat[0]) + whiteNumber + counter) + '.' + numberAndFormat[1]
    elif blackCam:
        new_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + blackNumber + counter) + '.' + numberAndFormat[1]

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
    old_name = ''
    old_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + counter) + '.JPG'
    if os.path.isfile(old_name):
        exist = True
        numberAndFormat[1] = 'JPG'
    else:
        old_name = ''
        old_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + counter) + '.MP4'
        if os.path.isfile(old_name):
            exist = True
            numberAndFormat[1] = 'MP4'
        else:
            old_name = ''
            old_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + counter) + '.jpg'
            if os.path.isfile(old_name):
                exist = True
                numberAndFormat[1] = 'jpg'
            else:
                old_name = ''
                old_name = stickyG + 'SAM_' + str(int(numberAndFormat[0]) + counter) + '.mp4'
                if os.path.isfile(old_name):
                    exist = True
                    numberAndFormat[1] = 'mp4'
                else:
                    exist = False
    counter += 1

msg = QMessageBox()
msg.setWindowTitle("Success message")
msg.setText("All Files are renamed :)")
x = msg.exec_()  # this will show our messagebox
