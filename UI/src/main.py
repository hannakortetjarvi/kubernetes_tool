import sys
import json
import os.path
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_form import Ui_Widget
from utils.command_line import command_call

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(self.CURRENT_DIRECTORY, "../../images/ex1.png")

        self.exercises_open = False
        self.exercise_one_open = False
        self.previously_clicked = self.ui.mainButton
        self.previously_clicked_style = self.ui.mainButton.styleSheet()
        self.ui.mainButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

        #self.ui.runButton.clicked.connect(lambda: self.button_clicked)

        self.ui.loginButton.clicked.connect(self.userLogin)
        self.ui.mainButton.clicked.connect(lambda: self.menuClicked("mainButton"))
        self.ui.exercisesButton.clicked.connect(lambda: self.menuClicked("exercisesButton"))
        self.ui.userInfoButton.clicked.connect(lambda: self.menuClicked("userInfoButton"))
        self.ui.infoButton.clicked.connect(lambda: self.menuClicked("infoButton"))
        self.ui.settingsButton.clicked.connect(lambda: self.menuClicked("settingsButton"))
        self.ui.logoutButton.clicked.connect(self.userLogout)

        self.ui.exerciseOneButton.clicked.connect(lambda: self.exerciseClicked(1))
        self.ui.exerciseOneMenuButton.clicked.connect(lambda: self.exerciseClicked(1))
        self.ui.exerciseOneOneButton.clicked.connect(lambda: self.exerciseClicked(11))
        self.ui.exerciseOneOneMenuButton.clicked.connect(lambda: self.exerciseClicked(11))
        self.ui.exerciseOneTwoButton.clicked.connect(lambda: self.exerciseClicked(12))
        self.ui.exerciseOneTwoMenuButton.clicked.connect(lambda: self.exerciseClicked(12))
        self.ui.exerciseOneThreeButton.clicked.connect(lambda: self.exerciseClicked(13))
        self.ui.exerciseOneThreeMenuButton.clicked.connect(lambda: self.exerciseClicked(13))
        self.ui.exerciseOneFourButton.clicked.connect(lambda: self.exerciseClicked(14))
        self.ui.exerciseOneFourMenuButton.clicked.connect(lambda: self.exerciseClicked(14))
        self.ui.prevOneOne.clicked.connect(lambda: self.exerciseClicked(1))
        self.ui.nextOneOne.clicked.connect(lambda: self.exerciseClicked(12))
        self.ui.prevOneTwo.clicked.connect(lambda: self.exerciseClicked(11))
        self.ui.nextOneTwo.clicked.connect(lambda: self.exerciseClicked(13))
        self.ui.prevOneThree.clicked.connect(lambda: self.exerciseClicked(12))
        self.ui.nextOneThree.clicked.connect(lambda: self.exerciseClicked(14))
        self.ui.prevOneFour.clicked.connect(lambda: self.exerciseClicked(13))
        self.ui.nextOneFour.clicked.connect(lambda: self.menuClicked("exercisesButton"))
        self.ui.exercisesShow.clicked.connect(lambda: self.arrowClicked(0))
        self.ui.exerciseOneShow.clicked.connect(lambda: self.arrowClicked(1))

        self.ui.loginButton.setCursor(Qt.PointingHandCursor)
        btns = self.findChildren(QPushButton)
        for btn in btns:
            btn.setCursor(Qt.PointingHandCursor)

        self.ui.exOneImage.setPixmap(QPixmap(filename))
        self.setupExercise()

    def userLogin(self):
        self.username = self.ui.userNameEdit.text()
        if self.username == "":
            self.ui.loginWarning.setText("Syötä nimi!")
        elif ' ' in self.username:
            self.ui.loginWarning.setText("Nimi ei voi sisältää välilyöntiä!")
        else:
            main = self.ui.menuPages.findChild(QLabel, "subMain")
            user_info = self.ui.menuPages.findChild(QLabel, "subUserInfo")
            main.setText(main.text() + self.username + "!")
            user_info.setText(user_info.text() + self.username)
            self.ui.menuPages.setCurrentIndex(0)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.showExerciseMenu(False)
            self.ui.exerciseOneMenuLayout.setVisible(False)

    def userLogout(self):
        main = self.ui.menuPages.findChild(QLabel, "subMain")
        user_info = self.ui.menuPages.findChild(QLabel, "subUserInfo")
        leng = len(self.username) + 1
        main.setText(main.text()[:-leng])
        leng = leng - 1
        user_info.setText(user_info.text()[:-leng])
        self.username = ""
        self.exercises_open = False
        self.exercise_one_open = False
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.exerciseOneMenuLayout.setVisible(False)
        self.ui.exercisesShow.setText("▲")
        self.ui.exerciseOneShow.setText("▲")
        self.changeBoldedText(self.ui.mainButton)
    
    def setupExercise(self):
        cluster = os.path.join(self.CURRENT_DIRECTORY, "../../images/cluster.png")
        cluster_pixmap = QPixmap(cluster)
        self.ui.clusterImage.setPixmap(cluster_pixmap)

    def arrowClicked(self, num):
        if num == 0 and not self.exercises_open:
            self.ui.exerciseOneMenuLayout.setVisible(True)
            self.ui.exercisesShow.setText("▼")
            self.exercises_open = True
        elif num == 0 and self.exercises_open:
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.showExerciseMenu(False)
            self.ui.exercisesShow.setText("▲")
            self.ui.exerciseOneShow.setText("▲")
            self.exercise_one_open = False
            self.exercises_open = False
        elif num == 1 and not self.exercise_one_open:
            self.showExerciseMenu(True)
            self.ui.exerciseOneShow.setText("▼")
            self.exercise_one_open = True
        elif num == 1 and self.exercise_one_open:
            self.showExerciseMenu(False)
            self.ui.exerciseOneShow.setText("▲")
            self.exercise_one_open = False

    def exerciseClicked(self, num):
        if num == 1:
            self.ui.exerciseOneShow.setVisible(True)
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            self.ui.exerciseOneShow.setText("▼")
            self.showExerciseMenu(True)
            self.changeBoldedText(self.ui.exerciseOneMenuButton)
        elif num == 11:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(1)
            self.changeBoldedText(self.ui.exerciseOneOneMenuButton)
        elif num == 12:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(2)
            self.changeBoldedText(self.ui.exerciseOneTwoMenuButton)
        elif num == 13:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(3)
            self.changeBoldedText(self.ui.exerciseOneThreeMenuButton)
        elif num == 14:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(4)
            self.changeBoldedText(self.ui.exerciseOneFourMenuButton)

    def showExerciseMenu(self, value):
        self.ui.exerciseOneOneMenuButton.setVisible(value)
        self.ui.exerciseOneTwoMenuButton.setVisible(value)
        self.ui.exerciseOneThreeMenuButton.setVisible(value)
        self.ui.exerciseOneFourMenuButton.setVisible(value)

    def changeBoldedText(self, btn):
        btn_prev = self.previously_clicked
        btn_prev.setStyleSheet(self.previously_clicked_style)
        self.previously_clicked = btn
        self.previously_clicked_style = btn.styleSheet()
        btn.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

    def menuClicked(self, name):
        self.exercises_open = False
        self.exercise_one_open = False
        self.ui.exercisesShow.setText("▲")
        self.ui.exerciseOneShow.setText("▲")
        if name == "mainButton":
            self.ui.menuPages.setCurrentIndex(0)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.showExerciseMenu(False)
            self.changeBoldedText(self.ui.mainButton)
        elif name == "exercisesButton":
            self.exercises_open = True
            self.ui.exercisesShow.setText("▼")
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            self.ui.exerciseOneMenuLayout.setVisible(True)
            self.showExerciseMenu(False)
            self.changeBoldedText(self.ui.exercisesButton)
        elif name == "userInfoButton":
            self.ui.menuPages.setCurrentIndex(2)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.showExerciseMenu(False)
            self.changeBoldedText(self.ui.userInfoButton)
        elif name == "infoButton":
            self.ui.menuPages.setCurrentIndex(3)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.showExerciseMenu(False)
            self.changeBoldedText(self.ui.infoButton)
        elif name == "settingsButton":
            self.ui.menuPages.setCurrentIndex(4)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.showExerciseMenu(False)
            self.changeBoldedText(self.ui.settingsButton)

    def button_clicked(self):
        print("test")
        #cmd = self.ui.inputEdit.toPlainText()
        #rtn = command_call(cmd)
        #self.ui.resultBrowser.setPlainText(rtn)



# pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py && python UI/src/main.py
if __name__ == "__main__":
    #command_call("pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py")
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())
    