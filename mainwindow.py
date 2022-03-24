from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 220, 571, 31))
        self.additem_lineEdit.setText("")
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(10, 10, 571, 201))
        self.my_listWidget.setObjectName("my_listWidget")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.editItem())
        self.EditButton.setGeometry(QtCore.QRect(590, 120, 111, 31))
        self.EditButton.setObjectName("EditButton")
        self.ClearAllButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clearItem())
        self.ClearAllButton.setGeometry(QtCore.QRect(590, 180, 111, 31))
        self.ClearAllButton.setObjectName("ClearAllButton")
        self.RemoveItemButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.removeItem())
        self.RemoveItemButton.setGeometry(QtCore.QRect(590, 60, 111, 31))
        self.RemoveItemButton.setObjectName("RemoveItemButton")
        self.AddItemButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.appendItem())
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
        self.additem_lineEdit.setPlaceholderText(_translate("MainWindow", "add list item here."))
        self.ClearAllButton.setText(_translate("MainWindow", "Clear Button"))
        self.RemoveItemButton.setText(_translate("MainWindow", "Remove Item"))
        self.AddItemButton.setText(_translate("MainWindow", "Add Item"))
        self.EditButton.setText(_translate("MainWindow","Edit Item"))

    def appendItem(self):
        text=self.additem_lineEdit.text()
        self.my_listWidget.addItem(text)
        self.additem_lineEdit.clear()

    def editItem(self):
        for index in range(self.my_listWidget.count()):
            item=self.my_listWidget.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        selectedObject=self.my_listWidget.currentIndex()
        if selectedObject.isValid():
            item=self.my_listWidget.itemFromIndex(selectedObject)
            if not item.isSelected():
                item.setSelected(True)
        self.my_listWidget.edit(selectedObject)

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
    sys.exit(app.exec())
