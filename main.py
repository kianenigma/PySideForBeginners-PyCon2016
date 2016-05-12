import sys
from PySide import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        # Call the parent constructor
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        # set size, title, icon
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Hello PySide')
        self.setWindowIcon(QtGui.QIcon('./resources/logo.png'))

        # add more widgets
        self.page_title = QtGui.QLabel("Hello again", self)
        self.page_title.move(100, 5)

        self.btn = QtGui.QPushButton("Click me", self)
        self.btn.move(100, 30)

        self.show()


def main():
    # Main Qt App starts here.
    # Note that we can create more han one widget
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    #ex_two = Example()

    # event handling and execution begins at app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()