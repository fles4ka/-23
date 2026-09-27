import sys
import difflib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QRadioButton, QPushButton, QLabel, QGroupBox,
    QCalendarWidget, QTimeEdit, QLineEdit, QListWidget, QSpinBox,
    QDoubleSpinBox, QTextEdit, QMessageBox, QStatusBar
)
from PyQt5.QtCore import Qt, QTime


# ==============================================================================
# №1 (1 балл): Приложение «Текстовый флаг»
# ==============================================================================
class Task1Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.colors_options = ["Красный", "Зелёный", "Белый", "Синий", "Жёлтый"]

        self.group1 = self.create_color_group("Полоса 1")
        self.group2 = self.create_color_group("Полоса 2")
        self.group3 = self.create_color_group("Полоса 3")

        h_layout.addWidget(self.group1)
        h_layout.addWidget(self.group2)
        h_layout.addWidget(self.group3)

        self.draw_btn = QPushButton("Нарисовать")
        self.draw_btn.clicked.connect(self.draw_flag)

        self.result_label = QLabel("Выберите цвета и нажмите кнопку")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-weight: bold; font-size: 13px;")

        main_layout.addLayout(h_layout)
        main_layout.addWidget(self.draw_btn)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def create_color_group(self, title):
        group = QGroupBox(title)
        vbox = QVBoxLayout()
        for i, color in enumerate(self.colors_options):
            rb = QRadioButton(color)
            if i == 0:
                rb.setChecked(True)
            vbox.addWidget(rb)
        group.setLayout(vbox)
        return group

    def draw_flag(self):
        selected_colors = []
        for group in [self.group1, self.group2, self.group3]:
            for rb in group.findChildren(QRadioButton):
                if rb.isChecked():
                    selected_colors.append(rb.text())

        self.result_label.setText(f"{selected_colors[0]}, {selected_colors[1]}, {selected_colors[2]}")


# ==============================================================================
# №2 (3 балла): Программа-ежедневник
# ==============================================================================
class Task2Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())

        self.event_input = QLineEdit()
        self.event_input.setPlaceholderText("Введите название события...")

        self.add_btn = QPushButton("Добавить")
        self.add_btn.clicked.connect(self.add_event)

        self.list_widget = QListWidget()

        layout.addWidget(QLabel("Выберите дату:"))
        layout.addWidget(self.calendar)
        layout.addWidget(QLabel("Выберите время:"))
        layout.addWidget(self.time_edit)
        layout.addWidget(self.event_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(QLabel("События (отсортированы по возрастанию даты):"))
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_event(self):
        event_name = self.event_input.text().strip()
        if not event_name:
            QMessageBox.warning(self, "Ошибка", "Введите название события!")
            return

        date_str = self.calendar.selectedDate().toString("yyyy-MM-dd")
        time_str = self.time_edit.time().toString("HH:mm")

        item_text = f"{date_str} {time_str} — {event_name}"
        self.list_widget.addItem(item_text)
        self.list_widget.sortItems()
        self.event_input.clear()


# ==============================================================================
# №3 (3 балла): Записная книжка
# ==============================================================================
class Task3Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя контакта")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Номер телефона")

        self.add_btn = QPushButton("Добавить")
        self.add_btn.clicked.connect(self.add_contact)

        self.list_widget = QListWidget()

        layout.addWidget(QLabel("Имя контакта:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Номер телефона:"))
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(QLabel("Список контактов:"))
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Заполните имя и номер телефона!")
            return

        self.list_widget.addItem(f"{name}: {phone}")
        self.name_input.clear()
        self.phone_input.clear()


# ==============================================================================
# №4 (4 балла): Игра «Псевдоним»
# ==============================================================================
class Task4Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.stones = 0
        self.game_active = False
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        init_layout = QHBoxLayout()
        init_layout.addWidget(QLabel("Количество камней (N):"))
        self.initial_stones_spin = QSpinBox()
        self.initial_stones_spin.setRange(4, 100)
        self.initial_stones_spin.setValue(15)
        init_layout.addWidget(self.initial_stones_spin)

        self.start_btn = QPushButton("Начать новую игру")
        self.start_btn.clicked.connect(self.start_game)
        init_layout.addWidget(self.start_btn)

        layout.addLayout(init_layout)

        self.status_label = QLabel("Задайте N и нажмите «Начать новую игру»")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #1a237e;")
        layout.addWidget(self.status_label)

        turn_layout = QHBoxLayout()
        turn_layout.addWidget(QLabel("Ваш ход (взять камни):"))
        self.take_spin = QSpinBox()
        self.take_spin.setRange(1, 3)
        turn_layout.addWidget(self.take_spin)

        self.take_btn = QPushButton("Взять")
        self.take_btn.clicked.connect(self.player_turn)
        turn_layout.addWidget(self.take_btn)

        layout.addLayout(turn_layout)

        self.log_list = QListWidget()
        layout.addWidget(QLabel("Ход игры:"))
        layout.addWidget(self.log_list)

        self.setLayout(layout)

    def start_game(self):
        self.stones = self.initial_stones_spin.value()
        self.game_active = True
        self.log_list.clear()
        self.update_spin_limit()
        self.status_label.setText(f"Осталось камней на столе: {self.stones}")
        self.log_list.addItem(f"--- Игра началась! На столе {self.stones} камней. Ваш ход! ---")

    def update_spin_limit(self):
        max_possible = min(3, self.stones) if self.stones > 0 else 1
        self.take_spin.setRange(1, max_possible)

    def player_turn(self):
        if not self.game_active:
            QMessageBox.warning(self, "Ошибка", "Начните новую игру!")
            return

        take = self.take_spin.value()

        if take > self.stones or take < 1:
            QMessageBox.warning(self, "Ошибка", f"Нельзя взять {take} камней! На столе: {self.stones}.")
            return

        self.stones -= take
        self.log_list.addItem(f"Игрок взял: {take} шт. (Осталось: {self.stones})")

        if self.stones == 0:
            self.status_label.setText("Вы выиграли!")
            self.log_list.addItem("Победа Игрока!")
            self.game_active = False
            return

        ai_take = self.stones % 4
        if ai_take == 0:
            ai_take = 1

        self.stones -= ai_take
        self.log_list.addItem(f"Компьютер взял: {ai_take} шт. (Осталось: {self.stones})")

        if self.stones == 0:
            self.status_label.setText("Компьютер выиграл!")
            self.log_list.addItem("Победа Компьютера!")
            self.game_active = False
        else:
            self.status_label.setText(f"Осталось камней на столе: {self.stones}")
            self.update_spin_limit()


# ==============================================================================
# №5 (4 балла): Проверка на антиплагиат
# ==============================================================================
class Task5Widget(QWidget):
    def __init__(self, status_bar):
        super().__init__()
        self.status_bar = status_bar
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        thresh_layout = QHBoxLayout()
        thresh_layout.addWidget(QLabel("Порог антиплагиата (%):"))
        self.threshold_spin = QDoubleSpinBox()
        self.threshold_spin.setRange(0.0, 100.0)
        self.threshold_spin.setValue(50.0)
        thresh_layout.addWidget(self.threshold_spin)

        layout.addLayout(thresh_layout)

        texts_layout = QHBoxLayout()

        v1 = QVBoxLayout()
        v1.addWidget(QLabel("Текст 1:"))
        self.text1_edit = QTextEdit()
        v1.addWidget(self.text1_edit)

        v2 = QVBoxLayout()
        v2.addWidget(QLabel("Текст 2:"))
        self.text2_edit = QTextEdit()
        v2.addWidget(self.text2_edit)

        texts_layout.addLayout(v1)
        texts_layout.addLayout(v2)

        layout.addLayout(texts_layout)

        self.calc_btn = QPushButton("Рассчитать результат")
        self.calc_btn.clicked.connect(self.check_plagiarism)
        layout.addWidget(self.calc_btn)

        self.setLayout(layout)

    def check_plagiarism(self):
        t1 = self.text1_edit.toPlainText()
        t2 = self.text2_edit.toPlainText()

        lines1 = [line.strip() for line in t1.splitlines() if line.strip()]
        lines2 = [line.strip() for line in t2.splitlines() if line.strip()]

        if not lines1 and not lines2:
            similarity = 100.0
        elif not lines1 or not lines2:
            similarity = 0.0
        else:
            same_lines = sum(1 for line in lines1 if line in lines2)
            max_lines = max(len(lines1), len(lines2))
            similarity = (same_lines / max_lines) * 100.0

        threshold = self.threshold_spin.value()
        res_text = f"Сходство: {similarity:.2f}% | Порог: {threshold:.2f}%"

        if similarity >= threshold:
            msg = f"ПЛАГИАТ ОБНАРУЖЕН! ({res_text})"
            self.status_bar.setStyleSheet(
                "QStatusBar { background-color : #d32f2f; color : white; font-weight: bold; }")
        else:
            msg = f"ПЛАГИАТ НЕ ОБНАРУЖЕН. ({res_text})"
            self.status_bar.setStyleSheet(
                "QStatusBar { background-color : #388e3c; color : white; font-weight: bold; }")

        self.status_bar.showMessage(msg)


# ==============================================================================
# Главное окно приложения
# ==============================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №2")

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Выберите задание во вкладках выше")

        self.tab_widget = QTabWidget()

        self.tab1 = Task1Widget()
        self.tab2 = Task2Widget()
        self.tab3 = Task3Widget()
        self.tab4 = Task4Widget()
        self.tab5 = Task5Widget(self.status_bar)

        self.tab_widget.addTab(self.tab1, "№1 Текстовый флаг")
        self.tab_widget.addTab(self.tab2, "№2 Ежедневник")
        self.tab_widget.addTab(self.tab3, "№3 Записная книжка")
        self.tab_widget.addTab(self.tab4, "№4 Псевдоним")
        self.tab_widget.addTab(self.tab5, "№5 Антиплагиат")

        # Сигнал переключения вкладок
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

        self.setCentralWidget(self.tab_widget)

        # При запуске вручную вызываем логику для первой вкладки, чтобы зафиксировать размер окна
        self.on_tab_changed(0)

    def on_tab_changed(self, index):
        if index == 0:
            # Для вкладки №1 жестко фиксируем размер окна
            self.setFixedSize(500, 350)
        else:
            # Для остальных вкладок снимаем фиксацию (разрешаем растягивать)
            self.setMinimumSize(600, 500)
            self.setMaximumSize(16777215, 16777215)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())