import sys
import json
import os.path
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_form import Ui_Widget
from utils.command_line import command_call
from utils.database import database

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.exercise_buttons_menu = [[self.ui.exerciseOneOneMenuButton, self.ui.exerciseOneTwoMenuButton, self.ui.exerciseOneThreeMenuButton, self.ui.exerciseOneFourMenuButton]]
        self.exercise_buttons = [[self.ui.exerciseOneOneButton, self.ui.exerciseOneTwoButton, self.ui.exerciseOneThreeButton, self.ui.exerciseOneFourButton]]
        self.exercise_buttons_next = [[self.ui.nextOneOne, self.ui.nextOneTwo, self.ui.nextOneThree, self.ui.nextOneFour]]
        self.button_stylesheet_clickable = self.ui.exerciseOneOneMenuButton.styleSheet()
        self.button_stylesheet_not_clickable = self.ui.exerciseOneTwoMenuButton.styleSheet()

        self.db = database()
        if self.db.getItems() == []:
            self.db.migrations()

        self.CURRENT_EXERCISE = []
        self.CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(self.CURRENT_DIRECTORY, "../../images/ex1.png")

        self.exercises_open = False
        self.exercise_one_open = False
        self.previously_clicked = self.ui.mainButton
        self.previously_clicked_style = self.ui.mainButton.styleSheet()
        self.ui.mainButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

        self.ui.runButtonOneThree.clicked.connect(lambda: self.button_clicked(1, 3, False))
        self.ui.runButtonOneFour.clicked.connect(lambda: self.button_clicked(1, 4, False))

        self.ui.loginButton.clicked.connect(self.userLogin)
        self.ui.mainButton.clicked.connect(lambda: self.menuClicked("mainButton"))
        self.ui.exercisesButton.clicked.connect(lambda: self.menuClicked("exercisesButton"))
        self.ui.userInfoButton.clicked.connect(lambda: self.menuClicked("userInfoButton"))
        self.ui.infoButton.clicked.connect(lambda: self.menuClicked("infoButton"))
        self.ui.settingsButton.clicked.connect(lambda: self.menuClicked("settingsButton"))
        self.ui.logoutButton.clicked.connect(self.userLogout)

        self.ui.exerciseOneButton.clicked.connect(lambda: self.exerciseClicked(1,0))
        self.ui.exerciseOneMenuButton.clicked.connect(lambda: self.exerciseClicked(1,0))
        self.ui.exerciseOneOneButton.clicked.connect(lambda: self.exerciseClicked(1,1))
        self.ui.exerciseOneOneMenuButton.clicked.connect(lambda: self.exerciseClicked(1,1))
        self.ui.exerciseOneTwoButton.clicked.connect(lambda: self.exerciseClicked(1,2))
        self.ui.exerciseOneTwoMenuButton.clicked.connect(lambda: self.exerciseClicked(1,2))
        self.ui.exerciseOneThreeButton.clicked.connect(lambda: self.exerciseClicked(1,3))
        self.ui.exerciseOneThreeMenuButton.clicked.connect(lambda: self.exerciseClicked(1,3))
        self.ui.exerciseOneFourButton.clicked.connect(lambda: self.exerciseClicked(1,4))
        self.ui.exerciseOneFourMenuButton.clicked.connect(lambda: self.exerciseClicked(1,4))
        self.ui.prevOneOne.clicked.connect(lambda: self.exerciseClicked(1,0))
        self.ui.nextOneOne.clicked.connect(lambda: self.exerciseClicked(1,2))
        self.ui.prevOneTwo.clicked.connect(lambda: self.exerciseClicked(1,1))
        self.ui.nextOneTwo.clicked.connect(lambda: self.exerciseClicked(1,3))
        self.ui.prevOneThree.clicked.connect(lambda: self.exerciseClicked(1,2))
        self.ui.nextOneThree.clicked.connect(lambda: self.exerciseClicked(1,4))
        self.ui.prevOneFour.clicked.connect(lambda: self.exerciseClicked(1,3))
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
            self.CURRENT_EXERCISE = self.db.init_user(self.username)
            print(self.CURRENT_EXERCISE)
            self.initExerciseButtons()

    def initExerciseButtons(self):
        exercise = self.CURRENT_EXERCISE[0]
        part = self.CURRENT_EXERCISE[1]

        for i in range(len(self.exercise_buttons_menu)):
            for j in range(len(self.exercise_buttons_menu[i])):
                button = self.exercise_buttons[i][j]
                menu_button = self.exercise_buttons_menu[i][j]
                next_button = self.exercise_buttons_next[i][j]
                menu_button.setStyleSheet(self.button_stylesheet_not_clickable)
                button.setEnabled(False)
                menu_button.setEnabled(False)
                next_button.setEnabled(False)

        for i in range(len(self.exercise_buttons)):
            if i > exercise:
                break
            for j in range(len(self.exercise_buttons_menu[i])):
                if i+1 == exercise and j > part:
                    break
                button = self.exercise_buttons[i][j]
                menu_button = self.exercise_buttons_menu[i][j]
                next_button = self.exercise_buttons_next[i][j]
                button.setEnabled(True)
                menu_button.setStyleSheet(self.button_stylesheet_clickable)
                menu_button.setEnabled(True)
                next_button.setEnabled(True)

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
        self.CURRENT_EXERCISE = [0,0]
    
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

    def exerciseClicked(self, ex, part):
        if not self.db.check_has_answer(ex, part):
            self.set_buttons(ex, part)
        
        if ex == 1 and part == 0:
            self.ui.exerciseOneShow.setVisible(True)
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            self.ui.exerciseOneShow.setText("▼")
            self.showExerciseMenu(True)
            self.changeBoldedText(self.ui.exerciseOneMenuButton)
        elif ex == 1 and part == 1:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(1)
            self.changeBoldedText(self.ui.exerciseOneOneMenuButton)
        elif ex == 1 and part == 2:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(2)
            self.changeBoldedText(self.ui.exerciseOneTwoMenuButton)
        elif ex == 1 and part == 3:
            self.ui.menuPages.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.exerciseOnePages.setCurrentIndex(3)
            self.changeBoldedText(self.ui.exerciseOneThreeMenuButton)
        elif ex == 1 and part == 4:
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

    def set_buttons(self, ex, part):
        if part != 0:
            if len(self.exercise_buttons[ex-1]) == part:
                if len(self.exercise_buttons) != ex:
                    button = self.exercise_buttons[ex][0]
                    menu_button = self.exercise_buttons_menu[ex][0]
                    next_button = self.exercise_buttons_next[ex-1][part-1]
                    button.setEnabled(True)
                    menu_button.setEnabled(True)
                    next_button.setEnabled(True)
                else:
                    next_button = self.exercise_buttons_next[ex-1][part-1]
                    next_button.setEnabled(True)
            elif len(self.exercise_buttons[ex-1]) != part:
                button = self.exercise_buttons[ex-1][part]
                menu_button = self.exercise_buttons_menu[ex-1][part]
                next_button = self.exercise_buttons_next[ex-1][part-1]
                button.setEnabled(True)
                menu_button.setStyleSheet(self.button_stylesheet_clickable)
                menu_button.setEnabled(True)
                next_button.setEnabled(True)

    def button_clicked(self, ex, part, is_command):
        correct = self.db.get_answer(ex, part)
        result = self.ui.inputEdit_5.toPlainText()
        print(correct)
        print(result)
        if result != correct:
            self.ui.resultBrowser_5.setPlainText("Väärin")
        else:
            self.db.update_current_exercise(ex, part, self.username)
            self.set_buttons(ex, part)
                #elif is_command:
                    #rtn = command_call(result)
                    #self.ui.resultBrowser.setPlainText(rtn)
                #elif not is_command:
                    #self.ui.resultBrowser.setPlainText("Oikein")



# pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py && python UI/src/main.py
if __name__ == "__main__":
    #command_call("pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py")
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())
    