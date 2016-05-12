import sys
from PySide import QtGui
from PySide import QtCore
import widgets.orderedGrid
from threading import Timer


class Communicate(QtCore.QObject):
    ping = QtCore.Signal()

    # Create an editing object
    def __init__(self):
        super(Communicate, self).__init__()

        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.do_ping)
        timer.start(1000)

    def do_ping(self):
        print "Emitting!"
        self.ping.emit()


class Example(QtGui.QMainWindow):

    def __init__(self):
        # Call the parent constructor
        super(Example, self).__init__()

        # layout can't be applied to a mainWindow, Its a Main Window !
        self.main_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.ping_count = 0
        self.init_ui()

    def init_ui(self):
        # now we have a Status bar!
        self.statusBar().showMessage('Application is ready!')

        # add a Menu Bar and Toolbar
        # We must first create an action
        exit_action = QtGui.QAction(QtGui.QIcon('pyside.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        # more on .connect later
        exit_action.triggered.connect(self.close)

        dummy_action = QtGui.QAction('Dummy', self)
        dummy_action.setStatusTip('I Will do nothing')

        # Create a Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
        file_menu.addAction(dummy_action)

        # Create o Toolbar
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)
        toolbar.addAction(dummy_action)

        # set size, title, icon
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Hello PySide')

        # set a tooltip for the parent widget
        self.setToolTip('This is a <b>QMainWindow</b> widget')

        # add more widgets
        # page_title = QtGui.QLabel("Hello again", self)
        # page_title.move(100, 80)

        # .move calls are not chained, absolute geometry is used
        # page_title.move(120, 80)
        # page_title.move(120, 200)
        # page_title.move(120, 210)

        # page_title.setToolTip('This is a <b>Label</b> widget')

        self.lcd = QtGui.QLCDNumber(self)

        btn = QtGui.QPushButton("Click me", self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn1 = QtGui.QPushButton("Click me 2", self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.slider.move(100, 130)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(btn1)
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.slider)

        self.main_widget.setLayout(vbox)

        # Time to bind some signals

        # todo do you seeing what i see ?
        # if the event has parameters, they will be assigned to variables
        # if not a custom value could be used
        # slider.valueChange.connect(lcd.display)

        self.slider.valueChanged.connect(lambda x: self.on_slider_change(x, 2))

        # a `clicked` signal is emitted each time we click a button
        btn.clicked.connect(self.button_clicked)
        btn1.clicked.connect(self.button_clicked)
        # What if we wand to have a custom slot ?

        # Time to use Custom signals
        self.c = Communicate()
        self.c.ping.connect(self.handle_foreign_ping)

        self.show()

    def handle_foreign_ping(self):
        print "ping"

    def button_clicked(self):
        # todo suppose we want to use a property of another widget or the sender,
        # What could we do ?
        # user Sender, make the sender an attribute
        # or use lambda functions ( will see soon )
        sender = self.sender()
        print sender
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def keyPressEvent(self, e):
        # Another way of handling signals , is overriding default signals
        print e.key()
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def on_slider_change(self, x, y):
        print "Yooohooo, we have the x parameter :", x, y
        self.lcd.display(x)


def main():
    # Main Qt App starts here.
    # Note that we can create more han one widget
    app = QtGui.QApplication(sys.argv)
    ex = Example()

    # ex_two = Example()

    # create an widget with ordered grid
    # ordered_grid = widgets.orderedGrid.Ordered()
    # ordered_grid.show()

    # event handling and execution begins at app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
