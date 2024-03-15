import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from ui_form import Ui_Widget
from utils.command_line import command_call

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        

        self.ui.runButton.clicked.connect(self.button_clicked)
        self.ui.loginButton.clicked.connect(self.userLogin)
        self.ui.mainButton.clicked.connect(lambda: self.ui.menuPages.setCurrentIndex(0))
        self.ui.exercisesButton.clicked.connect(lambda: self.ui.menuPages.setCurrentIndex(1))
        self.ui.userInfoButton.clicked.connect(lambda: self.ui.menuPages.setCurrentIndex(2))
        self.ui.infoButton.clicked.connect(lambda: self.ui.menuPages.setCurrentIndex(3))
        self.ui.settingsButton.clicked.connect(lambda: self.ui.menuPages.setCurrentIndex(4))
        self.ui.logoutButton.clicked.connect(self.userLogout)

        self.initPages()

    def userLogin(self):
        self.username = self.ui.userNameEdit.text()
        if self.username == "":
            self.ui.loginWarning.setText("Syötä nimi!")
        else:
            page = self.ui.menuPages.findChild(QWidget, "userInfoPage")
            for child in page.findChildren(QLabel):
                object_name = child.objectName()
                if "sub" in object_name:
                    child.setText(child.text() + self.username)
            page = self.ui.menuPages.findChild(QWidget, "mainPage")
            for child in page.findChildren(QLabel):
                object_name = child.objectName()
                if "sub" in object_name:
                    child.setText(child.text() + self.username)
            self.ui.stackedWidget.setCurrentIndex(1)

    def userLogout(self):
        page = self.ui.menuPages.findChild(QWidget, "userInfoPage")
        for child in page.findChildren(QLabel):
            object_name = child.objectName()
            if "sub" in object_name:
                leng = len(self.username)
                child.setText(child.text()[:-leng])
        page = self.ui.menuPages.findChild(QWidget, "mainPage")
        for child in page.findChildren(QLabel):
            object_name = child.objectName()
            if "sub" in object_name:
                leng = len(self.username)
                child.setText(child.text()[:-leng])
        self.username = ""
        self.ui.stackedWidget.setCurrentIndex(0)

    def button_clicked(self):
        cmd = self.ui.inputEdit.toPlainText()
        rtn = command_call(cmd)
        self.ui.resultBrowser.setPlainText(rtn)

    def initPages(self):
        with open('data/pages.json') as f:
            data = json.load(f)
            for page_data in data['pages']:
                index = page_data["index"]
                page_widget = self.ui.menuPages.widget(index)
                if page_widget:
                    for child in page_widget.findChildren(QLabel):
                        object_name = child.objectName()
                        if "title" in object_name:
                            child.setText(page_data["title"])
                        elif "sub" in object_name:
                            child.setText(page_data["subtitle"])
                        elif "desc" in object_name:
                            child.setText(page_data["description"])

# pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py && python UI/src/main.py
if __name__ == "__main__":
    #command_call("pyside6-uic UI/QtUI/form.ui -o UI/src/ui_form.py")
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())