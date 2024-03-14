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
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(1570, 834)
        Widget.setWindowTitle(u"Kubernetes Learning Tool")
        Widget.setStyleSheet(u"background-color: rgb(240, 255, 254);")
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

        self.verticalLayout_7.addWidget(self.title)

        self.sub = QLabel(self.verticalLayoutWidget_2)
        self.sub.setObjectName(u"sub")

        self.verticalLayout_7.addWidget(self.sub)

        self.desc = QLabel(self.verticalLayoutWidget_2)
        self.desc.setObjectName(u"desc")

        self.verticalLayout_7.addWidget(self.desc)

        self.menuPages.addWidget(self.mainPage)
        self.exercisesPage = QWidget()
        self.exercisesPage.setObjectName(u"exercisesPage")
        self.verticalLayoutWidget_4 = QWidget(self.exercisesPage)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 10, 1211, 801))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.title_4 = QLabel(self.verticalLayoutWidget_4)
        self.title_4.setObjectName(u"title_4")

        self.verticalLayout_10.addWidget(self.title_4)

        self.sub_4 = QLabel(self.verticalLayoutWidget_4)
        self.sub_4.setObjectName(u"sub_4")

        self.verticalLayout_10.addWidget(self.sub_4)

        self.desc_4 = QLabel(self.verticalLayoutWidget_4)
        self.desc_4.setObjectName(u"desc_4")

        self.verticalLayout_10.addWidget(self.desc_4)

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

        self.verticalLayout_12.addWidget(self.title_6)

        self.sub_6 = QLabel(self.verticalLayoutWidget_6)
        self.sub_6.setObjectName(u"sub_6")

        self.verticalLayout_12.addWidget(self.sub_6)

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

        self.verticalLayout_9.addWidget(self.title_3)

        self.sub_3 = QLabel(self.verticalLayoutWidget_3)
        self.sub_3.setObjectName(u"sub_3")

        self.verticalLayout_9.addWidget(self.sub_3)

        self.desc_3 = QLabel(self.verticalLayoutWidget_3)
        self.desc_3.setObjectName(u"desc_3")

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

        self.verticalLayout_11.addWidget(self.title_5)

        self.sub_5 = QLabel(self.verticalLayoutWidget_5)
        self.sub_5.setObjectName(u"sub_5")

        self.verticalLayout_11.addWidget(self.sub_5)

        self.desc_5 = QLabel(self.verticalLayoutWidget_5)
        self.desc_5.setObjectName(u"desc_5")

        self.verticalLayout_11.addWidget(self.desc_5)

        self.menuPages.addWidget(self.settingsPage)
        self.exercisePage = QWidget()
        self.exercisePage.setObjectName(u"exercisePage")
        self.layoutWidget = QWidget(self.exercisePage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, 4, 1221, 801))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_6.addWidget(self.label_11)

        self.infoBrowser = QTextBrowser(self.layoutWidget)
        self.infoBrowser.setObjectName(u"infoBrowser")
        self.infoBrowser.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.verticalLayout_6.addWidget(self.infoBrowser)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.inputEdit = QTextEdit(self.layoutWidget)
        self.inputEdit.setObjectName(u"inputEdit")
        self.inputEdit.setBaseSize(QSize(0, 4))
        self.inputEdit.setAutoFillBackground(False)
        self.inputEdit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.horizontalLayout_11.addWidget(self.inputEdit)

        self.runButton = QPushButton(self.layoutWidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(0, 0))
        self.runButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 5px;\n"
"padding-top: 15px;\n"
"padding-bottom: 15px;")

        self.horizontalLayout_11.addWidget(self.runButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"padding-left: 2px;")

        self.verticalLayout_6.addWidget(self.label_12)

        self.resultBrowser = QTextBrowser(self.layoutWidget)
        self.resultBrowser.setObjectName(u"resultBrowser")
        self.resultBrowser.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 10px;")

        self.verticalLayout_6.addWidget(self.resultBrowser)

        self.verticalLayout_6.setStretch(1, 6)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(4, 3)
        self.menuPages.addWidget(self.exercisePage)
        self.verticalLayoutWidget = QWidget(self.loggedPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 311, 791))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainButton = QPushButton(self.verticalLayoutWidget)
        self.mainButton.setObjectName(u"mainButton")

        self.verticalLayout.addWidget(self.mainButton)

        self.exercisesButton = QPushButton(self.verticalLayoutWidget)
        self.exercisesButton.setObjectName(u"exercisesButton")

        self.verticalLayout.addWidget(self.exercisesButton)

        self.userInfoButton = QPushButton(self.verticalLayoutWidget)
        self.userInfoButton.setObjectName(u"userInfoButton")

        self.verticalLayout.addWidget(self.userInfoButton)

        self.infoButton = QPushButton(self.verticalLayoutWidget)
        self.infoButton.setObjectName(u"infoButton")

        self.verticalLayout.addWidget(self.infoButton)

        self.settingsButton = QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName(u"settingsButton")

        self.verticalLayout.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.verticalLayoutWidget)
        self.logoutButton.setObjectName(u"logoutButton")

        self.verticalLayout.addWidget(self.logoutButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.loggedPage)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        self.loginButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu", None))
        self.title.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.sub.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.desc.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.title_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.sub_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.desc_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.title_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.sub_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.desc_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.title_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.sub_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.desc_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.title_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.sub_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.desc_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt;\">TEHT\u00c4V\u00c4N NIMI/NUMERO</span></p></body></html>", None))
        self.runButton.setText(QCoreApplication.translate("Widget", u" Aja komento", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tuloste:</span></p></body></html>", None))
        self.mainButton.setText(QCoreApplication.translate("Widget", u"Etusivu", None))
        self.exercisesButton.setText(QCoreApplication.translate("Widget", u"Teht\u00e4v\u00e4t", None))
        self.userInfoButton.setText(QCoreApplication.translate("Widget", u"K\u00e4ytt\u00e4j\u00e4n tiedot", None))
        self.infoButton.setText(QCoreApplication.translate("Widget", u"Tietoja", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"Asetukset", None))
        self.logoutButton.setText(QCoreApplication.translate("Widget", u"Kirjaudu ulos", None))
        pass
    # retranslateUi

