import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
clipboard = app.clipboard()
clipboard.setText(sys.stdin.read())

