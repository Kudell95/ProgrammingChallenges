from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()



#initialisation
app = QApplication([])
window = QWidget()

#this is where you define the widgets


layout = QVBoxLayout()
button = QPushButton('Click')

#add listeners for actions
button.clicked.connect(on_button_clicked)

#assign layout to window
window.setLayout(layout)
button.show()

#window.show() #display window
app.exec_() #execute app - creates process