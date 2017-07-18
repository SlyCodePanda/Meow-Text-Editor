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
        self.ui.setWindowTitle("Meow Text")


        # Open.
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionOpen.setStatusTip('Open File')
        self.ui.actionOpen.triggered.connect(self.file_open)

        # Save.
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionSave.setStatusTip('Save File')
        self.ui.actionSave.triggered.connect(self.file_save)

        # Exit.
        self.ui.actionQuit.setShortcut("Ctrl+Q")
        self.ui.actionQuit.setStatusTip('Quit Application')
        self.ui.actionQuit.triggered.connect(self.close_application)

        
        self.home()


    def home(self):
        self.ui.show()
        #self.show()


    def editor(self):
        #self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        print( 'Editor has loaded!')


    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        # Opening with the intention to read ('r').
        file = open(name, 'r')

        # Need to call the editor, because it is not there by default. 
        self.editor()

        with file:
            text = file.read()
            self.ui.textEdit.setText(text)


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        # Intention to write the file ('w')
        file = open(name, 'w')
        text = self.ui.textEdit.toPlainText()
        file.write(text)
        file.close()


    def close_application(self):
        # Pop-Up Message:
        choice = QtGui.QMessageBox.question(self, 'Quit',
                                            "Are you sure you want to leave meow?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print( "Closing Meow...")
            sys.exit()
        else:
            pass


# Our 'main'.
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()