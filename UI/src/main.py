import sys
import json
import os.path
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from ui_form import Ui_Widget
from utils.command_line import command_call

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

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

        self.ui.exerciseOneMenuLayout.setVisible(False)

        self.ui.exercisesShow.clicked.connect(lambda: self.arrowClicked(0))
        self.ui.exerciseOneShow.clicked.connect(lambda: self.arrowClicked(1))


        self.ui.exOneImage.setPixmap(QPixmap(filename))

    def userLogin(self):
        self.username = self.ui.userNameEdit.text()
        if self.username == "":
            self.ui.loginWarning.setText("Syötä nimi!")
        elif ' ' in self.username:
            self.ui.loginWarning.setText("Nimi ei voi sisältää välilyöntiä!")
        else:
            main = self.ui.menuPages.findChild(QLabel, "subMain")
            main.setText(main.text() + self.username + "!")
            user_info = self.ui.menuPages.findChild(QLabel, "subUserInfo")
            user_info.setText(user_info.text() + self.username)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)

    def userLogout(self):
        main = self.ui.menuPages.findChild(QLabel, "subMain")
        leng = len(self.username) + 1
        main.setText(main.text()[:-leng])
        user_info = self.ui.menuPages.findChild(QLabel, "subUserInfo")
        leng = leng - 1
        user_info.setText(user_info.text()[:-leng])
        self.username = ""
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.exerciseOneMenuLayout.setVisible(False)
        self.ui.exercisesShow.setText("▲")
        self.ui.exerciseOneShow.setText("▲")
        self.exercises_open = False
        self.exercise_one_open = False
        btn = self.previously_clicked
        btn.setStyleSheet(self.previously_clicked_style)
        self.previously_clicked = self.ui.mainButton
        self.previously_clicked_style = self.ui.mainButton.styleSheet()
        self.ui.mainButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

    def arrowClicked(self, num):
        if num == 0 and not self.exercises_open:
            self.ui.exerciseOneMenuLayout.setVisible(True)
            self.ui.exercisesShow.setText("▼")
            self.exercises_open = True
        elif num == 0 and self.exercises_open:
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.ui.exercisesShow.setText("▲")
            self.ui.exerciseOneShow.setText("▲")
            self.exercise_one_open = False
            self.exercises_open = False
        elif num == 1 and not self.exercise_one_open:
            self.ui.exerciseOneOneMenuButton.setVisible(True)
            self.ui.exerciseOneTwoMenuButton.setVisible(True)
            self.ui.exerciseOneThreeMenuButton.setVisible(True)
            self.ui.exerciseOneFourMenuButton.setVisible(True)
            self.ui.exerciseOneShow.setText("▼")
            self.exercise_one_open = True
        elif num == 1 and self.exercise_one_open:
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.ui.exerciseOneShow.setText("▲")
            self.exercise_one_open = False

    def exerciseClicked(self, num):
        btn = self.previously_clicked
        btn.setStyleSheet(self.previously_clicked_style)
        if num == 1:
            self.ui.exerciseOneShow.setVisible(True)
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            self.ui.exerciseOneShow.setText("▼")
            self.ui.exerciseOneOneMenuButton.setVisible(True)
            self.ui.exerciseOneTwoMenuButton.setVisible(True)
            self.ui.exerciseOneThreeMenuButton.setVisible(True)
            self.ui.exerciseOneFourMenuButton.setVisible(True)
            self.previously_clicked = self.ui.exerciseOneMenuButton
            self.previously_clicked_style = self.ui.exerciseOneMenuButton.styleSheet()
            self.ui.exerciseOneMenuButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif num == 11:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(1)
            self.previously_clicked = self.ui.exerciseOneOneMenuButton
            self.previously_clicked_style = self.ui.exerciseOneOneMenuButton.styleSheet()
            self.ui.exerciseOneOneMenuButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif num == 12:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(2)
            self.previously_clicked = self.ui.exerciseOneTwoMenuButton
            self.previously_clicked_style = self.ui.exerciseOneTwoMenuButton.styleSheet()
            self.ui.exerciseOneTwoMenuButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif num == 13:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(3)
            self.previously_clicked = self.ui.exerciseOneThreeMenuButton
            self.previously_clicked_style = self.ui.exerciseOneThreeMenuButton.styleSheet()
            self.ui.exerciseOneThreeMenuButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif num == 14:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(4)
            self.previously_clicked = self.ui.exerciseOneFourMenuButton
            self.previously_clicked_style = self.ui.exerciseOneFourMenuButton.styleSheet()
            self.ui.exerciseOneFourMenuButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

    def menuClicked(self, name):
        self.exercises_open = False
        self.exercise_one_open = False
        self.ui.exercisesShow.setText("▲")
        self.ui.exerciseOneShow.setText("▲")
        btn = self.previously_clicked
        btn.setStyleSheet(self.previously_clicked_style)
        if name == "mainButton":
            self.ui.menuPages.setCurrentIndex(0)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.previously_clicked = self.ui.mainButton
            self.previously_clicked_style = self.ui.mainButton.styleSheet()
            self.ui.mainButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif name == "exercisesButton":
            self.exercises_open = True
            self.ui.exercisesShow.setText("▼")
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            self.ui.exerciseOneMenuLayout.setVisible(True)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.previously_clicked = self.ui.exercisesButton
            self.previously_clicked_style = self.ui.exercisesButton.styleSheet()
            self.ui.exercisesButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif name == "userInfoButton":
            self.ui.menuPages.setCurrentIndex(2)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.previously_clicked = self.ui.userInfoButton
            self.previously_clicked_style = self.ui.userInfoButton.styleSheet()
            self.ui.userInfoButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif name == "infoButton":
            self.ui.menuPages.setCurrentIndex(3)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.previously_clicked = self.ui.infoButton
            self.previously_clicked_style = self.ui.infoButton.styleSheet()
            self.ui.infoButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")
        elif name == "settingsButton":
            self.ui.menuPages.setCurrentIndex(4)
            self.ui.exerciseOneMenuLayout.setVisible(False)
            self.ui.exerciseOneOneMenuButton.setVisible(False)
            self.ui.exerciseOneTwoMenuButton.setVisible(False)
            self.ui.exerciseOneThreeMenuButton.setVisible(False)
            self.ui.exerciseOneFourMenuButton.setVisible(False)
            self.previously_clicked = self.ui.settingsButton
            self.previously_clicked_style = self.ui.settingsButton.styleSheet()
            self.ui.settingsButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

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
    