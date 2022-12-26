import re
import subprocess
import sys
import alsaaudio

from PySide6.QtWidgets import QWidget, QApplication
from main_form import Ui_Form
from datetime import datetime as dt


def get_volume_level():
    volume_level = subprocess.run(["amixer", "-D", "pulse", "get", "Master"], stdout=subprocess.PIPE)
    return int(re.search(r'\d{1,3}%', volume_level.stdout.decode('utf-8'))[0][:-1])


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

        self.ui.dial_sound.setValue(get_volume_level())
        # get_volume = subprocess.run(["amixer", "-D", "pulse", "get", "Master"], stdout=subprocess.PIPE)
        print('set_volume', subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "10%"]))
        # print('get_volume', get_volume.stdout.decode('utf-8'))

        self.ui.pushButton_OK.clicked.connect(self.create_command)
        self.ui.pushButton_Cancel.clicked.connect(self.stop_timer)
        self.ui.dial_sound.valueChanged.connect(self.changed_sound_volume)

    def timer_number(self):
        if self.ui.dial_timer.value() == 9:
            return [self.ui.timeEdit_timer.text(), f'Компьютер выключится в {self.ui.timeEdit_timer.text()}']
        else:
            return [str(self.ui.dial_timer.value()), f'Компьютер выключится через '
                                                     f'{str(self.ui.dial_timer.value())} мин']

    def create_command(self):
        time_timer = self.timer_number()
        timer_start = subprocess.Popen(['shutdown', '-h', time_timer[0]], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
        self.ui.label_status.setText(f'Компьютер выключится в {time_timer[1]}')
        print('timer_start', timer_start.communicate())

    def stop_timer(self):
        subprocess.run(['shutdown', '-c'])
        self.ui.label_status.setText('Таймер выключения отключён.')

    def stats_timer(self):
        status = subprocess.run(['busctl', 'get-property', 'org.freedesktop.login1',
                                 '/org/freedesktop/login1', 'org.freedesktop.login1.Manager', 'ScheduledShutdown'],
                                stdout=subprocess.PIPE)
        time_list = status.stdout.decode('utf-8').split()
        print(time_list[2])
        if int(time_list[2]) == 0:
            self.ui.label_status.setText('Таймер выключения не установлен.')
        else:
            self.ui.label_status.setText(f"Время выключения: {dt.fromtimestamp(int(time_list[2][0:-6])): %H:%M}")

    def changed_sound_volume(self):
        subprocess.call(["amixer", "-D", "pulse", "sset", "Master", f'{self.ui.dial_sound.value()}%'],
                        stdout=subprocess.PIPE)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainTimer()
    window.show()

    sys.exit(app.exec())
