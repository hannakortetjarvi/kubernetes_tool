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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(1570, 834)
        Widget.setWindowTitle(u"Kubernetes Learning Tool")
        Widget.setStyleSheet(u"background-color: rgb(240, 255, 254);\n"
"font: 10pt \"Consolas\";")
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
        self.loginButton.setGeometry(QRect(220, 420, 121, 61))
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
        self.label.setGeometry(QRect(40, 180, 191, 20))
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
        font.setFamilies([u"Consolas"])
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1209, 691))
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

        self.progressBarOneGlobal = QProgressBar(self.horizontalLayoutWidget)
        self.progressBarOneGlobal.setObjectName(u"progressBarOneGlobal")
        self.progressBarOneGlobal.setStyleSheet(u"border: 1px solid;")
        self.progressBarOneGlobal.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBarOneGlobal)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.exTwoImage = QLabel(self.verticalLayoutWidget_7)
        self.exTwoImage.setObjectName(u"exTwoImage")
        self.exTwoImage.setMaximumSize(QSize(150, 150))
        self.exTwoImage.setPixmap(QPixmap(u"../../images/ex1.png"))
        self.exTwoImage.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.exTwoImage)

        self.exerciseOneButton_2 = QPushButton(self.verticalLayoutWidget_7)
        self.exerciseOneButton_2.setObjectName(u"exerciseOneButton_2")
        self.exerciseOneButton_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.exerciseOneButton_2.sizePolicy().hasHeightForWidth())
        self.exerciseOneButton_2.setSizePolicy(sizePolicy)
        self.exerciseOneButton_2.setMinimumSize(QSize(0, 40))
        self.exerciseOneButton_2.setFont(font)
        self.exerciseOneButton_2.setStyleSheet(u"border: none;\n"
"color: rgb(0, 85, 255);")
        self.exerciseOneButton_2.setCheckable(False)

        self.horizontalLayout_36.addWidget(self.exerciseOneButton_2)

        self.progressBarTwoGlobal = QProgressBar(self.verticalLayoutWidget_7)
        self.progressBarTwoGlobal.setObjectName(u"progressBarTwoGlobal")
        self.progressBarTwoGlobal.setStyleSheet(u"border: 1px solid;")
        self.progressBarTwoGlobal.setValue(24)

        self.horizontalLayout_36.addWidget(self.progressBarTwoGlobal)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_36)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.exercisesMain)
        self.exerciseOne = QWidget()
        self.exerciseOne.setObjectName(u"exerciseOne")
        self.exerciseOne.setStyleSheet(u"")
        self.verticalLayoutWidget_8 = QWidget(self.exerciseOne)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 1211, 801))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.exerciseOnePages = QStackedWidget(self.verticalLayoutWidget_8)
        self.exerciseOnePages.setObjectName(u"exerciseOnePages")
        self.one = QWidget()
        self.one.setObjectName(u"one")
        self.verticalLayoutWidget_9 = QWidget(self.one)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 0, 1201, 781))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.title_7 = QLabel(self.verticalLayoutWidget_9)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setMaximumSize(QSize(16777215, 50))
        self.title_7.setFont(font)

        self.verticalLayout_17.addWidget(self.title_7)

        self.sub_6 = QLabel(self.verticalLayoutWidget_9)
        self.sub_6.setObjectName(u"sub_6")
        self.sub_6.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_17.addWidget(self.sub_6)

        self.exerciseOneOneButton = QPushButton(self.verticalLayoutWidget_9)
        self.exerciseOneOneButton.setObjectName(u"exerciseOneOneButton")

        self.verticalLayout_17.addWidget(self.exerciseOneOneButton)

        self.exerciseOneTwoButton = QPushButton(self.verticalLayoutWidget_9)
        self.exerciseOneTwoButton.setObjectName(u"exerciseOneTwoButton")

        self.verticalLayout_17.addWidget(self.exerciseOneTwoButton)

        self.exerciseOneThreeButton = QPushButton(self.verticalLayoutWidget_9)
        self.exerciseOneThreeButton.setObjectName(u"exerciseOneThreeButton")

        self.verticalLayout_17.addWidget(self.exerciseOneThreeButton)

        self.exerciseOneFourButton = QPushButton(self.verticalLayoutWidget_9)
        self.exerciseOneFourButton.setObjectName(u"exerciseOneFourButton")

        self.verticalLayout_17.addWidget(self.exerciseOneFourButton)

        self.label_7 = QLabel(self.verticalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.exerciseOnePages.addWidget(self.one)
        self.oneOne = QWidget()
        self.oneOne.setObjectName(u"oneOne")
        self.layoutWidget_2 = QWidget(self.oneOne)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 1211, 761))
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

        self.verticalLayout_8.setStretch(1, 6)
        self.exerciseOnePages.addWidget(self.oneOne)
        self.oneTwo = QWidget()
        self.oneTwo.setObjectName(u"oneTwo")
        self.layoutWidget_3 = QWidget(self.oneTwo)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 1211, 761))
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
        self.infoBrowser_4.setMaximumSize(QSize(16777215, 145))
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
        self.textBrowser_3.setMaximumSize(QSize(16777215, 63))
        self.textBrowser_3.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.textBrowser_3)

        self.textBrowser_5 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_5.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_14.addWidget(self.textBrowser_5)

        self.textBrowser_8 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setMaximumSize(QSize(16777215, 30))
        self.textBrowser_8.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.textBrowser_8)

        self.textBrowser_9 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_9.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_14.addWidget(self.textBrowser_9)

        self.textBrowser_10 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setMaximumSize(QSize(16777215, 30))
        self.textBrowser_10.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.textBrowser_10)

        self.textBrowser_11 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_11.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_14.addWidget(self.textBrowser_11)

        self.textBrowser_6 = QTextBrowser(self.layoutWidget_3)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.verticalLayout_14.addWidget(self.textBrowser_6)

        self.verticalLayout_14.setStretch(1, 6)
        self.exerciseOnePages.addWidget(self.oneTwo)
        self.oneThree = QWidget()
        self.oneThree.setObjectName(u"oneThree")
        self.layoutWidget_4 = QWidget(self.oneThree)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 1211, 761))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_15.setSpacing(7)
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

        self.label_3 = QLabel(self.layoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top: 20px;\n"
"padding-bottom: 20px;")

        self.verticalLayout_15.addWidget(self.label_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_8 = QLabel(self.layoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.oneThreeCombo_1 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.addItem("")
        self.oneThreeCombo_1.setObjectName(u"oneThreeCombo_1")
        self.oneThreeCombo_1.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_11.addWidget(self.oneThreeCombo_1)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.label_9 = QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.oneThreeCombo_2 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.addItem("")
        self.oneThreeCombo_2.setObjectName(u"oneThreeCombo_2")
        self.oneThreeCombo_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.oneThreeCombo_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.label_11 = QLabel(self.layoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.oneThreeCombo_3 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.addItem("")
        self.oneThreeCombo_3.setObjectName(u"oneThreeCombo_3")
        self.oneThreeCombo_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_14.addWidget(self.oneThreeCombo_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 10, -1, -1)
        self.label_12 = QLabel(self.layoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.oneThreeCombo_4 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.addItem("")
        self.oneThreeCombo_4.setObjectName(u"oneThreeCombo_4")
        self.oneThreeCombo_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.oneThreeCombo_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 10, -1, -1)
        self.label_13 = QLabel(self.layoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.oneThreeCombo_5 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.addItem("")
        self.oneThreeCombo_5.setObjectName(u"oneThreeCombo_5")
        self.oneThreeCombo_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_18.addWidget(self.oneThreeCombo_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 10, -1, -1)
        self.label_14 = QLabel(self.layoutWidget_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.oneThreeCombo_6 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.addItem("")
        self.oneThreeCombo_6.setObjectName(u"oneThreeCombo_6")
        self.oneThreeCombo_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_15.addWidget(self.oneThreeCombo_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 10, -1, -1)
        self.label_16 = QLabel(self.layoutWidget_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)

        self.oneThreeCombo_7 = QComboBox(self.layoutWidget_4)
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.addItem("")
        self.oneThreeCombo_7.setObjectName(u"oneThreeCombo_7")
        self.oneThreeCombo_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_20.addWidget(self.oneThreeCombo_7)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)

        self.checkOneThree = QPushButton(self.layoutWidget_4)
        self.checkOneThree.setObjectName(u"checkOneThree")
        self.checkOneThree.setMinimumSize(QSize(200, 40))
        self.checkOneThree.setFont(font)
        self.checkOneThree.setStyleSheet(u"margin-top: 10px;")

        self.horizontalLayout_22.addWidget(self.checkOneThree)


        self.verticalLayout_15.addLayout(self.horizontalLayout_22)

        self.infoBrowser_5 = QTextBrowser(self.layoutWidget_4)
        self.infoBrowser_5.setObjectName(u"infoBrowser_5")
        self.infoBrowser_5.setStyleSheet(u"border-top: none;")

        self.verticalLayout_15.addWidget(self.infoBrowser_5)

        self.exerciseOnePages.addWidget(self.oneThree)
        self.oneFour = QWidget()
        self.oneFour.setObjectName(u"oneFour")
        self.layoutWidget_5 = QWidget(self.oneFour)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 0, 1201, 761))
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
        self.infoBrowser_6.setMaximumSize(QSize(16777215, 90))
        self.infoBrowser_6.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top:10px;")

        self.verticalLayout_16.addWidget(self.infoBrowser_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.oneFourInput_1 = QTextEdit(self.layoutWidget_5)
        self.oneFourInput_1.setObjectName(u"oneFourInput_1")
        self.oneFourInput_1.setMaximumSize(QSize(16777215, 50))
        self.oneFourInput_1.setBaseSize(QSize(0, 4))
        self.oneFourInput_1.setAutoFillBackground(False)
        self.oneFourInput_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_16.addWidget(self.oneFourInput_1)

        self.oneFourButton_1 = QPushButton(self.layoutWidget_5)
        self.oneFourButton_1.setObjectName(u"oneFourButton_1")
        self.oneFourButton_1.setMinimumSize(QSize(0, 0))
        self.oneFourButton_1.setMaximumSize(QSize(16777215, 50))
        self.oneFourButton_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;\n"
"background-color: rgb(176, 194, 221);")

        self.horizontalLayout_16.addWidget(self.oneFourButton_1)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.label_18 = QLabel(self.layoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_16.addWidget(self.label_18)

        self.oneFourResult_1 = QTextBrowser(self.layoutWidget_5)
        self.oneFourResult_1.setObjectName(u"oneFourResult_1")
        self.oneFourResult_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_16.addWidget(self.oneFourResult_1)

        self.textBrowser_13 = QTextBrowser(self.layoutWidget_5)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setMaximumSize(QSize(16777215, 40))
        self.textBrowser_13.setStyleSheet(u"border: none;\n"
"margin-top:10px;")

        self.verticalLayout_16.addWidget(self.textBrowser_13)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.oneFourInput_2 = QTextEdit(self.layoutWidget_5)
        self.oneFourInput_2.setObjectName(u"oneFourInput_2")
        self.oneFourInput_2.setMaximumSize(QSize(16777215, 50))
        self.oneFourInput_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_28.addWidget(self.oneFourInput_2)

        self.oneFourButton_2 = QPushButton(self.layoutWidget_5)
        self.oneFourButton_2.setObjectName(u"oneFourButton_2")
        self.oneFourButton_2.setMaximumSize(QSize(16777215, 50))
        self.oneFourButton_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;\n"
"background-color: rgb(176, 194, 221);")

        self.horizontalLayout_28.addWidget(self.oneFourButton_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_28)

        self.label_19 = QLabel(self.layoutWidget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_16.addWidget(self.label_19)

        self.oneFourResult_2 = QTextBrowser(self.layoutWidget_5)
        self.oneFourResult_2.setObjectName(u"oneFourResult_2")
        self.oneFourResult_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_16.addWidget(self.oneFourResult_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)

        self.verticalLayout_16.setStretch(1, 6)
        self.verticalLayout_16.setStretch(2, 1)
        self.verticalLayout_16.setStretch(4, 3)
        self.exerciseOnePages.addWidget(self.oneFour)

        self.verticalLayout_3.addWidget(self.exerciseOnePages)

        self.progressBarOne = QProgressBar(self.verticalLayoutWidget_8)
        self.progressBarOne.setObjectName(u"progressBarOne")
        self.progressBarOne.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBarOne)

        self.stackedWidget_2.addWidget(self.exerciseOne)
        self.exerciseTwo = QWidget()
        self.exerciseTwo.setObjectName(u"exerciseTwo")
        self.verticalLayoutWidget_10 = QWidget(self.exerciseTwo)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(0, 0, 1211, 801))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.exerciseTwoPages = QStackedWidget(self.verticalLayoutWidget_10)
        self.exerciseTwoPages.setObjectName(u"exerciseTwoPages")
        self.two = QWidget()
        self.two.setObjectName(u"two")
        self.verticalLayoutWidget_11 = QWidget(self.two)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(0, 0, 1211, 781))
        self.verticalLayout_18 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.title_8 = QLabel(self.verticalLayoutWidget_11)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setMaximumSize(QSize(16777215, 50))
        self.title_8.setFont(font)

        self.verticalLayout_18.addWidget(self.title_8)

        self.sub_7 = QLabel(self.verticalLayoutWidget_11)
        self.sub_7.setObjectName(u"sub_7")
        self.sub_7.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_18.addWidget(self.sub_7)

        self.exerciseTwoOneButton = QPushButton(self.verticalLayoutWidget_11)
        self.exerciseTwoOneButton.setObjectName(u"exerciseTwoOneButton")

        self.verticalLayout_18.addWidget(self.exerciseTwoOneButton)

        self.exerciseTwoTwoButton = QPushButton(self.verticalLayoutWidget_11)
        self.exerciseTwoTwoButton.setObjectName(u"exerciseTwoTwoButton")

        self.verticalLayout_18.addWidget(self.exerciseTwoTwoButton)

        self.exerciseTwoThreeButton = QPushButton(self.verticalLayoutWidget_11)
        self.exerciseTwoThreeButton.setObjectName(u"exerciseTwoThreeButton")

        self.verticalLayout_18.addWidget(self.exerciseTwoThreeButton)

        self.exerciseTwoFourButton = QPushButton(self.verticalLayoutWidget_11)
        self.exerciseTwoFourButton.setObjectName(u"exerciseTwoFourButton")

        self.verticalLayout_18.addWidget(self.exerciseTwoFourButton)

        self.label_10 = QLabel(self.verticalLayoutWidget_11)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_18.addWidget(self.label_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.exerciseTwoPages.addWidget(self.two)
        self.twoOne = QWidget()
        self.twoOne.setObjectName(u"twoOne")
        self.layoutWidget_6 = QWidget(self.twoOne)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 0, 1211, 761))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.prevTwoOne = QPushButton(self.layoutWidget_6)
        self.prevTwoOne.setObjectName(u"prevTwoOne")
        self.prevTwoOne.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.prevTwoOne)

        self.label_15 = QLabel(self.layoutWidget_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.nextTwoOne = QPushButton(self.layoutWidget_6)
        self.nextTwoOne.setObjectName(u"nextTwoOne")

        self.horizontalLayout_9.addWidget(self.nextTwoOne)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.infoBrowser_3 = QTextBrowser(self.layoutWidget_6)
        self.infoBrowser_3.setObjectName(u"infoBrowser_3")
        self.infoBrowser_3.setMinimumSize(QSize(0, 210))
        self.infoBrowser_3.setMaximumSize(QSize(16777215, 16777215))
        self.infoBrowser_3.setFont(font)
        self.infoBrowser_3.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top: 10px;")

        self.verticalLayout_13.addWidget(self.infoBrowser_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.clusterImage_2 = QLabel(self.layoutWidget_6)
        self.clusterImage_2.setObjectName(u"clusterImage_2")
        self.clusterImage_2.setMinimumSize(QSize(300, 300))
        self.clusterImage_2.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.clusterImage_2)

        self.textBrowser_12 = QTextBrowser(self.layoutWidget_6)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setMinimumSize(QSize(0, 350))
        self.textBrowser_12.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout_10.addWidget(self.textBrowser_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.textBrowser_14 = QTextBrowser(self.layoutWidget_6)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setStyleSheet(u"border:none;")

        self.verticalLayout_13.addWidget(self.textBrowser_14)

        self.verticalLayout_13.setStretch(1, 6)
        self.exerciseTwoPages.addWidget(self.twoOne)
        self.twoTwo = QWidget()
        self.twoTwo.setObjectName(u"twoTwo")
        self.layoutWidget_7 = QWidget(self.twoTwo)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 0, 1211, 761))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.prevTwoTwo = QPushButton(self.layoutWidget_7)
        self.prevTwoTwo.setObjectName(u"prevTwoTwo")

        self.horizontalLayout_13.addWidget(self.prevTwoTwo)

        self.label_17 = QLabel(self.layoutWidget_7)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.nextTwoTwo = QPushButton(self.layoutWidget_7)
        self.nextTwoTwo.setObjectName(u"nextTwoTwo")

        self.horizontalLayout_13.addWidget(self.nextTwoTwo)


        self.verticalLayout_19.addLayout(self.horizontalLayout_13)

        self.infoBrowser_7 = QTextBrowser(self.layoutWidget_7)
        self.infoBrowser_7.setObjectName(u"infoBrowser_7")
        self.infoBrowser_7.setMaximumSize(QSize(16777215, 145))
        self.infoBrowser_7.setStyleSheet(u"border-top: 1px solid gray;")

        self.verticalLayout_19.addWidget(self.infoBrowser_7)

        self.textBrowser_15 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_15.setObjectName(u"textBrowser_15")
        self.textBrowser_15.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_15.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_15)

        self.textBrowser_16 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_16.setObjectName(u"textBrowser_16")
        self.textBrowser_16.setMaximumSize(QSize(16777215, 63))
        self.textBrowser_16.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_16)

        self.textBrowser_17 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_17.setObjectName(u"textBrowser_17")
        self.textBrowser_17.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_17.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_17)

        self.textBrowser_18 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_18.setObjectName(u"textBrowser_18")
        self.textBrowser_18.setMaximumSize(QSize(16777215, 30))
        self.textBrowser_18.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_18)

        self.textBrowser_19 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_19.setObjectName(u"textBrowser_19")
        self.textBrowser_19.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_19.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_19)

        self.textBrowser_20 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_20.setObjectName(u"textBrowser_20")
        self.textBrowser_20.setMaximumSize(QSize(16777215, 30))
        self.textBrowser_20.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_20)

        self.textBrowser_21 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_21.setObjectName(u"textBrowser_21")
        self.textBrowser_21.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_21.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_21)

        self.textBrowser_22 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_22.setObjectName(u"textBrowser_22")

        self.verticalLayout_19.addWidget(self.textBrowser_22)

        self.verticalLayout_19.setStretch(1, 6)
        self.exerciseTwoPages.addWidget(self.twoTwo)
        self.twoThree = QWidget()
        self.twoThree.setObjectName(u"twoThree")
        self.layoutWidget_8 = QWidget(self.twoThree)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(0, 0, 1211, 761))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.prevTwoThree = QPushButton(self.layoutWidget_8)
        self.prevTwoThree.setObjectName(u"prevTwoThree")

        self.horizontalLayout_19.addWidget(self.prevTwoThree)

        self.label_20 = QLabel(self.layoutWidget_8)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_19.addWidget(self.label_20)

        self.nextTwoThree = QPushButton(self.layoutWidget_8)
        self.nextTwoThree.setObjectName(u"nextTwoThree")

        self.horizontalLayout_19.addWidget(self.nextTwoThree)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.label_21 = QLabel(self.layoutWidget_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top: 20px;\n"
"padding-bottom: 20px;")

        self.verticalLayout_20.addWidget(self.label_21)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.label_22 = QLabel(self.layoutWidget_8)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_21.addWidget(self.label_22)

        self.oneThreeCombo_8 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.addItem("")
        self.oneThreeCombo_8.setObjectName(u"oneThreeCombo_8")
        self.oneThreeCombo_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.oneThreeCombo_8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 10, -1, -1)
        self.label_23 = QLabel(self.layoutWidget_8)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_23.addWidget(self.label_23)

        self.oneThreeCombo_9 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.addItem("")
        self.oneThreeCombo_9.setObjectName(u"oneThreeCombo_9")
        self.oneThreeCombo_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.oneThreeCombo_9)


        self.verticalLayout_20.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 10, -1, -1)
        self.label_24 = QLabel(self.layoutWidget_8)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.oneThreeCombo_10 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.addItem("")
        self.oneThreeCombo_10.setObjectName(u"oneThreeCombo_10")
        self.oneThreeCombo_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_24.addWidget(self.oneThreeCombo_10)


        self.verticalLayout_20.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 10, -1, -1)
        self.label_25 = QLabel(self.layoutWidget_8)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_25.addWidget(self.label_25)

        self.oneThreeCombo_11 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.addItem("")
        self.oneThreeCombo_11.setObjectName(u"oneThreeCombo_11")
        self.oneThreeCombo_11.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.oneThreeCombo_11)


        self.verticalLayout_20.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 10, -1, -1)
        self.label_26 = QLabel(self.layoutWidget_8)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.oneThreeCombo_12 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.addItem("")
        self.oneThreeCombo_12.setObjectName(u"oneThreeCombo_12")
        self.oneThreeCombo_12.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_26.addWidget(self.oneThreeCombo_12)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 10, -1, -1)
        self.label_27 = QLabel(self.layoutWidget_8)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_27.addWidget(self.label_27)

        self.oneThreeCombo_13 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.addItem("")
        self.oneThreeCombo_13.setObjectName(u"oneThreeCombo_13")
        self.oneThreeCombo_13.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.oneThreeCombo_13)


        self.verticalLayout_20.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 10, -1, -1)
        self.label_28 = QLabel(self.layoutWidget_8)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_29.addWidget(self.label_28)

        self.oneThreeCombo_14 = QComboBox(self.layoutWidget_8)
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.addItem("")
        self.oneThreeCombo_14.setObjectName(u"oneThreeCombo_14")
        self.oneThreeCombo_14.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_29.addWidget(self.oneThreeCombo_14)


        self.verticalLayout_20.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_3)

        self.checkTwoThree = QPushButton(self.layoutWidget_8)
        self.checkTwoThree.setObjectName(u"checkTwoThree")
        self.checkTwoThree.setMinimumSize(QSize(200, 40))
        self.checkTwoThree.setFont(font)
        self.checkTwoThree.setStyleSheet(u"margin-top: 10px;")

        self.horizontalLayout_30.addWidget(self.checkTwoThree)


        self.verticalLayout_20.addLayout(self.horizontalLayout_30)

        self.infoBrowser_8 = QTextBrowser(self.layoutWidget_8)
        self.infoBrowser_8.setObjectName(u"infoBrowser_8")
        self.infoBrowser_8.setStyleSheet(u"border-top: none;")

        self.verticalLayout_20.addWidget(self.infoBrowser_8)

        self.exerciseTwoPages.addWidget(self.twoThree)
        self.twoFour = QWidget()
        self.twoFour.setObjectName(u"twoFour")
        self.layoutWidget_9 = QWidget(self.twoFour)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(10, 0, 1201, 761))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.prevTwoFour = QPushButton(self.layoutWidget_9)
        self.prevTwoFour.setObjectName(u"prevTwoFour")

        self.horizontalLayout_31.addWidget(self.prevTwoFour)

        self.label_29 = QLabel(self.layoutWidget_9)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_31.addWidget(self.label_29)

        self.nextTwoFour = QPushButton(self.layoutWidget_9)
        self.nextTwoFour.setObjectName(u"nextTwoFour")

        self.horizontalLayout_31.addWidget(self.nextTwoFour)


        self.verticalLayout_21.addLayout(self.horizontalLayout_31)

        self.infoBrowser_9 = QTextBrowser(self.layoutWidget_9)
        self.infoBrowser_9.setObjectName(u"infoBrowser_9")
        self.infoBrowser_9.setMaximumSize(QSize(16777215, 90))
        self.infoBrowser_9.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top:10px;")

        self.verticalLayout_21.addWidget(self.infoBrowser_9)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.TwoFourInput = QTextEdit(self.layoutWidget_9)
        self.TwoFourInput.setObjectName(u"TwoFourInput")
        self.TwoFourInput.setMaximumSize(QSize(16777215, 50))
        self.TwoFourInput.setBaseSize(QSize(0, 4))
        self.TwoFourInput.setAutoFillBackground(False)
        self.TwoFourInput.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_32.addWidget(self.TwoFourInput)

        self.TwoFourButton = QPushButton(self.layoutWidget_9)
        self.TwoFourButton.setObjectName(u"TwoFourButton")
        self.TwoFourButton.setMinimumSize(QSize(0, 0))
        self.TwoFourButton.setMaximumSize(QSize(16777215, 50))
        self.TwoFourButton.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;\n"
"background-color: rgb(176, 194, 221);")

        self.horizontalLayout_32.addWidget(self.TwoFourButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_32)

        self.label_30 = QLabel(self.layoutWidget_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_21.addWidget(self.label_30)

        self.TwoFourResult = QTextBrowser(self.layoutWidget_9)
        self.TwoFourResult.setObjectName(u"TwoFourResult")
        self.TwoFourResult.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_21.addWidget(self.TwoFourResult)

        self.textBrowser_23 = QTextBrowser(self.layoutWidget_9)
        self.textBrowser_23.setObjectName(u"textBrowser_23")
        self.textBrowser_23.setMaximumSize(QSize(16777215, 40))
        self.textBrowser_23.setStyleSheet(u"border: none;\n"
"margin-top:10px;")

        self.verticalLayout_21.addWidget(self.textBrowser_23)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.TwoFourInput_2 = QTextEdit(self.layoutWidget_9)
        self.TwoFourInput_2.setObjectName(u"TwoFourInput_2")
        self.TwoFourInput_2.setMaximumSize(QSize(16777215, 50))
        self.TwoFourInput_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_33.addWidget(self.TwoFourInput_2)

        self.TwoFourButton_2 = QPushButton(self.layoutWidget_9)
        self.TwoFourButton_2.setObjectName(u"TwoFourButton_2")
        self.TwoFourButton_2.setMaximumSize(QSize(16777215, 50))
        self.TwoFourButton_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;\n"
"background-color: rgb(176, 194, 221);")

        self.horizontalLayout_33.addWidget(self.TwoFourButton_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_33)

        self.label_31 = QLabel(self.layoutWidget_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_21.addWidget(self.label_31)

        self.TwoFourResult_2 = QTextBrowser(self.layoutWidget_9)
        self.TwoFourResult_2.setObjectName(u"TwoFourResult_2")
        self.TwoFourResult_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_21.addWidget(self.TwoFourResult_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.verticalLayout_21.setStretch(1, 6)
        self.verticalLayout_21.setStretch(2, 1)
        self.verticalLayout_21.setStretch(4, 3)
        self.exerciseTwoPages.addWidget(self.twoFour)

        self.verticalLayout_4.addWidget(self.exerciseTwoPages)

        self.progressBarTwo = QProgressBar(self.verticalLayoutWidget_10)
        self.progressBarTwo.setObjectName(u"progressBarTwo")
        self.progressBarTwo.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBarTwo)

        self.stackedWidget_2.addWidget(self.exerciseTwo)
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

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.exerciseTwoMenuLayout = QWidget(self.verticalLayoutWidget)
        self.exerciseTwoMenuLayout.setObjectName(u"exerciseTwoMenuLayout")
        self.exerciseTwoMenuLayout.setMinimumSize(QSize(0, 30))
        self.exerciseTwoMenuButton = QPushButton(self.exerciseTwoMenuLayout)
        self.exerciseTwoMenuButton.setObjectName(u"exerciseTwoMenuButton")
        self.exerciseTwoMenuButton.setGeometry(QRect(0, 0, 281, 30))
        self.exerciseTwoMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseTwoMenuButton.setStyleSheet(u"padding-left: 20px;\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(0, 0, 0);")
        self.exerciseTwoShow = QPushButton(self.exerciseTwoMenuLayout)
        self.exerciseTwoShow.setObjectName(u"exerciseTwoShow")
        self.exerciseTwoShow.setGeometry(QRect(260, 0, 40, 30))
        self.exerciseTwoShow.setMinimumSize(QSize(0, 30))
        self.exerciseTwoShow.setMaximumSize(QSize(40, 16777215))
        self.exerciseTwoShow.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"border-left: 1px solid;\n"
"border-left-color: rgb(17, 66, 127);")

        self.horizontalLayout_35.addWidget(self.exerciseTwoMenuLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_35)

        self.exerciseTwoOneMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseTwoOneMenuButton.setObjectName(u"exerciseTwoOneMenuButton")
        self.exerciseTwoOneMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseTwoOneMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;")

        self.verticalLayout.addWidget(self.exerciseTwoOneMenuButton)

        self.exerciseTwoTwoMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseTwoTwoMenuButton.setObjectName(u"exerciseTwoTwoMenuButton")
        self.exerciseTwoTwoMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseTwoTwoMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")

        self.verticalLayout.addWidget(self.exerciseTwoTwoMenuButton)

        self.exerciseTwoThreeMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseTwoThreeMenuButton.setObjectName(u"exerciseTwoThreeMenuButton")
        self.exerciseTwoThreeMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseTwoThreeMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")

        self.verticalLayout.addWidget(self.exerciseTwoThreeMenuButton)

        self.exerciseTwoFourMenuButton = QPushButton(self.verticalLayoutWidget)
        self.exerciseTwoFourMenuButton.setObjectName(u"exerciseTwoFourMenuButton")
        self.exerciseTwoFourMenuButton.setMinimumSize(QSize(0, 30))
        self.exerciseTwoFourMenuButton.setStyleSheet(u"padding-left: 40px;\n"
"color: rgb(0, 0, 0);\n"
"text-align: left;\n"
"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"color: rgb(170, 170, 170);")

        self.verticalLayout.addWidget(self.exerciseTwoFourMenuButton)

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
        self.stackedWidget_2.setCurrentIndex(0)


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
        self.exTwoImage.setText("")
        self.exerciseOneButton_2.setText(QCoreApplication.translate("Widget", u"1. Sovellus klusterissa", None))
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
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">Kubernetes</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> on avoimen l\u00e4hdekoodin alusta, jonka avulla voidaan toteuttaa konttiorkestrointia. Kuberneteksen </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">klusteri</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\""
                        "> koordinoi joukkoa tietokoneita, jotka ovat yhteydess\u00e4 toisiinsa ja toimivat yhten\u00e4isen\u00e4 kokonaisuutena. Jotta Kuberneteksen hajautettua k\u00e4ytt\u00f6\u00f6nottomallia voitaisiin hy\u00f6dynt\u00e4\u00e4, sovellukset tulee pakata siten, ett\u00e4 ne eiv\u00e4t ole riippuvaisia yksitt\u00e4isist\u00e4 is\u00e4nt\u00e4koneista. Sovellukset tulee siis </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">kontittaa. </span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Kubernetes automatisoi sovelluskonttien yll\u00e4pitoa klusterissa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kuberneteksen klusteri koostuu kahden "
                        "tyyppisest\u00e4 p\u00e4\u00e4komponentista:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">        -</span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\"> </span><span style=\" font-family:'Candara'; font-size:11pt;\">Ohjaustaso koordinoi klusteria</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">        -</span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\"> </span><span style=\" font-family:'Candara'; font-size:11pt;\">Solmut ovat klusterin ty\u00f6ntekij\u00f6it\u00e4, jotka ajavat kontitettuja sovelluksia</span></p></body></html>", None))
        self.clusterImage.setText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ohjaustaso</span><span style=\" font-family:'Candara'; font-size:11pt;\"> vastaa klusterin yll\u00e4pidosta. Ohjaustaso hallinnoi klusterin kaikkia aktiviteetteja, kuten sovellusten aikataulutusta, sovellusten skaalauksesta sek\u00e4 halutun tilan yll\u00e4pidosta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Ohjaustasosta l\u00f6ytyy viisi erilaista komponenttia. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">API-palvelin</span><span style=\" font-family:'Candara'; font-size:11pt;\"> paljastaa Kubernetes APIn klusterille ja toimii frontendin\u00e4 ohjaustasolle. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">etcd</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on johdonmukainen ja saatavilla oleva avainarvos\u00e4il\u00f6 kaikille klusteritiedoille. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ajastin</span><span style=\" font-family:'Candara'; font-size:11pt;\"> seuraa luotuja "
                        "s\u00e4ili\u00f6it\u00e4 ja valitsee niille sopivan solmun. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ohjainmanageri </span><span style=\" font-family:'Candara'; font-size:11pt;\">ajaa ohjainprosesseja, ja </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">pilviohjainmanageri </span><span style=\" font-family:'Candara'; font-size:11pt;\">upottaa klusteriin pilvikohtaisen ohjauslogiikan, ajaa pilveen liittyvi\u00e4 ohjainprosesseja ja mahdollistaa yhdist\u00e4misen pilvitarjoajan APIin.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Solmu</span><span style=\" font-family:'Candara'; font-siz"
                        "e:11pt;\"> on virtuaalikone tai fyysinen kone, joka k\u00e4ytt\u00e4ytyy ty\u00f6ntekij\u00e4koneena Kuberneteksen klusterissa. Solmuja on klusterissa aina ainakin yksi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Solmu koostuu my\u00f6s erilaisista komponenteista. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Kubelet</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on agentti, joka itsen\u00e4isesti yll\u00e4pit\u00e4\u00e4 solmua ja kommunikoi ohjaustason kanssa. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">V\u00e4lipalvelin</span><span style=\" font-family:'Candara'; font-size:11pt;\""
                        "> yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6ja. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Kontin ajoaika</span><span style=\" font-family:'Candara'; font-size:11pt;\"> vastaa konttien toteutuksesta ja elinkaaren hallinnasta. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">S\u00e4ili\u00f6 </span><span style=\" font-family:'Candara'; font-size:11pt;\">on joukko solmussa ajettavia kontteja.</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kuberneteksen klusteri voidaan luoda fyysiselle koneelle tai virtuaalikoneelle. T\u00e4ss\u00e4 oppimisty\u00f6kalussa klusterin luonti toteutetaan Minikuben avulla, jota k\u00e4sitell\u00e4\u00e4n seuraavassa osiossa.</span></p></body></html>", None))
        self.prevOneTwo.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.2. Minikube</span></p></body></html>", None))
        self.nextOneTwo.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Minikube</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on kevyt ja lokaalisti ajettava Kubernetes. Minikube luo virtuaalikoneen paikalliselle koneellesi ja ottaa k\u00e4ytt\u00f6\u00f6n yksinkertaisen klusterin. Luotu klusteri sis\u00e4lt\u00e4\u00e4 yhden solmun. Minikuben komentorivik\u00e4ytt\u00f6liittym\u00e4"
                        " tarjoaa mahdollisuuden ajaa klusterin perustoimintoja.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Minikuben sivuilta voi tarkkailla Minikubesta l\u00f6ytyvi\u00e4 komentoja: </span><a href=\"https://minikube.sigs.k8s.io/docs/commands/\"><span style=\" font-family:'Candara'; font-size:11pt; text-decoration: underline; color:#0078d4;\">https://minikube.sigs.k8s.io/docs/commands/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Klusterin voi k\u00e4ynnist\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Minikuben 1.32.0 versiossa on raportoitu h\u00e4iri\u00f6it\u00e4 eri k\u00e4ytt\u00f6j\u00e4rjestelmill\u00e4. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0</span><span style=\" font-family:'Candara'; font-size:11pt;\"> (tai mahdollisesti my\u00f6hempi ve"
                        "rsio), on klusterin k\u00e4ynnistyksen yhteydess\u00e4 hyv\u00e4 k\u00e4ytt\u00e4\u00e4 jotain muuta kun version mukana tulevaa alkuper\u00e4ist\u00e4 kuvaa. Alla on esimerkki vaihtoehtoisesta ajamisesta:</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start --base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830</span></p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kun on valmis lopettamaan klusterin k\u00e4yt\u00f6n, klusteri voidaan pys\u00e4ytt\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube stop</span></p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Vaihtoehtoisesti jos kokee, ettei klusteria en\u00e4\u00e4 tarvitse ollenkaan, Minikuben virtuaalikone ja sen yhteydess\u00e4 my\u00f6s klusteri voidaan poistaa:</span></p></body></html>", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube delete</span></p></body></html>", None))
        self.prevOneThree.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.3. Klusterin rakenne</span></p></body></html>", None))
        self.nextOneThree.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">Valitse klusterin komponentti, joka sopii parhaiten esitettyyn ominaisuuteen/ty\u00f6teht\u00e4v\u00e4\u00e4n.</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">1. Joukko ajettavia kontteja.</span></p></body></html>", None))
        self.oneThreeCombo_1.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_1.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_1.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_1.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_1.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_1.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_1.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_1.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_1.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_1.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_1.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_1.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.oneThreeCombo_1.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">2. Yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6j\u00e4.</span></p></body></html>", None))
        self.oneThreeCombo_2.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_2.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_2.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_2.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_2.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_2.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_2.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_2.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_2.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_2.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_2.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_2.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_11.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">3. Mahdollistaa klusterin yhdist\u00e4misen pilvitarjoajan APIin.</span></p></body></html>", None))
        self.oneThreeCombo_3.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_3.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_3.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_3.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_3.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_3.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_3.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_3.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_3.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_3.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_3.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_3.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_12.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">4. Huolehtii yleisesti klusterin yll\u00e4pidosta.</span></p></body></html>", None))
        self.oneThreeCombo_4.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_4.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_4.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_4.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_4.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_4.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_4.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_4.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_4.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_4.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_4.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_4.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_13.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">5. Valitsee s\u00e4ili\u00f6lle sopivan solmun.</span></p></body></html>", None))
        self.oneThreeCombo_5.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_5.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_5.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_5.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_5.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_5.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_5.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_5.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_5.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_5.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_5.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_5.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_14.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">6. Kommunikoi solmussa ohjaustason kanssa.</span></p></body></html>", None))
        self.oneThreeCombo_6.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_6.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_6.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_6.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_6.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_6.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_6.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_6.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_6.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_6.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_6.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_6.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_16.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">7. Klusterin ty\u00f6ntekij\u00e4kone.</span></p></body></html>", None))
        self.oneThreeCombo_7.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_7.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_7.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_7.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_7.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_7.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_7.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_7.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_7.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_7.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_7.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_7.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.checkOneThree.setText(QCoreApplication.translate("Widget", u"Tarkista vastaukset", None))
        self.prevOneFour.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.4. Klusterin luonti</span></p></body></html>", None))
        self.nextOneFour.setText(QCoreApplication.translate("Widget", u"Lopeta", None))
        self.infoBrowser_6.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">1. Luo Minikubella klusteri.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Huom! Muista lis\u00e4t\u00e4 komennon loppuun </span><span style=\" font-family:'Courier New'; font-size:11pt; color:#000000;"
                        "\">--base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830 </span><span style=\" font-family:'Candara'; font-size:11pt;\">jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0 (tai vanhempi). Voit tarkistaa version etusivulta.</span></p></body></html>", None))
        self.oneFourButton_1.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.oneFourResult_1.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI Symbol'; font-size:11pt;\"><br /></p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">2. Pys\u00e4yt\u00e4 klusteri.</span></p></body></html>", None))
        self.oneFourButton_2.setText(QCoreApplication.translate("Widget", u"Aja komento", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.title_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">1. Sovellus klusterissa</span></p></body></html>", None))
        self.sub_7.setText("")
        self.exerciseTwoOneButton.setText(QCoreApplication.translate("Widget", u"1.1. Kubernetes klusterin perusteet", None))
        self.exerciseTwoTwoButton.setText(QCoreApplication.translate("Widget", u"1.2. Minikube", None))
        self.exerciseTwoThreeButton.setText(QCoreApplication.translate("Widget", u"1.3. Klusterin rakenne", None))
        self.exerciseTwoFourButton.setText(QCoreApplication.translate("Widget", u"1.4. Klusterin luonti", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.prevTwoOne.setText(QCoreApplication.translate("Widget", u"Palaa teht\u00e4v\u00e4sivulle", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.1. Kubernetes-klusteri</span></p></body></html>", None))
        self.nextTwoOne.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">Kubernetes</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> on avoimen l\u00e4hdekoodin alusta, jonka avulla voidaan toteuttaa konttiorkestrointia. Kuberneteksen </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">klusteri</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\""
                        "> koordinoi joukkoa tietokoneita, jotka ovat yhteydess\u00e4 toisiinsa ja toimivat yhten\u00e4isen\u00e4 kokonaisuutena. Jotta Kuberneteksen hajautettua k\u00e4ytt\u00f6\u00f6nottomallia voitaisiin hy\u00f6dynt\u00e4\u00e4, sovellukset tulee pakata siten, ett\u00e4 ne eiv\u00e4t ole riippuvaisia yksitt\u00e4isist\u00e4 is\u00e4nt\u00e4koneista. Sovellukset tulee siis </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700;\">kontittaa. </span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Kubernetes automatisoi sovelluskonttien yll\u00e4pitoa klusterissa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kuberneteksen klusteri koostuu kahden "
                        "tyyppisest\u00e4 p\u00e4\u00e4komponentista:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">        -</span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\"> </span><span style=\" font-family:'Candara'; font-size:11pt;\">Ohjaustaso koordinoi klusteria</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">        -</span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\"> </span><span style=\" font-family:'Candara'; font-size:11pt;\">Solmut ovat klusterin ty\u00f6ntekij\u00f6it\u00e4, jotka ajavat kontitettuja sovelluksia</span></p></body></html>", None))
        self.clusterImage_2.setText("")
        self.textBrowser_12.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ohjaustaso</span><span style=\" font-family:'Candara'; font-size:11pt;\"> vastaa klusterin yll\u00e4pidosta. Ohjaustaso hallinnoi klusterin kaikkia aktiviteetteja, kuten sovellusten aikataulutusta, sovellusten skaalauksesta sek\u00e4 halutun tilan yll\u00e4pidosta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Ohjaustasosta l\u00f6ytyy viisi erilaista komponenttia. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">API-palvelin</span><span style=\" font-family:'Candara'; font-size:11pt;\"> paljastaa Kubernetes APIn klusterille ja toimii frontendin\u00e4 ohjaustasolle. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">etcd</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on johdonmukainen ja saatavilla oleva avainarvos\u00e4il\u00f6 kaikille klusteritiedoille. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ajastin</span><span style=\" font-family:'Candara'; font-size:11pt;\"> seuraa luotuja "
                        "s\u00e4ili\u00f6it\u00e4 ja valitsee niille sopivan solmun. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Ohjainmanageri </span><span style=\" font-family:'Candara'; font-size:11pt;\">ajaa ohjainprosesseja, ja </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">pilviohjainmanageri </span><span style=\" font-family:'Candara'; font-size:11pt;\">upottaa klusteriin pilvikohtaisen ohjauslogiikan, ajaa pilveen liittyvi\u00e4 ohjainprosesseja ja mahdollistaa yhdist\u00e4misen pilvitarjoajan APIin.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Solmu</span><span style=\" font-family:'Candara'; font-siz"
                        "e:11pt;\"> on virtuaalikone tai fyysinen kone, joka k\u00e4ytt\u00e4ytyy ty\u00f6ntekij\u00e4koneena Kuberneteksen klusterissa. Solmuja on klusterissa aina ainakin yksi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Solmu koostuu my\u00f6s erilaisista komponenteista. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Kubelet</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on agentti, joka itsen\u00e4isesti yll\u00e4pit\u00e4\u00e4 solmua ja kommunikoi ohjaustason kanssa. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">V\u00e4lipalvelin</span><span style=\" font-family:'Candara'; font-size:11pt;\""
                        "> yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6ja. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Kontin ajoaika</span><span style=\" font-family:'Candara'; font-size:11pt;\"> vastaa konttien toteutuksesta ja elinkaaren hallinnasta. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">S\u00e4ili\u00f6 </span><span style=\" font-family:'Candara'; font-size:11pt;\">on joukko solmussa ajettavia kontteja.</span></p></body></html>", None))
        self.textBrowser_14.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kuberneteksen klusteri voidaan luoda fyysiselle koneelle tai virtuaalikoneelle. T\u00e4ss\u00e4 oppimisty\u00f6kalussa klusterin luonti toteutetaan Minikuben avulla, jota k\u00e4sitell\u00e4\u00e4n seuraavassa osiossa.</span></p></body></html>", None))
        self.prevTwoTwo.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.2. Minikube</span></p></body></html>", None))
        self.nextTwoTwo.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_7.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Minikube</span><span style=\" font-family:'Candara'; font-size:11pt;\"> on kevyt ja lokaalisti ajettava Kubernetes. Minikube luo virtuaalikoneen paikalliselle koneellesi ja ottaa k\u00e4ytt\u00f6\u00f6n yksinkertaisen klusterin. Luotu klusteri sis\u00e4lt\u00e4\u00e4 yhden solmun. Minikuben komentorivik\u00e4ytt\u00f6liittym\u00e4"
                        " tarjoaa mahdollisuuden ajaa klusterin perustoimintoja.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Minikuben sivuilta voi tarkkailla Minikubesta l\u00f6ytyvi\u00e4 komentoja: </span><a href=\"https://minikube.sigs.k8s.io/docs/commands/\"><span style=\" font-family:'Candara'; font-size:11pt; text-decoration: underline; color:#0078d4;\">https://minikube.sigs.k8s.io/docs/commands/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; font-size:11pt; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Klusterin voi k\u00e4ynnist\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_15.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start</span></p></body></html>", None))
        self.textBrowser_16.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Minikuben 1.32.0 versiossa on raportoitu h\u00e4iri\u00f6it\u00e4 eri k\u00e4ytt\u00f6j\u00e4rjestelmill\u00e4. </span><span style=\" font-family:'Candara'; font-size:11pt; font-weight:700;\">Jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0</span><span style=\" font-family:'Candara'; font-size:11pt;\"> (tai mahdollisesti my\u00f6hempi ve"
                        "rsio), on klusterin k\u00e4ynnistyksen yhteydess\u00e4 hyv\u00e4 k\u00e4ytt\u00e4\u00e4 jotain muuta kun version mukana tulevaa alkuper\u00e4ist\u00e4 kuvaa. Alla on esimerkki vaihtoehtoisesta ajamisesta:</span></p></body></html>", None))
        self.textBrowser_17.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube start --base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830</span></p></body></html>", None))
        self.textBrowser_18.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Kun on valmis lopettamaan klusterin k\u00e4yt\u00f6n, klusteri voidaan pys\u00e4ytt\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_19.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube stop</span></p></body></html>", None))
        self.textBrowser_20.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Vaihtoehtoisesti jos kokee, ettei klusteria en\u00e4\u00e4 tarvitse ollenkaan, Minikuben virtuaalikone ja sen yhteydess\u00e4 my\u00f6s klusteri voidaan poistaa:</span></p></body></html>", None))
        self.textBrowser_21.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; font-size:11pt; color:#e6edf3;\">$ minikube delete</span></p></body></html>", None))
        self.prevTwoThree.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.3. Klusterin rakenne</span></p></body></html>", None))
        self.nextTwoThree.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">Valitse klusterin komponentti, joka sopii parhaiten esitettyyn ominaisuuteen/ty\u00f6teht\u00e4v\u00e4\u00e4n.</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">1. Joukko ajettavia kontteja.</span></p></body></html>", None))
        self.oneThreeCombo_8.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_8.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_8.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_8.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_8.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_8.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_8.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_8.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_8.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_8.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_8.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_8.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.oneThreeCombo_8.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">2. Yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6j\u00e4.</span></p></body></html>", None))
        self.oneThreeCombo_9.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_9.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_9.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_9.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_9.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_9.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_9.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_9.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_9.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_9.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_9.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_9.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_24.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">3. Mahdollistaa klusterin yhdist\u00e4misen pilvitarjoajan APIin.</span></p></body></html>", None))
        self.oneThreeCombo_10.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_10.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_10.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_10.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_10.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_10.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_10.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_10.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_10.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_10.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_10.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_10.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_25.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">4. Huolehtii yleisesti klusterin yll\u00e4pidosta.</span></p></body></html>", None))
        self.oneThreeCombo_11.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_11.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_11.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_11.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_11.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_11.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_11.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_11.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_11.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_11.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_11.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_11.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_26.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">5. Valitsee s\u00e4ili\u00f6lle sopivan solmun.</span></p></body></html>", None))
        self.oneThreeCombo_12.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_12.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_12.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_12.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_12.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_12.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_12.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_12.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_12.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_12.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_12.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_12.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_27.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">6. Kommunikoi solmussa ohjaustason kanssa.</span></p></body></html>", None))
        self.oneThreeCombo_13.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_13.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_13.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_13.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_13.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_13.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_13.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_13.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_13.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_13.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_13.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_13.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.label_28.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">7. Klusterin ty\u00f6ntekij\u00e4kone.</span></p></body></html>", None))
        self.oneThreeCombo_14.setItemText(0, QCoreApplication.translate("Widget", u"Valitse komponentti", None))
        self.oneThreeCombo_14.setItemText(1, QCoreApplication.translate("Widget", u"Ajastin", None))
        self.oneThreeCombo_14.setItemText(2, QCoreApplication.translate("Widget", u"API-palvelin", None))
        self.oneThreeCombo_14.setItemText(3, QCoreApplication.translate("Widget", u"etcd", None))
        self.oneThreeCombo_14.setItemText(4, QCoreApplication.translate("Widget", u"Kontin ajoaika", None))
        self.oneThreeCombo_14.setItemText(5, QCoreApplication.translate("Widget", u"Kubelet", None))
        self.oneThreeCombo_14.setItemText(6, QCoreApplication.translate("Widget", u"Ohjainmanageri", None))
        self.oneThreeCombo_14.setItemText(7, QCoreApplication.translate("Widget", u"Ohjaustaso", None))
        self.oneThreeCombo_14.setItemText(8, QCoreApplication.translate("Widget", u"Pilviohjainmanageri", None))
        self.oneThreeCombo_14.setItemText(9, QCoreApplication.translate("Widget", u"Solmu(t)", None))
        self.oneThreeCombo_14.setItemText(10, QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None))
        self.oneThreeCombo_14.setItemText(11, QCoreApplication.translate("Widget", u"V\u00e4lipalvelin", None))

        self.checkTwoThree.setText(QCoreApplication.translate("Widget", u"Tarkista vastaukset", None))
        self.prevTwoFour.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.4. Klusterin luonti</span></p></body></html>", None))
        self.nextTwoFour.setText(QCoreApplication.translate("Widget", u"Lopeta", None))
        self.infoBrowser_9.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">1. Luo Minikubella klusteri.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">Huom! Muista lis\u00e4t\u00e4 komennon loppuun </span><span style=\" font-family:'Courier New'; font-size:11pt; color:#000000;"
                        "\">--base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830 </span><span style=\" font-family:'Candara'; font-size:11pt;\">jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0 (tai vanhempi). Voit tarkistaa version etusivulta.</span></p></body></html>", None))
        self.TwoFourButton.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.TwoFourResult.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI Symbol'; font-size:11pt;\"><br /></p></body></html>", None))
        self.textBrowser_23.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-size:11pt;\">2. Pys\u00e4yt\u00e4 klusteri.</span></p></body></html>", None))
        self.TwoFourButton_2.setText(QCoreApplication.translate("Widget", u"Aja komento", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
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
        self.exerciseTwoMenuButton.setText(QCoreApplication.translate("Widget", u"2. Sovellus klusterissa", None))
        self.exerciseTwoShow.setText(QCoreApplication.translate("Widget", u"\u25b2", None))
        self.exerciseTwoOneMenuButton.setText(QCoreApplication.translate("Widget", u"2.1. K\u00e4ytt\u00f6\u00f6notto", None))
        self.exerciseTwoTwoMenuButton.setText(QCoreApplication.translate("Widget", u"2.2. Kubectl", None))
        self.exerciseTwoThreeMenuButton.setText(QCoreApplication.translate("Widget", u"2.3. Kubectl-komennot", None))
        self.exerciseTwoFourMenuButton.setText(QCoreApplication.translate("Widget", u"2.4. K\u00e4ytt\u00f6\u00f6noton luonti", None))
        self.userInfoButton.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n tiedot", None))
        self.infoButton.setText(QCoreApplication.translate("Widget", u"Tietoja", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"Asetukset", None))
        self.logoutButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu ulos", None))
        pass
    # retranslateUi

