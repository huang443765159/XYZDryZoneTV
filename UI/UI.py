# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 690, 410))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.sale_info = QtWidgets.QLabel(self.groupBox)
        self.sale_info.setGeometry(QtCore.QRect(0, 20, 421, 240))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sale_info.setFont(font)
        self.sale_info.setText("")
        self.sale_info.setAlignment(QtCore.Qt.AlignCenter)
        self.sale_info.setObjectName("sale_info")
        self.shop_info = QtWidgets.QLabel(self.groupBox)
        self.shop_info.setGeometry(QtCore.QRect(0, 260, 421, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shop_info.setFont(font)
        self.shop_info.setText("")
        self.shop_info.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_info.setObjectName("shop_info")
        self.user_info = QtWidgets.QLabel(self.groupBox)
        self.user_info.setGeometry(QtCore.QRect(0, 330, 421, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_info.setFont(font)
        self.user_info.setText("")
        self.user_info.setAlignment(QtCore.Qt.AlignCenter)
        self.user_info.setObjectName("user_info")
        self.car_frame = QtWidgets.QLabel(self.groupBox)
        self.car_frame.setGeometry(QtCore.QRect(420, 20, 270, 172))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.car_frame.setFont(font)
        self.car_frame.setText("")
        self.car_frame.setObjectName("car_frame")
        self.qr_info = QtWidgets.QLabel(self.groupBox)
        self.qr_info.setGeometry(QtCore.QRect(440, 190, 218, 210))
        self.qr_info.setText("")
        self.qr_info.setObjectName("qr_info")
        self.btn_sale_info = QtWidgets.QToolButton(self.centralwidget)
        self.btn_sale_info.setGeometry(QtCore.QRect(10, 420, 200, 22))
        self.btn_sale_info.setObjectName("btn_sale_info")
        self.btn_car_frame = QtWidgets.QToolButton(self.centralwidget)
        self.btn_car_frame.setGeometry(QtCore.QRect(250, 420, 200, 22))
        self.btn_car_frame.setObjectName("btn_car_frame")
        self.btn_user_info = QtWidgets.QToolButton(self.centralwidget)
        self.btn_user_info.setGeometry(QtCore.QRect(490, 420, 200, 22))
        self.btn_user_info.setObjectName("btn_user_info")
        self.btn_qr_info = QtWidgets.QToolButton(self.centralwidget)
        self.btn_qr_info.setGeometry(QtCore.QRect(10, 450, 200, 22))
        self.btn_qr_info.setObjectName("btn_qr_info")
        self.btn_shop_info = QtWidgets.QToolButton(self.centralwidget)
        self.btn_shop_info.setGeometry(QtCore.QRect(250, 450, 200, 22))
        self.btn_shop_info.setObjectName("btn_shop_info")
        self.btn_clear = QtWidgets.QToolButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(490, 450, 200, 22))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DryTV"))
        self.groupBox.setTitle(_translate("MainWindow", "TV"))
        self.btn_sale_info.setText(_translate("MainWindow", "SALE_INFO"))
        self.btn_car_frame.setText(_translate("MainWindow", "CAR_FRAME"))
        self.btn_user_info.setText(_translate("MainWindow", "USER_INFO"))
        self.btn_qr_info.setText(_translate("MainWindow", "QR_INFO"))
        self.btn_shop_info.setText(_translate("MainWindow", "SHOP_INFO"))
        self.btn_clear.setText(_translate("MainWindow", "CLEAR"))