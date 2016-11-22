# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sinac/Code/Calculator/Calculator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    
    def __init__(self):
        self.currentValue = []
        self.mathSymbol = ''
        self.previousValue = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(605, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.numFour = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numFour.sizePolicy().hasHeightForWidth())
        self.numFour.setSizePolicy(sizePolicy)
        self.numFour.setObjectName(_fromUtf8("numFour"))
        self.gridLayout_2.addWidget(self.numFour, 2, 1, 1, 1)
        self.numSix = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numSix.sizePolicy().hasHeightForWidth())
        self.numSix.setSizePolicy(sizePolicy)
        self.numSix.setObjectName(_fromUtf8("numSix"))
        self.gridLayout_2.addWidget(self.numSix, 2, 3, 1, 1)
        self.numEight = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numEight.sizePolicy().hasHeightForWidth())
        self.numEight.setSizePolicy(sizePolicy)
        self.numEight.setObjectName(_fromUtf8("numEight"))
        self.gridLayout_2.addWidget(self.numEight, 1, 2, 1, 1)
        self.numNine = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numNine.sizePolicy().hasHeightForWidth())
        self.numNine.setSizePolicy(sizePolicy)
        self.numNine.setObjectName(_fromUtf8("numNine"))
        self.gridLayout_2.addWidget(self.numNine, 1, 3, 1, 1)
        self.numSeven = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numSeven.sizePolicy().hasHeightForWidth())
        self.numSeven.setSizePolicy(sizePolicy)
        self.numSeven.setObjectName(_fromUtf8("numSeven"))
        self.gridLayout_2.addWidget(self.numSeven, 1, 1, 1, 1)
        self.numFive = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numFive.sizePolicy().hasHeightForWidth())
        self.numFive.setSizePolicy(sizePolicy)
        self.numFive.setObjectName(_fromUtf8("numFive"))
        self.gridLayout_2.addWidget(self.numFive, 2, 2, 1, 1)
        self.numThree = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numThree.sizePolicy().hasHeightForWidth())
        self.numThree.setSizePolicy(sizePolicy)
        self.numThree.setObjectName(_fromUtf8("numThree"))
        self.gridLayout_2.addWidget(self.numThree, 3, 3, 1, 1)
        self.numTwo = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numTwo.sizePolicy().hasHeightForWidth())
        self.numTwo.setSizePolicy(sizePolicy)
        self.numTwo.setObjectName(_fromUtf8("numTwo"))
        self.gridLayout_2.addWidget(self.numTwo, 3, 2, 1, 1)
        self.numOne = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numOne.sizePolicy().hasHeightForWidth())
        self.numOne.setSizePolicy(sizePolicy)
        self.numOne.setObjectName(_fromUtf8("numOne"))
        self.gridLayout_2.addWidget(self.numOne, 3, 1, 1, 1)
        self.clear = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.gridLayout_2.addWidget(self.clear, 4, 3, 1, 1)
        self.numZero = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numZero.sizePolicy().hasHeightForWidth())
        self.numZero.setSizePolicy(sizePolicy)
        self.numZero.setObjectName(_fromUtf8("numZero"))
        self.gridLayout_2.addWidget(self.numZero, 4, 1, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 2, 2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plusSign = QtGui.QPushButton(self.centralwidget)
        self.plusSign.setObjectName(_fromUtf8("plusSign"))
        self.verticalLayout.addWidget(self.plusSign)
        self.minusSign = QtGui.QPushButton(self.centralwidget)
        self.minusSign.setObjectName(_fromUtf8("minusSign"))
        self.verticalLayout.addWidget(self.minusSign)
        self.multiplicationSign = QtGui.QPushButton(self.centralwidget)
        self.multiplicationSign.setObjectName(_fromUtf8("multiplicationSign"))
        self.verticalLayout.addWidget(self.multiplicationSign)
        self.divisionSign = QtGui.QPushButton(self.centralwidget)
        self.divisionSign.setObjectName(_fromUtf8("divisionSign"))
        self.verticalLayout.addWidget(self.divisionSign)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.equalSign = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalSign.sizePolicy().hasHeightForWidth())
        self.equalSign.setSizePolicy(sizePolicy)
        self.equalSign.setMinimumSize(QtCore.QSize(0, 28))
        self.equalSign.setObjectName(_fromUtf8("equalSign"))
        self.verticalLayout_2.addWidget(self.equalSign)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 2, 2, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 531))
        self.lcdNumber.setNumDigits(10)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.numZero.clicked.connect(self.push_zero)
        self.numOne.clicked.connect(self.push_one)
        self.numTwo.clicked.connect(self.push_two)
        self.numThree.clicked.connect(self.push_three)
        self.numFour.clicked.connect(self.push_four)
        self.numFive.clicked.connect(self.push_five)
        self.numSix.clicked.connect(self.push_six)
        self.numSeven.clicked.connect(self.push_seven)
        self.numEight.clicked.connect(self.push_eight)
        self.numNine.clicked.connect(self.push_nine)
        self.clear.clicked.connect(self.push_clear)
        self.plusSign.clicked.connect(self.push_add)
        self.equalSign.clicked.connect(self.push_equals)
        self.minusSign.clicked.connect(self.push_subtract)
        self.multiplicationSign.clicked.connect(self.push_multiply)
        self.divisionSign.clicked.connect(self.push_divide)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator", None))
        self.numFour.setText(_translate("MainWindow", "4", None))
        self.numSix.setText(_translate("MainWindow", "6", None))
        self.numEight.setText(_translate("MainWindow", "8", None))
        self.numNine.setText(_translate("MainWindow", "9", None))
        self.numSeven.setText(_translate("MainWindow", "7", None))
        self.numFive.setText(_translate("MainWindow", "5", None))
        self.numThree.setText(_translate("MainWindow", "3", None))
        self.numTwo.setText(_translate("MainWindow", "2", None))
        self.numOne.setText(_translate("MainWindow", "1", None))
        self.clear.setText(_translate("MainWindow", "Clear", None))
        self.numZero.setText(_translate("MainWindow", "0", None))
        self.plusSign.setText(_translate("MainWindow", "+", None))
        self.minusSign.setText(_translate("MainWindow", "-", None))
        self.multiplicationSign.setText(_translate("MainWindow", "*", None))
        self.divisionSign.setText(_translate("MainWindow", "/", None))
        self.equalSign.setText(_translate("MainWindow", "=", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
    
    def push_zero(self):
        self.currentValue.append(0)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_one(self):
        self.currentValue.append(1)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_two(self):
        self.currentValue.append(2)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_three(self):
        self.currentValue.append(3)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_four(self):
        self.currentValue.append(4)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
    
    def push_five(self):
        self.currentValue.append(5)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_six(self):
        self.currentValue.append(6)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_seven(self):
        self.currentValue.append(7)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_eight(self):
        self.currentValue.append(8)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_nine(self):
        self.currentValue.append(9)
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
        
    def push_add(self):
        self.mathSymbol = 'add'
        self.previousValue = ''.join(str(x) for x in self.currentValue)
        self.currentValue = []
        
    def push_subtract(self):
        self.mathSymbol = 'subtract'
        self.previousValue = ''.join(str(x) for x in self.currentValue)
        self.currentValue = []
    
    def push_multiply(self):
        self.mathSymbol = 'multiply'
        self.previousValue = ''.join(str(x) for x in self.currentValue)
        self.currentValue = []
    
    def push_divide(self):
        self.mathSymbol = 'divide'
        self.previousValue = ''.join(str(x) for x in self.currentValue)
        self.currentValue = []
    
    def push_clear(self):
        self.currentValue = []
        self.mathSymbol = []
        self.previousValue = []
        self.lcdNumber.display(0)
        
    def push_equals(self):
        firstNum = int(self.previousValue)
        secondNum = int(''.join(str(x) for x in self.currentValue))
        self.currentValue = []
        
        if self.mathSymbol == 'add': 
            solution = firstNum + secondNum
            self.currentValue = [x for x in str(solution)]
        elif self.mathSymbol == 'subtract':
            solution = firstNum - secondNum
            self.currentValue = [x for x in str(solution)]
        elif self.mathSymbol == 'multiply':
            solution = firstNum * secondNum
            self.currentValue = [x for x in str(solution)]
        elif self.mathSymbol == 'divide':
            solution = firstNum / secondNum
            self.currentValue = [x for x in str(solution)]
        self.lcdNumber.display(''.join(str(x) for x in self.currentValue))
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

