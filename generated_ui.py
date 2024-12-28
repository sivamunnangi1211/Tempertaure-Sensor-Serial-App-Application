# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 580) 
        MainWindow.setStyleSheet("background-color: #f5f5dc;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.companyNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.companyNameLabel.setGeometry(QtCore.QRect(300, 50, 800, 30))  # Increase the width and adjust x position
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setText("Controlytics AI Private Limited")
        self.companyNameLabel.setStyleSheet("color: green;")
        self.companyNameLabel.setObjectName("companyNameLabel")

        # Unified style for all QLabel widgets
        common_style = """
            color: #2C3E50;              /* Text color */
            font-size: 15px;             /* Font size */
            font-weight: bold;           /* Font weight */
        """
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 280, 81, 21)) #baud rate
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(common_style)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0)) #format 
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(common_style)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 0, 0)) #databits
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(common_style)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 0, 0)) #parity
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(common_style)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 0, 0)) #stopbits
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(common_style)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))  #view as heading
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet(common_style)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 360, 120, 21))  # fixed transmission
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet(common_style)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 520, 87, 21))  #io drive mode
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet(common_style)
        self.label_12= QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 440, 157, 21))  #wireless wake up time
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet(common_style)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 280, 87, 21))  #fec switch
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet(common_style)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 520, 127, 21))  #transmission power
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet(common_style)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 360, 117, 21))  #UART parity bit
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet(common_style)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 440, 107, 21))  #Air data rate
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet(common_style)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(690, 360, 107, 21))  #Address
        self.label_18.setObjectName("label_18")
        self.label_18.setStyleSheet(common_style)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(690, 280, 87, 21))  #Frame
        self.label_20.setObjectName("label_20")
        self.label_20.setStyleSheet(common_style)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)  # port selection
        self.comboBox.setGeometry(QtCore.QRect(410, 140, 200, 40))
        self.comboBox.setObjectName("comboBox")
        
        # Set styles to make the ComboBox more appealing
        self.comboBox.setStyleSheet("""
            QComboBox {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
                color: #333;
                background-color: #f0f0f0;
            }
        """)

        common_combobox_style = """
            QComboBox {
                color: #2C3E50;                /* Text color */
                font-size: 14px;               /* Font size */
                font-weight: bold;             /* Font weight */
                background-color: #ECF0F1;     /* Background color */
                border: 2px solid #4CAF50;     /* Border color */
                padding: 5px;                  /* Padding */
                border-radius: 8px;            /* Rounded corners */
                min-height: 30px;              /* Minimum height */
            }
            QComboBox:hover {
                background-color: #D5DBDB;     /* Background color on hover */
                border: 2px solid #AAB7B8;     /* Border color on hover */
            }
            QComboBox:focus {
                background-color: #FDFEFE;     /* Background color on focus */
                border: 2px solid #5DADE2;     /* Border color on focus */
            }
            QComboBox QListView {
                background-color: #F2F4F4;     /* Dropdown list background */
                border: 1px solid #BDC3C7;
                color: #2C3E50;
                font-size: 14px;
                selection-background-color: #AED6F1; /* Background color for selected item */
                selection-color: #1B2631;      /* Text color for selected item */
                outline: none;                 /* Removes outline */
            }
            QComboBox QAbstractItemView {
                background-color: #F2F4F4;     /* Background color of the item view */
                border: 1px solid #BDC3C7;
                selection-background-color: #AED6F1; /* Selection background color */
                selection-color: #1B2631;      /* Selection text color */
                padding: 3px;
                border-radius: 5px;
            }
            QComboBox::item {
                padding: 8px;                  /* Item padding */
            }
            QComboBox::item:hover {
                background-color: #D6EAF8;     /* Background color when hovering over an item */
                color: #154360;                /* Text color on hover */
            }
            QComboBox::item:selected {
                background-color: #85C1E9;     /* Selected item background color */
                color: #1B2631;                /* Selected item text color */
            }
            
        """

        common_button_style = """
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 20px;  /* Adjust size as needed */
            }
            QPushButton:hover {
                color: blue;  /* Optional: change color on hover */
            }
        """   

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)   
        self.comboBox_2.setGeometry(QtCore.QRect(0,0,0,0))    #9600 values dropdown
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setStyleSheet(common_combobox_style)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(0,0,0,0))    #String or Hex dropdown
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setStyleSheet(common_combobox_style)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(0,0,0,0))   # 5,8 values dropdown
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setStyleSheet(common_combobox_style)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(0,0,0,0))   # no parity,event parity dropdown
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setStyleSheet(common_combobox_style)
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(0,0,0,0))   #1,1.5,2 values dropdown
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setStyleSheet(common_combobox_style)
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(0,0,0,0))   # hex,string,chart dropdown
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setStyleSheet(common_combobox_style)
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(470, 430, 150, 32))   #250ms values dropdown
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.setEditable(True)
        # self.infoButton_8 = self.create_info_button(630, 430, "infoButton_8", common_button_style)
        self.comboBox_8.setStyleSheet(common_combobox_style)
        self.comboBox_9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_9.setGeometry(QtCore.QRect(470, 270, 150, 32))    #FEC dropdown
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.setEditable(True)
        self.infoButton_9 = self.create_info_button(630, 270, "infoButton_9", common_button_style)
        self.comboBox_9.setStyleSheet(common_combobox_style)
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(130, 510, 150, 32))    #20dBm dropdown
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.setEditable(True)
        # self.infoButton_10 = self.create_info_button(290, 510, "infoButton_10", common_button_style)
        self.comboBox_10.setStyleSheet(common_combobox_style)
        self.comboBox_11 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_11.setGeometry(QtCore.QRect(130, 430, 150, 32))    #0.3k values dropdown
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.setEditable(True)
        self.infoButton_11 = self.create_info_button(290, 430, "infoButton_11", common_button_style)
        self.comboBox_11.setStyleSheet(common_combobox_style)
        self.comboBox_12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_12.setGeometry(QtCore.QRect(130, 350, 150, 32))    #8N1 dropdown
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.setEditable(True)
        # self.infoButton_12 = self.create_info_button(290, 350, "infoButton_12", common_button_style)
        self.comboBox_12.setStyleSheet(common_combobox_style)
        self.comboBox_13 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_13.setGeometry(QtCore.QRect(470, 350, 150, 32))    #Transmit Power dropdown
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.setEditable(True)
        self.infoButton_13 = self.create_info_button(630, 350, "infoButton_13", common_button_style) 
        self.comboBox_13.setStyleSheet(common_combobox_style)
        self.comboBox_14 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_14.setGeometry(QtCore.QRect(470, 510, 150, 32))    #Temperature Drodown
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.setEditable(True)
        self.infoButton_14 = self.create_info_button(630, 510, "infoButton_14", common_button_style)
        self.comboBox_14.setStyleSheet(common_combobox_style)
        self.comboBox_15 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_15.setGeometry(QtCore.QRect(770, 350, 150, 32))   #No of Wires Dropdown
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.setEditable(True)  # Allow text entry
        self.infoButton_15 = self.create_info_button(930, 350, "infoButton_15", common_button_style)
        self.comboBox_15.setStyleSheet(common_combobox_style)
        self.comboBox_18 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_18.setGeometry(QtCore.QRect(770,270,150,32))   #PT Dropdown
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.setEditable(True)
        # self.infoButton_18 = self.create_info_button(930, 270, "infoButton_18", common_button_style)
        self.comboBox_18.setStyleSheet(common_combobox_style)
        self.comboBox_19 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_19.setGeometry(QtCore.QRect(130, 270, 150, 32))   # baud rate 
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.setEditable(True)
        # self.infoButton_19 = self.create_info_button(290, 270, "infoButton_19", common_button_style)
        self.comboBox_19.setStyleSheet(common_combobox_style)

 # Call the method to populate dropdowns

        # Styling for buttons
        button_style = """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                margin-right: 20px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
                padding: 5px 10px;
            }
            QPushButton:hover {ju
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """

        # Create buttons
        self.pushButton = QtWidgets.QPushButton("Connect", self.centralwidget)
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setGeometry(QtCore.QRect(630, 130, 151, 32))  # Button at (590, 130), Size (81, 32)
        self.pushButton_2 = QtWidgets.QPushButton("Refresh Port", self.centralwidget)
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 170, 151, 32))  # Button at (690, 170), Size (81, 32)
        self.pushButton_3 = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 200, 151, 40))  # Button at (620, 213), Size (81, 32)
        self.pushButton_4 = QtWidgets.QPushButton("Disconnect", self.centralwidget)
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 170, 151, 32))  # Button at (590, 170), Size (81, 32)
        self.pushButton_5 = QtWidgets.QPushButton("Set Params", self.centralwidget)
        self.pushButton_5.setStyleSheet(button_style)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 213, 151, 32))  # Button at (520, 213), Size (81, 32)
        self.pushButton_6 = QtWidgets.QPushButton("Version", self.centralwidget)
        self.pushButton_6.setStyleSheet(button_style)
        self.pushButton_6.setGeometry(QtCore.QRect(790, 130, 151, 32))  # Button at (690, 130), Size (81, 32)
        self.pushButton_7 = QtWidgets.QPushButton("Test", self.centralwidget)
        self.pushButton_7.setStyleSheet(button_style)
        self.pushButton_7.setGeometry(QtCore.QRect(790, 50, 151, 32))   #300, 50, 800, 30

        # Set window title and dimensions
        self.setWindowTitle("Controlytics.AI")
        self.setGeometry(400, 200, 960, 600)  # Set the window position and size (left, top, width, height)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(350, 300, 111, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(480, 300, 111, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(490, 220, 185, 25)) #command box
        # self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 140, 350, 101))  # response box
        self.textEdit_2.setObjectName("textEdit_2")


        self.info_map = {
            "infoButton_9": "1.After turn off FEC, the actual data transmission rate increases while anti-interference ability decreases. Also the transmission distance is relatively short.\n 2.Both Communication parties must keep on the same pages about turn-on or turn-off FEC.",
            "infoButton_11": "1.The air data rate must keep the same for both communication parties.\n2.The lower the air data rate, the longer the transmitting distance, better anti-interference performance and longer transmitting time.",
            "infoButton_13": "1.In fixed transmission mode,the first three bytes of each user's data frame can be used as high/low address and channel.\n2.The module changes its address and channel when transmit. And it will revert to original setting after complete the process.",
            "infoButton_14": "1.This bit is used to the module internal pull-up resistor. It also increases the levels adaptability in case of open drain.\n 2.But in some cases, it may need external pull-up resistor.",
            "infoButton_15": "Address and channel selection values should be the same because, for successful communication between a pair of devices, they need to match",
            "infoButton_17": "Address and channel selection values should be the same because, for successful communication between a pair of devices, they need to match",
        }
        # Set styles to enhance the appearance of the QTextEdit
        self.textEdit_2.setStyleSheet("""
            QTextEdit {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 8px;
                background-color: #f0f8ff;
                color: #333;
                font-size: 14px;
                font-weight: bold;
            }
            QTextEdit:hover {
                border: 2px solid #45a049;
                background-color: #e0f7fa;
            }
            QTextEdit:focus {
                border: 2px solid #008080;
                background-color: #e6f7ff;
            }
        """)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(100, 100, 813, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def create_combobox(self, x, y, name, style):
        comboBox = QtWidgets.QComboBox(self.centralwidget)
        comboBox.setGeometry(QtCore.QRect(x, y, 160, 32))
        comboBox.setObjectName(name)
        comboBox.setStyleSheet(style)
        return comboBox

    def create_info_button(self, x, y, name, style):
        button = QtWidgets.QPushButton(self.centralwidget)
        button.setGeometry(QtCore.QRect(x, y + 10, 22, 22))  # Move button down by 5 pixels
        button.setObjectName(name)
        button.setStyleSheet(style + """
            QPushButton {
                border-radius: 10px;  /* Decreased radius for less roundness */
                border: 2px solid blue;  /* Border width and color */
                background-color: #f0f0f0;  /* Background color */
                color: black;  /* Text color */
                font-size: 15px;  /* Adjust font size */
                padding: 0px;  /* Remove padding */
            }
            QPushButton:hover {
                background-color: #d0d0d0;  /* Change background on hover */
            }
        """)
        button.setText("?")  # Set text to '?'
        button.clicked.connect(self.show_info)
        return button

    def show_info(self):
        sender = self.sender()
        button_name = sender.objectName()
        
        # Get the corresponding information for the button
        info_text = self.info_map.get(button_name, "No information available.")
        
        # Display the information in a message box
        QtWidgets.QMessageBox.information(self, "Info", info_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controlytics.ai"))
        self.label_2.setText(_translate("MainWindow", "Network ID(NID)"))
        # self.label_4.setText(_translate("MainWindow", "Format: "))
        # self.label_6.setText(_translate("MainWindow", "Data Bits: "))
        # self.label_7.setText(_translate("MainWindow", "Parity: "))
        # self.label_8.setText(_translate("MainWindow", "Stop Bits: "))
        # self.label_9.setText(_translate("MainWindow", "View as: "))
        self.label_10.setText(_translate("MainWindow", "Transmit Power"))
        self.label_11.setText(_translate("MainWindow", "Temperature Threshold"))
        self.label_12.setText(_translate("MainWindow", "Transmit Pin Change"))
        self.label_13.setText(_translate("MainWindow", "Sleep Time"))
        self.label_14.setText(_translate("MainWindow", "Sensor Type"))
        self.label_15.setText(_translate("MainWindow", "Unique ID(UID)"))
        self.label_16.setText(_translate("MainWindow", "Destination ID(DID)"))
        self.label_18.setText(_translate("MainWindow", "No Of Wires"))
        self.label_20.setText(_translate("MainWindow", "PT"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh Ports"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_5.setText(_translate("MainWindow", "Set Params"))
        self.pushButton_6.setText(_translate("MainWindow", "Version"))
        self.checkBox.setText(_translate("MainWindow", "Carriage return(\"r\")"))
        self.checkBox_2.setText(_translate("MainWindow", "New Line(\"n\")"))
        