from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog, QLineEdit, QFileDialog, QAction
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

        layout_container = QHBoxLayout()

        menu_layout = QVBoxLayout()

        button = QPushButton('Choose Picture')
        button.clicked.connect(self.selectFile)
        menu_layout.addWidget(button)
        menu_layout.addWidget(QPushButton('Choose Point Generation Choice'))
        menu_layout.addWidget(QPushButton('Generate Tesselation'))

        picture_viewer = QGridLayout()

        pixmap = QPixmap(240,240)
        pixmap.fill(QColor(53, 53, 53))
        self.original_pic.setPixmap(pixmap)
        self.point_line_pic.setPixmap(pixmap)
        self.tesselated_pic.setPixmap(pixmap)

        for i, pic in enumerate([self.original_pic, self.point_line_pic, self.tesselated_pic]):
            picture_viewer.addWidget(pic, 0, i)

        for i, label in enumerate(["Original", "Chosen Points & Triangles", "Tesselated"]):
            pic_label = QLabel(label)
            pic_label.setAlignment(Qt.AlignCenter)
            picture_viewer.addWidget(pic_label, 1, i)

        layout_container.addLayout(menu_layout)
        layout_container.addLayout(picture_viewer)
        
        self.setLayout(layout_container)
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
        if (file_name == ""):
            pass
        else:
            pixmap = QPixmap(file_name).scaled(240, 240, Qt.KeepAspectRatio)
            self.original_pic.setPixmap(pixmap)

app = QApplication([])
ex = TesselateWindow()
ex.dark_theme(app)
sys.exit(app.exec_())