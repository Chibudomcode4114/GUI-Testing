import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    QApplication,
    QLineEdit,
    QLabel,
    QFormLayout,
    QRadioButton,
    QAction
)


# Toolbar Section
class menudemo(QMainWindow):

 def __init__(self, parent=None):
    super(menudemo, self).__init__(parent)
    
    layout = QHBoxLayout()
    bar=self.menuBar()
    file=bar.addMenu("File")
    file.addAction("New")
    
    save=QAction("Save",self)
    save.setShortcut("Ctrl+S")
    file.addAction(save)
    
    edit=file.addMenu("Edit")
    edit.addAction("copy")
    edit.addAction("paste")
    
    quit=QAction("Quit",self)
    file.addAction(quit)
    file.triggered[QAction].connect(self.processtrigger)
    self.setLayout(layout)
    # self.setWindowTitle("menu demo")

    
 def processtrigger(self,q):
     print(q.text()+" is triggered")



# Main forms layout
def window():
 app = QApplication(sys.argv)
 win = QWidget()
 l1=QLabel("Name")
 nm=QLineEdit()
 
 l2=QLabel("Address")
 add1=QLineEdit()
 add2=QLineEdit()
 fbox=QFormLayout()
 fbox.addRow(l1,nm)
 vbox=QVBoxLayout()
 
 vbox.addWidget(add1)
 vbox.addWidget(add2)
 fbox.addRow(l2,vbox)
 hbox=QHBoxLayout()
 r1=QRadioButton("Male")
 r2=QRadioButton("Female")
 hbox.addWidget(r1)
 hbox.addWidget(r2)
 hbox.addStretch()
 fbox.addRow(QLabel("Sex"),hbox)
 fbox.addRow(QPushButton("Submit"),QPushButton("Cancel"))
 
 win.setLayout(fbox)
 
 win.setWindowTitle("PyQt")
 win.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 window()


def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
      main()