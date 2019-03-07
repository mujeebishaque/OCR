
from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
from tkinter import messagebox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1038, 521)
        MainWindow.setMaximumSize(QtCore.QSize(1100, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 40, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(460, 100, 561, 251))
        self.textbox.setObjectName("textbox")
        self.select_img = QtWidgets.QPushButton(self.centralwidget)
        self.select_img.setGeometry(QtCore.QRect(150, 400, 131, 41))
        self.select_img.setObjectName("select_img")
        self.img_txt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_txt_btn.setGeometry(QtCore.QRect(680, 400, 131, 41))
        self.img_txt_btn.setObjectName("img_txt_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 470, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.img_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img_lbl.setGeometry(QtCore.QRect(30, 70, 411, 301))
        self.img_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.img_lbl.setText("")
        self.img_lbl.setObjectName("img_lbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.select_img.clicked.connect(self.set_image)
        self.img_txt_btn.clicked.connect(self.im2txt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python OCR"))
        self.label.setText(_translate("MainWindow", "OCR Python GUI Application"))
        self.select_img.setText(_translate("MainWindow", "Select Image"))
        self.img_txt_btn.setText(_translate("MainWindow", "Convert Image To Text"))
        self.label_2.setText(_translate("MainWindow", "Made with <3 @ 2019"))
 
    def set_image(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files(*.jpg *.jpeg *.png)")
        
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.img_lbl.width(), self.img_lbl.height(), QtCore.Qt.KeepAspectRatio)
            self.img_lbl.setPixmap(pixmap)
            self.img_lbl.setAlignment(QtCore.Qt.AlignCenter) 
            #url = QUrl.fromLocalFile(fileName)
            self.URL_OF_IMG = pathlib.Path(fileName)

    def im2txt(self):
        import argparse
        import cv2
        import os
        try:
            from PIL import Image
        except ImportError:
            import Image
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'OCR', 'Tesseract-OCR', 'tesseract.exe')
        # load the example image and convert it to grayscale
        image = cv2.imread(str(self.URL_OF_IMG))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        self.textbox.append(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

