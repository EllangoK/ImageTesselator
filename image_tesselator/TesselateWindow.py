from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog, QLineEdit, QFileDialog, QAction
import sys

class TesselateWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.original_pic = QLabel()
        self.point_line_pic = QLabel()
        self.tesselated_pic = QLabel()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Tesselator')

        layout = QVBoxLayout()

        button = QPushButton('Choose Picture')
        button.clicked.connect(self.selectFile)
        layout.addWidget(button)
        layout.addWidget(QPushButton('Choose Point Generation Choice'))
        layout.addWidget(QPushButton('Generate Tesselation'))

        picture_viewer = QHBoxLayout()
        picture_viewer.addLayout(layout)

        pixmap = QPixmap('images/black.jpg').scaled(240, 240, Qt.KeepAspectRatio)
        self.original_pic.setPixmap(pixmap)
        self.point_line_pic.setPixmap(pixmap)
        self.tesselated_pic.setPixmap(pixmap)

        picture_viewer.addWidget(self.original_pic)
        picture_viewer.addWidget(self.point_line_pic)
        picture_viewer.addWidget(self.tesselated_pic)
        
        self.setLayout(picture_viewer)
        self.show()

    def dark_theme(self, app):
        app.setStyle('Fusion')
        
        dark_palette = QPalette()

        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        app.setPalette(dark_palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    def selectFile(self):
        file_name = QFileDialog.getOpenFileName()[0]
        print(file_name)
        pixmap = QPixmap(file_name).scaled(240, 240, Qt.KeepAspectRatio)
        self.original_pic.setPixmap(pixmap)

app = QApplication([])
ex = TesselateWindow()
ex.dark_theme(app)
sys.exit(app.exec_())