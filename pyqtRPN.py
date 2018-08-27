import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from rpn import rpn

qtCreatorFile = "./mainwindow.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
# class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calcEntry.returnPressed.connect(self.updateScreen)

        self.cmds = {
        "?": self.showHelp,
        "sh": self.showStack,
        "w": self.welcome,
        "exit": self.appExit
        }

self.R = rpn("")
        self.welcome()

    def updateScreen(self):
        entryStr = self.calcEntry.text()
        if entryStr in self.cmds:
            self.cmds[entryStr]()
        else:
            self.R.update(entryStr)
            rpnOut = self.R.getStack()
            self.calcScreen.setText(rpnOut)
#            self.calcScreen.append(entryStr)
            self.calcEntry.setText("")

    def showHelp(self):
        self.calcScreen.setFontPointSize(10)
        self.calcScreen.setText(self.R.help())
        self.calcScreen.setFontPointSize(14)
        self.calcEntry.setText("")

    def showStack(self):
        self.calcScreen.setText(self.R.show())
        self.calcEntry.setText("")

    def welcome(self):
        self.calcScreen.setText("")
        self.calcScreen.append(" ")
        self.calcScreen.append(" ")
        self.calcScreen.append(" ")
        self.calcScreen.setFontPointSize(16)
        textLine = " "*6 + "RPN Calculator"
        self.calcScreen.append(textLine)
        self.calcScreen.setFontPointSize(14)
        self.calcScreen.append(" ")
        self.calcScreen.append(" ")
        textLine = " "*6 + "Darrell Harriman"
        self.calcScreen.append(textLine)
        self.calcScreen.append(" ")
        self.calcScreen.append(" ")
        self.calcScreen.setFontPointSize(12)
        textLine = " "*7 + "harrimand@gmail.com"
        self.calcScreen.append(textLine)

        self.calcScreen.append(" ")
        self.calcScreen.append(" ")
        textLine = " "*7 + "Press Enter to Begin"
        self.calcScreen.append(textLine)

        self.calcScreen.append(" ")
        textLine = " "*8 + "Enter ? for help"
        self.calcScreen.append(textLine)

        self.calcScreen.setFontPointSize(14)
        self.calcEntry.setText("")

    def appExit(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


"""
http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/
http://pythonprogramminglanguage.com/pyqt-textarea/
"""


