from PySide6 import QtCore, QtGui, QtWidgets
from pathlib import Path
import platform
import sqlite3
import os

if (platform.system()=="Windows"):
    if (os.path.exists(os.path.expanduser( '~' )+'/AppData/Roaming/To-Do') == False):
        os.mkdir(os.path.expanduser( '~' )+'/AppData/Roaming/To-Do')
        print("Save Path Created Successfully!")
    else:
        print("Save Path Exists!")
        connection = sqlite3.connect(os.path.expanduser( '~' )+'/AppData/Roaming/To-Do/todolist.db')
        crs = connection.cursor()
        crs.execute("""CREATE TABLE if not exists todolist(
            listItem text
        )""")
        connection.commit()
        crs.close()
else:
    if (os.path.exists(os.path.expanduser('~')+"/.To-Do") == False):
        os.mkdir(os.path.expanduser('~')+"/.To-Do")
        print("Save Path Created Successfully!")
    else:
        print("Save Path exists!")
        connection = sqlite3.connect(os.path.expanduser('~')+"/.To-Do/todolist.db")
        crs = connection.cursor()
        crs.execute("""CREATE TABLE if not exists todolist(
                    listItem text
                )""")
        connection.commit()
        crs.close()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        '''self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 220, 571, 31))
        self.additem_lineEdit.setText("")
        self.additem_lineEdit.setObjectName("additem_lineEdit")'''
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(10, 10, 571, 220))
        self.my_listWidget.setObjectName("my_listWidget")
        self.my_listWidget.itemDoubleClicked.connect(self._handleDoubleClickedEvent)
        self._saveAll() if QtCore.QEvent == QtCore.Qt.Key_Enter else 0
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self._saveAll())
        self.SaveButton.setGeometry(QtCore.QRect(590, 110, 111, 31))
        self.SaveButton.setObjectName("SaveButton")
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
        self.menubar.setGeometry(QtCore.QRect(0, 100, 707, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.grabAll()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do List App"))
        #self.additem_lineEdit.setPlaceholderText(_translate("MainWindow", "add list item here."))
        self.ClearAllButton.setText(_translate("MainWindow", "Clear"))
        self.RemoveItemButton.setText(_translate("MainWindow", "Remove"))
        self.AddItemButton.setText(_translate("MainWindow", "Add"))
        self.SaveButton.setText(_translate("MainWindow","Save"))

    def grabAll(self):
        if (platform.system() == "Windows"):
            connection = sqlite3.connect(os.path.expanduser( '~' )+'/AppData/Roaming/To-Do/todolist.db')
            crs = connection.cursor()
            crs.execute('SELECT * FROM todolist')
            records = crs.fetchall()
            connection.commit()
            crs.close()
            for record in records:
                self.my_listWidget.addItem(str(record[0]))
        else:
            connection = sqlite3.connect(os.path.expanduser('~')+"/.To-Do/todolist.db")
            crs = connection.cursor()
            crs.execute('SELECT * FROM todolist')
            records = crs.fetchall()
            connection.commit()
            crs.close()
            for record in records:
                self.my_listWidget.addItem(str(record[0]))

    def appendItem(self):
        #text=self.additem_lineEdit.text()
        self.my_listWidget.addItem("")
        #self.additem_lineEdit.clear()

    # this function has been replaced with the double click event
    ''' def editItem(self):
        for index in range(self.my_listWidget.count()):
            item=self.my_listWidget.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        selectedObject=self.my_listWidget.currentIndex()
        if selectedObject.isValid():
            item=self.my_listWidget.itemFromIndex(selectedObject)
            if not item.isSelected():
                item.setSelected(True)
        self.my_listWidget.edit(selectedObject) '''

    def removeItem(self):
        selectedObject=self.my_listWidget.currentRow()
        self.my_listWidget.takeItem(selectedObject)

    def clearItem(self):
        self.my_listWidget.clear()

    def _handleDoubleClickedEvent(self, item):
        color = item.background()
        item.setSelected(True)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item=self.my_listWidget.itemFromIndex(self.my_listWidget.currentIndex())

    def _saveAll(self):
        if (platform.system() == "Windows"):
            connection = sqlite3.connect(os.path.expanduser( '~' )+'/AppData/Roaming/To-Do/todolist.db')
            crs = connection.cursor()
            crs.execute('DELETE FROM todolist;', )
            itemList = []
            for index in range(self.my_listWidget.count()):
                if index not in itemList:
                    itemList.append(self.my_listWidget.item(index))
            for item in itemList:
                crs.execute("INSERT INTO todolist VALUES (:item)",
                            {
                                'item': item.text(),
                            })
            connection.commit()
            crs.close()
            _message = QtWidgets.QMessageBox()
            _message.setWindowTitle("Success")
            _message.setText("Save Successful")
            _message.setIcon(QtWidgets.QMessageBox.Information)
            _message.exec()
        else:
            connection = sqlite3.connect(os.path.expanduser('~')+"/.To-Do/todolist.db")
            crs = connection.cursor()
            crs.execute('DELETE FROM todolist;',)
            itemList=[]
            for index in range(self.my_listWidget.count()):
                if index not in itemList:
                    itemList.append(self.my_listWidget.item(index))
            for item in itemList:
                crs.execute("INSERT INTO todolist VALUES (:item)",
                            {
                                'item': item.text(),
                            })
            connection.commit()
            crs.close()
            _message=QtWidgets.QMessageBox()
            _message.setWindowTitle("Success")
            _message.setText("Save Successful")
            _message.setIcon(QtWidgets.QMessageBox.Information)
            _message.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
