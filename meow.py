import sys
from PyQt4 import QtCore, QtGui, uic


# Window inherits from the Qt widget 'MainWindow'
class Window(QtGui.QMainWindow):

    # Any core application stuff goes in the 'init' function.
    def __init__(self):
        super(Window, self).__init__()

        # Set up the user interface from Designer.
        self.ui = uic.loadUi("meow.ui")
    
        # Starting point: 50, 50. And 500 pixels wide, 300 pixels tall.
        self.ui.setGeometry(50, 50, 500, 300)
        self.ui.setWindowTitle("Meow Text Editor")

        
        self.home()


    def home(self):
        self.ui.show()
        #self.show()


# Our 'main'.
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()