#--coding: utf-8 --
from datetime import datetime
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

        self.exercise_buttons = [[self.ui.exerciseOneOneButton, self.ui.exerciseOneTwoButton, self.ui.exerciseOneThreeButton, self.ui.exerciseOneFourButton],
                                 [self.ui.exerciseTwoOneButton, self.ui.exerciseTwoTwoButton, self.ui.exerciseTwoThreeButton, self.ui.exerciseTwoFourButton]]
        self.exercise_buttons_next = [[self.ui.nextOneOne, self.ui.nextOneTwo, self.ui.nextOneThree, self.ui.nextOneFour],
                                      [self.ui.nextTwoOne, self.ui.nextTwoTwo, self.ui.nextTwoThree, self.ui.nextTwoFour]]
        self.exercise_buttons_prev = [[self.ui.prevOneOne, self.ui.prevOneTwo, self.ui.prevOneThree, self.ui.prevOneFour],
                                      [self.ui.prevTwoOne, self.ui.prevTwoTwo, self.ui.prevTwoThree, self.ui.prevTwoFour]]
        self.exercise_buttons_menu = [[self.ui.exerciseOneOneMenuButton, self.ui.exerciseOneTwoMenuButton, self.ui.exerciseOneThreeMenuButton, self.ui.exerciseOneFourMenuButton],
                                        [self.ui.exerciseTwoOneMenuButton, self.ui.exerciseTwoTwoMenuButton, self.ui.exerciseTwoThreeMenuButton, self.ui.exerciseTwoFourMenuButton]]
        self.exercise_main_buttons = [self.ui.exerciseOneButton, self.ui.exerciseTwoButton]
        self.exercise_main_buttons_menu = [self.ui.exerciseOneMenuButton, self.ui.exerciseTwoMenuButton]
        self.exercise_layouts = [self.ui.exerciseOneMenuLayout, self.ui.exerciseTwoMenuLayout]
        self.exercise_arrows = [self.ui.exerciseOneShow, self.ui.exerciseTwoShow]
        self.exercise_pages = [self.ui.exerciseOnePages, self.ui.exerciseTwoPages]
        self.progress_bars = [self.ui.progressBarOne, self.ui.progressBarTwo]
        self.progress_bars_global = [self.ui.progressBarOneGlobal, self.ui.progressBarTwoGlobal]
        
        self.button_stylesheet_clickable = self.ui.exerciseOneOneMenuButton.styleSheet()
        self.button_stylesheet_not_clickable = self.ui.exerciseOneTwoMenuButton.styleSheet()
        self.combo_style = self.ui.oneThreeCombo_1.styleSheet()
        self.ui.oneFourButton_2.setEnabled(False)
        self.ui.twoFourButton_2.setEnabled(False)

        self.db = database()
        if self.db.getItems() == []:
            self.db.migrations()

        self.CURRENT_EXERCISE = []
        self.CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        ex1_image = os.path.join(self.CURRENT_DIRECTORY, "../../images/ex1.png")
        ex2_image = os.path.join(self.CURRENT_DIRECTORY, "../../images/ex2.png")

        self.exercises_open = [False, False, False]
        self.previously_clicked = self.ui.mainButton
        self.previously_clicked_style = self.ui.mainButton.styleSheet()
        self.ui.mainButton.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

        self.ui.checkOneThree.clicked.connect(lambda: self.check_combo(1, 3))
        self.ui.oneFourButton_1.clicked.connect(lambda: self.check_command(1, 4, 1))
        self.ui.oneFourButton_2.clicked.connect(lambda: self.check_command(1, 4, 2))
        self.ui.twoFourButton_1.clicked.connect(lambda: self.check_command(2, 4, 1))
        self.ui.twoFourButton_2.clicked.connect(lambda: self.check_command(2, 4, 2))
        self.ui.checkTwoThree.clicked.connect(lambda: self.check_inputs(2, 3))

        self.ui.loginButton.clicked.connect(self.userLogin)
        self.ui.mainButton.clicked.connect(lambda: self.menuClicked("mainButton"))
        self.ui.commandButton.clicked.connect(lambda: self.menuClicked("commandButton"))
        self.ui.exercisesButton.clicked.connect(lambda: self.menuClicked("exercisesButton"))
        self.ui.infoButton.clicked.connect(lambda: self.menuClicked("infoButton"))
        self.ui.settingsButton.clicked.connect(lambda: self.menuClicked("settingsButton"))
        self.ui.logoutButton.clicked.connect(self.userLogout)

        self.exercise_main_buttons_menu[0].clicked.connect(lambda: self.exerciseClicked(1,0))
        self.exercise_main_buttons_menu[1].clicked.connect(lambda: self.exerciseClicked(2,0))
        self.exercise_main_buttons[0].clicked.connect(lambda: self.exerciseClicked(1,0))
        self.exercise_main_buttons[1].clicked.connect(lambda: self.exerciseClicked(2,0))
        self.exercise_buttons[0][0].clicked.connect(lambda: self.exerciseClicked(1,1))
        self.exercise_buttons_menu[0][0].clicked.connect(lambda: self.exerciseClicked(1,1))
        self.exercise_buttons[0][1].clicked.connect(lambda: self.exerciseClicked(1,2))
        self.exercise_buttons_menu[0][1].clicked.connect(lambda: self.exerciseClicked(1,2))
        self.exercise_buttons[0][2].clicked.connect(lambda: self.exerciseClicked(1,3))
        self.exercise_buttons_menu[0][2].clicked.connect(lambda: self.exerciseClicked(1,3))
        self.exercise_buttons[0][3].clicked.connect(lambda: self.exerciseClicked(1,4))
        self.exercise_buttons_menu[0][3].clicked.connect(lambda: self.exerciseClicked(1,4))
        self.exercise_buttons[1][0].clicked.connect(lambda: self.exerciseClicked(2,1))
        self.exercise_buttons_menu[1][0].clicked.connect(lambda: self.exerciseClicked(2,1))
        self.exercise_buttons[1][1].clicked.connect(lambda: self.exerciseClicked(2,2))
        self.exercise_buttons_menu[1][1].clicked.connect(lambda: self.exerciseClicked(2,2))
        self.exercise_buttons[1][2].clicked.connect(lambda: self.exerciseClicked(2,3))
        self.exercise_buttons_menu[1][2].clicked.connect(lambda: self.exerciseClicked(2,3))
        self.exercise_buttons[1][3].clicked.connect(lambda: self.exerciseClicked(2,4))
        self.exercise_buttons_menu[1][3].clicked.connect(lambda: self.exerciseClicked(2,4))

        self.exercise_buttons_prev[0][0].clicked.connect(lambda: self.exerciseClicked(1,0))
        self.exercise_buttons_prev[1][0].clicked.connect(lambda: self.exerciseClicked(2,0))
        self.exercise_buttons_next[0][0].clicked.connect(lambda: self.exerciseClicked(1,2))
        self.exercise_buttons_next[1][0].clicked.connect(lambda: self.exerciseClicked(2,2))
        self.exercise_buttons_prev[0][1].clicked.connect(lambda: self.exerciseClicked(1,1))
        self.exercise_buttons_prev[1][1].clicked.connect(lambda: self.exerciseClicked(2,1))
        self.exercise_buttons_next[0][1].clicked.connect(lambda: self.exerciseClicked(1,3))
        self.exercise_buttons_next[1][1].clicked.connect(lambda: self.exerciseClicked(2,3))
        self.exercise_buttons_prev[0][2].clicked.connect(lambda: self.exerciseClicked(1,2))
        self.exercise_buttons_prev[1][2].clicked.connect(lambda: self.exerciseClicked(2,2))
        self.exercise_buttons_next[0][2].clicked.connect(lambda: self.exerciseClicked(1,4))
        self.exercise_buttons_next[1][2].clicked.connect(lambda: self.exerciseClicked(2,4))
        self.exercise_buttons_prev[0][3].clicked.connect(lambda: self.exerciseClicked(1,3))
        self.exercise_buttons_prev[1][3].clicked.connect(lambda: self.exerciseClicked(2,3))
        self.exercise_buttons_next[0][3].clicked.connect(lambda: self.menuClicked("exercisesButton"))
        self.exercise_buttons_next[1][3].clicked.connect(lambda: self.menuClicked("exercisesButton"))

        self.ui.commandLineButton.clicked.connect(lambda: self.run_command_line())
        self.ui.exercisesShow.clicked.connect(lambda: self.arrowClicked(0))
        self.exercise_arrows[0].clicked.connect(lambda: self.arrowClicked(1))
        self.exercise_arrows[1].clicked.connect(lambda: self.arrowClicked(2))

        self.ui.loginButton.setCursor(Qt.PointingHandCursor)
        btns = self.findChildren(QPushButton)
        for btn in btns:
            btn.setCursor(Qt.PointingHandCursor)

        self.ui.exOneImage.setPixmap(QPixmap(ex1_image))
        self.ui.exTwoImage.setPixmap(QPixmap(ex2_image))
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

            for i in range(len(self.exercise_layouts)):
                self.exercise_layouts[i].setVisible(False)
                self.showExerciseMenu(False, i)

            self.CURRENT_EXERCISE = self.db.init_user(self.username)
            self.initExerciseButtons()

            success, res = command_call("minikube version")
            if not success:
                self.ui.labelMinikube.setText(self.ui.labelMinikube.text() + "VERSIOTA EI LÖYTYNYT")
            else:
                version = res.split("\n")[1].split(': ')[1]
                self.ui.labelMinikube.setText(self.ui.labelMinikube.text() + version)
            success, res = command_call("kubectl version --client=true")
            if not success:
                self.ui.labelKubectl.setText(self.ui.labelKubectl.text() + "VERSIOTA EI LÖYTYNYT")
            else:
                version = res.split("\n")[1].split(': ')[1]
                self.ui.labelKubectl.setText(self.ui.labelKubectl.text() + version)
        self.informAchievements()

    def initExerciseButtons(self):
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
            temp = 0
            for j in range(len(self.exercise_buttons_menu[i])):
                if self.CURRENT_EXERCISE[i] < j and j != 0:
                    break
                button = self.exercise_buttons[i][j]
                menu_button = self.exercise_buttons_menu[i][j]
                button.setEnabled(True)
                menu_button.setStyleSheet(self.button_stylesheet_clickable)
                menu_button.setEnabled(True)
                if j != 0:
                    next_button = self.exercise_buttons_next[i][j-1]
                    next_button.setEnabled(True)
                temp = j + 1
            if temp >= self.CURRENT_EXERCISE[i] and self.CURRENT_EXERCISE[i] != 0:
                next_button = self.exercise_buttons_next[i][self.CURRENT_EXERCISE[i]-1]
                next_button.setEnabled(True)
                self.update_progress_bar(self.progress_bars[i], i+1)
                self.update_progress_bar(self.progress_bars_global[i], i+1)

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

        for i in range(len(self.exercises_open)):
            self.exercises_open[i] = False

        self.ui.stackedWidget.setCurrentIndex(0)
        for layout in self.exercise_layouts:
            layout.setVisible(False)
        self.ui.exercisesShow.setText("▲")
        for arrow in self.exercise_arrows:
            arrow.setText("▲")
        self.changeBoldedText(self.ui.mainButton)
        self.CURRENT_EXERCISE = [0,0]
    
    def setupExercise(self):
        cluster = os.path.join(self.CURRENT_DIRECTORY, "../../images/cluster.png")
        cluster_pixmap = QPixmap(cluster)
        self.ui.clusterImage.setPixmap(cluster_pixmap)

    def arrowClicked(self, num):
        if num == 0 and self.exercises_open[0] == False:
            for layout in self.exercise_layouts:
                layout.setVisible(True)
            for arrow in self.exercise_arrows:
                arrow.setVisible(True)
                arrow.setText("▲")
            self.ui.exercisesShow.setText("▼")
            self.exercises_open[0] = True
        elif num == 0 and self.exercises_open[0] == True:
            for layout in self.exercise_layouts:
                layout.setVisible(False)
            for arrow in self.exercise_arrows:
                arrow.setVisible(False)
                arrow.setText("▲")
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.ui.exercisesShow.setText("▲")
            self.exercises_open[2] = False
            self.exercises_open[1] = False
            self.exercises_open[0] = False
        else:
            is_open = not self.exercises_open[num]
            self.exercises_open[num] = is_open
            self.showExerciseMenu(is_open, num-1)
            if is_open:
                self.exercise_arrows[num-1].setText("▼")
            else:
                self.exercise_arrows[num-1].setText("▲")

    def exerciseClicked(self, ex, part):
        if part != 0 and not self.db.check_has_answer(ex, part):
            if part >= self.CURRENT_EXERCISE[ex-1]:
                self.db.update_current_exercise(ex, part, self.username)
                self.update_progress_bar(self.progress_bars[ex-1], ex)
                self.update_progress_bar(self.progress_bars_global[ex-1], ex)
                self.informAchievements()
            self.set_buttons(ex, part)

        self.ui.menuPages.setCurrentIndex(2)
        self.ui.stackedWidget_2.setCurrentIndex(ex)

        for i in range(len(self.exercise_pages)):
            self.exercise_pages[i].setCurrentIndex(part)
        
        if part == 0:
            self.changeBoldedText(self.exercise_main_buttons_menu[ex-1])
            self.exercise_arrows[ex-1].setVisible(True)
            self.exercise_arrows[ex-1].setText("▼")
            self.showExerciseMenu(True, ex-1)
        else:
            self.changeBoldedText(self.exercise_buttons_menu[ex-1][part-1])
            for i in range(len(self.exercise_arrows)):
                if i+1 == ex:
                    continue
                self.exercise_arrows[i].setText("▲")
                self.exercises_open[i+1] = False
                self.showExerciseMenu(False, i)

    def showExerciseMenu(self, value, num):
        for button in self.exercise_buttons_menu[num]:
            button.setVisible(value)

    def changeBoldedText(self, btn):
        btn_prev = self.previously_clicked
        btn_prev.setStyleSheet(self.previously_clicked_style)
        self.previously_clicked = btn
        self.previously_clicked_style = btn.styleSheet()
        btn.setStyleSheet(self.previously_clicked_style + "font-weight: bold;")

    def menuClicked(self, name):
        self.exercises_open[0] = False
        self.exercises_open[1] = False
        self.exercises_open[2] = False
        self.ui.exercisesShow.setText("▲")
        for arrow in self.exercise_arrows:
            arrow.setText("▲")
        if name == "mainButton":
            self.ui.menuPages.setCurrentIndex(0)
            for layout in self.exercise_layouts:
                layout.setVisible(False)
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.changeBoldedText(self.ui.mainButton)
        elif name == "commandButton":
            self.ui.menuPages.setCurrentIndex(1)
            for layout in self.exercise_layouts:
                layout.setVisible(False)
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.changeBoldedText(self.ui.commandButton)
        elif name == "exercisesButton":
            self.exercises_open[0] = True
            self.ui.exercisesShow.setText("▼")
            self.ui.menuPages.setCurrentIndex(2)
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.ui.exerciseOnePages.setCurrentIndex(0)
            for layout in self.exercise_layouts:
                layout.setVisible(True)
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.changeBoldedText(self.ui.exercisesButton)
        elif name == "infoButton":
            self.ui.menuPages.setCurrentIndex(3)
            for layout in self.exercise_layouts:
                layout.setVisible(False)
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.changeBoldedText(self.ui.infoButton)
        elif name == "settingsButton":
            self.ui.menuPages.setCurrentIndex(4)
            for layout in self.exercise_layouts:
                layout.setVisible(False)
            self.showExerciseMenu(False, 0)
            self.showExerciseMenu(False, 1)
            self.changeBoldedText(self.ui.settingsButton)

    def set_buttons(self, ex, part):
        if part != 0:
            if len(self.exercise_buttons[ex-1]) != part:
                button = self.exercise_buttons[ex-1][part]
                menu_button = self.exercise_buttons_menu[ex-1][part]
                next_button = self.exercise_buttons_next[ex-1][part-1]
                button.setEnabled(True)
                menu_button.setStyleSheet(self.button_stylesheet_clickable)
                menu_button.setEnabled(True)
                next_button.setEnabled(True)
            else:
                next_button = self.exercise_buttons_next[ex-1][part-1]
                next_button.setEnabled(True)

    def get_feedback_amount(self, code):
        error_file_location = os.path.join(self.CURRENT_DIRECTORY, "utils/return_values.json")
        error_file = open(error_file_location)
        errors = json.load(error_file)["data"]
        feedback_value = self.ui.feedbackValue.value()
        feedback = ""
        if feedback_value >= 1:
            feedback += "Väärin!"
        if feedback_value >= 2:
            error = [x for x in errors if x["code"] == code][0]["return"]
            feedback += "\n" + error
        if feedback_value >= 3:
            error = [x for x in errors if x["code"] == code][0]["details"]
            feedback += "\n" + error
        return feedback

    def run_command_line(self):
        self.ui.commandLine.setText("")
        result = self.ui.commandInput.toPlainText()
        rtn = multiple_line_command_call(result, self.ui.commandLine)
        if rtn == None or rtn == "":
            return_text = ""
        else:
            return_text = self.get_feedback_amount(6)
            return_text += "\n" + str(rtn)
        self.ui.commandLine.append(return_text)

    def check_command(self, ex, part, cmd):
        correct = self.db.get_answer(ex, part)
        result = ""
        browser = ""
        inputs = [[self.ui.oneFourInput_1, self.ui.oneFourInput_2], [self.ui.twoFourInput_1, self.ui.twoFourInput_2]]
        result_browsers = [[self.ui.oneFourResult_1, self.ui.oneFourResult_2], [self.ui.twoFourResult_1, self.ui.twoFourResult_2]]
        buttons = [[self.ui.oneFourButton_1, self.ui.oneFourButton_2], [self.ui.twoFourButton_1, self.ui.twoFourButton_2]]

        correct = correct[cmd-1]
        result = inputs[ex-1][cmd-1].toPlainText()
        browser = result_browsers[ex-1][cmd-1]
        browser.setText("")

        ok = True
        return_text = ""
        if result == "":
            return_text = self.get_feedback_amount(5)
            ok = False
        elif correct[len(correct)-1] == '*':
            parts_correct = correct[:-1].split(" ")
            parts_result = result.split(" ")
            parts_result = [x for x in parts_result if x != ""]
            if parts_result[0] != parts_correct[0]:
                return_text = self.get_feedback_amount(2)
                ok = False
            elif len(parts_result) == 1 or parts_result[1] != parts_correct[1]:
                return_text = self.get_feedback_amount(3)
                ok = False
        elif '!insert' in correct.split(' '):
            parts_correct = correct.split(" ")
            parts_result = result.split(" ")
            if parts_result[0] != parts_correct[0]:
                return_text = self.get_feedback_amount(2)
                ok = False
            else:
                for i in range(len(parts_correct)):
                    if i+1 > len(parts_result):
                        return_text = self.get_feedback_amount(3)
                        ok = False
                        break
                    if parts_correct[i] == '!insert':
                        continue
                    if parts_correct[i] != parts_result[i]:
                        return_text = self.get_feedback_amount(3)
                        ok = False
                        break
        else:
            if result != correct:
                parts_correct = correct[:-1].split(" ")
                parts_result = result.split(" ")
                parts_result = [x for x in parts_result if x != ""]
                if parts_result[0] != parts_correct[0]:
                    return_text = self.get_feedback_amount(2)
                else:
                    return_text = self.get_feedback_amount(3)
                ok = False

        if ok:
            if cmd == len(inputs):
                if part >= self.CURRENT_EXERCISE[ex-1]:
                    self.db.update_current_exercise(ex, part, self.username)
                    self.update_progress_bar(self.progress_bars[ex-1], ex)
                    self.update_progress_bar(self.progress_bars_global[ex-1], ex)
                    self.informAchievements()
                self.set_buttons(ex, part)
            else:
                style = buttons[ex-1][cmd-1].styleSheet()
                buttons[ex-1][cmd].setEnabled(True)
                buttons[ex-1][cmd].setStyleSheet(style)
            rtn = multiple_line_command_call(result, browser)
            if rtn == None or rtn == "":
                return_text = ""
            else:
                return_text = self.get_feedback_amount(1)
                return_text += "Vastaus oli silti oikein."
        browser.append(return_text)
            
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
            if part >= self.CURRENT_EXERCISE[ex-1]:
                self.db.update_current_exercise(ex, part, self.username)
                self.update_progress_bar(self.progress_bars[ex-1], ex)
                self.update_progress_bar(self.progress_bars_global[ex-1], ex)
                self.informAchievements()
            self.set_buttons(ex, part)
        self.ui.infoBrowser_5.setText(return_value)

    def check_inputs(self, ex, part):
        correct = self.db.get_answer(ex, part)
        inputs = [self.ui.inputTwoThree_1, self.ui.inputTwoThree_2, self.ui.inputTwoThree_3, self.ui.inputTwoThree_4,
                  self.ui.inputTwoThree_5, self.ui.inputTwoThree_6]
        labels = [self.ui.resultTwoThree_1, self.ui.resultTwoThree_2, self.ui.resultTwoThree_3, self.ui.resultTwoThree_4,
                  self.ui.resultTwoThree_5, self.ui.resultTwoThree_6]
        return_value = ""
        for i in range(len(inputs)):
            input = inputs[i].text()
            input_set = input.split(' ')
            correct_vals = correct[i]
            print(f'input set: {input_set}')
            print(f'correct vals: {correct_vals}')
            if input.replace(' ', '') == "" and return_value == "":
                return_value = f'Ensimmäinen havaittu virhe: Kohdassa {i+1}. ei ole annettu komentoa.'
            if input not in correct_vals:
                labels[i].setText('Väärin!')
                if return_value == "":
                    for j in range(len(correct_vals)):
                        ok = False
                        correct_set = correct_vals[j].split(' ')
                        print(f'correct set: {correct_set}')
                        for k in range(len(correct_set)):
                            if len(input_set) <= k:
                                return_value = f'Ensimmäinen havaittu virhe: Kohdassa {i+1}. puuttuu komennosta osa/osia.'
                            elif correct_set[k] != input_set[k]:
                                ok = True
                                break
                        if ok:
                            return_value = f'Ensimmäinen havaittu virhe: Kohdassa {i+1}. väärä komennon osa: {input_set[k]}.'
                        if return_value != "":
                            break
            elif input not in correct_vals and return_value == "":
                return_value = f'Ensimmäinen havaittu virhe: Kohdassa {i+1}. annettu liian pitkä komento.'
            else:
                labels[i].setText('Oikein!')
        if return_value == "":
            return_value = "Kaikki oikein!"
            if part >= self.CURRENT_EXERCISE[ex-1]:
                self.db.update_current_exercise(ex, part, self.username)
                self.update_progress_bar(self.progress_bars[ex-1], ex)
                self.update_progress_bar(self.progress_bars_global[ex-1], ex)
                self.informAchievements()
            self.set_buttons(ex, part)
        self.ui.infoTwoThree.setText(return_value)

    def update_progress_bar(self, bar, ex):
        if ex == 0:
             bar.setValue(0)
        else:
            progress = round((self.db.get_exercise(self.username)[ex-1] / self.db.exercise_count(ex)), 2) * 100
            bar.setValue(progress)

    def informAchievements(self):
        exercises = self.db.get_exercise(self.username)
        achievementTable = self.ui.achievements
        achievementTable.setText("")

        for i in range(len(exercises)):
            part = exercises[i]
            count = self.db.exercise_count(i+1)
            if count == part:
                achievementTable.append(f"Käyttäjä {self.username} on suorittanut tehtäväkokonaisuuden {i+1}!")
        date = datetime.now()
        formatted_date = date.strftime("%d-%m-%Y %H:%M")
        achievementTable.append(f"\nSaavutustaulu on luotu {formatted_date}.")



        



# pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py && python UI/src/main.py
if __name__ == "__main__":
    #command_call("pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py")
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())