# Libraries
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel, QComboBox, QMessageBox
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya.OpenMayaUI import MQtUtil
import yaml

# Class 
class MyWindow(MayaQWidgetDockableMixin, QDialog):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent = parent)
        mayaMainWindowPtr = MQtUtil.mainWindow() 
        #self.mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow)

        # Yaml File Load
        fileYamlLocation = "C:/Users/KrisPC/Desktop/Tool.yaml"
        ymlFile = open(fileYamlLocation, "r") #Load in the yml File
        self.ymlInfo = yaml.load(ymlFile, Loader=yaml.FullLoader)
        comboUsernameID = (self.ymlInfo["user"]["usernameID"])
        comboFT = (self.ymlInfo["user"]["filetype"])

        # Window Settings
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle('Import/Export Tool')
        self.resize(300, 100)

        # UI Options
        
        # Labels and Combo Boxes
        self.comboUserLabel = QLabel("Username:")
        self.comboFTLabel = QLabel("File Type:")
        self.comboUserBox = QComboBox()
        self.comboUserBox.addItems(comboUsernameID)
        self.comboFTBox = QComboBox()
        self.comboFTBox.addItems(comboFT)

        # Buttons
        self.helpButton = QPushButton('Help')
        self.importButton = QPushButton('Import')
        self.exportButton = QPushButton('Export')
        self.helpButton.clicked.connect(self.buttonHelp)
        self.importButton.clicked.connect(self.buttonImport)
        self.exportButton.clicked.connect(self.buttonExport)
        
        # Main Layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.comboUserLabel)
        self.mainLayout.addWidget(self.comboUserBox)
        self.mainLayout.addWidget(self.comboFTLabel)
        self.mainLayout.addWidget(self.comboFTBox)
        self.mainLayout.addWidget(self.importButton)
        self.mainLayout.addWidget(self.exportButton)
        self.mainLayout.addWidget(self.helpButton)
        self.setLayout(self.mainLayout)

    # Dockable
    def run(self):
        self.show(dockable = True)
        
    # Help
    def buttonHelp(self):
        print("Helping!")
        QMessageBox.about(None, 'Help', (self.ymlInfo["help"]))
        
    # Import
    def buttonImport(self):
        print("Importing!")
        UserFileName =(self.comboUserBox.currentText())
        cmds.file("C:/Users/KrisPC/Documents/maya/projects/default/scenes/kk2crt.mb",i=True)

    # Export
    def buttonExport(self):
        print("Exporting!")
        UserFileRename =(self.comboUserBox.currentText())
        UserFileType =(self.comboFTBox.currentText())
        cmds.file(rename=UserFileRename)
        cmds.file(save=True, type=UserFileType)

# Build
myWin = MyWindow()
myWin.run()

