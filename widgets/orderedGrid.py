from PySide.QtGui import *

class Ordered(QWidget) :
    def __init__(self):
        # Call the parent constructor
        super(Ordered, self).__init__()

        self.init_ui()

    def init_ui(self):
        # create 5 buttons
        # todo think why we omitted self here
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")

        # CSS
        button1.setStyleSheet("background-color:#434A54; color:#E6E9ED")
        button2.setStyleSheet("background-color:#434A54; color:#E6E9ED")
        button3.setStyleSheet("background-color:#434A54; color:#E6E9ED")
        button4.setStyleSheet("background-color:#434A54; color:#E6E9ED")
        button5.setStyleSheet("background-color:#434A54; color:#E6E9ED")

        # add them to a layout
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        # important to assign the created layout to something !
        self.setLayout(layout)

        # some useful stuff
        self.setFixedSize(400, 100)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        print qr
        cp = QDesktopWidget().availableGeometry().center()
        print cp
        qr.moveCenter(cp)
        self.move(qr.topLeft())
