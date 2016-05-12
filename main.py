import sys
from PySide import QtGui
import widgets.orderedGrid

class Example(QtGui.QMainWindow):

    def __init__(self):
        # Call the parent constructor
        super(Example, self).__init__()

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
        self.setToolTip('This is a <b>QWidget</b> widget')

        # add more widgets
        page_title = QtGui.QLabel("Hello again", self)
        page_title.move(100, 80)

        # .move calls are not chained, absolute geometry is used
        page_title.move(120, 80)
        page_title.move(120, 200)
        page_title.move(120, 210)

        page_title.setToolTip('This is a <b>Label</b> widget')

        btn = QtGui.QPushButton("Click me", self)
        btn.move(100, 100)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.show()


def main():
    # Main Qt App starts here.
    # Note that we can create more han one widget
    app = QtGui.QApplication(sys.argv)
    ex = Example()

    # ex_two = Example()

    # create an widget with ordered grid
    ordered_grid = widgets.orderedGrid.Ordered()
    ordered_grid.show()

    # event handling and execution begins at app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
