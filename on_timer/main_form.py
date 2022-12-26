# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 503)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"font: 500 italic 16pt \"Yrsa Medium\";")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.timeEdit_timer = QTimeEdit(Form)
        self.timeEdit_timer.setObjectName(u"timeEdit_timer")
        self.timeEdit_timer.setStyleSheet(u"font: italic 16pt \"Sans Serif\";")

        self.horizontalLayout_3.addWidget(self.timeEdit_timer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dial_timer = QDial(Form)
        self.dial_timer.setObjectName(u"dial_timer")
        self.dial_timer.setMaximum(120)

        self.horizontalLayout_2.addWidget(self.dial_timer)

        self.lcdNumber_minutes = QLCDNumber(Form)
        self.lcdNumber_minutes.setObjectName(u"lcdNumber_minutes")
        font = QFont()
        font.setFamilies([u"Yrsa Medium"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        self.lcdNumber_minutes.setFont(font)

        self.horizontalLayout_2.addWidget(self.lcdNumber_minutes)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.dial_sound = QDial(Form)
        self.dial_sound.setObjectName(u"dial_sound")
        self.dial_sound.setMaximum(100)

        self.gridLayout.addWidget(self.dial_sound, 2, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"font: italic 16pt \"Sans Serif\";")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_status)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_OK = QPushButton(Form)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.horizontalLayout.addWidget(self.pushButton_OK)

        self.pushButton_Cancel = QPushButton(Form)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)
        self.dial_timer.valueChanged.connect(self.lcdNumber_minutes.display)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0442\u0430\u0439\u043c\u0435\u0440\u0430 \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445: ", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c:", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

