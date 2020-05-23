from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor, QPixmap, QIcon, QIntValidator
from PySide2.QtWidgets import QSizePolicy, QLineEdit, QSlider, QApplication, QTabBar, QSizePolicy, QComboBox, QToolButton, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog, QLineEdit, QFileDialog, QAction, QErrorMessage
import sys

class TesselateWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.original_pic = QLabel()
        self.point_line_pic = QLabel()
        self.tesselated_pic = QLabel()

        self.slider_field = QLineEdit()

        self.generation_type = "Random"
        self.points = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Tesselator')
        layout_container = QHBoxLayout()

        menu_layout = QVBoxLayout()
        button = QPushButton('Choose Picture')
        button.clicked.connect(self.selectFile)
        menu_layout.addWidget(button)

        generation_layout = QGridLayout()
        generation_layout.addWidget(QLabel("Generation Types"), 0, 0)
        generation_type = QComboBox()
        generation_type.addItems(["Random", "Highest Entropy"])
        generation_type.activated[str].connect(self.update_generation_type)
        policy = QSizePolicy()
        policy.setHorizontalPolicy(QSizePolicy.Expanding)
        generation_type.setSizePolicy(policy)
        generation_layout.addWidget(generation_type, 0, 1)
        menu_layout.addLayout(generation_layout)

        points_layout = QGridLayout()
        points_layout.addWidget(QLabel("Point Count"), 0, 0)
        self.slider_field.setAlignment(Qt.AlignCenter)
        self.slider_field.setValidator(QIntValidator())
        self.slider_field.textChanged[str].connect(self.update_points_field)
        self.slider_field.setText("0")
        points_layout.addWidget(self.slider_field, 0, 1)

        slider = QSlider(Qt.Horizontal)
        slider.setSingleStep(10)
        slider.setMinimum(0)
        slider.setMaximum(1000)
        slider.valueChanged[int].connect(self.update_points_slider)
        points_layout.addWidget(slider, 1, 0, 1, 2)
        
        menu_layout.addLayout(points_layout)

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
            if file_name.endswith(('.jpg', '.png', '.jpeg')):
                pixmap = QPixmap(file_name).scaledToWidth(240)
                self.original_pic.setPixmap(pixmap)
            else:
                img_error = QErrorMessage()
                img_error.showMessage('Oh no!')

    def update_generation_type(self, value):
        self.generation_type = value
        print(self.generation_type)

    def update_points_slider(self, value):
        self.slider_field.setText(str(value))
        self.points = int(value)

    def update_points_field(self, value):
        self.points = int(value)

app = QApplication([])
ex = TesselateWindow()
ex.dark_theme(app)
sys.exit(app.exec_())
