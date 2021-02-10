import sys
from PyQt5.QtWidgets import QPushButton, QGridLayout, QLineEdit, QApplication, QWidget
from math import sqrt

class Button():
    def __init__(self, text, results):
        self.results = results
        self.text = text
        self.CreateButton = QPushButton(str(text))
        self.CreateButton.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, value):
        if value == "=":
            try:
                res = eval(self.results.text())
                self.results.setText(str(res))
            except:
                self.results.setText("Math Error")
        elif value == "AC":
            self.results.setText("0")
        elif value == "DEL":
            self.results.setText(self.results.text()[:-1])
            if len(self.results.text()) == 0 or self.results.text() == "Math Erro":
                self.results.setText("0")
        elif value == "√":
            try:
                self.results.setText(str(sqrt(eval(self.results.text()))))
            except:
                self.results.setText("Math Error")
        else:
            if self.results.text() == "0" or self.results.text() == "Math Error":
                self.results.setText(str(value))
            else:
                self.results.setText(self.results.text()+str(value))

class mainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.createApp()

    def createApp(self):
        grid = QGridLayout()

        results = QLineEdit("0")
        grid.addWidget(results,0,0,1,4)

        Buttons = ["AC", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, "00", ".", "="]
        row = 4
        col = 0

        for button in Buttons:
            if col>3:
                col = 0
                row+=1
            newButton = Button(button, results)
            grid.addWidget(newButton.CreateButton,row,col,1,1)
            col += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApplication()
    sys.exit(app.exec_())