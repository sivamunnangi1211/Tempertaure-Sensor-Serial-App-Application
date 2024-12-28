from PyQt5 import QtCore, QtGui, QtWidgets  

class MainWindow(QtWidgets.QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Control Panel")  
        self.setGeometry(100, 100, 1000, 600)  # Set the window size  

        # Setup UI components  
        self.setup_ui()  

    def setup_ui(self):  
        # Setup image label  
        self.image_label = self.setup_image_label(self)  

        # Setup company name label  
        self.company_name_label = self.setup_company_name_label(self)  

        # Setup labels and combo boxes  
        self.labels, self.combo_boxes = self.setup_labels(self)  

        # Setup text edit  
        self.text_edit = self.setup_text_edit(self)  

        # Setup buttons  
        self.buttons = self.setup_buttons(self)  

        # Setup serial port combo box  
        self.serial_port_combo_box = self.setup_combobox(self)  

    def setup_image_label(self, parent):  
        """Sets up the QLabel for displaying an image."""  
        imageLabel = QtWidgets.QLabel(parent)  
        imageLabel.setGeometry(QtCore.QRect(10, 10, 200, 120))  # Position (x, y) and size (width, height)  
        imageLabel.setPixmap(QtGui.QPixmap(r"images/logo.png"))  # Path to the image  
        imageLabel.setScaledContents(True)  # Scale the image to fit the label size  
        imageLabel.setObjectName("imageLabel")  
        return imageLabel  

    def setup_company_name_label(self, parent):  
        """Sets up the QLabel for displaying the company name."""  
        companyNameLabel = QtWidgets.QLabel(parent)  
        companyNameLabel.setGeometry(QtCore.QRect(300, 50, 800, 30))  # Increase the width and adjust x position  
        font = QtGui.QFont()  
        font.setPointSize(20)  
        font.setBold(True)  
        companyNameLabel.setFont(font)  
        companyNameLabel.setText("Controlytics AI Private Limited")  
        companyNameLabel.setStyleSheet("color: green;")  
        companyNameLabel.setObjectName("companyNameLabel")  
        return companyNameLabel  

    def setup_labels(self, parent):  
        """Sets up multiple QLabel widgets with a common style and corresponding QComboBox widgets."""  
        common_style = """  
            color: #2C3E50;              /* Text color */  
            font-size: 15px;             /* Font size */  
            font-weight: bold;           /* Font weight */  
        """  

        labels = {}  
        combo_boxes = {}  # Dictionary to hold the combo boxes  

        # Existing Baud Rate Label  
        label_2 = QtWidgets.QLabel(parent)  
        label_2.setGeometry(QtCore.QRect(30, 280, 81, 21))  # Position and size  
        label_2.setObjectName("label_2")  
        label_2.setText("Baud Rate")  
        label_2.setStyleSheet(common_style)  
        labels["label_2"] = label_2  

        # New Labels with corresponding QComboBoxes  
        labels_info = [  
            (360, 360, 120, 31, "label_10", "Transmit Power"),  
            (360, 520, 87, 31, "label_11", "Temperature Threshold"),  
            (30, 520, 120, 31, "label_12", "Sensor Type"),  
            (360, 280, 87, 31, "label_13", "Sleep Time"),  
            (360, 440, 87, 31, "label_20", "Transmit Pin Change"),  
            (30, 440, 127, 31, "label_14", "Destination ID(DID)"),  
            (30, 280, 117, 31, "label_15", "Network ID(NID)"),  
            (30, 360, 107, 31, "label_16", "Unique ID(UID)"),  
            (690, 360, 107, 31, "label_18", "No Of Wires"),  
            (690, 280, 107, 31, "label_19", "PT"),  
        ]  

        for x, y, w, h, obj_name, text in labels_info:  
            label = QtWidgets.QLabel(parent)  
            label.setGeometry(QtCore.QRect(x, y, w, h))  
            label.setObjectName(obj_name)  
            label.setText(text)  
            label.setStyleSheet(common_style)  
            labels[obj_name] = label  

            # Create a QComboBox for each label  
            combo_box = QtWidgets.QComboBox(parent)  
            combo_box.setGeometry(QtCore.QRect(x + w + 10, y, 150, 30))  # Position next to the label  
            combo_box.setObjectName(f"{obj_name}_comboBox")  
            combo_boxes[obj_name] = combo_box  # Store the combo box in the dictionary  

        return labels, combo_boxes  # Return both labels and combo boxes  

    def setup_text_edit(self, parent):  
        """Sets up a QTextEdit widget with custom styles."""  
        text_edit = QtWidgets.QTextEdit(parent)  
        text_edit.setGeometry(QtCore.QRect(30, 140, 350, 101))  # Position and size  
        text_edit.setObjectName("textEdit_2")  

        # Set the stylesheet for QTextEdit  
        text_edit.setStyleSheet("""  
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

        return text_edit  

    def setup_buttons(self, parent):  
        """Sets up buttons with custom styles and adds them to the parent widget."""  
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
            QPushButton:hover {  
                background-color: #45a049;  
            }  
            QPushButton:pressed {  
                background-color: #388E3C;  
            }  
        """  

        # Create buttons  
        buttons = []  
        pushButton = QtWidgets.QPushButton("Connect", parent)  
        pushButton.setStyleSheet(button_style)  
        pushButton.setGeometry(QtCore.QRect(630, 130, 151, 32))  
        buttons.append(pushButton)  

        pushButton_2 = QtWidgets.QPushButton("Refresh Port", parent)  
        pushButton_2.setStyleSheet(button_style)  
        pushButton_2.setGeometry(QtCore.QRect(790, 170, 151, 32))  
        buttons.append(pushButton_2)  

        pushButton_3 = QtWidgets.QPushButton("Clear", parent)  
        pushButton_3.setStyleSheet(button_style)  
        pushButton_3.setGeometry(QtCore.QRect(450, 200, 151, 40))  
        buttons.append(pushButton_3)  

        pushButton_4 = QtWidgets.QPushButton("Disconnect", parent)  
        pushButton_4.setStyleSheet(button_style)  
        pushButton_4.setGeometry(QtCore.QRect(630, 170, 151, 32))  
        buttons.append(pushButton_4)  

        pushButton_5 = QtWidgets.QPushButton("Set Params", parent)  
        pushButton_5.setStyleSheet(button_style)  
        pushButton_5.setGeometry(QtCore.QRect(790, 213, 151, 32))  
        buttons.append(pushButton_5)  

        pushButton_6 = QtWidgets.QPushButton("Version", parent)  
        pushButton_6.setStyleSheet(button_style)  
        pushButton_6.setGeometry(QtCore.QRect(790, 130, 151, 32))  
        buttons.append(pushButton_6)  

        pushButton_command = QtWidgets.QPushButton("Get Params", parent)  
        pushButton_command.setGeometry(QtCore.QRect(630, 213, 151, 32))  
        pushButton_command.setStyleSheet(button_style)  
        buttons.append(pushButton_command)  

        return buttons  

    def setup_combobox(self, parent):  
        """Sets up a QComboBox for selecting serial ports."""  
        comboBox = QtWidgets.QComboBox(parent)  
        comboBox.setGeometry(QtCore.QRect(415, 140, 180, 30))  # Position and size  
        comboBox.setObjectName("serialPortComboBox")  
        return comboBox  

if __name__ == "__main__":  
    import sys  
    app = QtWidgets.QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())