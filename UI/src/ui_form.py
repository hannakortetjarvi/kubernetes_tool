# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(1562, 834)
        Widget.setWindowTitle(u"Interaktiivinen Kubernetes Oppimisty\u00f6kalu")
        Widget.setStyleSheet(u"background-color: rgb(240, 255, 254);\n"
"font: 11pt \"Consolas\";")
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
        self.menuPages.setGeometry(QRect(320, 0, 1221, 811))
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayoutWidget_2 = QWidget(self.mainPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 1211, 791))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget_2)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
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
        self.labelKubectl.setStyleSheet(u"border-bottom: 1px dotted;\n"
"padding-bottom: 15px;")

        self.verticalLayout_7.addWidget(self.labelKubectl)

        self.textBrowser_27 = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_27.setObjectName(u"textBrowser_27")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_27.sizePolicy().hasHeightForWidth())
        self.textBrowser_27.setSizePolicy(sizePolicy)
        self.textBrowser_27.setMinimumSize(QSize(0, 0))
        self.textBrowser_27.setMaximumSize(QSize(16777215, 130))
        self.textBrowser_27.setStyleSheet(u"border: none;\n"
"padding-top: 5px;")

        self.verticalLayout_7.addWidget(self.textBrowser_27)

        self.textBrowser_28 = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_28.setObjectName(u"textBrowser_28")
        self.textBrowser_28.setMinimumSize(QSize(0, 100))
        self.textBrowser_28.setMaximumSize(QSize(16777215, 150))
        self.textBrowser_28.setStyleSheet(u"border: none;\n"
"padding-top: 5px;")

        self.verticalLayout_7.addWidget(self.textBrowser_28)

        self.textBrowser_29 = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_29.setObjectName(u"textBrowser_29")
        self.textBrowser_29.setMinimumSize(QSize(0, 100))
        self.textBrowser_29.setMaximumSize(QSize(16777215, 200))
        self.textBrowser_29.setStyleSheet(u"border: none;\n"
"padding-top: 5px;")

        self.verticalLayout_7.addWidget(self.textBrowser_29)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_13)

        self.textBrowser_25 = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_25.setObjectName(u"textBrowser_25")
        self.textBrowser_25.setMinimumSize(QSize(0, 100))
        self.textBrowser_25.setMaximumSize(QSize(16777215, 150))
        self.textBrowser_25.setStyleSheet(u"border: none;\n"
"padding-top: 5px;")

        self.verticalLayout_7.addWidget(self.textBrowser_25)

        self.menuPages.addWidget(self.mainPage)
        self.commandPage = QWidget()
        self.commandPage.setObjectName(u"commandPage")
        self.verticalLayoutWidget_12 = QWidget(self.commandPage)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_22 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.title_9 = QLabel(self.verticalLayoutWidget_12)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setMaximumSize(QSize(16777215, 50))
        self.title_9.setFont(font)

        self.verticalLayout_22.addWidget(self.title_9)

        self.label_32 = QLabel(self.verticalLayoutWidget_12)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_22.addWidget(self.label_32)

        self.label_33 = QLabel(self.verticalLayoutWidget_12)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_22.addWidget(self.label_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.commandInput = QTextEdit(self.verticalLayoutWidget_12)
        self.commandInput.setObjectName(u"commandInput")
        sizePolicy.setHeightForWidth(self.commandInput.sizePolicy().hasHeightForWidth())
        self.commandInput.setSizePolicy(sizePolicy)
        self.commandInput.setMinimumSize(QSize(0, 40))
        self.commandInput.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_34.addWidget(self.commandInput)

        self.commandLineButton = QPushButton(self.verticalLayoutWidget_12)
        self.commandLineButton.setObjectName(u"commandLineButton")
        self.commandLineButton.setMinimumSize(QSize(170, 40))
        self.commandLineButton.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"background-color: rgb(176, 194, 221);")

        self.horizontalLayout_34.addWidget(self.commandLineButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_34)

        self.commandLine = QTextBrowser(self.verticalLayoutWidget_12)
        self.commandLine.setObjectName(u"commandLine")
        self.commandLine.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_22.addWidget(self.commandLine)

        self.menuPages.addWidget(self.commandPage)
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
        self.widget.setMinimumSize(QSize(0, 150))
        self.widget.setMaximumSize(QSize(16777215, 150))
        self.widget.setStyleSheet(u"margin-bottom:10px")
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

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.exerciseOneButton = QPushButton(self.horizontalLayoutWidget)
        self.exerciseOneButton.setObjectName(u"exerciseOneButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exerciseOneButton.sizePolicy().hasHeightForWidth())
        self.exerciseOneButton.setSizePolicy(sizePolicy1)
        self.exerciseOneButton.setFont(font)
        self.exerciseOneButton.setStyleSheet(u"border: none;\n"
"color: rgb(0, 85, 255);\n"
"margin-top: 8px;")

        self.verticalLayout_5.addWidget(self.exerciseOneButton)

        self.label_26 = QLabel(self.horizontalLayoutWidget)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_5.addWidget(self.label_26)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.progressBarOneGlobal = QProgressBar(self.horizontalLayoutWidget)
        self.progressBarOneGlobal.setObjectName(u"progressBarOneGlobal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBarOneGlobal.sizePolicy().hasHeightForWidth())
        self.progressBarOneGlobal.setSizePolicy(sizePolicy2)
        self.progressBarOneGlobal.setMinimumSize(QSize(400, 0))
        self.progressBarOneGlobal.setStyleSheet(u"border: 1px solid;")
        self.progressBarOneGlobal.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBarOneGlobal)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.verticalLayoutWidget_7)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 150))
        self.widget_3.setMaximumSize(QSize(16777215, 150))
        self.widget_3.setStyleSheet(u"margin-bottom:10px;")
        self.horizontalLayoutWidget_3 = QWidget(self.widget_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 1201, 152))
        self.horizontalLayout_37 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.exTwoImage = QLabel(self.horizontalLayoutWidget_3)
        self.exTwoImage.setObjectName(u"exTwoImage")
        self.exTwoImage.setMaximumSize(QSize(150, 150))
        self.exTwoImage.setPixmap(QPixmap(u"../../images/ex1.png"))
        self.exTwoImage.setScaledContents(True)

        self.horizontalLayout_37.addWidget(self.exTwoImage)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.exerciseTwoButton = QPushButton(self.horizontalLayoutWidget_3)
        self.exerciseTwoButton.setObjectName(u"exerciseTwoButton")
        sizePolicy1.setHeightForWidth(self.exerciseTwoButton.sizePolicy().hasHeightForWidth())
        self.exerciseTwoButton.setSizePolicy(sizePolicy1)
        self.exerciseTwoButton.setFont(font)
        self.exerciseTwoButton.setStyleSheet(u"border: none;\n"
"color: rgb(0, 85, 255);\n"
"margin-top: 8px;")

        self.verticalLayout_23.addWidget(self.exerciseTwoButton)

        self.label_27 = QLabel(self.horizontalLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_23.addWidget(self.label_27)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_9)

        self.progressBarTwoGlobal = QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBarTwoGlobal.setObjectName(u"progressBarTwoGlobal")
        sizePolicy2.setHeightForWidth(self.progressBarTwoGlobal.sizePolicy().hasHeightForWidth())
        self.progressBarTwoGlobal.setSizePolicy(sizePolicy2)
        self.progressBarTwoGlobal.setMinimumSize(QSize(400, 0))
        self.progressBarTwoGlobal.setStyleSheet(u"border: 1px solid;")
        self.progressBarTwoGlobal.setValue(0)

        self.verticalLayout_23.addWidget(self.progressBarTwoGlobal)


        self.horizontalLayout_37.addLayout(self.verticalLayout_23)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.textBrowser_12 = QTextBrowser(self.verticalLayoutWidget_9)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setStyleSheet(u"border: none;\n"
"border-top: 1px dotted;\n"
"padding-top: 10px;")

        self.verticalLayout_17.addWidget(self.textBrowser_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.infoBrowser_6.setFont(font)
        self.infoBrowser_6.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top:10px;")

        self.verticalLayout_16.addWidget(self.infoBrowser_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.oneFourInput_1 = QTextEdit(self.layoutWidget_5)
        self.oneFourInput_1.setObjectName(u"oneFourInput_1")
        self.oneFourInput_1.setMaximumSize(QSize(16777215, 40))
        self.oneFourInput_1.setBaseSize(QSize(0, 4))
        self.oneFourInput_1.setFont(font)
        self.oneFourInput_1.setAutoFillBackground(False)
        self.oneFourInput_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_16.addWidget(self.oneFourInput_1)

        self.oneFourButton_1 = QPushButton(self.layoutWidget_5)
        self.oneFourButton_1.setObjectName(u"oneFourButton_1")
        self.oneFourButton_1.setMinimumSize(QSize(120, 0))
        self.oneFourButton_1.setMaximumSize(QSize(16777215, 40))
        self.oneFourButton_1.setStyleSheet(u"border: 1px solid gray;\n"
"padding-right: 5px;\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgb(176, 194, 221);\n"
"color: rgb(0, 0, 0);")

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
        self.oneFourInput_2.setMaximumSize(QSize(16777215, 40))
        self.oneFourInput_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_28.addWidget(self.oneFourInput_2)

        self.oneFourButton_2 = QPushButton(self.layoutWidget_5)
        self.oneFourButton_2.setObjectName(u"oneFourButton_2")
        self.oneFourButton_2.setMinimumSize(QSize(120, 0))
        self.oneFourButton_2.setMaximumSize(QSize(16777215, 40))
        self.oneFourButton_2.setStyleSheet(u"border: 1px solid gray;\n"
"padding-right: 5px;\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"color: rgb(197, 197, 197);\n"
"background-color: rgb(144, 144, 144);")

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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.textBrowser_14 = QTextBrowser(self.verticalLayoutWidget_11)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setStyleSheet(u"border: none;\n"
"border-top: 1px dotted;\n"
"padding-top: 10px;")

        self.verticalLayout_18.addWidget(self.textBrowser_14)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.verticalLayout_13.setStretch(1, 6)
        self.exerciseTwoPages.addWidget(self.twoOne)
        self.twoTwo = QWidget()
        self.twoTwo.setObjectName(u"twoTwo")
        self.layoutWidget_7 = QWidget(self.twoTwo)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 0, 1211, 751))
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
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.label_17)

        self.nextTwoTwo = QPushButton(self.layoutWidget_7)
        self.nextTwoTwo.setObjectName(u"nextTwoTwo")

        self.horizontalLayout_13.addWidget(self.nextTwoTwo)


        self.verticalLayout_19.addLayout(self.horizontalLayout_13)

        self.infoBrowser_7 = QTextBrowser(self.layoutWidget_7)
        self.infoBrowser_7.setObjectName(u"infoBrowser_7")
        self.infoBrowser_7.setMinimumSize(QSize(0, 145))
        self.infoBrowser_7.setMaximumSize(QSize(16777215, 160))
        self.infoBrowser_7.setStyleSheet(u"border-top: 1px solid gray;")

        self.verticalLayout_19.addWidget(self.infoBrowser_7)

        self.textBrowser_15 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_15.setObjectName(u"textBrowser_15")
        self.textBrowser_15.setMaximumSize(QSize(16777215, 42))
        self.textBrowser_15.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_15)

        self.textBrowser_18 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_18.setObjectName(u"textBrowser_18")
        self.textBrowser_18.setMaximumSize(QSize(16777215, 55))
        self.textBrowser_18.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_18)

        self.textBrowser_19 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_19.setObjectName(u"textBrowser_19")
        self.textBrowser_19.setMaximumSize(QSize(16777215, 43))
        self.textBrowser_19.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_19)

        self.textBrowser_16 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_16.setObjectName(u"textBrowser_16")
        self.textBrowser_16.setMinimumSize(QSize(0, 75))
        self.textBrowser_16.setMaximumSize(QSize(16777215, 80))
        self.textBrowser_16.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_16)

        self.textBrowser_17 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_17.setObjectName(u"textBrowser_17")
        self.textBrowser_17.setMaximumSize(QSize(16777215, 39))
        self.textBrowser_17.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_17)

        self.textBrowser_20 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_20.setObjectName(u"textBrowser_20")
        self.textBrowser_20.setMaximumSize(QSize(16777215, 35))
        self.textBrowser_20.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_20)

        self.textBrowser_21 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_21.setObjectName(u"textBrowser_21")
        self.textBrowser_21.setMinimumSize(QSize(0, 43))
        self.textBrowser_21.setMaximumSize(QSize(16777215, 45))
        self.textBrowser_21.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_21)

        self.textBrowser_22 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_22.setObjectName(u"textBrowser_22")
        self.textBrowser_22.setMinimumSize(QSize(0, 80))
        self.textBrowser_22.setMaximumSize(QSize(16777215, 85))
        self.textBrowser_22.setStyleSheet(u"border: none;")

        self.verticalLayout_19.addWidget(self.textBrowser_22)

        self.textBrowser_24 = QTextBrowser(self.layoutWidget_7)
        self.textBrowser_24.setObjectName(u"textBrowser_24")
        self.textBrowser_24.setMinimumSize(QSize(0, 43))
        self.textBrowser_24.setMaximumSize(QSize(16777215, 45))
        self.textBrowser_24.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"")

        self.verticalLayout_19.addWidget(self.textBrowser_24)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_11)

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

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.tableWidget = QTableWidget(self.layoutWidget_8)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem21)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setMinimumSize(QSize(550, 270))
        self.tableWidget.setMaximumSize(QSize(550, 270))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(38)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)

        self.horizontalLayout_21.addWidget(self.tableWidget)

        self.tableWidget_3 = QTableWidget(self.layoutWidget_8)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        if (self.tableWidget_3.rowCount() < 10):
            self.tableWidget_3.setRowCount(10)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem43)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy3.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy3)
        self.tableWidget_3.setMinimumSize(QSize(601, 270))
        self.tableWidget_3.setMaximumSize(QSize(16777215, 270))
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setGridStyle(Qt.SolidLine)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(211)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(19)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(19)
        self.tableWidget_3.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_21.addWidget(self.tableWidget_3)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.textBrowser_26 = QTextBrowser(self.layoutWidget_8)
        self.textBrowser_26.setObjectName(u"textBrowser_26")
        sizePolicy3.setHeightForWidth(self.textBrowser_26.sizePolicy().hasHeightForWidth())
        self.textBrowser_26.setSizePolicy(sizePolicy3)
        self.textBrowser_26.setMinimumSize(QSize(0, 100))
        self.textBrowser_26.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_20.addWidget(self.textBrowser_26)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.labelTwoThree_1 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_1.setObjectName(u"labelTwoThree_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelTwoThree_1.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_29.addWidget(self.labelTwoThree_1)

        self.resultTwoThree_1 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_1.setObjectName(u"resultTwoThree_1")

        self.horizontalLayout_29.addWidget(self.resultTwoThree_1)

        self.inputTwoThree_1 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_1.setObjectName(u"inputTwoThree_1")
        self.inputTwoThree_1.setMaximumSize(QSize(430, 300))

        self.horizontalLayout_29.addWidget(self.inputTwoThree_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.labelTwoThree_2 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_2.setObjectName(u"labelTwoThree_2")
        sizePolicy4.setHeightForWidth(self.labelTwoThree_2.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_27.addWidget(self.labelTwoThree_2)

        self.resultTwoThree_2 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_2.setObjectName(u"resultTwoThree_2")

        self.horizontalLayout_27.addWidget(self.resultTwoThree_2)

        self.inputTwoThree_2 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_2.setObjectName(u"inputTwoThree_2")
        self.inputTwoThree_2.setMaximumSize(QSize(430, 16777215))

        self.horizontalLayout_27.addWidget(self.inputTwoThree_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.labelTwoThree_3 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_3.setObjectName(u"labelTwoThree_3")
        sizePolicy4.setHeightForWidth(self.labelTwoThree_3.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout_26.addWidget(self.labelTwoThree_3)

        self.resultTwoThree_3 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_3.setObjectName(u"resultTwoThree_3")

        self.horizontalLayout_26.addWidget(self.resultTwoThree_3)

        self.inputTwoThree_3 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_3.setObjectName(u"inputTwoThree_3")
        self.inputTwoThree_3.setMaximumSize(QSize(430, 16777215))

        self.horizontalLayout_26.addWidget(self.inputTwoThree_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.labelTwoThree_4 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_4.setObjectName(u"labelTwoThree_4")
        sizePolicy4.setHeightForWidth(self.labelTwoThree_4.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout_25.addWidget(self.labelTwoThree_4)

        self.resultTwoThree_4 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_4.setObjectName(u"resultTwoThree_4")

        self.horizontalLayout_25.addWidget(self.resultTwoThree_4)

        self.inputTwoThree_4 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_4.setObjectName(u"inputTwoThree_4")
        self.inputTwoThree_4.setMaximumSize(QSize(430, 16777215))

        self.horizontalLayout_25.addWidget(self.inputTwoThree_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.labelTwoThree_5 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_5.setObjectName(u"labelTwoThree_5")
        sizePolicy4.setHeightForWidth(self.labelTwoThree_5.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_23.addWidget(self.labelTwoThree_5)

        self.resultTwoThree_5 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_5.setObjectName(u"resultTwoThree_5")

        self.horizontalLayout_23.addWidget(self.resultTwoThree_5)

        self.inputTwoThree_5 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_5.setObjectName(u"inputTwoThree_5")
        self.inputTwoThree_5.setMaximumSize(QSize(430, 16777215))

        self.horizontalLayout_23.addWidget(self.inputTwoThree_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.labelTwoThree_6 = QLabel(self.layoutWidget_8)
        self.labelTwoThree_6.setObjectName(u"labelTwoThree_6")
        sizePolicy4.setHeightForWidth(self.labelTwoThree_6.sizePolicy().hasHeightForWidth())
        self.labelTwoThree_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_24.addWidget(self.labelTwoThree_6)

        self.resultTwoThree_6 = QLabel(self.layoutWidget_8)
        self.resultTwoThree_6.setObjectName(u"resultTwoThree_6")

        self.horizontalLayout_24.addWidget(self.resultTwoThree_6)

        self.inputTwoThree_6 = QLineEdit(self.layoutWidget_8)
        self.inputTwoThree_6.setObjectName(u"inputTwoThree_6")
        self.inputTwoThree_6.setMaximumSize(QSize(430, 16777215))

        self.horizontalLayout_24.addWidget(self.inputTwoThree_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)


        self.verticalLayout_20.addLayout(self.verticalLayout_6)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_3)

        self.checkTwoThree = QPushButton(self.layoutWidget_8)
        self.checkTwoThree.setObjectName(u"checkTwoThree")
        self.checkTwoThree.setMinimumSize(QSize(200, 30))
        self.checkTwoThree.setFont(font)
        self.checkTwoThree.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.checkTwoThree)


        self.verticalLayout_20.addLayout(self.horizontalLayout_30)

        self.infoTwoThree = QLabel(self.layoutWidget_8)
        self.infoTwoThree.setObjectName(u"infoTwoThree")

        self.verticalLayout_20.addWidget(self.infoTwoThree)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)

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
        self.infoBrowser_9.setMinimumSize(QSize(0, 0))
        self.infoBrowser_9.setMaximumSize(QSize(16777215, 110))
        self.infoBrowser_9.setStyleSheet(u"border-top: 1px solid gray;\n"
"padding-top:10px;")

        self.verticalLayout_21.addWidget(self.infoBrowser_9)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.twoFourInput_1 = QTextEdit(self.layoutWidget_9)
        self.twoFourInput_1.setObjectName(u"twoFourInput_1")
        self.twoFourInput_1.setMaximumSize(QSize(16777215, 50))
        self.twoFourInput_1.setBaseSize(QSize(0, 4))
        self.twoFourInput_1.setAutoFillBackground(False)
        self.twoFourInput_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_32.addWidget(self.twoFourInput_1)

        self.twoFourButton_1 = QPushButton(self.layoutWidget_9)
        self.twoFourButton_1.setObjectName(u"twoFourButton_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.twoFourButton_1.sizePolicy().hasHeightForWidth())
        self.twoFourButton_1.setSizePolicy(sizePolicy5)
        self.twoFourButton_1.setMinimumSize(QSize(120, 0))
        self.twoFourButton_1.setMaximumSize(QSize(16777215, 50))
        self.twoFourButton_1.setStyleSheet(u"border: 1px solid gray;\n"
"padding-right: 5px;\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgb(176, 194, 221);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_32.addWidget(self.twoFourButton_1)


        self.verticalLayout_21.addLayout(self.horizontalLayout_32)

        self.label_30 = QLabel(self.layoutWidget_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_21.addWidget(self.label_30)

        self.twoFourResult_1 = QTextBrowser(self.layoutWidget_9)
        self.twoFourResult_1.setObjectName(u"twoFourResult_1")
        self.twoFourResult_1.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_21.addWidget(self.twoFourResult_1)

        self.textBrowser_23 = QTextBrowser(self.layoutWidget_9)
        self.textBrowser_23.setObjectName(u"textBrowser_23")
        self.textBrowser_23.setMaximumSize(QSize(16777215, 40))
        self.textBrowser_23.setStyleSheet(u"border: none;\n"
"margin-top:10px;")

        self.verticalLayout_21.addWidget(self.textBrowser_23)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.twoFourInput_2 = QTextEdit(self.layoutWidget_9)
        self.twoFourInput_2.setObjectName(u"twoFourInput_2")
        self.twoFourInput_2.setMaximumSize(QSize(16777215, 50))
        self.twoFourInput_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.horizontalLayout_33.addWidget(self.twoFourInput_2)

        self.twoFourButton_2 = QPushButton(self.layoutWidget_9)
        self.twoFourButton_2.setObjectName(u"twoFourButton_2")
        self.twoFourButton_2.setMinimumSize(QSize(120, 0))
        self.twoFourButton_2.setMaximumSize(QSize(16777215, 50))
        self.twoFourButton_2.setStyleSheet(u"border: 1px solid gray;\n"
"padding-right: 5px;\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"color: rgb(197, 197, 197);\n"
"background-color: rgb(144, 144, 144);")

        self.horizontalLayout_33.addWidget(self.twoFourButton_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_33)

        self.label_31 = QLabel(self.layoutWidget_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_21.addWidget(self.label_31)

        self.twoFourResult_2 = QTextBrowser(self.layoutWidget_9)
        self.twoFourResult_2.setObjectName(u"twoFourResult_2")
        self.twoFourResult_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_21.addWidget(self.twoFourResult_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.subUserInfo = QLabel(self.verticalLayoutWidget_5)
        self.subUserInfo.setObjectName(u"subUserInfo")
        self.subUserInfo.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_11.addWidget(self.subUserInfo)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_21 = QLabel(self.verticalLayoutWidget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_36.addWidget(self.label_21)

        self.label_23 = QLabel(self.verticalLayoutWidget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_23)

        self.feedbackValue = QSlider(self.verticalLayoutWidget_5)
        self.feedbackValue.setObjectName(u"feedbackValue")
        self.feedbackValue.setMaximumSize(QSize(400, 16777215))
        self.feedbackValue.setMinimum(1)
        self.feedbackValue.setMaximum(3)
        self.feedbackValue.setValue(2)
        self.feedbackValue.setOrientation(Qt.Horizontal)

        self.horizontalLayout_36.addWidget(self.feedbackValue)

        self.label_22 = QLabel(self.verticalLayoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_36.addWidget(self.label_22)


        self.verticalLayout_11.addLayout(self.horizontalLayout_36)

        self.label_25 = QLabel(self.verticalLayoutWidget_5)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_11.addWidget(self.label_25)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_12)

        self.label_24 = QLabel(self.verticalLayoutWidget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border: 1px dotted;\n"
"padding:5px;")

        self.verticalLayout_11.addWidget(self.label_24)

        self.achievements = QTextBrowser(self.verticalLayoutWidget_5)
        self.achievements.setObjectName(u"achievements")
        self.achievements.setMinimumSize(QSize(0, 400))
        self.achievements.setStyleSheet(u"border: 1px dotted;")

        self.verticalLayout_11.addWidget(self.achievements)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

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

        self.commandButton = QPushButton(self.verticalLayoutWidget)
        self.commandButton.setObjectName(u"commandButton")
        self.commandButton.setMinimumSize(QSize(0, 30))
        self.commandButton.setLayoutDirection(Qt.LeftToRight)
        self.commandButton.setStyleSheet(u"border-bottom: 1px solid black;\n"
"border-radius: 0;\n"
"text-align: left;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.commandButton)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.loggedPage)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        self.loginButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu", None))
        self.loginWarning.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n nimi:", None))
        self.title.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Interaktiivinen Kubernetes Oppimisty\u00f6kalu</span></p></body></html>", None))
        self.subMain.setText(QCoreApplication.translate("Widget", u"Hei ", None))
        self.desc.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-weight:700;\">Tervetuloa interaktiiviseen Kubernetes oppimisty\u00f6kaluun!</span></p></body></html>", None))
        self.labelMinikube.setText(QCoreApplication.translate("Widget", u"K\u00e4yt\u00f6ss\u00e4 oleva Minikube versio: ", None))
        self.labelKubectl.setText(QCoreApplication.translate("Widget", u"K\u00e4yt\u00f6ss\u00e4 oleva Kubectl Client versio: ", None))
        self.textBrowser_27.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">T\u00e4m\u00e4n ty\u00f6kalun tarkoituksena on olla tukena avustamassa k\u00e4ytt\u00e4j\u00e4\u00e4 ymm\u00e4rt\u00e4m\u00e4\u00e4n ja k\u00e4ytt\u00e4m\u00e4\u00e4n Kubernetest\u00e4. Ty\u00f6kalu tarjoaa informaatiota Kubernetekseen liittyvist\u00e4 aihealueista ja teht\u00e4vien muodossa tukee k\u00e4ytt\u00e4j\u00e4\u00e4 l\u00e4hestym\u00e4\u00e4n n\u00e4it\u00e4"
                        " aiheita. Ty\u00f6kalun teht\u00e4vien tavoitteena on opettaa Kuberneteksen klustereihin liittyv\u00e4t perustoiminnallisuudet sek\u00e4 niiden ymm\u00e4rt\u00e4miseen tarvittava teoria. N\u00e4ihin perustoiminnallisuuksiin kuuluu mm. klustereiden luonti, laajentaminen, muokkaaminen ja poistaminen sek\u00e4 sovelluksien k\u00e4ytt\u00f6\u00f6notto ja hallinta klustereiden sis\u00e4ll\u00e4.</span></p></body></html>", None))
        self.textBrowser_28.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#000000;\">ESITIEDOT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Ennen ty\u00f6kalun k\u00e4ytt\u00f6\u00e4 on hyv\u00e4 ymm\u00e4rt\u00e4\u00e4 perusasiat konteista (engl. container). Moni konttien parissa t\u00f6it\u00e4 tekev\u00e4 yritys"
                        " on n\u00e4it\u00e4 kuvaillut sivuillansa, kuten mm.:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">	- Google Cloud: </span><a href=\"https://cloud.google.com/learn/what-are-containers\"><span style=\" text-decoration: underline; color:#007af4;\">https://cloud.google.com/learn/what-are-containers</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">	- Microsoft Azure: </span><a href=\"https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container\"><span style=\" text-decoration: underline; color:#007af4;\">https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container</span></a></p></body></html>", None))
        self.textBrowser_29.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#000000;\">TARVITTAVAT TEKNOLOGIAT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Jotta teht\u00e4vi\u00e4 voidaan suorittaa niin kuten ty\u00f6kalussa ne ollaan suunniteltu suoritettavaksi, ty\u00f6kalua ajavalle koneelle tulee asentaa seuraav"
                        "at teknologiat:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">	- </span><span style=\" font-weight:700; color:#000000;\">Minikube</span><span style=\" color:#000000;\">: </span><a href=\"https://minikube.sigs.k8s.io/docs/start/\"><span style=\" text-decoration: underline; color:#007af4;\">https://minikube.sigs.k8s.io/docs/start/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">	- </span><span style=\" font-weight:700; color:#000000;\">Kubectl</span><span style=\" color:#000000;\">: </span><a href=\"https://kubernetes.io/docs/tasks/tools/#kubectl\"><span style=\" text-decoration: underline; color:#007af4;\">https://kubernetes.io/docs/tasks/tools/#kubectl</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" color:#000000;\">Jos koneellasi on n\u00e4m\u00e4 teknologiat asennettu onnistuneesti, t\u00e4lle sivulle tulostuu teknologioiden asennetut versiot kohtiin </span><span style=\" font-style:italic; color:#000000;\">K\u00e4yt\u00f6ss\u00e4 oleva Minikube versio</span><span style=\" color:#000000;\"> ja </span><span style=\" font-style:italic; color:#000000;\">K\u00e4yt\u00f6ss\u00e4 oleva Kubectl Client versio</span><span style=\" color:#000000;\">.</span></p></body></html>", None))
        self.textBrowser_25.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#7e7e7e;\">Huom! T\u00e4m\u00e4 versio sovelluksesta ei ole viel\u00e4 valmis toteutus. Jos j\u00e4it kaipaamaan lis\u00e4\u00e4 ymm\u00e4rryst\u00e4 Kuberneteksesta ja klusterin mahdollisista toiminnallisuuksista, voit tutustua aiheeseen enemm\u00e4n Kuberneteksen sivuilla:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#535353;\">	- </span><a href=\"https://kubernetes.io/docs/home/\"><span style=\" text-decoration: underline; color:#57a8ff;\">https://kubernetes.io/docs/home/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#535353;\">	- </span><a href=\"https://kubernetes.io/docs/tasks/\"><span style=\" text-decoration: underline; color:#57a8ff;\">https://kubernetes.io/docs/tasks/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#535353;\">	- </span><a href=\"https://kubernetes.io/docs/tutorials/\"><span style=\" text-decoration: underline; color:#57a8ff;\">https://kubernetes.io/docs/tutorials/</span></a></p></body></html>", None))
        self.title_9.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Komentokehote</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Widget", u"Voit testata komentojen ajamista t\u00e4ss\u00e4 komentokehotteessa. Komentokehote toimii kuten lokaali komentokehotteesi ja on", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"yhteydess\u00e4 koneeseesi.", None))
        self.commandLineButton.setText(QCoreApplication.translate("Widget", u"Aja komento", None))
        self.title_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Teht\u00e4v\u00e4t</span></p></body></html>", None))
        self.sub_4.setText("")
        self.desc_4.setText("")
        self.exOneImage.setText("")
        self.exerciseOneButton.setText(QCoreApplication.translate("Widget", u"1. Klusterit", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"Oppimistavoitteet: Kubernetes ja sen klusteri, Minikube, Minikuben k\u00e4ytt\u00f6", None))
        self.exTwoImage.setText("")
        self.exerciseTwoButton.setText(QCoreApplication.translate("Widget", u"2. Sovellus klusterissa", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"Oppimistavoitteet: Sovelluksen k\u00e4ytt\u00f6\u00f6notto klusterissa, Kubectl, Kubectl:n k\u00e4ytt\u00f6", None))
        self.title_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">1. Klusterit</span></p></body></html>", None))
        self.sub_6.setText("")
        self.exerciseOneOneButton.setText(QCoreApplication.translate("Widget", u"1.1. Kubernetes-klusterin perusteet", None))
        self.exerciseOneTwoButton.setText(QCoreApplication.translate("Widget", u"1.2. Minikube", None))
        self.exerciseOneThreeButton.setText(QCoreApplication.translate("Widget", u"1.3. Klusterin rakenne", None))
        self.exerciseOneFourButton.setText(QCoreApplication.translate("Widget", u"1.4. Klusterin luonti", None))
        self.label_7.setText("")
        self.textBrowser_12.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Teht\u00e4v\u00e4kokonaisuus koostuu kahdesta teoriaosuudesta ja kahdesta teht\u00e4v\u00e4osuudesta:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	1.1. Teoriaosuus k\u00e4sittelee Kubernetest\u00e4 ja sen klusteria</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\">	1.2. Teoriaosuus k\u00e4sittelee Minikubea ja sen komentoja</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	1.3. Teht\u00e4v\u00e4 k\u00e4sittelee klusterin rakennetta eli sen komponentteja</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	1.4. Teht\u00e4v\u00e4 k\u00e4sittele Minikuben k\u00e4ytt\u00f6\u00e4 klusterin luomiseen</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Teht\u00e4v\u00e4n toteuttamiseen riitt\u00e4\u00e4, ett\u00e4 <span style=\" font-weight:700;\">ymm\u00e4rt\u00e4\u00e4 perustiedot konteista</span> ja <span style=\" font-weight:700;\">Minikube on asennettuna kone"
                        "elle</span>.</p></body></html>", None))
        self.prevOneOne.setText(QCoreApplication.translate("Widget", u"Palaa teht\u00e4v\u00e4sivulle", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.1. Kubernetes-klusteri</span></p></body></html>", None))
        self.nextOneOne.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">Kubernetes</span><span style=\" font-family:'Segoe UI';\"> on avoimen l\u00e4hdekoodin alusta, jonka avulla voidaan toteuttaa konttiorkestrointia. Kuberneteksen </span><span style=\" font-family:'Segoe UI'; font-weight:700;\">klusteri</span><span style=\" font-family:'Segoe UI';\"> koordinoi joukkoa tietokoneita, jotka ovat yhteydess\u00e4 toi"
                        "siinsa ja toimivat yhten\u00e4isen\u00e4 kokonaisuutena. Jotta Kuberneteksen hajautettua k\u00e4ytt\u00f6\u00f6nottomallia voitaisiin hy\u00f6dynt\u00e4\u00e4, sovellukset tulee pakata siten, ett\u00e4 ne eiv\u00e4t ole riippuvaisia yksitt\u00e4isist\u00e4 is\u00e4nt\u00e4koneista. Sovellukset tulee siis </span><span style=\" font-family:'Segoe UI'; font-weight:700;\">kontittaa. </span><span style=\" font-family:'Segoe UI';\">Kubernetes automatisoi sovelluskonttien yll\u00e4pitoa klusterissa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Kuberneteksen klusteri koostuu kahden tyyppisest\u00e4 p\u00e4\u00e4komponentista:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">        -</span><span style=\" font-family:'Candara'; font-weight:700;\"> </span><span style=\" font-family:'Candara';\">Ohjaustaso koordinoi klusteria</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">        -</span><span style=\" font-family:'Candara'; font-weight:700;\"> </span><span style=\" font-family:'Candara';\">Solmut ovat klusterin ty\u00f6ntekij\u00f6it\u00e4, jotka ajavat kontitettuja sovelluksia</span></p></body></html>", None))
        self.clusterImage.setText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-weight:700;\">Ohjaustaso</span><span style=\" font-family:'Candara';\"> vastaa klusterin yll\u00e4pidosta. Ohjaustaso hallinnoi klusterin kaikkia aktiviteetteja, kuten sovellusten aikataulutusta, sovellusten skaalauksesta sek\u00e4 halutun tilan yll\u00e4pidosta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Ohjaustasosta l\u00f6ytyy viisi erilaista komponenttia. </span><span style=\" font-family:'Candara'; font-weight:700;\">API-palvelin</span><span style=\" font-family:'Candara';\"> paljastaa Kubernetes APIn klusterille ja toimii frontendin\u00e4 ohjaustasolle. </span><span style=\" font-family:'Candara'; font-weight:700;\">etcd</span><span style=\" font-family:'Candara';\"> on johdonmukainen ja saatavilla oleva avainarvos\u00e4il\u00f6 kaikille klusteritiedoille. </span><span style=\" font-family:'Candara'; font-weight:700;\">Ajastin</span><span style=\" font-family:'Candara';\"> seuraa luotuja s\u00e4ili\u00f6it\u00e4 ja valitsee niille sopivan solmun. </span><span style=\" font-family:'Candara'; font-weight:700;\">Ohjainmanageri </span><span style=\""
                        " font-family:'Candara';\">ajaa ohjainprosesseja, ja </span><span style=\" font-family:'Candara'; font-weight:700;\">pilviohjainmanageri </span><span style=\" font-family:'Candara';\">upottaa klusteriin pilvikohtaisen ohjauslogiikan, ajaa pilveen liittyvi\u00e4 ohjainprosesseja ja mahdollistaa yhdist\u00e4misen pilvitarjoajan APIin.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-weight:700;\">Solmu</span><span style=\" font-family:'Candara';\"> on virtuaalikone tai fyysinen kone, joka k\u00e4ytt\u00e4ytyy ty\u00f6ntekij\u00e4koneena Kuberneteksen klusterissa. Solmuja on klusterissa aina ainakin yksi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Solmu koostuu my\u00f6s erilaisista komponenteista. </span><span style=\" font-family:'Candara'; font-weight:700;\">Kubelet</span><span style=\" font-family:'Candara';\"> on agentti, joka itsen\u00e4isesti yll\u00e4pit\u00e4\u00e4 solmua ja kommunikoi ohjaustason kanssa. </span><span style=\" font-family:'Candara'; font-weight:700;\">V\u00e4lipalvelin</span><span style=\" font-family:'Candara';\"> yll\u00e4pit\u00e4\u00e4 solmujen verkkos\u00e4\u00e4nt\u00f6ja. </span><span style=\" font-family:'Candara'; font-weight:700;\">Kontin ajoaika</span><span style=\" font-family:'Candara';\"> vastaa konttien toteutuksesta ja elinkaaren hallinnasta. </span><span style=\" font-family:'Candara'; font-weight:700;\">S\u00e4ili\u00f6 </span><span style=\" font-family:'Ca"
                        "ndara';\">on joukko solmussa ajettavia kontteja.</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Kuberneteksen klusteri voidaan luoda fyysiselle koneelle tai virtuaalikoneelle. T\u00e4ss\u00e4 oppimisty\u00f6kalussa klusterin luonti toteutetaan Minikuben avulla, jota k\u00e4sitell\u00e4\u00e4n seuraavassa osiossa.</span></p></body></html>", None))
        self.prevOneTwo.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">1.2. Minikube</span></p></body></html>", None))
        self.nextOneTwo.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara'; font-weight:700;\">Minikube</span><span style=\" font-family:'Candara';\"> on kevyt ja lokaalisti ajettava Kubernetes. Minikube luo virtuaalikoneen paikalliselle koneellesi ja ottaa k\u00e4ytt\u00f6\u00f6n yksinkertaisen klusterin. Luotu klusteri sis\u00e4lt\u00e4\u00e4 yhden solmun. Minikuben komentorivik\u00e4ytt\u00f6liittym\u00e4 tarjoaa mahdollisuuden ajaa k"
                        "lusterin perustoimintoja.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Minikuben sivuilta voi tarkkailla Minikubesta l\u00f6ytyvi\u00e4 komentoja: </span><a href=\"https://minikube.sigs.k8s.io/docs/commands/\"><span style=\" font-family:'Candara'; text-decoration: underline; color:#0078d4;\">https://minikube.sigs.k8s.io/docs/commands/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Candara'; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                        "style=\" font-family:'Candara';\">Klusterin voi k\u00e4ynnist\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ minikube start</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Minikuben 1.32.0 versiossa on raportoitu h\u00e4iri\u00f6it\u00e4 eri k\u00e4ytt\u00f6j\u00e4rjestelmill\u00e4. </span><span style=\" font-family:'Candara'; font-weight:700;\">Jos k\u00e4yt\u00f6ss\u00e4si on Minikuben versio 1.32.0</span><span style=\" font-family:'Candara';\"> (tai mahdollisesti my\u00f6hempi versio), on klusterin k\u00e4ynnistyksen yhteydess"
                        "\u00e4 hyv\u00e4 k\u00e4ytt\u00e4\u00e4 jotain muuta kun version mukana tulevaa alkuper\u00e4ist\u00e4 kuvaa. Alla on esimerkki vaihtoehtoisesta ajamisesta:</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ minikube start --base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830</span></p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Kun on valmis lopettamaan klusterin k\u00e4yt\u00f6n, klusteri voidaan pys\u00e4ytt\u00e4\u00e4 komennolla:</span></p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ minikube stop</span></p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Vaihtoehtoisesti jos kokee, ettei klusteria en\u00e4\u00e4 tarvitse ollenkaan, Minikuben virtuaalikone ja sen yhteydess\u00e4 my\u00f6s klusteri voidaan poistaa:</span></p></body></html>", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ minikube delete</span></p></body></html>", None))
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
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">1. Luo Minikubella klusteri.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Huom! Muista lis\u00e4t\u00e4 komennon loppuun &quot;--base-image gcr.io/k8s-minikube/kicbase-builds:v0.0.42-1703092832-17830&quot; jos k\u00e4yt\u00f6ss\u00e4"
                        "si on Minikuben versio 1.32.0 (tai vanhempi). Voit tarkistaa version etusivulta.</span></p></body></html>", None))
        self.oneFourButton_1.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.oneFourResult_1.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI Symbol';\"><br /></p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">2. Pys\u00e4yt\u00e4 klusteri.</span></p></body></html>", None))
        self.oneFourButton_2.setText(QCoreApplication.translate("Widget", u"Aja komento", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.title_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">2. Sovellus klusterissa</span></p></body></html>", None))
        self.sub_7.setText("")
        self.exerciseTwoOneButton.setText(QCoreApplication.translate("Widget", u"2.1. K\u00e4ytt\u00f6\u00f6notto", None))
        self.exerciseTwoTwoButton.setText(QCoreApplication.translate("Widget", u"2.2. Kubectl", None))
        self.exerciseTwoThreeButton.setText(QCoreApplication.translate("Widget", u"2.3. Kubectl-komennot", None))
        self.exerciseTwoFourButton.setText(QCoreApplication.translate("Widget", u"2.4. K\u00e4ytt\u00f6\u00f6noton luonti", None))
        self.label_10.setText("")
        self.textBrowser_14.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Teht\u00e4v\u00e4kokonaisuus koostuu kahdesta teoriaosuudesta ja kahdesta teht\u00e4v\u00e4osuudesta:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	2.1. Teoriaosuus k\u00e4sittelee Kuberneteksen k\u00e4ytt\u00f6\u00f6nottoja</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\">	2.2. Teoriaosuus k\u00e4sittelee Kubectl:l\u00e4\u00e4 ja sen komentoja</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	2.3. Teht\u00e4v\u00e4 k\u00e4sittelee Kubectl:n komentoja ja niihin sis\u00e4ltyvi\u00e4 resursseja</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	2.4. Teht\u00e4v\u00e4 k\u00e4sittele k\u00e4ytt\u00f6\u00f6noton luontia Kubectl:ll\u00e4</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Teht\u00e4v\u00e4n toteuttamiseksi <span style=\" font-weight:700;\">t\u00e4ytyy ymm\u00e4rt\u00e4\u00e4 perustiedot konteista,</span> <span style=\" font-weight:700;\">Miniku"
                        "be ja Kubectl tulee olla asennettuna koneelle </span>sek\u00e4<span style=\" font-weight:700;\"> tulee olla ymm\u00e4rrys Kuberneteksen klusterista ja sen luonnista. </span>Teht\u00e4v\u00e4 2.4. my\u00f6s odottaa, ett\u00e4 <span style=\" font-weight:700;\">k\u00e4yt\u00f6ss\u00e4 olevan koneen Minikubella on klusteri olemassa ja k\u00e4ynniss\u00e4</span>.</p></body></html>", None))
        self.prevTwoOne.setText(QCoreApplication.translate("Widget", u"Palaa teht\u00e4v\u00e4sivulle", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">2.1. K\u00e4ytt\u00f6\u00f6notto</span></p></body></html>", None))
        self.nextTwoOne.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kubernetes-klusterin ollessa k\u00e4ynniss\u00e4, sen p\u00e4\u00e4lle voidaan ottaa k\u00e4ytt\u00f6\u00f6n kontitettuja sovelluksia. T\u00e4m\u00e4 tapahtuu luomalla Kubernetes <span style=\" font-weight:700;\">K\u00e4ytt\u00f6\u00f6notto</span>. K\u00e4ytt\u00f6\u00f6notto opastaa Kubernetesta <span style=\" font-weight:700;\">luomaan ja p\u00e4ivitt\u00e4m\u00e4\u00e4n sovelluksen esiintymi\u00e4"
                        "</span>. Kun k\u00e4ytt\u00f6\u00f6notto on luotu, Kuberneteksen ohjaustaso ajastaa k\u00e4ytt\u00f6\u00f6nottossa olevia sovelluksen esiintymi\u00e4 ajettavaksi klusterin solmuissa.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kuberneteksell\u00e4 on ohjain, joka on vastuussa k\u00e4ytt\u00f6\u00f6notoista. Kun sovelluksen esiintym\u00e4t on luotu, Kuberneteksen k\u00e4ytt\u00f6\u00f6noton ohjain seuraa luotuja esiintymi\u00e4 jatkuvasti. Jos solmu, jolla esiintym\u00e4 sijaitsee kaatuu tai poistetaan, k\u00e4ytt\u00f6\u00f6noton ohjain korvaa esiintym\u00e4n toisella esiintym\u00e4ll\u00e4, joka sijaitsee tai sijoitetaan eri solmulla. T\u00e4ll\u00e4 tavalla mahdollistetaan k\u00e4ytt\u00f6\u00f6noton <span style=\" font-weight:700;\">itsens\u00e4 parannettavuus </spa"
                        "n>huoltojen tai virhetilanteiden sattuessa.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">K\u00e4ytt\u00f6\u00f6notolle kerrotaan sen <span style=\" font-weight:700;\">haluttu tila</span>, ja k\u00e4ytt\u00f6\u00f6noton ohjain ohjaa hallitusti k\u00e4ytt\u00f6\u00f6noton nykyist\u00e4 tilaa kohti m\u00e4\u00e4ritetty\u00e4 haluttua tilaa. K\u00e4ytt\u00f6\u00f6noton luontia ja hallintaa toteutetaan <span style=\" font-weight:700;\">Kubectl</span>:ll\u00e4, joka on komentorivik\u00e4ytt\u00f6liittym\u00e4. Kubectl k\u00e4ytt\u00e4\u00e4 Kuberneteksen APIa klusterin kanssa vuorovaikuttamisessa.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Seuraavassa osiossa perehdyt\u00e4\u00e4n tarkemmin Kubectl:l\u00e4\u00e4n.</p></body></html>", None))
        self.prevTwoTwo.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">2.2. Kubectl</span></p></body></html>", None))
        self.nextTwoTwo.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        self.infoBrowser_7.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">T\u00e4ss\u00e4 osiossa k\u00e4yd\u00e4\u00e4n l\u00e4pi Kubectl-komentoja, joiden avulla voidaan luoda k\u00e4ytt\u00f6\u00f6nottoja, jotka ajavat sovelluksia klusterissa.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">K\u00e4ytt\u00f6\u00f6nottoa luodessa t\u00e4ytyy m\u00e4\u00e4ritt\u00e4\u00e4 sovelluksen ajamiseen k\u00e4ytett\u00e4v\u00e4 kontin kuva sek\u00e4 <span style=\" font-weight:700;\">kopioiden</span> (engl. replica) m\u00e4\u00e4r\u00e4, joita haluaa ajaa. Kopiot varmistavat korkean saavutettavuuden, skaalautuvuuden ja vikasietoisuuden yll\u00e4pit\u00e4m\u00e4ll\u00e4 identtisi\u00e4 esiintymi\u00e4 s\u00e4ili\u00f6ist\u00e4.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kubectl-komennot seuraavat seuraavanlaista pohjaa:</p></body></html>", None))
        self.textBrowser_15.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ kubectl </span><span style=\" font-family:'Courier New'; font-style:italic; color:#e6edf3;\">toiminto resurssi</span></p></body></html>", None))
        self.textBrowser_18.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kubectl:ll\u00e4 voidaan varmistaa, ett\u00e4 Kubectl on m\u00e4\u00e4ritelty kommunikoimaan klusterisi kanssa, sek\u00e4 tarkistaa samalla k\u00e4ytt\u00e4j\u00e4- ja palvelinversiot:</p></body></html>", None))
        self.textBrowser_19.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ kubectl version</span></p></body></html>", None))
        self.textBrowser_16.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Komento toteuttaa esitetyn toiminnon (esim. luonti/create, m\u00e4\u00e4rittely/describe ja poisto/delete) esitettyyn resurssiin (esim. solmu/node, k\u00e4ytt\u00f6\u00f6notto/deployment). --help -lipun k\u00e4ytt\u00f6 komennon j\u00e4lkeen tarjoaa ylim\u00e4\u00e4r\u00e4ist\u00e4 tietoa mahdollisista parametreista:</p></body></html>", None))
        self.textBrowser_17.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ kubectl get nodes --help</span></p></body></html>", None))
        self.textBrowser_20.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">T\u00e4t\u00e4 komentopohjaa hy\u00f6dynt\u00e4m\u00e4ll\u00e4 voidaan seuraavalla komennolla luoda k\u00e4ytt\u00f6\u00f6notto sovellukselle:</span></p></body></html>", None))
        self.textBrowser_21.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ kubectl create deployment </span><span style=\" font-family:'Courier New'; font-style:italic; color:#e6edf3;\">k\u00e4ytt\u00f6\u00f6noton-nimi</span><span style=\" font-family:'Courier New'; color:#e6edf3;\"> --image=</span><span style=\" font-family:'Courier New'; font-style:italic; color:#e6edf3;\">k\u00e4ytett\u00e4v\u00e4"
                        "-kuva</span></p></body></html>", None))
        self.textBrowser_22.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kopioiden m\u00e4\u00e4r\u00e4 on oletusarvona 1. Jos kopioita halutaan enemm\u00e4n k\u00e4ytt\u00f6\u00f6noton luonnin yhteydess\u00e4,<span style=\" font-style:italic;\"> --replicas=m\u00e4\u00e4r\u00e4</span> lipulla voidaan m\u00e4\u00e4ritt\u00e4\u00e4 kopioiden m\u00e4\u00e4r\u00e4. Kun k\u00e4ytt\u00f6\u00f6notto on luotu, sen olemassaolo voidaan tarkistaa hakemalla Kubectl:ll\u00e4 olemassao"
                        "levat k\u00e4ytt\u00f6\u00f6notot:</p></body></html>", None))
        self.textBrowser_24.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'Courier New'; color:#e6edf3;\">$ kubectl get deployments</span></p></body></html>", None))
        self.prevTwoThree.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">2.3. Kubectl-komennot</span></p></body></html>", None))
        self.nextTwoThree.setText(QCoreApplication.translate("Widget", u"Seuraava", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Toiminto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Lis\u00e4tietoa", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"create", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Luo resurssi", None));
        ___qtablewidgetitem4 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"delete", None));
        ___qtablewidgetitem5 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Poista resurssi", None));
        ___qtablewidgetitem6 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"describe", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"N\u00e4yt\u00e4 resurssin/resurssien tiedot", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"drain", None));
        ___qtablewidgetitem9 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"Tyhjenn\u00e4 solmu huoltoa varten", None));
        ___qtablewidgetitem10 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"edit", None));
        ___qtablewidgetitem11 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"Muokkaa resurssia", None));
        ___qtablewidgetitem12 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget", u"expose", None));
        ___qtablewidgetitem13 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget", u"Paljasta resurssi uutena palveluna", None));
        ___qtablewidgetitem14 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Widget", u"get", None));
        ___qtablewidgetitem15 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Widget", u"Hae ja tulosta luodut resurssit", None));
        ___qtablewidgetitem16 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Widget", u"label", None));
        ___qtablewidgetitem17 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Widget", u"P\u00e4ivit\u00e4 resurssin luokitteluleimoja", None));
        ___qtablewidgetitem18 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Widget", u"run", None));
        ___qtablewidgetitem19 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Widget", u"Luo ja aja kuva s\u00e4ili\u00f6ss\u00e4", None));
        ___qtablewidgetitem20 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Widget", u"scale", None));
        ___qtablewidgetitem21 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Widget", u"Aseta uusi koko resurssille", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Widget", u"Resurssi (lyhenne)", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Widget", u"Lis\u00e4tietoa", None));

        __sortingEnabled1 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Widget", u"node (no)", None));
        ___qtablewidgetitem25 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Widget", u"Solmu", None));
        ___qtablewidgetitem26 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Widget", u"pod (po)", None));
        ___qtablewidgetitem27 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6", None));
        ___qtablewidgetitem28 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Widget", u"secret", None));
        ___qtablewidgetitem29 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Widget", u"Salaisuus", None));
        ___qtablewidgetitem30 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Widget", u"service (svc)", None));
        ___qtablewidgetitem31 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Widget", u"Palvelu", None));
        ___qtablewidgetitem32 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Widget", u"deployment (deploy)", None));
        ___qtablewidgetitem33 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00f6\u00f6notto", None));
        ___qtablewidgetitem34 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Widget", u"replicasets (rs)", None));
        ___qtablewidgetitem35 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Widget", u"S\u00e4ili\u00f6kopioiden joukko", None));
        ___qtablewidgetitem36 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Widget", u"job", None));
        ___qtablewidgetitem37 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Widget", u"Solmulla ajettava teht\u00e4v\u00e4", None));
        ___qtablewidgetitem38 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Widget", u"role", None));
        ___qtablewidgetitem39 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Widget", u"Rooli, jonka voi asettaa resurssille", None));
        ___qtablewidgetitem40 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Widget", u"all", None));
        ___qtablewidgetitem41 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Widget", u"Kaikki resurssit", None));
        ___qtablewidgetitem42 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Widget", u"replicationcontroller (rc)", None));
        ___qtablewidgetitem43 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Widget", u"Kopioinnin ohjain, huolehtii ett\u00e4 m\u00e4\u00e4ritetty s\u00e4ili\u00f6(t) on saatavilla", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled1)

        self.textBrowser_26.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kirjoita komento, joka toteuttaa esitetyn toiminnon oikeanlaiselle resurssille. Taulukoissa on esitetty k\u00e4ytett\u00e4v\u00e4t toiminnot ja resurssit. Dokumentaatio: <span style=\" color:#00aaff;\">https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands</span><br />Huom! Resurssin muutos monikoksi esim. node -&gt; nodes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Huom! Resurssin nimi kerrotaan usein joko v\u00e4lily\u00f6nnin tai /-merkin j\u00e4lkeen, esim. pod foo tai pod/foo</p></body></html>", None))
        self.labelTwoThree_1.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>1. Poista palvelu, jonka nimi on <span style=\" font-style:italic;\">'palve'</span></p></body></html>", None))
        self.resultTwoThree_1.setText("")
        self.labelTwoThree_2.setText(QCoreApplication.translate("Widget", u"2. Hae s\u00e4ili\u00f6kopioiden joukot:", None))
        self.resultTwoThree_2.setText("")
        self.labelTwoThree_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>3. Muokkaa <span style=\" font-style:italic;\">'johtaja'</span> nimist\u00e4 roolia:</p></body></html>", None))
        self.resultTwoThree_3.setText("")
        self.labelTwoThree_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>4. Skaalaa <span style=\" font-style:italic;\">'k\u00e4ytt\u00f6'</span> nimist\u00e4 k\u00e4ytt\u00f6\u00f6nottoa kolmeen --replicas -lipulla:</p></body></html>", None))
        self.resultTwoThree_4.setText("")
        self.labelTwoThree_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>5. Paljasta <span style=\" font-style:italic;\">'validi-s\u00e4ili\u00f6'</span> niminen s\u00e4ili\u00f6:</p></body></html>", None))
        self.resultTwoThree_5.setText("")
        self.labelTwoThree_6.setText(QCoreApplication.translate("Widget", u"6. N\u00e4yt\u00e4 teht\u00e4vien tiedot:", None))
        self.resultTwoThree_6.setText("")
        self.checkTwoThree.setText(QCoreApplication.translate("Widget", u"Tarkista vastaukset", None))
        self.infoTwoThree.setText("")
        self.prevTwoFour.setText(QCoreApplication.translate("Widget", u"Edellinen", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">2.4. K\u00e4ytt\u00f6\u00f6noton luonti</span></p></body></html>", None))
        self.nextTwoFour.setText(QCoreApplication.translate("Widget", u"Lopeta", None))
        self.infoBrowser_9.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">1. Ota sovellus k\u00e4ytt\u00f6\u00f6n klusterissa luomalla k\u00e4ytt\u00f6\u00f6notto. K\u00e4yt\u00e4 komennon yhteydess\u00e4 kuvaa --image=gcr.io/google-samples/kubernetes-bootcamp:v1. Varmista, ett\u00e4 sinulla on minikubella luotu klusteri k\u00e4ynniss\u00e4 joko suorittamalla teht\u00e4v\u00e4sarja 1. Klusterit, tai ajamalla minikube start -komento K"
                        "omentokehote-v\u00e4lilehdell\u00e4.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">Huom! Muista lis\u00e4t\u00e4 k\u00e4ytt\u00f6\u00f6notolle nimi, nimen voit valita itse.</span></p></body></html>", None))
        self.twoFourButton_1.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.twoFourResult_1.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI Symbol';\"><br /></p></body></html>", None))
        self.textBrowser_23.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Candara';\">2. Hae k\u00e4ytt\u00f6\u00f6notot ja varmista, ett\u00e4 luomasi k\u00e4ytt\u00f6\u00f6notto on olemassa.</span></p></body></html>", None))
        self.twoFourButton_2.setText(QCoreApplication.translate("Widget", u"Aja komento", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.title_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Tietoja</span></p></body></html>", None))
        self.desc_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Interaktiivinen Kubernetes Oppimisty\u00f6kalu </p><p>Versio: v0.1<br/>Version julkaisup\u00e4iv\u00e4: 9.5.2024.</p><p>Kehitt\u00e4j\u00e4: Hanna Kortetj\u00e4rvi</p><p>Sovellus on kehitetty Qt Creatorilla<br/>Application has been developed with Qt Creator</p><p>L\u00e4hteet: <br/>- Kubernetes, <a href=\"https://kubernetes.io/\"><span style=\" text-decoration: underline; color:#007af4;\">https://kubernetes.io/</span></a><br/>- minikube, <a href=\"https://minikube.sigs.k8s.io/docs/start/\"><span style=\" text-decoration: underline; color:#007af4;\">https://minikube.sigs.k8s.io/docs/start/</span></a><br/>- kubectl, <a href=\"https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#plugin\"><span style=\" text-decoration: underline; color:#007af4;\">https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#plugin</span></a><br/>- Qt, <a href=\"https://www.qt.io/product/development-tools\"><span style=\" text-decoration: underline; color:#007af4;\">https://www.qt"
                        ".io/product/development-tools</span></a><br/></p><p><br/></p></body></html>", None))
        self.title_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Asetukset</span></p></body></html>", None))
        self.sub_5.setText("")
        self.subUserInfo.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n nimi: ", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"Palautteen m\u00e4\u00e4r\u00e4:", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"Minimoi palaute", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Maksimoi palaute", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"Palautteen m\u00e4\u00e4r\u00e4\u00e4 muokkaamalla voit m\u00e4\u00e4ritt\u00e4\u00e4, kuinka paljon palautetta haluat ty\u00f6kalun tulostavan virhetilanteessa.", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"Suoritukset:", None))
        self.mainButton.setText(QCoreApplication.translate("Widget", u"Etusivu", None))
        self.commandButton.setText(QCoreApplication.translate("Widget", u"Komentokehote", None))
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
        self.infoButton.setText(QCoreApplication.translate("Widget", u"Tietoja sovelluksesta", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"Asetukset", None))
        self.logoutButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu ulos", None))
        pass
    # retranslateUi

