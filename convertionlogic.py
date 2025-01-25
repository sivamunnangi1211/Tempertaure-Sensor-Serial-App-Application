from PyQt5 import QtCore, QtGui, QtWidgets  # Ensure you have PyQt5 installed  

class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):  
        MainWindow.setObjectName("MainWindow")  
        MainWindow.resize(800, 600)  
        self.centralwidget = QtWidgets.QWidget(MainWindow)  
        self.centralwidget.setObjectName("centralwidget")  

        MainWindow.setCentralWidget(self.centralwidget)  

        # Set up the main window  
        self.retranslateUi(MainWindow)  
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  

    def retranslateUi(self, MainWindow):  
        _translate = QtCore.QCoreApplication.translate  
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Monitor App"))  

class SerialMonitorApp(QtWidgets.QMainWindow, Ui_MainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setupUi(self)  
        self.setup_additional_ui()  # Ensure this is called to set up the UI elements  

    def setup_additional_ui(self):  
        # Connect combo boxes to the combined conversion function  
        self.comboBox_11.currentIndexChanged.connect(self.convert_values)  
        self.comboBox_12.currentIndexChanged.connect(self.convert_values)  
        self.comboBox_19.currentIndexChanged.connect(self.convert_values)  
        self.comboBox_10.currentIndexChanged.connect(self.convert_values)  

    def convert_values(self):  
        # Get the selected values from the combo boxes  
        value_11 = self.comboBox_11.currentText()  
        value_12 = self.comboBox_12.currentText()  
        value_19 = self.comboBox_19.currentText()  
        selected_type = self.comboBox_10.currentText()  

        # Convert to hex for the first three combo boxes if the values are not empty  
        if value_11.isdigit():  
            hex_value_11 = hex(int(value_11))[2:].upper().zfill(4)  # Convert to hex, remove '0x', and pad to 4 digits  
            print(f"Hex Value 11: {hex_value_11}")  # Print to terminal  

        if value_12.isdigit():  
            hex_value_12 = hex(int(value_12))[2:].upper().zfill(4)  # Convert to hex, remove '0x', and pad to 4 digits  
            print(f"Hex Value 12: {hex_value_12}")  # Print to terminal  

        if value_19.isdigit():  
            hex_value_19 = hex(int(value_19))[2:].upper().zfill(4)  # Convert to hex, remove '0x', and pad to 4 digits  
            print(f"Hex Value 19: {hex_value_19}")  # Print to terminal  

        # Define the mapping of options to 3-bit binary values  
        binary_mapping = {  
            "RTD": "000",          # 0  
            "TC-K type": "001",    # 1  
            "TC-J type": "010",    # 2  
            "TC-N type": "011",    # 3  
            "TC-T type": "100",    # 4  
            "TC-S type": "101",    # 5  
            "TC-R type": "110",    # 6  
            "TC-E type": "111"     # 7  
        }  

        # Get the binary value based on the selected type  
        binary_value = binary_mapping.get(selected_type, "000")  # Default to 000 if not found  

        # Print the binary value to the terminal  
        print(f"Sensor Type: {selected_type}, Binary Value: {binary_value}")  

if __name__ == "__main__":  
    import sys  
    app = QtWidgets.QApplication(sys.argv)  
    window = SerialMonitorApp()  
    window.show()  
    sys.exit(app.exec_())