#--coding: utf-8 --

import sys
import json
import os.path
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QFontDatabase, QFont
from PySide6.QtCore import Qt
from ui_form import Ui_Widget
from utils.command_line import command_call, multiple_line_command_call
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
        self.combo_style = self.ui.oneThreeCombo_1.styleSheet()

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

        self.ui.checkOneThree.clicked.connect(lambda: self.check_combo(1, 3))
        self.ui.oneFourButton_1.clicked.connect(lambda: self.check_command(1, 4, 1))
        self.ui.oneFourButton_2.clicked.connect(lambda: self.check_command(1, 4, 2))

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
            self.initExerciseButtons()
            success, res = command_call("minikube version")
            if not success:
                self.ui.labelMinikube.setText(self.ui.labelMinikube.text() + "VERSION NOT FOUND")
            else:
                version = res.split("\n")[1].split(': ')[1]
                self.ui.labelMinikube.setText(self.ui.labelMinikube.text() + version)
            success, res = command_call("kubectl version --client=true")
            if not success:
                self.ui.labelKubectl.setText(self.ui.labelKubectl.text() + "VERSION NOT FOUND")
            else:
                version = res.split("\n")[1].split(': ')[1]
                self.ui.labelKubectl.setText(self.ui.labelKubectl.text() + version)

    def initExerciseButtons(self):
        progress_bars = [self.ui.progressBarOne]
        progress_bars_global = [self.ui.progressBarOneGlobal]
        exercise = self.CURRENT_EXERCISE[0]
        part = self.CURRENT_EXERCISE[1]

        for i in range(len(self.exercise_buttons_menu)):
            for j in range(len(self.exercise_buttons_menu[i])):
                button = self.exercise_buttons[i][j]
                menu_button = self.exercise_buttons_menu[i][j]
                next_button = self.exercise_buttons_next[i][j-1]
                menu_button.setStyleSheet(self.button_stylesheet_not_clickable)
                button.setEnabled(False)
                menu_button.setEnabled(False)
                next_button.setEnabled(False)

        for i in range(len(self.exercise_buttons)):
            if i > exercise:
                break
            j = 0
            temp = -1
            for j in range(len(self.exercise_buttons_menu[i])):
                if i+1 == exercise and j > part:
                    break
                button = self.exercise_buttons[i][j]
                menu_button = self.exercise_buttons_menu[i][j]
                button.setEnabled(True)
                menu_button.setStyleSheet(self.button_stylesheet_clickable)
                menu_button.setEnabled(True)
                if j != 0:
                    next_button = self.exercise_buttons_next[i][j-1]
                    next_button.setEnabled(True)
                elif temp == -1:
                    temp = j
            if temp >= part:
                self.update_progress_bar(progress_bars[i], i+1, j)
                self.update_progress_bar(progress_bars_global[i], i+1, j)

    def userLogout(self):
        self.ui.labelMinikube.setText("Käytössä oleva Minikube versio: ")
        self.ui.labelKubectl.setText("Käytössä oleva Kubectl Client versio: ")
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
        self.CURRENT_EXERCISE = [1,0]
    
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
        if part != 0 and not self.db.check_has_answer(ex, part):
            if ex >= self.CURRENT_EXERCISE[0] and part >= self.CURRENT_EXERCISE[1]:
                self.db.update_current_exercise(ex, part, self.username)
                self.update_progress_bar(self.ui.progressBarOne, ex, part)
                self.update_progress_bar(self.ui.progressBarOneGlobal, ex, part)
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

    def check_command(self, ex, part, cmd):
        correct = self.db.get_answer(ex, part)
        result = ""
        browser = ""
        inputs = [self.ui.oneFourInput_1, self.ui.oneFourInput_2]
        result_browsers = [self.ui.oneFourResult_1, self.ui.oneFourResult_2]
        if ex == 1 and part == 4 and cmd == 1:
            correct = correct[0]
            result = inputs[0].toPlainText()
            browser = result_browsers[0]

        if ex == 1 and part == 4 and cmd == 2:
            correct = correct[1]
            result = inputs[1].toPlainText()
            browser = result_browsers[1]

        ok = True
        if correct[len(correct)-1] == '*':
            if not result.startswith(correct[:-1]):
                ok = False
        else:
            if result != correct:
                ok = False
        
        if ok:
            if cmd == len(inputs):
                if ex >= self.CURRENT_EXERCISE[0] and part >= self.CURRENT_EXERCISE[1]:
                    self.db.update_current_exercise(ex, part, self.username)
                    if ex == 1:
                        self.update_progress_bar(self.ui.progressBarOne, ex, part)
                        self.update_progress_bar(self.ui.progressBarOneGlobal, ex, part)
                self.set_buttons(ex, part)
            _, rtn = multiple_line_command_call(result, browser)
        else:
            browser.setPlainText("Väärin")
            
    def check_combo(self, ex, part):
        correct = self.db.get_answer(ex, part)
        combos = [self.ui.oneThreeCombo_1, self.ui.oneThreeCombo_2, self.ui.oneThreeCombo_3, self.ui.oneThreeCombo_4,
                  self.ui.oneThreeCombo_5, self.ui.oneThreeCombo_6, self.ui.oneThreeCombo_7]
        return_value = ""
        
        for i in range(len(combos)):
            index = combos[i].currentIndex()
            if correct[i] != index:
                return_value += f"Kohta {i+1}. on väärin.\n"
        if return_value == "":
            return_value = "Oikein!"
            if ex >= self.CURRENT_EXERCISE[0] and part >= self.CURRENT_EXERCISE[1]:
                self.db.update_current_exercise(ex, part, self.username)
                if ex == 1:
                    self.update_progress_bar(self.ui.progressBarOne, ex, part)
                    self.update_progress_bar(self.ui.progressBarOneGlobal, ex, part)
            self.set_buttons(ex, part)
        self.ui.infoBrowser_5.setText(return_value)

    def update_progress_bar(self, bar, ex, part):
        if ex == 0:
             bar.setValue(0)
        else:
            progress = round((self.db.get_exercise(self.username)[1] / self.db.exercise_count(ex)), 2) * 100
            bar.setValue(progress)
        



# pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py && python UI/src/main.py
if __name__ == "__main__":
    #command_call("pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py")
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())