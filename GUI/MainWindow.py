# -*- coding: utf-8 -*-

# Form generated from reading UI file 'mainwindow.ui'

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(695, 695)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 560, 301, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(205, 171, 143);")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(51, 209, 122);")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nonpoland_in_lcd = QLCDNumber(self.verticalLayoutWidget)
        self.nonpoland_in_lcd.setObjectName(u"nonpoland_in_lcd")

        self.horizontalLayout_3.addWidget(self.nonpoland_in_lcd)

        self.nonpoland_out_lcd = QLCDNumber(self.verticalLayoutWidget)
        self.nonpoland_out_lcd.setObjectName(u"nonpoland_out_lcd")

        self.horizontalLayout_3.addWidget(self.nonpoland_out_lcd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(380, 560, 301, 91))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.verticalLayout_4.addWidget(self.label_15)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"background-color: rgb(87, 227, 137);")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_17 = QLabel(self.verticalLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_8.addWidget(self.label_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.poland_in_lcd = QLCDNumber(self.verticalLayoutWidget_3)
        self.poland_in_lcd.setObjectName(u"poland_in_lcd")

        self.horizontalLayout_9.addWidget(self.poland_in_lcd)

        self.poland_out_lcd = QLCDNumber(self.verticalLayoutWidget_3)
        self.poland_out_lcd.setObjectName(u"poland_out_lcd")

        self.horizontalLayout_9.addWidget(self.poland_out_lcd)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(460, 110, 221, 171))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.set_time_spinbox = QSpinBox(self.verticalLayoutWidget_4)
        self.set_time_spinbox.setObjectName(u"set_time_spinbox")
        self.set_time_spinbox.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setBold(False)
        self.set_time_spinbox.setFont(font1)
        self.set_time_spinbox.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.set_time_spinbox)

        self.time_unit_combobox = QComboBox(self.verticalLayoutWidget_4)
        self.time_unit_combobox.addItem("")
        self.time_unit_combobox.addItem("")
        self.time_unit_combobox.addItem("")
        self.time_unit_combobox.setObjectName(u"time_unit_combobox")
        self.time_unit_combobox.setMaximumSize(QSize(16777215, 25))
        self.time_unit_combobox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.time_unit_combobox)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.start_btn = QPushButton(self.verticalLayoutWidget_4)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout_5.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.verticalLayoutWidget_4)
        self.stop_btn.setObjectName(u"stop_btn")

        self.verticalLayout_5.addWidget(self.stop_btn)

        self.close_btn = QPushButton(self.centralwidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(590, 660, 89, 25))
        self.timer_label = QLabel(self.centralwidget)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setGeometry(QRect(460, 470, 221, 49))
        self.timer_label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 50, 381, 501))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.video_label = QLabel(self.verticalLayoutWidget_2)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setAutoFillBackground(True)
        self.video_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.video_label)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.label_5)

        self.video_process_label = QLabel(self.verticalLayoutWidget_2)
        self.video_process_label.setObjectName(u"video_process_label")
        self.video_process_label.setAutoFillBackground(True)
        self.video_process_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.video_process_label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 681, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgb(153, 193, 241);\n"
"border-color: rgb(26, 95, 180);")
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(460, 340, 221, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.selected_file_label = QLabel(self.verticalLayoutWidget_5)
        self.selected_file_label.setObjectName(u"selected_file_label")
        self.selected_file_label.setMaximumSize(QSize(16777215, 20))
        self.selected_file_label.setFont(font1)

        self.verticalLayout_2.addWidget(self.selected_file_label)

        self.browse_btn = QPushButton(self.verticalLayoutWidget_5)
        self.browse_btn.setObjectName(u"browse_btn")

        self.verticalLayout_2.addWidget(self.browse_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bee Counter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Non Poland BEE</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>  IN</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Poland BEE</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"IN", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Set Timmer</p></body></html>", None))
        self.time_unit_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"sec", None))
        self.time_unit_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"min", None))
        self.time_unit_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"hour", None))

        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">00:00:00</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Raw Video</span></p></body></html>", None))
        self.video_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Processing Video</span></p></body></html>", None))
        self.video_process_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">BEE COUNTING</p></body></html>", None))
        self.selected_file_label.setText("")
        self.browse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse Video", None))
    # retranslateUi

