from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QColorDialog, QFileDialog, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PIL.Image import Image
from core import LsystemImage, Lsystem
from utils import decart_to_image_coords, angle_part_of_circle, deg_to_rad, strings_to_dict, image_to_pixmap


class LsystemStringGenerator(QObject):
    finishSignal = pyqtSignal()

    @pyqtSlot()
    def generate(self, lsystem: Lsystem, iteration: int) -> None:
        lsystem.update_strings(iteration)
        self.finishSignal.emit()


class LsystemImageDrawer(QObject):
    finishSignal = pyqtSignal()

    @pyqtSlot()
    def draw(self, lsystem_image: LsystemImage, iteration: int) -> None:
        lsystem_image.update_image(iteration)
        self.finishSignal.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox_size_x = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_size_x.setMinimum(1)
        self.spinBox_size_x.setMaximum(1000)
        self.spinBox_size_x.setObjectName("spinBox_size_x")
        self.horizontalLayout_6.addWidget(self.spinBox_size_x)
        self.spinBox_size_y = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_size_y.setMinimum(1)
        self.spinBox_size_y.setMaximum(1000)
        self.spinBox_size_y.setObjectName("spinBox_size_y")
        self.horizontalLayout_6.addWidget(self.spinBox_size_y)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)
        self.spinBox_start_angle = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_start_angle.setMaximum(360)
        self.spinBox_start_angle.setObjectName("spinBox_start_angle")
        self.gridLayout_3.addWidget(self.spinBox_start_angle, 5, 1, 1, 1)
        self.spinBox_angle = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_angle.setEnabled(False)
        self.spinBox_angle.setMaximum(360)
        self.spinBox_angle.setObjectName("spinBox_angle")
        self.gridLayout_3.addWidget(self.spinBox_angle, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spinBox_start_x = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_start_x.setMinimum(-500)
        self.spinBox_start_x.setMaximum(500)
        self.spinBox_start_x.setObjectName("spinBox_start_x")
        self.horizontalLayout_7.addWidget(self.spinBox_start_x)
        self.spinBox_start_y = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_start_y.setMinimum(-500)
        self.spinBox_start_y.setMaximum(500)
        self.spinBox_start_y.setObjectName("spinBox_start_y")
        self.horizontalLayout_7.addWidget(self.spinBox_start_y)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_3.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.spinBox_plane_div = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_plane_div.setMinimum(2)
        self.spinBox_plane_div.setMaximum(360)
        self.spinBox_plane_div.setObjectName("spinBox_plane_div")
        self.gridLayout_3.addWidget(self.spinBox_plane_div, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)
        self.spinBox_step_length = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_step_length.setMinimum(1)
        self.spinBox_step_length.setMaximum(500)
        self.spinBox_step_length.setObjectName("spinBox_step_length")
        self.gridLayout_3.addWidget(self.spinBox_step_length, 6, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_angle_mode = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_angle_mode.setObjectName("radioButton_angle_mode")
        self.buttonGroup_rotation_mode = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_rotation_mode.setObjectName(
            "buttonGroup_rotation_mode")
        self.buttonGroup_rotation_mode.addButton(self.radioButton_angle_mode)
        self.horizontalLayout.addWidget(self.radioButton_angle_mode)
        self.radioButton_div_mode = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_div_mode.setChecked(True)
        self.radioButton_div_mode.setObjectName("radioButton_div_mode")
        self.buttonGroup_rotation_mode.addButton(self.radioButton_div_mode)
        self.horizontalLayout.addWidget(self.radioButton_div_mode)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_initiator = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_initiator.setObjectName("lineEdit_initiator")
        self.horizontalLayout_2.addWidget(self.lineEdit_initiator)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_rules = QtWidgets.QPlainTextEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plainTextEdit_rules.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_rules.setSizePolicy(sizePolicy)
        self.plainTextEdit_rules.setObjectName("plainTextEdit_rules")
        self.gridLayout_2.addWidget(self.plainTextEdit_rules, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider_step = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_step.setMinimum(1)
        self.horizontalSlider_step.setMaximum(50)
        self.horizontalSlider_step.setPageStep(1)
        self.horizontalSlider_step.setSliderPosition(1)
        self.horizontalSlider_step.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_step.setInvertedAppearance(False)
        self.horizontalSlider_step.setInvertedControls(False)
        self.horizontalSlider_step.setTickPosition(
            QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_step.setTickInterval(100)
        self.horizontalSlider_step.setObjectName("horizontalSlider_step")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_step)
        self.spinBox_step = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_step.setMinimum(1)
        self.spinBox_step.setMaximum(50)
        self.spinBox_step.setObjectName("spinBox_step")
        self.horizontalLayout_3.addWidget(self.spinBox_step)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_ch_bg_color = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ch_bg_color.setObjectName("pushButton_ch_bg_color")
        self.horizontalLayout_8.addWidget(self.pushButton_ch_bg_color)
        self.pushButton_ch_line_color = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ch_line_color.setObjectName("pushButton_ch_line_color")
        self.horizontalLayout_8.addWidget(self.pushButton_ch_line_color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_update.setObjectName("pushButton_update")
        self.verticalLayout_2.addWidget(self.pushButton_update)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_2.addWidget(self.pushButton_clear)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_save_image = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_save_image.sizePolicy().hasHeightForWidth())
        self.pushButton_save_image.setSizePolicy(sizePolicy)
        self.pushButton_save_image.setObjectName("pushButton_save_image")
        self.horizontalLayout_5.addWidget(self.pushButton_save_image)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinBox_scale = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_scale.setMinimum(1)
        self.spinBox_scale.setMaximum(1000)
        self.spinBox_scale.setObjectName("spinBox_scale")
        self.horizontalLayout_5.addWidget(self.spinBox_scale)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_result = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 0, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_saveas = QtWidgets.QAction(MainWindow)
        self.action_saveas.setObjectName("action_saveas")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu.addAction(self.action_new)
        self.menu.addSeparator()
        self.menu.addAction(self.action_open)
        self.menu.addSeparator()
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "L-системы: новый уровень"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.label_3.setText(_translate("MainWindow", "Угол поворота"))
        self.label_9.setText(_translate(
            "MainWindow", "Начальные координаты (x, y)"))
        self.label_4.setText(_translate(
            "MainWindow", "На сколько углов делится плоскость"))
        self.label_2.setText(_translate("MainWindow", "Название системы:"))
        self.label_8.setText(_translate(
            "MainWindow", "Размеры изображения (x, y)"))
        self.lineEdit_name.setPlaceholderText(_translate(
            "MainWindow", "Стандатное название - lsystem"))
        self.label.setText(_translate("MainWindow", "Начальный угол поворота"))
        self.label_10.setText(_translate("MainWindow", "Длина одного шага"))
        self.groupBox_3.setTitle(_translate(
            "MainWindow", "Режим вычисления угла поворота"))
        self.radioButton_angle_mode.setText(_translate("MainWindow", "Угол"))
        self.radioButton_div_mode.setText(
            _translate("MainWindow", "Деление плоскости"))
        self.label_6.setText(_translate("MainWindow", "Аксиома (инициатор)"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Теоремы"))
        self.plainTextEdit_rules.setPlaceholderText(_translate(
            "MainWindow", "Теоремы системы по одной на строке"))
        self.label_5.setText(_translate("MainWindow", "Шаг эволюции"))
        self.pushButton_ch_bg_color.setText(
            _translate("MainWindow", "Выбрать цвет фона"))
        self.pushButton_ch_line_color.setText(
            _translate("MainWindow", "Выбрать цвет линий"))
        self.pushButton_update.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_save_image.setText(
            _translate("MainWindow", "Сохранить результат"))
        self.label_7.setText(_translate("MainWindow", "Множитель масштаба"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Результат"))
        self.label_result.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_new.setText(_translate("MainWindow", "Новая система"))
        self.action_open.setText(_translate(
            "MainWindow", "Загрузить из файла..."))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_saveas.setText(_translate(
            "MainWindow", "Сохранить как..."))
        self.action_exit.setText(_translate("MainWindow", "Выход"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.bg_color = "#000000"
        self.line_color = "#FFFFFF"
        self.image = None
        self.clear_path()

    def initUi(self):
        self.setupUi(self)
        self.retranslateUi(self)
        self.spinBox_step.valueChanged.connect(self.update_step_slider)
        self.horizontalSlider_step.valueChanged.connect(
            self.update_step_spinbox)
        self.pushButton_update.clicked.connect(self.update_label)
        self.pushButton_ch_bg_color.clicked.connect(self.request_bg_color)
        self.pushButton_ch_line_color.clicked.connect(self.request_line_color)
        self.pushButton_clear.clicked.connect(self.clear_label)
        self.radioButton_angle_mode.clicked.connect(self.set_angle_mode)
        self.radioButton_div_mode.clicked.connect(self.set_plane_div_mode)
        self.pushButton_save_image.clicked.connect(self.save_image)
        self.action_open.triggered.connect(self.open)
        self.action_new.triggered.connect(self.new)
        self.action_save.triggered.connect(self.save)
        self.action_saveas.triggered.connect(self.saveas)
        self.action_exit.triggered.connect(exit)

    def new(self):
        self.clear_path()
        self.spinBox_angle.setValue(0)
        self.spinBox_plane_div.setValue(2)
        self.spinBox_start_angle.setValue(0)
        self.spinBox_step.setValue(1)
        self.horizontalSlider_step.setValue(1)
        self.lineEdit_name.clear()
        self.lineEdit_initiator.clear()
        self.plainTextEdit_rules.clear()
        self.clear_label()

    def save_data(self):
        name = self.lineEdit_name.text()
        if not name:
            name = "lsystem"
        if self.radioButton_angle_mode.isChecked():
            angle_div = self.spinBox_angle.value()
        else:
            angle_div = self.spinBox_plane_div.value()
        initiator = self.lineEdit_initiator.text()
        rules_text = self.plainTextEdit_rules.toPlainText()
        with open(self.path, "w") as f:
            f.write(name + "\n")
            f.write(str(angle_div) + "\n")
            f.write(initiator + "\n")
            f.write(rules_text + "\n")

    def save(self):
        if self.path is not None:
            self.save_data()
        else:
            self.saveas()

    def saveas(self):
        try:
            self.path = self.requset_save_path(
                "Сохранить l-систему", "l-system files (*.ls)")
            self.save_data()
        except FileNotFoundError:
            return

    def open(self):
        try:
            self.path = self.request_open_path(
                "Открыть l-систему", "l-system files (*.ls)")
        except FileNotFoundError:
            return
        self.load_data()

    def show_messagebox(self, message):
        msgbox = QMessageBox(self)
        msgbox.setText(message)
        msgbox.show()

    def load_data(self):
        with open(self.path, "r") as f:
            text = f.read()
        lines = text.strip().split("\n")
        lines = tuple(line.strip() for line in lines)
        print(lines)
        print(*map(lambda line: " " in line, lines[3:]))
        if not (lines[1].isdecimal() and
                all(map(lambda line: " " in line, lines[3:]))):
            self.clear_path()
            self.show_messagebox("Неверный формат файла!")
            return
        try:
            mode = self.request_choice(
                "Как загрузить данные", "Выберите режим поворотов", ("Деление плоскости", "Угол"))
        except InterruptedError:
            self.clear_path()
            return
        name = lines[0]
        angle_div = int(lines[1])
        initiator = lines[2]
        rules_text = "\n".join(lines[3:])
        if mode == "Угол":
            self.set_angle_mode()
            self.spinBox_angle.setValue(angle_div)
        else:
            self.set_plane_div_mode()
            self.spinBox_plane_div.setValue(angle_div)
        self.lineEdit_name.setText(name)
        self.lineEdit_initiator.setText(initiator)
        self.plainTextEdit_rules.setPlainText(rules_text)

    def clear_path(self):
        self.path = None

    def request_choice(self, header, request, variants):
        val, ok = QInputDialog.getItem(
            self, header, request, variants, editable=False)
        if ok:
            return val
        else:
            raise InterruptedError

    def request_bg_color(self):
        try:
            self.bg_color = self.request_color()
        except ValueError:
            return

    def request_line_color(self):
        try:
            self.line_color = self.request_color()
        except ValueError:
            return

    def request_open_path(self, request, filter):
        path = QFileDialog.getOpenFileName(
            self, request, "", filter)[0]
        if path:
            return path
        raise FileNotFoundError

    def requset_save_path(self, request, filter):
        path = QFileDialog.getSaveFileName(
            self, request, "", filter)[0]
        if path:
            return path
        raise FileNotFoundError

    def request_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            return color.name()
        else:
            raise ValueError

    def request_bg_color(self):
        try:
            self.bg_color = self.request_color()
        except ValueError:
            return

    def request_line_color(self):
        try:
            self.line_color = self.request_color()
        except ValueError:
            return

    def generate_image(self, scale=1):
        if not self.check_values():
            raise ValueError
        size = (self.spinBox_size_x.value() * scale,
                self.spinBox_size_y.value() * scale)
        start_coords = (self.spinBox_start_x.value() * scale,
                        self.spinBox_start_y.value() * scale)
        start_coords = decart_to_image_coords(start_coords, size)
        if self.radioButton_div_mode.isChecked():
            rotation_angle = angle_part_of_circle(
                self.spinBox_plane_div.value())
        else:
            rotation_angle = deg_to_rad(self.spinBox_angle.value())
        start_angle = deg_to_rad(self.spinBox_start_angle.value())
        rules = strings_to_dict(self.get_rule_strings(), " ")
        step_length = self.spinBox_step_length.value() * scale
        initiator = self.lineEdit_initiator.text()
        iterations = self.horizontalSlider_step.value()
        string_gen_params = (initiator, rules, iterations)
        draw_params = (start_coords, start_angle, rotation_angle,
                       step_length, self.line_color)
        image_params = (size, self.bg_color, draw_params)
        self.image = gen_string_and_draw(string_gen_params, image_params)

    def check_values(self):
        return self.lineEdit_initiator.text() and self.plainTextEdit_rules.toPlainText()

    def get_rule_strings(self):
        text = self.plainTextEdit_rules.toPlainText()
        return text.split("\n")

    def update_step_slider(self):
        self.horizontalSlider_step.setValue(self.spinBox_step.value())

    def update_step_spinbox(self):
        self.spinBox_step.setValue(self.horizontalSlider_step.value())

    def update_label(self):
        try:
            self.generate_image()
        except ValueError:
            return
        pixmap = image_to_pixmap(self.image)
        self.label_result.setPixmap(pixmap)

    def clear_label(self):
        self.label_result.clear()

    def set_angle_mode(self):
        self.radioButton_angle_mode.setChecked(True)
        self.spinBox_angle.setEnabled(True)
        self.spinBox_plane_div.setEnabled(False)

    def set_plane_div_mode(self):
        self.radioButton_div_mode.setChecked(True)
        self.spinBox_angle.setEnabled(False)
        self.spinBox_plane_div.setEnabled(True)

    def save_image(self):
        try:
            path = self.requset_save_path("Сохранить", "All files")
        except FileNotFoundError:
            return
        scale = self.spinBox_scale.value()
        self.generate_image(scale)
        img = self.image.convert("RGB")
        img.save(path)
