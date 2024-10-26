import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

app = QApplication([])

window = QMainWindow()
window.setWindowTitle('Yash is trying to do something. Help him!')
window.setGeometry(100, 100, 400, 200)

label = QLabel("You said: ", window)
label.move(150, 80)

textInput = QLineEdit(window)
textInput.setPlaceholderText("Enter text here")
textInput.setGeometry(5, 130, 390, 30)

def updateText():    
    label.setText("You said: " + textInput.text())

btnInput = QPushButton("Forward", window)
btnInput.setGeometry(5, 160, 390, 30)
btnInput.clicked.connect(updateText)


window.show()

sys.exit(app.exec())
