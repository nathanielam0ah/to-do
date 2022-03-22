from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 220, 571, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(10, 10, 571, 201))
        self.my_listWidget.setObjectName("my_listWidget")
        self.ClearAllButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clearItem())
        self.ClearAllButton.setGeometry(QtCore.QRect(590, 180, 111, 31))
        self.ClearAllButton.setObjectName("ClearAllButton")
        self.RemoveItemButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.removeItem())
        self.RemoveItemButton.setGeometry(QtCore.QRect(590, 90, 111, 31))
        self.RemoveItemButton.setObjectName("RemoveItemButton")
        self.AddItemButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.appendItem())
        self.AddItemButton.setGeometry(QtCore.QRect(590, 10, 111, 31))
        self.AddItemButton.setObjectName("AddItemButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do List App"))
        self.ClearAllButton.setText(_translate("MainWindow", "Clear Button"))
        self.RemoveItemButton.setText(_translate("MainWindow", "Remove Item"))
        self.AddItemButton.setText(_translate("MainWindow", "Add Item"))

    def appendItem(self):
        item=self.additem_lineEdit.text()
        self.my_listWidget.addItem(item)
        self.additem_lineEdit.clear()

    def removeItem(self):
        selectedObject=self.my_listWidget.currentRow()
        self.my_listWidget.takeItem(selectedObject)

    def clearItem(self):
        self.my_listWidget.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
