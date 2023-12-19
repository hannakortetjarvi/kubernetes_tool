import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from utils.command_line import command_call

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        cmd = self.ui.textEdit.toPlainText()
        rtn = command_call(cmd)
        self.ui.textBrowser.setPlainText(rtn)

if __name__ == "__main__":
    command_call("pyside6-uic QtUI/form.ui -o ui_form.py")
    command_call('copy "QtUI/ui_form.py" "src/ui_form.py"')
    app = QApplication(sys.argv)
    widget = MyApplication()
    widget.show()
    sys.exit(app.exec())