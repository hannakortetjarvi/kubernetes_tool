# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(1570, 834)
        Widget.setWindowTitle(u"Kubernetes Learning Tool")
        Widget.setStyleSheet(u"background-color: rgb(240, 255, 254);\n"
"font: 10pt \"Candara\";")
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 1551, 811))
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.frame = QFrame(self.loginPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(590, 150, 351, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(230, 430, 111, 51))
        self.loginButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;")
        self.userNameEdit = QLineEdit(self.frame)
        self.userNameEdit.setObjectName(u"userNameEdit")
        self.userNameEdit.setGeometry(QRect(42, 200, 271, 26))
        self.loginWarning = QLabel(self.frame)
        self.loginWarning.setObjectName(u"loginWarning")
        self.loginWarning.setGeometry(QRect(40, 230, 271, 20))
        self.loginWarning.setStyleSheet(u"color : red;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 180, 111, 20))
        self.stackedWidget.addWidget(self.loginPage)
        self.loggedPage = QWidget()
        self.loggedPage.setObjectName(u"loggedPage")
        self.menuPages = QStackedWidget(self.loggedPage)
        self.menuPages.setObjectName(u"menuPages")
        self.menuPages.setGeometry(QRect(320, 0, 1231, 811))
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayoutWidget_2 = QWidget(self.mainPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget_2)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)

        self.verticalLayout_7.addWidget(self.title)

        self.subMain = QLabel(self.verticalLayoutWidget_2)
        self.subMain.setObjectName(u"subMain")
        self.subMain.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.subMain)

        self.desc = QLabel(self.verticalLayoutWidget_2)
        self.desc.setObjectName(u"desc")
        self.desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.desc)

        self.labelMinikube = QLabel(self.verticalLayoutWidget_2)
        self.labelMinikube.setObjectName(u"labelMinikube")

        self.verticalLayout_7.addWidget(self.labelMinikube)

        self.labelKubectl = QLabel(self.verticalLayoutWidget_2)
        self.labelKubectl.setObjectName(u"labelKubectl")

        self.verticalLayout_7.addWidget(self.labelKubectl)

        self.textBrowser_7 = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_7.setObjectName(u"textBrowser_7")

        self.verticalLayout_7.addWidget(self.textBrowser_7)

        self.menuPages.addWidget(self.mainPage)
        self.exercisesPage = QWidget()
        self.exercisesPage.setObjectName(u"exercisesPage")
        self.exercisesPage.setStyleSheet(u"")
        self.stackedWidget_2 = QStackedWidget(self.exercisesPage)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 10, 1211, 801))
        self.exercisesMain = QWidget()
        self.exercisesMain.setObjectName(u"exercisesMain")
        self.verticalLayoutWidget_4 = QWidget(self.exercisesMain)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 1211, 801))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.title_4 = QLabel(self.verticalLayoutWidget_4)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setMaximumSize(QSize(16777215, 50))
        self.title_4.setFont(font)

        self.verticalLayout_10.addWidget(self.title_4)

        self.sub_4 = QLabel(self.verticalLayoutWidget_4)
        self.sub_4.setObjectName(u"sub_4")
        self.sub_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_10.addWidget(self.sub_4)

        self.desc_4 = QLabel(self.verticalLayoutWidget_4)
        self.desc_4.setObjectName(u"desc_4")

        self.verticalLayout_10.addWidget(self.desc_4)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1209, 687))
        self.verticalLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 1211, 691))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget_7)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 155))
        self.widget.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1201, 152))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.exOneImage = QLabel(self.horizontalLayoutWidget)
        self.exOneImage.setObjectName(u"exOneImage")
        self.exOneImage.setMaximumSize(QSize(150, 150))
        self.exOneImage.setPixmap(QPixmap(u"../../images/ex1.png"))
        self.exOneImage.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.exOneImage)

        self.exerciseOneButton = QPushButton(self.horizontalLayoutWidget)
        self.exerciseOneButton.setObjectName(u"exerciseOneButton")
        self.exerciseOneButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exerciseOneButton.sizePolicy().hasHeightForWidth())
        self.exerciseOneButton.setSizePolicy(sizePolicy)
        self.exerciseOneButton.setMinimumSize(QSize(0, 40))
        self.exerciseOneButton.setFont(font)
        self.exerciseOneButton.setStyleSheet(u"border: none;\n"
"color: rgb(0, 85, 255);")
        self.exerciseOneButton.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.exerciseOneButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.exercisesMain)
        self.exerciseOne = QWidget()
        self.exerciseOne.setObjectName(u"exerciseOne")
        self.exerciseOne.setStyleSheet(u"")
        self.exerciseOnePages = QStackedWidget(self.exerciseOne)
        self.exerciseOnePages.setObjectName(u"exerciseOnePages")
        self.exerciseOnePages.setGeometry(QRect(-10, 0, 1221, 801))
        self.one = QWidget()
        self.one.setObjectName(u"one")
        self.verticalLayoutWidget_8 = QWidget(self.one)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 0, 1211, 801))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.title_7 = QLabel(self.verticalLayoutWidget_8)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setMaximumSize(QSize(16777215, 50))
        self.title_7.setFont(font)

        self.verticalLayout_17.addWidget(self.title_7)

        self.sub_6 = QLabel(self.verticalLayoutWidget_8)
        self.sub_6.setObjectName(u"sub_6")
        self.sub_6.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_17.addWidget(self.sub_6)

        self.exerciseOneOneButton = QPushButton(self.verticalLayoutWidget_8)
        self.exerciseOneOneButton.setObjectName(u"exerciseOneOneButton")

        self.verticalLayout_17.addWidget(self.exerciseOneOneButton)

        self.exerciseOneTwoButton = QPushButton(self.verticalLayoutWidget_8)
        self.exerciseOneTwoButton.setObjectName(u"exerciseOneTwoButton")

        self.verticalLayout_17.addWidget(self.exerciseOneTwoButton)

        self.exerciseOneThreeButton = QPushButton(self.verticalLayoutWidget_8)
        self.exerciseOneThreeButton.setObjectName(u"exerciseOneThreeButton")

        self.verticalLayout_17.addWidget(self.exerciseOneThreeButton)

        self.exerciseOneFourButton = QPushButton(self.verticalLayoutWidget_8)
        self.exerciseOneFourButton.setObjectName(u"exerciseOneFourButton")

        self.verticalLayout_17.addWidget(self.exerciseOneFourButton)

        self.label_7 = QLabel(self.verticalLayoutWidget_8)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.exerciseOnePages.addWidget(self.one)
        self.oneOne = QWidget()
        self.oneOne.setObjectName(u"oneOne")
        self.layoutWidget_2 = QWidget(self.oneOne)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 0, 1201, 791))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevOneOne = QPushButton(self.layoutWidget_2)
        self.prevOneOne.setObjectName(u"prevOneOne")
        self.prevOneOne.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.prevOneOne)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.nextOneOne = QPushButton(self.layoutWidget_2)
        self.nextOneOne.setObjectName(u"nextOneOne")

        self.horizontalLayout.addWidget(self.nextOneOne)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.infoBrowser_2 = QTextBrowser(self.layoutWidget_2)
        self.infoBrowser_2.setObjectName(u"infoBrowser_2")
        self.infoBrowser_2.setMinimumSize(QSize(0, 210))
        self.infoBrowser_2.setMaximumSize(QSize(16777215, 16777215))
        self.infoBrowser_2.setFont(font)
        self.infoBrowser_2.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top: 10px;")

        self.verticalLayout_8.addWidget(self.infoBrowser_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clusterImage = QLabel(self.layoutWidget_2)
        self.clusterImage.setObjectName(u"clusterImage")
        self.clusterImage.setMinimumSize(QSize(300, 300))
        self.clusterImage.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.clusterImage)

        self.textBrowser_2 = QTextBrowser(self.layoutWidget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(0, 350))
        self.textBrowser_2.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout_3.addWidget(self.textBrowser_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.textBrowser = QTextBrowser(self.layoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"border:none;")

        self.verticalLayout_8.addWidget(self.textBrowser)

        self.progressBarOne = QProgressBar(self.layoutWidget_2)
        self.progressBarOne.setObjectName(u"progressBarOne")
        self.progressBarOne.setValue(24)

        self.verticalLayout_8.addWidget(self.progressBarOne)

        self.verticalLayout_8.setStretch(1, 6)
        self.exerciseOnePages.addWidget(self.oneOne)
        self.oneTwo = QWidget()
        self.oneTwo.setObjectName(u"oneTwo")
        self.layoutWidget_3 = QWidget(self.oneTwo)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 0, 1211, 801))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.prevOneTwo = QPushButton(self.layoutWidget_3)
        self.prevOneTwo.setObjectName(u"prevOneTwo")

        self.horizontalLayout_4.addWidget(self.prevOneTwo)

        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.nextOneTwo = QPushButton(self.layoutWidget_3)
        self.nextOneTwo.setObjectName(u"nextOneTwo")

        self.horizontalLayout_4.addWidget(self.nextOneTwo)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.infoBrowser_4 = QTextBrowser(self.layoutWidget_3)
        self.infoBrowser_4.setObjectName(u"infoBrowser_4")
        self.infoBrowser_4.setMaximumSize(QSize(16777215, 150))
        self.infoBrowser_4.setStyleSheet(u"border-top: 1px solid gray;")

        self.verticalLayout_14.addWidget(self.infoBrowser_4)

        self.textBrowser_4 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_4.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_14.addWidget(self.textBrowser_4)

        self.textBrowser_3 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_14.addWidget(self.textBrowser_3)

        self.textBrowser_5 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_5.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_14.addWidget(self.textBrowser_5)

        self.textBrowser_6 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.verticalLayout_14.addWidget(self.textBrowser_6)

        self.progressBarOne_3 = QProgressBar(self.layoutWidget_3)
        self.progressBarOne_3.setObjectName(u"progressBarOne_3")
        self.progressBarOne_3.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBarOne_3)

        self.verticalLayout_14.setStretch(1, 6)
        self.exerciseOnePages.addWidget(self.oneTwo)
        self.oneThree = QWidget()
        self.oneThree.setObjectName(u"oneThree")
        self.layoutWidget_4 = QWidget(self.oneThree)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 0, 1211, 801))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prevOneThree = QPushButton(self.layoutWidget_4)
        self.prevOneThree.setObjectName(u"prevOneThree")

        self.horizontalLayout_5.addWidget(self.prevOneThree)

        self.label_5 = QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.nextOneThree = QPushButton(self.layoutWidget_4)
        self.nextOneThree.setObjectName(u"nextOneThree")

        self.horizontalLayout_5.addWidget(self.nextOneThree)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)

        self.infoBrowser_5 = QTextBrowser(self.layoutWidget_4)
        self.infoBrowser_5.setObjectName(u"infoBrowser_5")
        self.infoBrowser_5.setStyleSheet(u"border-top: 1px solid gray;")

        self.verticalLayout_15.addWidget(self.infoBrowser_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.inputEdit_5 = QTextEdit(self.layoutWidget_4)
        self.inputEdit_5.setObjectName(u"inputEdit_5")
        self.inputEdit_5.setBaseSize(QSize(0, 4))
        self.inputEdit_5.setAutoFillBackground(False)
        self.inputEdit_5.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.horizontalLayout_15.addWidget(self.inputEdit_5)

        self.runButtonOneThree = QPushButton(self.layoutWidget_4)
        self.runButtonOneThree.setObjectName(u"runButtonOneThree")
        self.runButtonOneThree.setMinimumSize(QSize(0, 0))
        self.runButtonOneThree.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;")

        self.horizontalLayout_15.addWidget(self.runButtonOneThree)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.label_17 = QLabel(self.layoutWidget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_15.addWidget(self.label_17)

        self.resultBrowser_5 = QTextBrowser(self.layoutWidget_4)
        self.resultBrowser_5.setObjectName(u"resultBrowser_5")
        self.resultBrowser_5.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.verticalLayout_15.addWidget(self.resultBrowser_5)

        self.progressBarOne_4 = QProgressBar(self.layoutWidget_4)
        self.progressBarOne_4.setObjectName(u"progressBarOne_4")
        self.progressBarOne_4.setValue(24)

        self.verticalLayout_15.addWidget(self.progressBarOne_4)

        self.verticalLayout_15.setStretch(1, 6)
        self.verticalLayout_15.setStretch(2, 1)
        self.verticalLayout_15.setStretch(4, 3)
        self.exerciseOnePages.addWidget(self.oneThree)
        self.oneFour = QWidget()
        self.oneFour.setObjectName(u"oneFour")
        self.layoutWidget_5 = QWidget(self.oneFour)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 0, 1211, 801))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.prevOneFour = QPushButton(self.layoutWidget_5)
        self.prevOneFour.setObjectName(u"prevOneFour")

        self.horizontalLayout_6.addWidget(self.prevOneFour)

        self.label_6 = QLabel(self.layoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.nextOneFour = QPushButton(self.layoutWidget_5)
        self.nextOneFour.setObjectName(u"nextOneFour")

        self.horizontalLayout_6.addWidget(self.nextOneFour)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.infoBrowser_6 = QTextBrowser(self.layoutWidget_5)
        self.infoBrowser_6.setObjectName(u"infoBrowser_6")
        self.infoBrowser_6.setStyleSheet(u"border-top: 1px solid gray;")

        self.verticalLayout_16.addWidget(self.infoBrowser_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.inputEdit_6 = QTextEdit(self.layoutWidget_5)
        self.inputEdit_6.setObjectName(u"inputEdit_6")
        self.inputEdit_6.setBaseSize(QSize(0, 4))
        self.inputEdit_6.setAutoFillBackground(False)
        self.inputEdit_6.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.horizontalLayout_16.addWidget(self.inputEdit_6)

        self.runButtonOneFour = QPushButton(self.layoutWidget_5)
        self.runButtonOneFour.setObjectName(u"runButtonOneFour")
        self.runButtonOneFour.setMinimumSize(QSize(0, 0))
        self.runButtonOneFour.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;")

        self.horizontalLayout_16.addWidget(self.runButtonOneFour)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.label_18 = QLabel(self.layoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_16.addWidget(self.label_18)

        self.resultBrowser_6 = QTextBrowser(self.layoutWidget_5)
        self.resultBrowser_6.setObjectName(u"resultBrowser_6")
        self.resultBrowser_6.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.verticalLayout_16.addWidget(self.resultBrowser_6)

        self.progressBarOne_5 = QProgressBar(self.layoutWidget_5)
        self.progressBarOne_5.setObjectName(u"progressBarOne_5")
        self.progressBarOne_5.setValue(24)

        self.verticalLayout_16.addWidget(self.progressBarOne_5)

        self.verticalLayout_16.setStretch(1, 6)
        self.verticalLayout_16.setStretch(2, 1)
        self.verticalLayout_16.setStretch(4, 3)
        self.exerciseOnePages.addWidget(self.oneFour)
        self.stackedWidget_2.addWidget(self.exerciseOne)
        self.menuPages.addWidget(self.exercisesPage)
        self.userInfoPage = QWidget()
        self.userInfoPage.setObjectName(u"userInfoPage")
        self.verticalLayoutWidget_6 = QWidget(self.userInfoPage)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.title_6 = QLabel(self.verticalLayoutWidget_6)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setMaximumSize(QSize(16777215, 50))
        self.title_6.setFont(font)

        self.verticalLayout_12.addWidget(self.title_6)

        self.subUserInfo = QLabel(self.verticalLayoutWidget_6)
        self.subUserInfo.setObjectName(u"subUserInfo")
        self.subUserInfo.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.subUserInfo)

        self.desc_6 = QLabel(self.verticalLayoutWidget_6)
        self.desc_6.setObjectName(u"desc_6")

        self.verticalLayout_12.addWidget(self.desc_6)

        self.menuPages.addWidget(self.userInfoPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayoutWidget_3 = QWidget(self.infoPage)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.title_3 = QLabel(self.verticalLayoutWidget_3)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setMaximumSize(QSize(16777215, 50))
        self.title_3.setFont(font)

        self.verticalLayout_9.addWidget(self.title_3)

        self.desc_3 = QLabel(self.verticalLayoutWidget_3)
        self.desc_3.setObjectName(u"desc_3")
        self.desc_3.setScaledContents(False)
        self.desc_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.desc_3)

        self.menuPages.addWidget(self.infoPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayoutWidget_5 = QWidget(self.settingsPage)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.title_5 = QLabel(self.verticalLayoutWidget_5)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setMaximumSize(QSize(16777215, 60))
        self.title_5.setFont(font)

        self.verticalLayout_11.addWidget(self.title_5)

        self.sub_5 = QLabel(self.verticalLayoutWidget_5)
        self.sub_5.setObjectName(u"sub_5")
        self.sub_5.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_11.addWidget(self.sub_5)

        self.desc_5 = QLabel(self.verticalLayoutWidget_5)
        self.desc_5.setObjectName(u"desc_5")
        self.desc_5.setFont(font)

        self.verticalLayout_11.addWidget(self.desc_5)

        self.menuPages.addWidget(self.settingsPage)
        self.menu = QWidget(self.loggedPage)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 10, 321, 791))
        self.menu.setStyleSheet(u"background-color: rgb(175, 203, 250);\n"
"border-radius: 5px;")
        self.verticalLayoutWidget = QWidget(self.menu)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 301, 771))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainButton = QPushButton(self.verticalLayoutWidget)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setMinimumSize(QSize(0, 30))
        self.mainButton.setLayoutDirection(Qt.LeftToRight)
        self.mainButton.setStyleSheet(u"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"text-align: left;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.mainButton)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.exercisesButton = QPushButton(self.widget_2)
        self.exercisesButton.setObjectName(u"exercisesButton")
        self.exercisesButton.setGeometry(QRect(0, 0, 281, 30))
        self.exercisesButton.setMinimumSize(QSize(0, 30))
        self.exercisesButton.setStyleSheet(u"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(0, 0, 0);")
        self.exercisesShow = QPushButton(self.widget_2)
        self.exercisesShow.setObjectName(u"exercisesShow")
        self.exercisesShow.setGeometry(QRect(260, 0, 40, 30))
        self.exercisesShow.setMinimumSize(QSize(0, 30))
        self.exercisesShow.setMaximumSize(QSize(40, 16777215))
        self.exercisesShow.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-bottom: 1px solid black;\n"
"border-left: 1px solid;\n"
"border-left-color: rgb(17, 66, 127);\n"
"border-radius: 0")

        self.horizontalLayout_7.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.exerciseOneMenuLayout = QWidget(self.verticalLayoutWidget)
        self.exerciseOneMenuLayout.setObjectName(u"exerciseOneMenuLayout")
        self.exerciseOneMenuLayout.setMinimumSize(QSize(0, 30))
        self.exerciseOneMenuButton = QPushButton(self.exerciseOneMenuLayout)
        self.exerciseOneMenuButton.setObjectName(u"exerciseOneMenuButton")
        self.exerciseOneMenuButton.setGeometry(QRect(0, 0, 281, 30))
        self.exerciseOneMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseOneMenuButton.setStyleSheet(u"padding-left: 20px;\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(0, 0, 0);")
        self.exerciseOneShow = QPushButton(self.exerciseOneMenuLayout)
        self.exerciseOneShow.setObjectName(u"exerciseOneShow")
        self.exerciseOneShow.setGeometry(QRect(260, 0, 40, 30))
        self.exerciseOneShow.setMinimumSize(QSize(0, 30))
        self.exerciseOneShow.setMaximumSize(QSize(40, 16777215))
        self.exerciseOneShow.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"border-left: 1px solid;\n"
"border-left-color: rgb(17, 66, 127);")

        self.horizontalLayout_8.addWidget(self.exerciseOneMenuLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.exerciseOneOneMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseOneOneMenuButton.setObjectName(u"exerciseOneOneMenuButton")
        self.exerciseOneOneMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseOneOneMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.exerciseOneOneMenuButton)

        self.exerciseOneTwoMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseOneTwoMenuButton.setObjectName(u"exerciseOneTwoMenuButton")
        self.exerciseOneTwoMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseOneTwoMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")

        self.verticalLayout.addWidget(self.exerciseOneTwoMenuButton)

        self.exerciseOneThreeMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseOneThreeMenuButton.setObjectName(u"exerciseOneThreeMenuButton")
        self.exerciseOneThreeMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseOneThreeMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")

        self.verticalLayout.addWidget(self.exerciseOneThreeMenuButton)

        self.exerciseOneFourMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseOneFourMenuButton.setObjectName(u"exerciseOneFourMenuButton")
        self.exerciseOneFourMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseOneFourMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")
        self.exerciseOneFourMenuButton.setCheckable(False)

        self.verticalLayout.addWidget(self.exerciseOneFourMenuButton)

        self.userInfoButton = QPushButton(self.verticalLayoutWidget)
        self.userInfoButton.setObjectName(u"userInfoButton")
        self.userInfoButton.setMinimumSize(QSize(0, 30))
        self.userInfoButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.userInfoButton)

        self.infoButton = QPushButton(self.verticalLayoutWidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setMinimumSize(QSize(0, 30))
        self.infoButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.infoButton)

        self.settingsButton = QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(0, 30))
        self.settingsButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.verticalLayoutWidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setMinimumSize(QSize(0, 30))
        self.logoutButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.logoutButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.loggedPage)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        self.loginButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu", None))
        self.loginWarning.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n nimi:", None))
        self.title.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Kubernetes Oppimisty\u00f6kalu</span></p></body></html>", None))
        self.subMain.setText(QCoreApplication.translate("Widget", u"Hei ", None))
        self.desc.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Tervetuloa interaktiiviseen Kubernetes oppimisty\u00f6kaluun!</p></body></html>", None))
        self.labelMinikube.setText(QCoreApplication.translate("Widget", u"K\u00e4yt\u00f6ss\u00e4 oleva Minikube versio: ", None))
        self.labelKubectl.setText(QCoreApplication.translate("Widget", u"K\u00e4yt\u00f6ss\u00e4 oleva Kubectl Client versio: ", None))
        self.title_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Teht\u00e4v\u00e4t</span></p></body></html>", None))
        self.sub_4.setText("")
        self.desc_4.setText("")
        self.exOneImage.setText("")
        self.exerciseOneButton.setText(QCoreApplication.translate("Widget", u"1. Klusterit", None))
        self.title_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">1. Klusterit</span></p></body></html>", None))
        self.sub_6.setText("")
        self.exerciseOneOneButton.setText(QCoreApplication.translate("Widget", u"1.1. Kubernetes klusterin perusteet", None))
        self.exerciseOneTwoButton.setText(QCoreApplication.translate("Widget", u"1.2. Minikube", None))
        self.exerciseOneThreeButton.setText(QCoreApplication.translate("Widget", u"1.3. Klusterin rakenne", None))
        self.exerciseOneFourButton.setText(QCoreApplication.translate("Widget", u"1.4. Klusterin luonti", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.prevOneOne.setText(QCoreApplication.translate("Widget", u"Palaa teht\u00e4v\u00e4sivulle", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.1. Kubernetes-klusteri</span></p></body></html>", None))
        self.nextOneOne.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">Kubernetes</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> on avoimen l\u00e4hdekoodin alusta, jonka avulla voidaan toteuttaa konttiorkestrointia. Kuberneteksen </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">klusteri</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">"
                        " koordinoi joukkoa tietokoneita, jotka ovat yhteydess\u00e4 toisiinsa ja toimivat yhten\u00e4isen\u00e4 kokonaisuutena. Jotta Kuberneteksen hajautettua k\u00e4ytt\u00f6\u00f6nottomallia voitaisiin hy\u00f6dynt\u00e4\u00e4, sovellukset tulee pakata siten, ett\u00e4 ne eiv\u00e4t ole riippuvaisia yksitt\u00e4isist\u00e4 is\u00e4nt\u00e4koneista. Sovellukset tulee siis </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">kontittaa. </span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Kubernetes automatisoi sovelluskonttien yll\u00e4pitoa klusterissa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Kuberneteksen klusteri koostuu kahden tyyppisest\u00e4 p\u00e4"
                        "\u00e4komponentista:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        -</span><span style=\" font-size:11pt; font-weight:700;\"> </span><span style=\" font-size:11pt;\">Ohjaustaso koordinoi klusteria</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        -</span><span style=\" font-size:11pt; font-weight:700;\"> </span><span style=\" font-size:11pt;\">Solmut ovat klusterin ty\u00f6ntekij\u00f6it\u00e4, jotka ajavat kontitettuja sovelluksia</span></p></body></html>", None))
        self.clusterImage.setText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Ohjaustaso</span><span style=\" font-size:11pt;\"> vastaa klusterin yll\u00e4pidosta. Ohjaustaso hallinnoi klusterin kaikkia aktiviteetteja, kuten sovellusten aikataulutusta, sovellusten skaalauksesta sek\u00e4 halutun tilan yll\u00e4pidosta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ohjaustasosta l\u00f6ytyy viisi erilaista komponenttia. </span><span style=\" font-size:11pt; font-weight:700;\">API-palvelin</span><span style=\" font-size:11pt;\"> paljastaa Kubernetes APIn klusterille ja toimii frontendin\u00e4 ohjaustasolle. </span><span style=\" font-size:11pt; font-weight:700;\">etcd</span><span style=\" font-size:11pt;\"> on johdonmukainen ja saatavilla oleva avainarvos\u00e4il\u00f6 kaikille klusteritiedoille. </span><span style=\" font-size:11pt; font-weight:700;\">Ajastin</span><span style=\" font-size:11pt;\"> seuraa luotuja s\u00e4ili\u00f6it\u00e4 ja valitsee niille sopivan solmun. </span><span style=\" font-size:11pt; font-weight:700;\">Ohjainmanageri </span><span style=\" font-size:11pt;\">ajaa ohjainprosesseja, ja </span><span style=\" font-size:1"
                        "1pt; font-weight:700;\">pilviohjainmanageri </span><span style=\" font-size:11pt;\">upottaa klusteriin pilvikohtaisen ohjauslogiikan, ajaa pilveen liittyvi\u00e4 ohjainprosesseja ja mahdollistaa yhdist\u00e4misen pilvitarjoajan APIin.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Solmu</span><span style=\" font-size:11pt;\"> on virtuaalikone tai fyysinen kone, joka k\u00e4ytt\u00e4ytyy ty\u00f6ntekij\u00e4koneena Kuberneteksen klusterissa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Solmu koostuu my\u00f6s erilaisista komponenteista. </span><span style=\" font-size:11pt; font-weight:700;\">Kubelet</span><span style=\" font-size:11pt;\"> on agentti, joka itsen\u00e4isesti yll\u00e4pit\u00e4\u00e4 solmua ja kommunikoi ohjaustason kanssa. </span><span style=\" font-size:11pt; font-weight:700;\">V\u00e4lipalvelin</span><span style=\" font-size:11pt;\"> yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6ja. </span><span style=\" font-size:11pt; font-weight:700;\">Kontin ajoaika</span><span style=\" font-size:11pt;\"> vastaa konttien toteutuksesta ja elinkaaren hallinnasta. </span><span style=\" font-size:11pt; font-weight:700;\">S\u00e4ili\u00f6 </span><span style=\" font-size:11pt;\">on joukko solmussa ajettavia kontteja.</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Kuberneteksen klusteri voidaan luoda fyysiselle koneelle tai virtuaalikoneelle. T\u00e4ss\u00e4 oppimisty\u00f6kalussa klusterin luonti toteutetaan Minikuben avulla, jota k\u00e4sitell\u00e4\u00e4n seuraavassa osiossa.</span></p></body></html>", None))
        self.prevOneTwo.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.2. Minikube</span></p></body></html>", None))
        self.nextOneTwo.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Minikube</span><span style=\" font-size:11pt;\"> on kevyt ja lokaalisti ajettava Kubernetes. Minikube luo virtuaalikoneen paikalliselle koneellesi ja ottaa k\u00e4ytt\u00f6\u00f6n yksinkertaisen klusterin. Luotu klusteri sis\u00e4lt\u00e4\u00e4 yhden solmun. Minikuben komentorivik\u00e4ytt\u00f6liittym\u00e4 tarjoaa mahdollisuuden ajaa klusterin perust"
                        "oimintoja.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Minikuben sivuilta voi tarkkailla Minikubesta l\u00f6ytyvi\u00e4 komentoja: </span><a href=\"https://minikube.sigs.k8s.io/docs/commands/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0078d4;\">https://minikube.sigs.k8s.io/docs/commands/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Klusterin voi k\u00e4"
                        "ynnist\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Minikuben 1.32.0 versiossa on raportoitu h\u00e4iri\u00f6it\u00e4 eri k\u00e4ytt\u00f6j\u00e4rjestelmill\u00e4. </span><span style=\" font-size:11pt; font-weight:700;\">Jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0</span><span style=\" font-size:11pt;\"> (tai mahdollisesti my\u00f6hempi versio), on klusterin k\u00e4ynnistyksen yhteydess\u00e4 hyv\u00e4 k\u00e4"
                        "ytt\u00e4\u00e4 jotai muuta kun version mukana tulevaa alkuper\u00e4ist\u00e4 kuvaa. Alla on esimerkki vaihtoehtoisesta ajamisesta:</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Candara'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start --base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830</span></p></body></html>", None))
        self.prevOneThree.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.3. Klusterin rakenne</span></p></body></html>", None))
        self.nextOneThree.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.runButtonOneThree.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.prevOneFour.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.4. Klusterin luonti</span></p></body></html>", None))
        self.nextOneFour.setText(QCoreApplication.translate("Widget", u"Lopeta", None))
        self.runButtonOneFour.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.title_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">K\u00e4ytt\u00e4j\u00e4n tiedot</span></p></body></html>", None))
        self.subUserInfo.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n nimi: ", None))
        self.desc_6.setText("")
        self.title_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Tietoja</span></p></body></html>", None))
        self.desc_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Kubernetes Oppimisty\u00f6kalu </p><p>Versio: v0.1</p><p>Kehitt\u00e4j\u00e4: Hanna Kortetj\u00e4rvi</p><p>L\u00e4hteet: <br/>    - Kubernetes, https://kubernetes.io/<br/>    - minikube, https://minikube.sigs.k8s.io/docs/start/</p></body></html>", None))
        self.title_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Asetukset</span></p></body></html>", None))
        self.sub_5.setText("")
        self.desc_5.setText("")
        self.mainButton.setText(QCoreApplication.translate("Widget", u"Etusivu", None))
        self.exercisesButton.setText(QCoreApplication.translate("Widget", u"Teht\u00e4v\u00e4t", None))
        self.exercisesShow.setText(QCoreApplication.translate("Widget", u"\u25b2", None))
        self.exerciseOneMenuButton.setText(QCoreApplication.translate("Widget", u"1. Klusterit", None))
        self.exerciseOneShow.setText(QCoreApplication.translate("Widget", u"\u25b2", None))
        self.exerciseOneOneMenuButton.setText(QCoreApplication.translate("Widget", u"1.1. Kubernetes-klusteri", None))
        self.exerciseOneTwoMenuButton.setText(QCoreApplication.translate("Widget", u"1.2. Minikube", None))
        self.exerciseOneThreeMenuButton.setText(QCoreApplication.translate("Widget", u"1.3. Klusterin rakenne", None))
        self.exerciseOneFourMenuButton.setText(QCoreApplication.translate("Widget", u"1.4. Klusterin luonti", None))
        self.userInfoButton.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n tiedot", None))
        self.infoButton.setText(QCoreApplication.translate("Widget", u"Tietoja", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"Asetukset", None))
        self.logoutButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu ulos", None))
        pass
    # retranslateUi

