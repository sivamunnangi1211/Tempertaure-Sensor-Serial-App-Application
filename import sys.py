import sys  
import serial.tools.list_ports  
from PyQt5 import QtWidgets  
from generated_ui import (  
    setup_image_label,  
    setup_company_name_label,  
    setup_labels,  
    setup_text_edit,  
    setup_buttons,  
    setup_combobox,  # Import the setup_combobox function  
)  

class SimpleWindow(QtWidgets.QMainWindow):  
    def __init__(self):  
        super().__init__()  

        # Set up the main window properties  
        self.setWindowTitle('Controlytics AI')  
        self.setGeometry(400, 200, 960, 600)  # Main window position (x, y) and size (width, height)  

        # Set up the central widget  
        self.centralwidget = QtWidgets.QWidget(self)  
        self.setCentralWidget(self.centralwidget)  

        # Add the image label using the setup function from ui_setup.py  
        self.imageLabel = setup_image_label(self.centralwidget)  

        # Add the company name label using the setup function from ui_setup.py  
        self.companyNameLabel = setup_company_name_label(self.centralwidget)  

        # Add the labels and combo boxes using the setup function from ui_setup.py  
        self.labels, self.combo_boxes = setup_labels(self.centralwidget)  

        # Add the QTextEdit using the setup function from ui_setup.py  
        self.textEdit_2 = setup_text_edit(self.centralwidget)  

        # Add the buttons using the setup function from ui_setup.py  
        self.buttons = setup_buttons(self.centralwidget)  

        # Add the serial port combobox  
        self.serialPortComboBox = setup_combobox(self.centralwidget)  
        self.populate_serial_ports()  

    def populate_serial_ports(self):  
        """Populate the combo box with available serial ports."""  
        ports = serial.tools.list_ports.comports()  
        for port in ports:  
            self.serialPortComboBox.addItem(port.device)  

# Main entry point  
if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)  
    window = SimpleWindow()  
    window.show()  
    sys.exit(app.exec_())