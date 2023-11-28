import os
import uuid
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi
from ThuatToan.am_ban import AmBan
from ThuatToan.loc_cany import loc_canny
from ThuatToan.loc_laplacian import loc_laplacian
from ThuatToan.loc_min import loc_min
from ThuatToan.loc_otsu import loc_otsu
from ThuatToan.loc_prewitt import loc_prewitt
from ThuatToan.loc_sobel import loc_sobel
from ThuatToan.loc_trung_binh import loc_avg
from ThuatToan.phep_co import phep_co
from ThuatToan.phep_gian import phep_gian
from ThuatToan.tich_chap import tichchap
from ThuatToan.loc_trung_vi import trungvi
from ThuatToan.loc_max import loc_max
import cv2
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 608)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 290, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white;") 
        self.cbThuattoan = QtWidgets.QComboBox(self.centralwidget)
        self.cbThuattoan.setGeometry(QtCore.QRect(150, 340, 400, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        self.cbThuattoan.setFont(font)
        self.cbThuattoan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbThuattoan.setAutoFillBackground(False)
        self.cbThuattoan.setObjectName("cbThuattoan")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.cbThuattoan.addItem("")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(670, 330, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.btnRun.setFont(font)
        self.btnRun.setObjectName("btnRun")
        self.btnRun.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRun.setStyleSheet(
            "QPushButton {"
            "   border: 2px solid #8f8f91;"  # Màu viền
            "   border-radius: 10px;"  # Bo góc
            "   background-color: #ededed;"  # Màu nền
            "   padding: 5px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #d3d3d3;"  # Màu nền khi di chuột qua
            "}"
            "QPushButton:pressed {"
            "   background-color: #b3b3b3;"  # Màu nền khi nhấn
            "}"
        )
        self.filePath = QtWidgets.QLineEdit(self.centralwidget)
        self.filePath.setGeometry(QtCore.QRect(150, 180, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.filePath.setFont(font)
        self.filePath.setObjectName("filePath")
        self.btnChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseFile.setGeometry(QtCore.QRect(670, 176, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnChooseFile.setFont(font)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.btnChooseFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnChooseFile.setStyleSheet(
            "QPushButton {"
            "   border: 2px solid #8f8f91;"  # Màu viền
            "   border-radius: 10px;"  # Bo góc
            "   background-color: #ededed;"  # Màu nền
            "   padding: 5px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #d3d3d3;"  # Màu nền khi di chuột qua
            "}"
            "QPushButton:pressed {"
            "   background-color: #b3b3b3;"  # Màu nền khi nhấn
            "}"
        )
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 600, 51))
        self.label_2.setStyleSheet("color: white;") 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Thêm mã sau vào hàm setupUi để hiển thị hình ảnh nền
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1036, 608))  # Đặt kích thước và vị trí cho hình ảnh nền
        background_image = QtGui.QPixmap("img/Background.jpg")  # Thay "background.jpg" bằng đường dẫn tới hình ảnh nền của bạn
        background_image = background_image.scaled(self.background_label.size(), QtCore.Qt.IgnoreAspectRatio)
        self.background_label.setPixmap(background_image)
        self.background_label.lower()  # Đảm bảo hình ảnh nền nằm phía sau
        # Điều chỉnh kích thước và vị trí của các phần tử khác
        # self.label.setGeometry(QtCore.QRect(150, 290, 191, 41))
        # self.cbThuattoan.setGeometry(QtCore.QRect(150, 340, 400, 41))
        # self.btnRun.setGeometry(QtCore.QRect(670, 330, 191, 61))
        # self.filePath.setGeometry(QtCore.QRect(150, 180, 501, 41))
        # self.btnChooseFile.setGeometry(QtCore.QRect(670, 176, 191, 51))
        # self.label_2.setGeometry(QtCore.QRect(440, 40, 191, 51))

        
        self.btnChooseFile.clicked.connect(self.browserFiles)
        self.btnRun.clicked.connect(self.HandleImg)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Xử lý ảnh"))
        self.label.setText(_translate("MainWindow", "Chọn thuật toán"))
        self.cbThuattoan.setItemText(0, _translate("MainWindow", "Lọc trung vị"))
        self.cbThuattoan.setItemText(1, _translate("MainWindow", "Âm bản"))
        self.cbThuattoan.setItemText(2, _translate("MainWindow", "Ảnh binary"))
        self.cbThuattoan.setItemText(3, _translate("MainWindow", "Mờ Ảnh"))
        self.cbThuattoan.setItemText(4, _translate("MainWindow", "Cân bằng Histogram"))
        self.cbThuattoan.setItemText(5, _translate("MainWindow", "Lọc Max"))
        self.cbThuattoan.setItemText(6, _translate("MainWindow", "Lọc Min"))
        self.cbThuattoan.setItemText(7, _translate("MainWindow", "Lọc Trung Bình"))
        self.cbThuattoan.setItemText(8, _translate("MainWindow", "Lọc Prewitt"))
        self.cbThuattoan.setItemText(9, _translate("MainWindow", "Lọc Sobel"))
        self.cbThuattoan.setItemText(10, _translate("MainWindow", "Lọc Laplacian"))
        self.cbThuattoan.setItemText(11, _translate("MainWindow", "Lọc Cany"))
        self.cbThuattoan.setItemText(12, _translate("MainWindow", "Lọc Otsu"))
        self.cbThuattoan.setItemText(13, _translate("MainWindow", "Phép Co"))
        self.cbThuattoan.setItemText(14, _translate("MainWindow", "Phép Giãn"))
        self.btnRun.setText(_translate("MainWindow", "Xử lý"))
        self.btnChooseFile.setText(_translate("MainWindow", "Chọn Ảnh"))
        self.label_2.setText(_translate("MainWindow", "Lê Văn Kiên - B20DCCN355"))

    def browserFiles(self):
        # Lấy đường dẫn của thư mục làm việc hiện tại
        current_directory = os.getcwd()
        relative_path = os.path.join(current_directory, "img")
        fname=QFileDialog.getOpenFileName(None,"Open file",relative_path,"Images (*.png *.jpg *.webp)")
        self.filePath.setText(fname[0])
    
    def HandleImg(self):
        filePath=self.filePath.text()
        thuattoan=self.cbThuattoan.currentText()
        if filePath!="":
            img_in=cv2.imread(filePath,0)
            print(filePath)
            if thuattoan=="Lọc trung vị":
                img_out=trungvi(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Loc Trung Vi", np.hstack([img_in, img_out]))
            elif thuattoan=="Mờ Ảnh":
                Kernel_1=(1/3)*np.array([[1/3,1/3,1/3],
                    [1/3,1/3,1/3],
                    [1/3,1/3,1/3]])
                img_out=tichchap(img_in,Kernel_1)
                img_out=np.uint8(img_out)
                cv2.imshow("Mờ Ảnh",np.hstack([img_in, img_out]))
            elif thuattoan=="Âm bản":
                img_out=AmBan(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Am ban",np.hstack([img_in, img_out]))
            elif thuattoan=="Ảnh binary":
                img_out=cv2.threshold(img_in,127,255,cv2.THRESH_BINARY)[1]
                cv2.imshow("Binary image",np.hstack([img_in, img_out]))
            elif thuattoan=="Cân bằng Histogram":
                img_out=cv2.equalizeHist(img_in)
                cv2.imshow("Equalize Histogram",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Max":
                img_out=loc_max(img_in)
                img_out=np.uint8(img_out)
                img_out = cv2.resize(img_out, (img_in.shape[1], img_in.shape[0]))
                cv2.imshow("Loc Max",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Min":
                img_out=loc_min(img_in)
                img_out=np.uint8(img_out)
                img_out = cv2.resize(img_out, (img_in.shape[1], img_in.shape[0]))
                cv2.imshow("Loc Min",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Trung Bình":
                img_out=loc_avg(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Loc Trung Bình",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Prewitt":
                img_out=loc_prewitt(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Loc Prewitt",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Sobel":
                img_out=loc_sobel(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Loc Sobel",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Laplacian":
                img_out=loc_laplacian(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Loc Laplacian",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Cany":
                img_out=loc_canny(img_in,low_threshold=50, high_threshold=150)
                img_out=np.uint8(img_out)
                cv2.imshow("Lọc Cany",np.hstack([img_in, img_out]))
            elif thuattoan=="Lọc Otsu":
                img_out=loc_otsu(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Lọc Otsu",np.hstack([img_in, img_out]))
            elif thuattoan=="Phép Co":
                img_in=cv2.threshold(img_in,127,255,cv2.THRESH_BINARY)[1]
                img_out=phep_co(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Phep Co",np.hstack([img_in, img_out]))
            elif thuattoan=="Phép Giãn":
                img_in=cv2.threshold(img_in,127,255,cv2.THRESH_BINARY)[1]
                img_out=phep_gian(img_in)
                img_out=np.uint8(img_out)
                cv2.imshow("Phep Gian",np.hstack([img_in, img_out]))
            else:
                print()
            cv2.waitKey(0)
            key = cv2.waitKey(0)
            # Kiểm tra xem nút bấm có phải là 's' không (mã ASCII của 's' là 115)
            if key == 115:
                file_name = str(uuid.uuid4()) + ".jpg"
                current_directory = os.getcwd()
                save_path = os.path.join(current_directory, "imgresult\\"+file_name)
                cv2.imwrite(save_path, img_out)
                print(f"Ảnh đã được lưu thành công tại {save_path}")
                cv2.destroyAllWindows()
        else:
            QtWidgets.QMessageBox.warning(None, "Lưu ý", "Hãy chọn một tệp ảnh trước khi xử lý.")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
# pip install pyqt5-tools
# pyuic5 -x yourform.ui -o file.py
