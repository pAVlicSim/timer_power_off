import subprocess
import sys

from PySide6.QtWidgets import QWidget, QApplication
from main_form import Ui_Form
from datetime import datetime as dt


class MainTimer(QWidget):
    def __init__(self):
        super(MainTimer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.time_timer = ''
        try:
            self.stats_timer()
        except FileNotFoundError:
            print('No timer')

        self.ui.pushButton_OK.clicked.connect(self.create_command)
        self.ui.pushButton_Cancel.clicked.connect(self.stop_timer)

    def timer_number(self):
        if self.ui.lineEdit_timer.text() == '':
            return [self.ui.timeEdit_timer.text(), f'Компьютер выключится в {self.ui.timeEdit_timer.text()}']
        else:
            return [self.ui.lineEdit_timer.text(), f'Компьютер выключится через {self.ui.lineEdit_timer.text()} мин']

    def create_command(self):
        time_timer = self.timer_number()
        timer_start = subprocess.Popen(['shutdown', '-h', time_timer[0]], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
        self.ui.label_3.setText(f'Компьютер выключится в {time_timer[1]}')
        print('timer_start', timer_start.communicate())

    def stop_timer(self):
        subprocess.run(['shutdown', '-c'])
        self.ui.label_3.setText('Таймер выключения отключён.')

    def stats_timer(self):
        status = subprocess.run(['busctl', 'get-property', 'org.freedesktop.login1',
                                 '/org/freedesktop/login1', 'org.freedesktop.login1.Manager', 'ScheduledShutdown'],
                                stdout=subprocess.PIPE)
        time_list = status.stdout.decode('utf-8').split()
        print(time_list[2])
        if int(time_list[2]) == 0:
            self.ui.label_3.setText('Таймер выключения не установлен.')
        else:
            self.ui.label_3.setText(f"Время выключения: {dt.fromtimestamp(int(time_list[2][0:-6])): %H:%M}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainTimer()
    window.show()

    sys.exit(app.exec())
