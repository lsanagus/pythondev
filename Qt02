
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Spear(QDialog):
    def __init__(self):
        QDialog.__init__(self)
	layout = QVBoxLayout()
	self.label = QLabel("Hello, lorenzo")
	line_edit = QLineEdit(()
	bClose = QPushButton("Close")
	bProcess = QPushButton("Process")

	layout.addWidget(self.label)
	layout.addWidget(line_edit)
	layout.addWidget(bClose)
	layout.addWidget(bProcess)
	
	self.setLayout(layout)
	
	bClose.clicked.connect(self.close)
	bProcess.clicked.connect(self.close)

	line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
	self.label.setText(text)

app = QApplication(sys.argv)
dialog = Spear()
dialog.show()
exit( app.exec_() )
