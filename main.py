from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, QPropertyAnimation, QEasingCurve, Qt
import os
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.IniUI()

    def IniUI(self):
        self.setGeometry(400, 200, 500, 150)
        self.setWindowTitle('Página de Inicio')
        self.load_styles()
        self.main_info()
        
        self.setWindowOpacity(0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.start()
        
        self.show()

    def load_styles(self):
        ruta_qss = os.path.join(os.path.dirname(__file__), "Style.qss")
        if os.path.exists(ruta_qss):
            with open(ruta_qss, "r") as file_style:
                self.setStyleSheet(file_style.read())
        else:
            print(f"No se encontró Style.qss en: {ruta_qss}")

    def main_info(self):
        self.save_button = QPushButton('Nueva agenda')
        self.save_button.setObjectName("saveButton")
        icon_path_save = os.path.join(os.path.dirname(__file__), "icons", "agenda.png")
        if os.path.exists(icon_path_save):
            self.save_button.setIcon(QIcon(icon_path_save))
            self.save_button.setIconSize(QSize(24, 24))
        self.save_button.clicked.connect(self.save_form)

        self.send_button = QPushButton('Enviar Agenda')
        self.send_button.setObjectName("sendButton")
        icon_path_send = os.path.join(os.path.dirname(__file__), "icons", "send.png")
        if os.path.exists(icon_path_send):
            self.send_button.setIcon(QIcon(icon_path_send))
            self.send_button.setIconSize(QSize(24, 24))
        self.send_button.clicked.connect(self.send_agenda)

        self.primer_nivel_button = QPushButton('Primer Nivel')
        self.primer_nivel_button.setObjectName("primerNivelButton")
        icon_path_primer_nivel = os.path.join(os.path.dirname(__file__), "icons", "nivel.png")
        if os.path.exists(icon_path_primer_nivel):
            self.primer_nivel_button.setIcon(QIcon(icon_path_primer_nivel))
            self.primer_nivel_button.setIconSize(QSize(24, 24))
        self.primer_nivel_button.clicked.connect(self.mostrar_mensaje_pronto)

        self.json_to_excel_button = QPushButton('de json a excel')
        self.json_to_excel_button.setObjectName("jsonToExcelButton")
        self.json_to_excel_button.clicked.connect(self.convert_json_to_excel)

        self.excel_to_json_button = QPushButton('de excel a json')
        self.excel_to_json_button.setObjectName("excelToJsonButton")
        self.excel_to_json_button.clicked.connect(self.convert_excel_to_json)

        h_box_buttons = QHBoxLayout()
        h_box_buttons.addStretch()
        h_box_buttons.addWidget(self.save_button)
        h_box_buttons.addSpacing(20)
        h_box_buttons.addWidget(self.send_button)
        h_box_buttons.addSpacing(20)
        h_box_buttons.addWidget(self.primer_nivel_button)
        h_box_buttons.addStretch()

        h_box_conversion = QHBoxLayout()
        h_box_conversion.addStretch()
        h_box_conversion.addWidget(self.json_to_excel_button)
        h_box_conversion.addSpacing(20)
        h_box_conversion.addWidget(self.excel_to_json_button)
        h_box_conversion.addStretch()

        vertical_layout_main = QVBoxLayout()
        vertical_layout_main.addLayout(h_box_buttons)
        vertical_layout_main.addSpacing(10)
        vertical_layout_main.addLayout(h_box_conversion)

        self.setLayout(vertical_layout_main)


    def save_form(self):
        return
        
    def mostrar_mensaje_pronto(self):
        QMessageBox.information(self, "Información", "Pronto...")

    def send_agenda(self):
        return

    def convert_json_to_excel(self):
        return

    def convert_excel_to_json(self):
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
